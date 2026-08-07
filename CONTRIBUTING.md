# Contributing

Contributions welcome! Open a PR to add papers, datasets, benchmarks, or tools related to **rubric rewards** — rubrics, checklists, criteria sets, principles, constitutions, and scoring guides used to score, rank, verify, filter, or train modern generative models.

## Inclusion criteria

A resource must pass **one** of these two tests:

1. **The work defines, trains, applies, evaluates, or critiques an explicit criteria-based reward, judge, or verifier.** This includes rubric-conditioned reward models, rubric- or checklist-driven RL, LLM/VLM judges, process reward models whose steps are graded against criteria, programmatic verifiers whose target is expressed as criteria, and work on how criteria are generated, weighted, or gamed.
2. **The work directly enables criteria-based reward deployment *and* explicitly evaluates, represents, accepts, emits, or operates on a criteria artifact.** Rubric and criteria datasets, rubric-graded benchmarks, judge meta-benchmarks, and tooling that makes criteria-based scoring practical. Without the second clause this test admits any reward model or judge paper, which is exactly how the list drifted once already.

The list deliberately does **not** distinguish reward model from verifier. A learned rubric-conditioned reward model, an LLM judge reading a checklist, and a programmatic grader running assertions are three implementations of the same idea, and all three belong.

The list is also **not text-only**. Criteria-decomposed rewards for image, video, audio, 3D, embodied, and GUI agents are first-class.

### What does NOT qualify — apply these strictly

- **Single-scalar preference scorers with no criteria decomposition.** A model that emits one learned number is the opposite of a rubric. ImageReward, PickScore, and the HPS family appear only in **Foundations**, as the ancestors the field moved past.
- **Pre-foundation-model work.** Classical RL reward shaping, inverse RL, and pre-LLM assessment theory belong in **Foundations** or nowhere. The list's scope is the foundation-model era.
- **Generic capability papers** that mention an LLM judge in passing for evaluation without contributing to judging or criteria design.
- **Pure supervised fine-tuning or distillation** with no reward, preference, or criteria signal.
- **Domain applications** with no transferable methodological contribution beyond the domain.

### The criteria-artifact test — apply to every submission

Read the actual paper and answer this concretely: **where, exactly, are the criteria that get applied independently to the candidate output?** A submission qualifies only if you can fill this in:

- **Location** — §4.2 / Appendix B / released YAML / prompt template
- **Form** — natural-language items | executable predicates | scoring levels
- **Granularity** — task | instance | claim | step
- **Per-item output exposed** — yes / no

If you cannot fill it in, the work belongs in **Foundations**, an **adjacent collection**, or nowhere. These are related but not the same object, and only the first is core scope: a written rubric item, a broad attribute name, a learned reward head, a generated rationale, a process reward, a correctness verifier, an executable test, a multi-objective vector, an LLM judge, an environment success condition.

Two corollaries that have caused most of the drift here:

- **Fine-grained credit is not a fine-grained rubric.** Token-level or span-level attribution says where reward lands, not what standard was applied.
- **Named dimensions are not a rubric.** A composite of three opaque reward models is still a composite of opaque reward models, however well-named its components.

## Section placement

Read the live structure before placing anything — `grep -n '^## ' README.md` and `grep -n '^### ' README.md`. The README's own headers are the source of truth; the list below is a routing heuristic and will drift.

- Criteria produce the RL training signal → **Rubrics as Reward Signals for RL** (core algorithms; exploration/stability/aggregation; self-evolving; process/step/token-level credit).
- The contribution is *where criteria come from* → **Rubric Construction** (direct generation; contrastive generation; iterative refinement; online and co-evolving). This four-way split follows the field's own survey taxonomy.
- Checklists, constitutions, principles, specs, instruction hierarchies, constraint verification, or QA/atomic-claim decomposition → **Checklists, Principles, Constitutions, and Specs**.
- A trained scorer that consumes or emits criteria → **Rubric-Conditioned Reward Models**. Multi-head or dense reward models do not qualify on granularity alone.
- A program running several named predicates, acceptance conditions, or partial-credit rules → **Criteria Compilers and Programmatic Rubric Graders**. A monolithic correctness checker or proof verifier does not qualify.
- Step-level grading against an explicit criteria tree, error taxonomy, or weighted process components → **Process Reward Models and Step-Level Criteria**. Binary step-correctness labels do not qualify.
- Judges and judge science **specifically in their use of explicit criteria** → **Rubric-Conditioned Judges and Rubric-Specific Judge Science**. Generic judge training, position/verbosity bias, and calibration work goes to the dedicated judge lists. This wing is split three ways on purpose: trained artifacts, behavior science, and benchmarks. Keep it compact and cross-link to the dedicated judge lists rather than reproducing them.
- Criteria gaming, over-optimization, specification gaming, reward tampering → **Reward Hacking and Robustness**.
- Anything non-text → **Multimodal Rubric Rewards** or **Agent, GUI, and Embodied Verification**.
- Whether criteria-based judging is reliable at all → **Rubric Quality and Meta-Evaluation**.
- A benchmark or dataset → the corresponding **table**, not a bullet.

**Foundations is background, not subject matter.** It is deliberately selective and rarely updated. When unsure, prefer a specific topical section.

**Sibling lists are independent, not a division of labour.** The maintainer's other awesome-lists (`awesome-rm-for-video-generation`, `awesome-rl-for-video-generation`, `awesome-on-policy-distillation`, `awesome-llm-unlearning`) are each self-contained on their own scope, and so is this one. Overlap is expected and fine: a paper that is genuinely a criteria-decomposed reward belongs here whether or not another list also carries it. The only cross-repo use is the reverse direction — diffing a sibling to *find* relevant work this list is missing. Never omit an in-scope paper on the grounds that a sibling covers it.

## Entry format

```
- [Full Paper Title](url) *(Year)* — One-line description.
```

- Title must match the arXiv title **exactly**. Several papers in this area were retitled between versions — resolve the ID before adding, never trust a cached bibliography.
- Year in italic parens, em-dash separator.
- Description is **one sentence, ≤22 words**: one concrete mechanism phrase plus one differentiator. No benchmark numbers, no hyperparameters, no percentage gains, no model/dataset enumerations, no second mechanism clause joined by a semicolon or "and".
- Deletion test: at each comma or "and", try deleting the trailing clause. If the entry still tells a scanning reader why to click, that clause was bloat.

## Naming hazards

This literature has an unusual density of near-identical names. These are **different papers** — keep full titles visible and verify IDs:

- `EvoRubric` vs `EvoRubrics` vs `EvoLM`
- `Auto-Rubric` vs `Auto-Rubric as Reward` vs `AutoRubric` vs `AutoRubric-T2I` vs `AdaRubric`
- `OpenRubrics` vs `Open Rubric System`
- `R3` vs `mR3`; `RM-R1` vs `R1-Reward`
- `RubricRL` vs `RubiCap`
- `PRBench (Professional Reasoning) / PRBench (Physics Reproduction) · RubricBench` vs `RubricEval` vs `RubricRAG` vs `RubricHub`

## Verification requirement

Every arXiv ID must be resolved against the live abstract page or the arXiv API before it ships, and the title must match. A fabricated or stale citation costs more review time than a missing paper saves. If you cannot confirm an ID, omit the entry and say so.

## Batch additions

- **Flag section growth.** If a single update would double any subsection, consider whether it needs splitting or whether some entries are marginal.
- **Prioritize gap-filling over completeness.** A paper opening a new niche beats a fourth variant in a well-covered area.
- **Cap awareness.** Prefer 5-8 high-confidence additions over 12+ with several borderline entries.

## Taxonomy and reading path

- Update the taxonomy tables when a paper clearly fits an existing row. Skip taxonomy updates for papers that don't fit neatly.
- The Start Here reading path changes rarely. Only add a paper if it is the best introduction to a currently underrepresented topic.

## Duplication

Duplication across sections is acceptable for exceptionally central papers — the Core Rubric Reward Papers section deliberately cross-lists a dozen. Everywhere else, prefer one primary location.
