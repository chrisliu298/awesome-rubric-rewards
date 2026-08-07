#!/usr/bin/env python3
"""Build/refresh papers.tsv — the title-drift manifest for awesome-rubric-rewards.

Every arXiv entry in README.md is recorded with the title as stored in the list and
the title arXiv currently returns. `verify` fails when they diverge, which is this
repo's most persistent defect class: papers here are retitled between versions more
often than in most areas, and every catch so far has been luck.

  python3 scripts/build_manifest.py build     # refresh papers.tsv (network)
  python3 scripts/build_manifest.py verify    # exit 1 on drift (network)
  python3 scripts/build_manifest.py check     # offline: manifest covers README, no dupes
"""
import html, json, os, re, sys, time, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README, MANIFEST = os.path.join(ROOT, "README.md"), os.path.join(ROOT, "papers.tsv")
UA = {"User-Agent": "awesome-rubric-rewards-manifest (+https://github.com/chrisliu298/awesome-rubric-rewards)"}
ENTRY = re.compile(r'^[-|] \[([^\]]+)\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\)')


def parse_readme():
    """Return [(arxiv_id, stored_title, section)] in document order, first mention wins."""
    out, seen, section = [], set(), ""
    for line in open(README, encoding="utf-8"):
        h = re.match(r'^(#{2,4}) (.+)$', line)
        if h:
            section = h.group(2).strip()
            continue
        m = ENTRY.match(line)
        if m and m.group(2) not in seen:
            seen.add(m.group(2))
            out.append((m.group(2), m.group(1).strip(), section))
    return out


def fetch_title(aid):
    """Live arXiv title. abs page first — it is the only source that resolves papers
    posted in the last week, and HuggingFace has been observed returning a wrong title."""
    try:
        h = urllib.request.urlopen(urllib.request.Request(f"https://arxiv.org/abs/{aid}", headers=UA), timeout=30)
        m = re.search(r'<meta name="citation_title" content="([^"]+)"', h.read().decode("utf-8", "ignore"))
        if m:
            return re.sub(r'\s+', ' ', html.unescape(m.group(1))).strip()
    except Exception:
        pass
    try:
        r = urllib.request.urlopen(urllib.request.Request(f"https://huggingface.co/api/papers/{aid}", headers=UA), timeout=20)
        t = json.load(r).get("title")
        if t:
            return re.sub(r'\s+', ' ', t).strip()
    except Exception:
        pass
    return None


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', (s or "").lower()).strip()


def load_manifest():
    if not os.path.exists(MANIFEST):
        return {}
    rows = {}
    with open(MANIFEST, encoding="utf-8") as f:
        next(f, None)
        for line in f:
            c = line.rstrip("\n").split("\t")
            if len(c) == 5:
                rows[c[0]] = dict(zip(("arxiv_id", "stored_title", "current_arxiv_title", "last_verified", "section"), c))
    return rows


def write_manifest(rows):
    with open(MANIFEST, "w", encoding="utf-8") as f:
        f.write("arxiv_id\tstored_title\tcurrent_arxiv_title\tlast_verified\tsection\n")
        for aid in sorted(rows):
            r = rows[aid]
            f.write("\t".join(r[k].replace("\t", " ") for k in
                    ("arxiv_id", "stored_title", "current_arxiv_title", "last_verified", "section")) + "\n")


def cmd_check():
    entries = parse_readme()
    ids = [a for a, _, _ in entries]
    dupes = {i for i in ids if ids.count(i) > 1}
    rows = load_manifest()
    missing = [a for a in ids if a not in rows]
    stale = [a for a in rows if a not in set(ids)]
    drift = [a for a, t, _ in entries
             if a in rows and rows[a]["current_arxiv_title"] and norm(rows[a]["stored_title"]) != norm(t)]
    for label, xs in (("duplicate ids", sorted(dupes)), ("not in manifest", missing),
                      ("manifest rows no longer in README", stale),
                      ("README title changed since last build", drift)):
        if xs:
            print(f"FAIL {label}: {len(xs)}")
            for x in xs[:20]:
                print("   ", x)
    ok = not (dupes or missing or stale or drift)
    print(f"{'OK' if ok else 'FAIL'} check — {len(ids)} entries, {len(rows)} manifest rows")
    return 0 if ok else 1


def _refresh(today, only_missing):
    entries, rows = parse_readme(), load_manifest()
    todo = [e for e in entries if not (only_missing and e[0] in rows and rows[e[0]]["current_arxiv_title"])]
    print(f"resolving {len(todo)} of {len(entries)}", file=sys.stderr)
    for n, (aid, stored, section) in enumerate(todo, 1):
        cur = fetch_title(aid)
        rows[aid] = {"arxiv_id": aid, "stored_title": stored,
                     "current_arxiv_title": cur or (rows.get(aid, {}).get("current_arxiv_title", "")),
                     "last_verified": today if cur else rows.get(aid, {}).get("last_verified", ""),
                     "section": section}
        if n % 25 == 0:
            print(f"  {n}/{len(todo)}", file=sys.stderr)
        time.sleep(1.1)
    for aid, stored, section in entries:
        rows[aid]["stored_title"], rows[aid]["section"] = stored, section
    for aid in [a for a in rows if a not in {e[0] for e in entries}]:
        del rows[aid]
    write_manifest(rows)
    return entries, rows


def cmd_build(today):
    entries, rows = _refresh(today, only_missing=True)
    unresolved = [a for a in rows if not rows[a]["current_arxiv_title"]]
    print(f"wrote {MANIFEST}: {len(rows)} rows, {len(unresolved)} unresolved")
    return 0


def cmd_verify(today):
    entries, rows = _refresh(today, only_missing=False)
    bad = [(a, rows[a]["stored_title"], rows[a]["current_arxiv_title"]) for a in sorted(rows)
           if rows[a]["current_arxiv_title"] and norm(rows[a]["stored_title"]) != norm(rows[a]["current_arxiv_title"])]
    for a, s, c in bad:
        print(f"DRIFT {a}\n  stored : {s}\n  arxiv  : {c}")
    print(f"{'FAIL' if bad else 'OK'} verify — {len(bad)} drifted of {len(rows)}")
    return 1 if bad else 0


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    today = sys.argv[2] if len(sys.argv) > 2 else ""
    if cmd in ("build", "verify") and not today:
        sys.exit("build/verify need a date argument: build_manifest.py build 2026-08-07")
    sys.exit({"check": lambda: cmd_check(), "build": lambda: cmd_build(today),
              "verify": lambda: cmd_verify(today)}[cmd]())
