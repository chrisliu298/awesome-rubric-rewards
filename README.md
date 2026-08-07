# 📋 Awesome Rubric Rewards

<p align="center">
  <a href="https://awesome.re"><img src="https://img.shields.io/badge/Awesome-%F0%9F%93%8B_Rubric_Rewards-000000?style=for-the-badge&labelColor=000000" alt="Awesome Rubric Rewards"></a>
</p>

<p align="center">
  <!-- entry-count-start --><a href="#contents"><img src="https://img.shields.io/badge/Entries-862-000000?style=for-the-badge&labelColor=000000" alt="Entries"></a><!-- entry-count-end -->
  <a href="https://github.com/chrisliu298/awesome-rubric-rewards/stargazers"><img src="https://img.shields.io/github/stars/chrisliu298/awesome-rubric-rewards?style=for-the-badge&logo=github&logoColor=white&label=Stars&labelColor=000000&color=000000" alt="GitHub Stars"></a>
  <a href="https://github.com/chrisliu298/awesome-rubric-rewards/network/members"><img src="https://img.shields.io/github/forks/chrisliu298/awesome-rubric-rewards?style=for-the-badge&logo=github&logoColor=white&label=Forks&labelColor=000000&color=000000" alt="GitHub Forks"></a>
  <a href="https://github.com/chrisliu298/awesome-rubric-rewards/commits"><img src="https://img.shields.io/github/last-commit/chrisliu298/awesome-rubric-rewards?style=for-the-badge&logo=github&logoColor=white&label=Last%20Commit&labelColor=000000&color=000000" alt="Last Commit"></a>
</p>

A curated collection of papers, datasets, benchmarks, and code for **rubric rewards**: rubrics, checklists, criteria sets, principles, constitutions, and scoring guides used to score, rank, verify, filter, or train modern generative models.

> **Rubric reward** = an explicit, decomposed, human-readable set of criteria applied to a model output to produce a reward, a preference label, or a quality score. Three properties separate it from an ordinary reward model: the criteria are *written down* rather than latent in weights, *decomposed* into many items rather than collapsed to one scalar, and *inspectable* so a person can read, audit, and edit them.

The organizing idea: **rubrics turn open-ended objectives into inspectable reward specifications.** RLVR works wherever a checker already exists — a unit test, a math answer key. Rubrics supply an auditable *proxy* where none did, which is what makes RL tractable for writing, medicine, law, research, dialogue, and open-ended agentic work. The proxy is not a guarantee: its validity depends on whether the criteria capture the intended construct, whether the judge applies them faithfully, and whether the policy exploits what they omit. Every entry here is either building that specification, using it as a reward, measuring whether it holds, or documenting how it breaks.

This list deliberately ignores two distinctions the surrounding literature treats as important. **Reward model versus verifier** is not a boundary here — a learned rubric-conditioned reward model, an LLM judge reading a checklist, and a programmatic grader running assertions are three implementations of one idea. **Text versus everything else** is not a boundary either: criteria-decomposed rewards for image, video, audio, 3D, embodied, and GUI agents are first-class.

The scope is the **foundation-model era**. Single-scalar preference scorers, classical RL reward shaping, and pre-LLM assessment theory appear only in [Foundations](#foundations), as background for why the modern work looks the way it does.

The field splits into four partially overlapping camps:

1. **Rubrics as reward signals** — RL where a rubric, checklist, or criteria set produces the scalar or preference signal, especially in non-verifiable and open-ended domains.
2. **Criteria-consuming scorers** — rubric-conditioned reward models, LLM-as-a-judge systems, generative and reasoning judges, process reward models, and programmatic verifiers.
3. **Rubric construction and quality** — where criteria come from, how they aggregate, whether they are valid and reliable, and how they get gamed.
4. **Rubric-graded evaluation** — benchmarks and suites where a rubric grades, whether or not it yet drives training.

**New to the area?** Read [Start Here](#start-here). **Picking a method or benchmark?** Jump to [Quick Start by Goal](#quick-start-by-goal).

## Contents

- [Quick Start by Goal](#quick-start-by-goal)
- [Start Here](#start-here)
- [Taxonomy](#taxonomy)
- [Core Rubric Reward Papers](#core-rubric-reward-papers)
- [Foundations](#foundations)
  - [Preference modeling and RLHF background](#preference-modeling-and-rlhf-background)
  - [LLM-as-a-judge origins](#llm-as-a-judge-origins)
  - [Reward hacking and specification gaming before rubrics](#reward-hacking-and-specification-gaming-before-rubrics)
  - [Rubrics before LLMs: educational assessment](#rubrics-before-llms-educational-assessment)
  - [Single-scalar preference scorers for generative models](#single-scalar-preference-scorers-for-generative-models)
- [Rubrics as Reward Signals for RL](#rubrics-as-reward-signals-for-rl)
  - [Core algorithms](#core-algorithms)
  - [Exploration, stability, and aggregation](#exploration-stability-and-aggregation)
  - [Self-evolving and adaptive rubrics](#self-evolving-and-adaptive-rubrics)
  - [Process, step, and token-level rubric credit](#process-step-and-token-level-rubric-credit)
- [Rubric Construction](#rubric-construction)
  - [Direct generation](#direct-generation)
  - [Contrastive generation](#contrastive-generation)
  - [Iterative refinement](#iterative-refinement)
  - [Online and co-evolving generation](#online-and-co-evolving-generation)
- [Checklists, Principles, Constitutions, and Specs](#checklists-principles-constitutions-and-specs)
  - [Checklist feedback as reward](#checklist-feedback-as-reward)
  - [Constitutions and principle-following](#constitutions-and-principle-following)
  - [Specs and instruction hierarchies](#specs-and-instruction-hierarchies)
  - [Instruction and constraint verification](#instruction-and-constraint-verification)
  - [Question decomposition and atomic-claim verification](#question-decomposition-and-atomic-claim-verification)
- [Rubric-Conditioned Reward Models](#rubric-conditioned-reward-models)
  - [Rubric- and criteria-conditioned reward models](#rubric--and-criteria-conditioned-reward-models)
  - [Multi-attribute and multi-objective reward models](#multi-attribute-and-multi-objective-reward-models)
  - [Fine-grained, dense, and span-level rewards](#fine-grained-dense-and-span-level-rewards)
  - [Self-rewarding and self-generated criteria](#self-rewarding-and-self-generated-criteria)
- [Criteria Compilers and Programmatic Rubric Graders](#criteria-compilers-and-programmatic-rubric-graders)
- [Process Reward Models and Step-Level Criteria](#process-reward-models-and-step-level-criteria)
- [Rubric-Conditioned Judges and Rubric-Specific Judge Science](#rubric-conditioned-judges-and-rubric-specific-judge-science)
  - [Judge models and generative reward models](#judge-models-and-generative-reward-models)
  - [Critic models and explainable metrics](#critic-models-and-explainable-metrics)
  - [Judge behavior science: bias](#judge-behavior-science-bias)
  - [Judge behavior science: reliability and calibration](#judge-behavior-science-reliability-and-calibration)
  - [Judge behavior science: adversarial robustness](#judge-behavior-science-adversarial-robustness)
  - [Multi-agent, debate, and ensemble judges](#multi-agent-debate-and-ensemble-judges)
  - [Efficient judges](#efficient-judges)
- [Reward Hacking and Robustness](#reward-hacking-and-robustness)
  - [Rubric-specific hacking and attack surface](#rubric-specific-hacking-and-attack-surface)
  - [Reward model over-optimization and mitigations](#reward-model-over-optimization-and-mitigations)
  - [Specification gaming and reward tampering](#specification-gaming-and-reward-tampering)
- [Multimodal Rubric Rewards](#multimodal-rubric-rewards)
  - [Criteria-decomposed image rewards](#criteria-decomposed-image-rewards)
  - [Question decomposition for text-to-image](#question-decomposition-for-text-to-image)
  - [Multimodal judges and reward models](#multimodal-judges-and-reward-models)
  - [Multimodal reasoning rubrics](#multimodal-reasoning-rubrics)
  - [Video](#video)
  - [Audio, speech, and music](#audio-speech-and-music)
  - [3D generation](#3d-generation)
- [Agent, GUI, and Embodied Verification](#agent-gui-and-embodied-verification)
  - [GUI and computer-use agents](#gui-and-computer-use-agents)
  - [Embodied and robotic verification](#embodied-and-robotic-verification)
  - [Rubric rewards for agents, tool use, and software engineering](#rubric-rewards-for-agents-tool-use-and-software-engineering)
  - [Rubric rewards for deep research](#rubric-rewards-for-deep-research)
- [Rubric Quality and Meta-Evaluation](#rubric-quality-and-meta-evaluation)
- [Rubric-Graded Benchmarks](#rubric-graded-benchmarks)
- [Datasets](#datasets)
- [Human Annotation Rubrics and Protocols](#human-annotation-rubrics-and-protocols)
- [Domain-Specific Rubric RL](#domain-specific-rubric-rl)
- [Frontier-Lab Post-Training Recipes](#frontier-lab-post-training-recipes)
- [Surveys](#surveys)
- [Tooling, Frameworks, and Leaderboards](#tooling-frameworks-and-leaderboards)
- [Blogs, Explainers, and Living Documents](#blogs-explainers-and-living-documents)
- [Project Pages, Repos, and Useful Links](#project-pages-repos-and-useful-links)
- [Contributing](#contributing)
- [Citation](#citation)

## Quick Start by Goal

| Goal | Start with | Then read |
|---|---|---|
| New to the area | [Rubrics as Rewards](https://arxiv.org/abs/2507.17746), [Reinforcement Learning with Rubric Anchors](https://arxiv.org/abs/2508.12790) | [Checklists Are Better Than Reward Models](https://arxiv.org/abs/2507.18624), [From Holistic Evaluation to Structured Criteria](https://arxiv.org/abs/2606.08625) |
| Training a policy with rubric rewards | [Rubrics as Rewards](https://arxiv.org/abs/2507.17746), [Breaking the Exploration Bottleneck](https://arxiv.org/abs/2508.16949) | [Focal Reward](https://arxiv.org/abs/2605.26579), [PAPO](https://arxiv.org/abs/2603.26535), [Not Every Rubric Teaches Equally](https://arxiv.org/abs/2605.20164) |
| Generating rubrics automatically | [OpenRubrics](https://arxiv.org/abs/2510.07743), [Auto-Rubric](https://arxiv.org/abs/2510.17314) | [Rethinking Rubric Generation](https://arxiv.org/abs/2602.05125), [Online Rubrics Elicitation](https://arxiv.org/abs/2510.07284) |
| Building a rubric-conditioned reward model | [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507), [RM-R1](https://arxiv.org/abs/2505.02387) | [C2](https://arxiv.org/abs/2604.13618), [Prometheus](https://arxiv.org/abs/2310.08491) |
| Worried about reward hacking | [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474), [Rubrics as an Attack Surface](https://arxiv.org/abs/2602.13576) | [RIFT](https://arxiv.org/abs/2604.01375), [Reinforcement Learning with Robust Rubric Rewards](https://arxiv.org/abs/2605.30244) |
| Working on image or video generation | [VisionReward](https://arxiv.org/abs/2412.21059), [RubricRL](https://arxiv.org/abs/2511.20651) | [AutoRubric-T2I](https://arxiv.org/abs/2605.17602), [DeltaRubric](https://arxiv.org/abs/2605.09269), [Omni-RRM](https://arxiv.org/abs/2602.00846) |
| Working on agents or computer use | [Agentic Rubrics as Contextual Verifiers](https://arxiv.org/abs/2601.04171), [CM2](https://arxiv.org/abs/2602.12268) | [ARCO](https://arxiv.org/abs/2606.21262), [SeekJudge](https://arxiv.org/abs/2607.23263), [The Art of Building Verifiers](https://arxiv.org/abs/2604.06240) |
| Evaluating with rubrics | [HealthBench](https://arxiv.org/abs/2505.08775), [PaperBench](https://arxiv.org/abs/2504.01848) | [ProfBench](https://arxiv.org/abs/2510.18941), [RubricEval](https://arxiv.org/abs/2603.25133), [PReMISE](https://arxiv.org/abs/2605.30803) |

## Start Here

The fastest reading path through the area:

1. **The founding trio.** [Rubrics as Rewards](https://arxiv.org/abs/2507.17746), [Reinforcement Learning with Rubric Anchors](https://arxiv.org/abs/2508.12790), and [Checklists Are Better Than Reward Models](https://arxiv.org/abs/2507.18624) landed within weeks of each other in mid-2025 and are the near-universal citation anchors. Almost every later paper cites at least one.
2. **Why rubrics instead of a reward model.** [Chasing the Tail](https://arxiv.org/abs/2509.21500) shows where scalar reward models fail on fine gradations that a written criterion can name.
3. **Where the criteria come from.** [OpenRubrics](https://arxiv.org/abs/2510.07743) mines them contrastively from preference pairs; [Auto-Rubric](https://arxiv.org/abs/2510.17314) distills them from implicit reward-model weights.
4. **Making the reward hold up.** [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507) anchors criteria causally so the reward tracks the intended construct rather than spurious cues.
5. **How it breaks.** [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) separates verifier failure from rubric-design failure; [Rubrics as an Attack Surface](https://arxiv.org/abs/2602.13576) shows judges can be drifted deliberately.
6. **The judge underneath.** [Prometheus](https://arxiv.org/abs/2310.08491) established rubric-conditioned open evaluators; [RM-R1](https://arxiv.org/abs/2505.02387) turns reward modeling into chain-of-rubrics reasoning.
7. **Beyond text.** [VisionReward](https://arxiv.org/abs/2412.21059) is the cross-cutting image-and-video anchor; [RubricRL](https://arxiv.org/abs/2511.20651) and [DeltaRubric](https://arxiv.org/abs/2605.09269) show prompt-adaptive criteria for visual generation.
8. **Agents.** [Agentic Rubrics as Contextual Verifiers](https://arxiv.org/abs/2601.04171) and [DR Tulu](https://arxiv.org/abs/2511.19399) are the flagships for software engineering and deep research respectively.
9. **The survey.** [The Rules of the Game: A Survey of Rubrics for Large Language Models](https://openreview.net/forum?id=FnSimngGYk) organizes the field into construction, training, and evaluation.

## Taxonomy

Many papers fit multiple categories. The tables below are for orientation, not strict partitioning.

### By where the criteria come from

| Origin | Typical papers |
|---|---|
| Human- or expert-authored | [Rubric Anchors](https://arxiv.org/abs/2508.12790), [HealthBench](https://arxiv.org/abs/2505.08775), [PRBench (Professional Reasoning)](https://arxiv.org/abs/2511.11562), [ComplexConstraints](https://arxiv.org/abs/2606.09118) |
| Model-generated, task-level | [RubricHub](https://arxiv.org/abs/2601.08430), [ARES](https://arxiv.org/abs/2605.23454), [OptimSyn](https://arxiv.org/abs/2604.00536) |
| Model-generated, instance-specific | [Qworld](https://arxiv.org/abs/2603.23522), [WritingBench](https://arxiv.org/abs/2503.05244), [TICK](https://arxiv.org/abs/2410.03608), [DyCoRM](https://arxiv.org/abs/2605.25876) |
| Contrastively mined from preferences | [OpenRubrics](https://arxiv.org/abs/2510.07743), [CDRRM](https://arxiv.org/abs/2603.08035), [Auto-Rubric](https://arxiv.org/abs/2510.17314), [C2](https://arxiv.org/abs/2604.13618) |
| Self-generated by the policy | [Self-Rewarding Rubric-Based RL](https://arxiv.org/abs/2509.25534), [Think-with-Rubrics](https://arxiv.org/abs/2605.07461), [EvoRubric](https://arxiv.org/abs/2605.29847) |
| Spec-, policy-, or constitution-derived | [Constitutional AI](https://arxiv.org/abs/2212.08073), [Deliberative Alignment](https://arxiv.org/abs/2412.16339), [Rule Based Rewards](https://arxiv.org/abs/2411.01111) |
| Reference- or evidence-derived | [DEEPRUBRIC](https://arxiv.org/abs/2606.17029), [RefGrader](https://arxiv.org/abs/2510.09021), [RubricRAG](https://arxiv.org/abs/2603.20882) |

### By what applies the criteria

| Applier | Typical papers |
|---|---|
| LLM or VLM judge | [Prometheus](https://arxiv.org/abs/2310.08491), [G-Eval](https://arxiv.org/abs/2303.16634), [MLLM-as-a-Judge](https://arxiv.org/abs/2402.04788) |
| Trained rubric-conditioned reward model | [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507), [C2](https://arxiv.org/abs/2604.13618) |
| Process reward model, step-level | [Step-wise Rubric Rewards](https://arxiv.org/abs/2605.17291), [Dynamic and Generalizable PRM](https://arxiv.org/abs/2507.17849), [VisualPRM](https://arxiv.org/abs/2503.10291) |
| Programmatic verifier or rule engine | [Rule Based Rewards](https://arxiv.org/abs/2411.01111), [IFEval](https://arxiv.org/abs/2311.07911), [TRON](https://arxiv.org/abs/2606.01599) |
| Agentic evaluator dispatching tools | [VISTA](https://arxiv.org/abs/2510.15831), [SeekJudge](https://arxiv.org/abs/2607.23263), [VideoWeaver](https://arxiv.org/abs/2606.08091) |
| Hybrid routing across the above | [RLR3](https://arxiv.org/abs/2605.30244), [SCRIBE](https://arxiv.org/abs/2601.03555), [StitchCUDA](https://arxiv.org/abs/2603.02637) |

### By what evidence the criteria are checked against

A separate axis from the applier — the same judge can read a candidate alone, a reference, retrieved sources, or live environment state.

| Evidence | Typical papers |
|---|---|
| Candidate output alone | [Rubrics as Rewards](https://arxiv.org/abs/2507.17746), [Checklists Are Better Than Reward Models](https://arxiv.org/abs/2507.18624) |
| Reference answer or source text | [From Rubrics to Reliable Scores](https://arxiv.org/abs/2601.08654), [LLM-Rubric](https://arxiv.org/abs/2501.00274) |
| Retrieved external evidence | [ARBOR](https://arxiv.org/abs/2606.03239), [DR Tulu](https://arxiv.org/abs/2511.19399) |
| Environment or execution state | [OpenComputer](https://arxiv.org/abs/2605.19769), [MCP-Universe](https://arxiv.org/abs/2508.14704), [Interactive Reward Agent](https://arxiv.org/abs/2607.25904) |
| Geometry, physics, or sensor signal | [VIGOR](https://arxiv.org/abs/2603.16271), [PhyGround](https://arxiv.org/abs/2605.10806), [CamVerse](https://arxiv.org/abs/2512.02870) |

### By how criteria aggregate into a signal

| Aggregation | Typical papers |
|---|---|
| Binary checklist fraction | [Checklists Are Better Than Reward Models](https://arxiv.org/abs/2507.18624), [CM2](https://arxiv.org/abs/2602.12268), [GAMUT](https://arxiv.org/abs/2607.19322) |
| Point-weighted sum | [Rubrics as Rewards](https://arxiv.org/abs/2507.17746), [HealthBench](https://arxiv.org/abs/2505.08775) |
| Learned aggregator or expert gate | [ArmoRM](https://arxiv.org/abs/2406.12845), [MJ-VIDEO](https://arxiv.org/abs/2502.01719) |
| Dynamic or policy-aware reweighting | [Not Every Rubric Teaches Equally](https://arxiv.org/abs/2605.20164), [Focal Reward](https://arxiv.org/abs/2605.26579), [Learning What Matters](https://arxiv.org/abs/2604.05445) |
| Pairwise with criteria | [Open Rubric System](https://arxiv.org/abs/2602.14069), [DyCoRM](https://arxiv.org/abs/2605.25876) |
| Hierarchical or tree-structured | [Legal Issue Tree Rubrics](https://arxiv.org/abs/2512.01020), [QUEST](https://arxiv.org/abs/2605.24218), [DEEPRUBRIC](https://arxiv.org/abs/2606.17029) |
| Explicitly non-scalarized | [Alternating RL with Contextual Rubric Rewards](https://arxiv.org/abs/2603.15646), [Probabilistic Graphical Reward Aggregation](https://arxiv.org/abs/2606.03361) |

### By modality

| Modality | Typical papers |
|---|---|
| Text | the bulk of this list |
| Image generation | [RubricRL](https://arxiv.org/abs/2511.20651), [AutoRubric-T2I](https://arxiv.org/abs/2605.17602), [SpatialReward](https://arxiv.org/abs/2603.22228) |
| Video | [VisionReward](https://arxiv.org/abs/2412.21059), [Claim-Level Rubric Rewards](https://arxiv.org/abs/2607.05150) |
| Audio and music | [Evolving Rubrics for Audio Reasoning](https://arxiv.org/abs/2608.02831), [AnyAudio-Judge](https://arxiv.org/abs/2606.03116), [PrismAudio](https://arxiv.org/abs/2511.18833) |
| 3D | [CREward](https://arxiv.org/abs/2511.19995), [3DGen-Bench](https://arxiv.org/abs/2503.21745) |
| GUI and computer use | [SeekJudge](https://arxiv.org/abs/2607.23263), [OSReward](https://arxiv.org/abs/2607.28609), [CUARewardBench](https://arxiv.org/abs/2510.18596) |
| Embodied and robotic | [Robo-Dopamine](https://arxiv.org/abs/2512.23703), [RoboAlign-R1](https://arxiv.org/abs/2605.03821) |

## Core Rubric Reward Papers

The papers below are the fastest way to get a working mental model of the field.

- [Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains](https://arxiv.org/abs/2507.17746) *(2025)* — Turns weighted rubric checklists directly into on-policy RL reward for non-verifiable domains.
- [Reinforcement Learning with Rubric Anchors](https://arxiv.org/abs/2508.12790) *(2025)* — Builds a large rubric bank from human, model, and hybrid authorship as anchors for open-ended RL.
- [Checklists Are Better Than Reward Models For Aligning Language Models](https://arxiv.org/abs/2507.18624) *(2025)* — Scores instruction-specific weighted checklists with a judge, replacing the scalar reward model.
- [OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment](https://arxiv.org/abs/2510.07743) *(2025)* — Contrastive generation mines rules and principles by contrasting chosen against rejected responses.
- [Auto-Rubric: Learning From Implicit Weights to Explicit Rubrics for Reward Modeling](https://arxiv.org/abs/2510.17314) *(2025)* — Distills implicit reward-model preferences into explicit compressed criteria from few preference pairs.
- [Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning](https://arxiv.org/abs/2508.16949) *(2025)* — Rubric scaffolds widen rollout diversity to counter entropy collapse in reasoning RL.
- [Chasing the Tail: Effective Rubric-based Reward Modeling for Large Language Model Post-Training](https://arxiv.org/abs/2509.21500) *(2025)* — Shows criteria-based rewards curb over-optimization by separating fine gradations of quality.
- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507) *(2025)* — Grounds reward modeling in an explicit causal model of criteria to resist reward hacking.
- [R3: Robust Rubric-Agnostic Reward Models](https://arxiv.org/abs/2505.13388) *(2025)* — Produces rubric-agnostic scores with explicit reasoning traces justifying each judgment.
- [LLM-Rubric: A Multidimensional, Calibrated Approach to Automated Evaluation of Natural Language Texts](https://arxiv.org/abs/2501.00274) *(2024)* — Answers hand-written rubric questions separately, then calibrates them per human judge into an overall score.
- [RM-R1: Reward Modeling as Reasoning](https://arxiv.org/abs/2505.02387) *(2025)* — Reframes reward modeling as chain-of-rubrics reasoning refined with verifiable-reward RL.
- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) *(2026)* — Separates judge-verifier failure from rubric-design limitation as distinct sources of divergence.
- [DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research](https://arxiv.org/abs/2511.19399) *(2025)* — Criteria co-evolve with the policy to absorb newly discovered evidence mid-training.
- [HealthBench: Evaluating Large Language Models Towards Improved Human Health](https://arxiv.org/abs/2505.08775) *(2025)* — Physician-written weighted criteria grade realistic multi-turn health conversations.
- [PaperBench: Evaluating AI's Ability to Replicate AI Research](https://arxiv.org/abs/2504.01848) *(2025)* — Hierarchically decomposes paper replication into thousands of judge-graded criteria.
- [VisionReward: Fine-Grained Multi-Dimensional Human Preference Learning for Image and Video Generation](https://arxiv.org/abs/2412.21059) *(2024)* — Decomposes preference into weighted yes/no judgment questions across many dimensions.

## Foundations

Background rather than subject matter. These explain why modern rubric rewards look the way they do; they are not themselves rubric-reward work.

### Preference modeling and RLHF background

- [Deep reinforcement learning from human preferences](https://arxiv.org/abs/1706.03741) *(2017)* — Pairwise trajectory comparisons train a reward model from a tiny fraction of labeled interactions.
- [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) *(2017)* — The policy-gradient optimizer underlying most rubric-reward RL recipes.
- [Learning to summarize from human feedback](https://arxiv.org/abs/2009.01325) *(2020)* — Trains a reward model on human comparisons, then optimizes against it with RL.
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) *(2022)* — Pairs supervised fine-tuning with policy-gradient RL against a learned reward model.
- [Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2204.05862) *(2022)* — Establishes the helpful-harmless split and the canonical open preference dataset.
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) *(2023)* — Reparameterizes the reward so preferences train the policy with no separate reward model.
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300) *(2024)* — Introduces group-relative policy optimization, the optimizer most rubric-reward work builds on.
- [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948) *(2025)* — Cold-start supervised data plus multi-stage RL on rule-verified correctness elicits reasoning.
- [WorldPM: Scaling Human Preference Modeling](https://arxiv.org/abs/2505.10527) *(2025)* — Finds emergent scaling on objective preference metrics, absent on subjective ones.
- [Skywork-Reward: Bag of Tricks for Reward Modeling in LLMs](https://arxiv.org/abs/2410.18451) *(2024)* — Curates a compact filtered preference set, showing data quality beats scale for reward accuracy.
- [Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy](https://arxiv.org/abs/2507.01352) *(2025)* — Combines human and model filtering signals to scale preference-data curation.
- [Libra: Assessing and Improving Reward Model by Learning to Think](https://arxiv.org/abs/2507.21645) *(2025)* — Trains the reward model to reason before scoring rather than regress a scalar directly.
- [ImplicitRM: Unbiased Reward Modeling from Implicit Preference Data for LLM alignment](https://arxiv.org/abs/2603.23184) *(2026)* — Learns rewards from click-like implicit signals via stratification correcting action bias.
- [Sharpe Ratio-Guided Active Learning for Preference Optimization in RLHF](https://arxiv.org/abs/2503.22137) *(2025)* — Selects preference pairs by a risk-adjusted acquisition function rather than raw uncertainty.
- [LoRe: Personalizing LLMs via Low-Rank Reward Modeling](https://arxiv.org/abs/2504.14439) *(2025)* — Decomposes per-user reward into a shared low-rank basis for efficient personalization.
- [What Makes a Reward Model a Good Teacher? An Optimization Perspective](https://arxiv.org/abs/2503.15477) *(2025)* — Shows reward-model accuracy alone fails to predict downstream RL success.

### LLM-as-a-judge origins

- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) *(2023)* — Establishes the judging protocol and catalogs position, verbosity, and self-enhancement bias.
- [G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment](https://arxiv.org/abs/2303.16634) *(2023)* — Chain-of-thought form-filling scoring, the closest precursor to rubric-style judging.
- [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132) *(2024)* — Crowdsourced pairwise human-preference arena underlying modern leaderboards.
- [From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline](https://arxiv.org/abs/2406.11939) *(2024)* — Filters arena prompts by quality criteria into a high-separability static benchmark.
- [RLAIF vs. RLHF: Scaling Reinforcement Learning from Human Feedback with AI Feedback](https://arxiv.org/abs/2309.00267) *(2023)* — Shows a judge scoring with a detailed prompt preamble matches human-labeled reward models at scale.

### Reward hacking and specification gaming before rubrics

- [Concrete Problems in AI Safety](https://arxiv.org/abs/1606.06565) *(2016)* — Names reward hacking and wrong objective functions among core open AI-safety research problems.
- [Scalable agent alignment via reward modeling: a research direction](https://arxiv.org/abs/1811.07871) *(2018)* — Proposes learning a reward function from human interaction, then optimizing it via RL.
- [The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models](https://arxiv.org/abs/2201.03544) *(2022)* — Maps how agents exploit misspecified rewards and proposes anomaly detection.
- [Defining and Characterizing Reward Hacking](https://arxiv.org/abs/2209.13085) *(2022)* — Formally defines an unhackable proxy reward, showing only trivial reward pairs satisfy it.
- [Scaling Laws for Reward Model Overoptimization](https://arxiv.org/abs/2210.10760) *(2022)* — Fits how gold-reward quality diverges once a proxy reward is over-optimized.

### Rubrics before LLMs: educational assessment

Where the word comes from. Analytic versus holistic rubrics, inter-rater reliability, and automated scoring long predate this literature and anticipate several of its findings.

- [The challenges of changing teaching assistants' grading practices: Requiring students to show evidence of understanding](https://arxiv.org/abs/2102.07295) *(2021)* — Graders handed a rubric still skip requiring evidence, tracing resistance to prior habits.
- [Designing Reliable LLM-Assisted Rubric Scoring for Constructed Responses: Evidence from Physics Exams](https://arxiv.org/abs/2604.12227) *(2026)* — Fine-grained checklist criteria improve scoring consistency more than holistic ones.
- [LLM Essay Scoring Under Holistic and Analytic Rubrics: Prompt Effects and Bias](https://arxiv.org/abs/2604.00259) *(2026)* — Compares holistic against analytic criteria prompting for effects on scoring bias.

### Single-scalar preference scorers for generative models

The immediate ancestors of criteria-decomposed visual rewards. A single learned scalar is the opposite of a rubric, which is exactly why the field moved past them.

- [ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation](https://arxiv.org/abs/2304.05977) *(2023)* — Canonical learned text-to-image reward model paired with reward-gradient fine-tuning.
- [Human Preference Score: Better Aligning Text-to-Image Models with Human Preference](https://arxiv.org/abs/2303.14420) *(2023)* — Trains a contrastive scorer on human preference data to rank generated images.
- [Pick-a-Pic: An Open Dataset of User Preferences for Text-to-Image Generation](https://arxiv.org/abs/2305.01569) *(2023)* — Open crowd-sourced preference dataset yielding a widely reused preference predictor.
- [Human Preference Score v2: A Solid Benchmark for Evaluating Human Preferences of Text-to-Image Synthesis](https://arxiv.org/abs/2306.09341) *(2023)* — Scales preference scoring across diverse generators into a reusable evaluation metric.
- [HPSv3: Towards Wide-Spectrum Human Preference Score](https://arxiv.org/abs/2508.03789) *(2025)* — Wide-spectrum preference data with an uncertainty-aware vision-language preference model.
- [Learning to Maximize Speech Quality Directly Using MOS Prediction for Neural Text-to-Speech](https://arxiv.org/abs/2011.01174) *(2020)* — Optimizes a speech model directly against a single pretrained mean-opinion-score predictor.
- [DreamReward: Text-to-3D Generation with Human Preference](https://arxiv.org/abs/2403.14613) *(2024)* — Trains a single-scalar 3D preference reward model from rating and ranking comparisons.
- [RewardDance: Reward Scaling in Visual Generation](https://arxiv.org/abs/2509.08826) *(2025)* — Reformulates the preference score as a generative yes-token probability, scaling like a vision-language model.

## Rubrics as Reward Signals for RL

The heart of the list: work where a rubric produces the training signal.

### Core algorithms

- [Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains](https://arxiv.org/abs/2507.17746) *(2025)* — Turns weighted rubric checklists into on-policy judge reward, beating Likert-scale baselines.
- [Reinforcement Learning with Rubric Anchors](https://arxiv.org/abs/2508.12790) *(2025)* — Anchors reward on a large curated criteria bank to extend verifiable RL to open-ended tasks.
- [Rubric-Grounded RL: Structured Judge Rewards for Generalizable Reasoning](https://arxiv.org/abs/2605.08061) *(2026)* — A frozen judge scores weighted criteria conditioned on grounding the policy never sees.
- [Direct Reasoning Optimization: Token-Level Reasoning Reflectivity Meets Rubric Gates for Unverifiable Tasks](https://arxiv.org/abs/2506.13351) *(2025)* — Pairs a token-level reflectivity signal with rubric gates for unverifiable reasoning.
- [Self-Rewarding Rubric-Based Reinforcement Learning for Open-Ended Reasoning](https://arxiv.org/abs/2509.25534) *(2025)* — The model grades its own criteria-based reward, cutting judge cost.
- [ComplexConstraints and Beyond: Expert Rubrics for RLVR](https://arxiv.org/abs/2606.09118) *(2026)* — Extends verifiable-reward RL to multi-constraint instructions via expert criteria decomposition.
- [Think-with-Rubrics: From External Evaluator to Internal Reasoning Guidance](https://arxiv.org/abs/2605.07461) *(2026)* — Has the model generate its own criteria before answering, folding evaluation into the reasoning chain.
- [Open Rubric System: Scaling Reinforcement Learning with Pairwise Adaptive Rubric](https://arxiv.org/abs/2602.14069) *(2026)* — Instantiates pairwise adaptive criteria from two candidates' semantic differences on the fly.
- [Bootstrapping Post-training Signals for Open-ended Tasks via Rubric-based Self-play on Pre-training Text](https://arxiv.org/abs/2604.20051) *(2026)* — Self-play over raw pretraining text bootstraps criteria reward with no labels.
- [Rubric-based On-policy Distillation](https://arxiv.org/abs/2605.07396) *(2026)* — Scores student rollouts against generated weighted criteria instead of matching teacher logits.
- [ARCANE: A Multi-Agent Framework for Interpretable and Configurable Alignment](https://arxiv.org/abs/2512.06196) *(2025)* — Represents stakeholder preferences as weighted verifiable criteria generated per request, optimized by regularized policy updates.
- [Prompt-Level Reward Specifications for Open-Ended Post-Training](https://arxiv.org/abs/2605.29275) *(2026)* — Separates reward specification from computation, building reusable task-adaptive criteria and executable hard-constraint checkers offline.
- [Improving Data and Reward Design for Scientific Reasoning in Large Language Models](https://arxiv.org/abs/2602.08321) *(2026)* — Builds fine-grained criteria for open-ended science answers and trains against them for stability.
- [RLBFF: Binary Flexible Feedback to bridge between Human Feedback & Verifiable Rewards](https://arxiv.org/abs/2509.21319) *(2025)* — Converts free-text human feedback into binary principles usable as verifiable-style rewards.
- [Video Models Can Reason with Verifiable Rewards](https://arxiv.org/abs/2605.15458) *(2026)* — Recasts video generation as verifiable trajectories optimized against dense decomposed rule-based rewards.
- [Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234) *(2026)* — Splits a terminal video reward into timestep-aware credit across visual quality, motion, and alignment.
- [WorldCompass: Reinforcement Learning for Long-Horizon World Models](https://arxiv.org/abs/2602.09022) *(2026)* — Pairs an interaction-following accuracy reward with a visual-quality reward to resist hacking.
- [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899) *(2026)* — Uses criteria as a shared interface across agent, judge, and memory in a meta-RL loop.
- [Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning](https://arxiv.org/abs/2511.12344) *(2025)* — Criteria-driven dense rewards widen exploration across several reasoning domains at once.
- [When Rubrics Fail: Error Enumeration as Reward in Reference-Free RL Post-Training for Virtual Try-On](https://arxiv.org/abs/2603.05659) *(2026)* — Counts severity-weighted errors across task-relevant axes where no ideal reference answer exists.
- [ACE-RL: Adaptive Constraint-Enhanced Reward for Long-form Generation Reinforcement Learning](https://arxiv.org/abs/2509.04903) *(2025)* — Decomposes each instruction into adaptive fine-grained constraint criteria whose satisfaction becomes the reward.

### Exploration, stability, and aggregation

- [Breaking the Exploration Bottleneck: Rubric-Scaffolded Reinforcement Learning for General LLM Reasoning](https://arxiv.org/abs/2508.16949) *(2025)* — Rubric scaffolds widen rollout diversity to counter entropy collapse.
- [Not Every Rubric Teaches Equally: Policy-Aware Rubric Rewards for RLVR](https://arxiv.org/abs/2605.20164) *(2026)* — Reweights criteria by how strongly each currently discriminates the policy's own rollouts.
- [Focal Reward: Balanced Reinforcement Learning under Rubric-Based Rewards](https://arxiv.org/abs/2605.26579) *(2026)* — Adaptively reweights criteria so easy items stop dominating the gradient.
- [PAPO: Stabilizing Rubric Integration Training via Decoupled Advantage Normalization](https://arxiv.org/abs/2603.26535) *(2026)* — Normalizes criteria-process and outcome advantages separately to stop hacking-driven instability.
- [Alternating Reinforcement Learning with Contextual Rubric Rewards: Beyond the Scalarization Strategy](https://arxiv.org/abs/2603.15646) *(2026)* — Partitions criteria into meta-classes, avoiding scalarized weighted-sum aggregation.
- [Mitigating False Credit Propagation: Probabilistic Graphical Reward Aggregation for Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.03361) *(2026)* — A graphical model over criterion prerequisites withholds credit when a licensing condition went unmet.
- [Tournament-GRPO: Group-Wise Tournament Rewards for Reinforcement Learning in Open-Ended Long-Form Generation](https://arxiv.org/abs/2605.26958) *(2026)* — Criteria-guided tournaments among same-query rollouts produce normalized group rewards.
- [LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](https://arxiv.org/abs/2607.18110) *(2026)* — Distills judge critiques into reusable experiential knowledge instead of scalarizing criteria into one reward.
- [ArenaRL: Scaling RL for Open-Ended Agents via Tournament-based Relative Ranking](https://arxiv.org/abs/2601.06487) *(2026)* — Multi-level criteria drive pairwise tournament ranking in place of pointwise scalar scoring.
- [Experience is the Best Teacher: Motivating Effective Exploration in Reinforcement Learning for LLMs](https://arxiv.org/abs/2603.20046) *(2026)* — Treats rollouts that miss criteria as hindsight guidance, bonusing high-improvement responses.
- [RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://arxiv.org/abs/2602.21628) *(2026)* — Stratifies criteria by model competence to weight curriculum rewards across stages.
- [SCRIBE: Structured Mid-Level Supervision for Tool-Using Language Models](https://arxiv.org/abs/2601.03555) *(2026)* — Routes subgoals to skill-prototype verifiers instead of one monolithic judge, cutting variance.

### Self-evolving and adaptive rubrics

Note the naming hazard: **EvoRubric**, **EvoRubrics**, and **EvoLM** are three different papers with near-identical framing.

- [EvoRubric: Self-Evolving Rubric-Driven RL for Open-Ended Generation](https://arxiv.org/abs/2605.29847) *(2026)* — A meta-verifier, variance pruning, and peer consensus keep self-evolving criteria from collapsing.
- [EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolution for LLM Reinforcement Learning](https://arxiv.org/abs/2606.23038) *(2026)* — Adversarial co-evolution keeps criteria pace with emerging policy exploits.
- [EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics](https://arxiv.org/abs/2605.03871) *(2026)* — Alternately trains a discriminative criteria generator and the policy from its own outputs.
- [SERPO: Self-Evolving Rubric Policy Optimization for Open-Ended Test-Time Reinforcement Learning](https://arxiv.org/abs/2607.26873) *(2026)* — Evolves criteria at test time with no offline rubric set or external reward model.
- [SibylSense: Adaptive Rubric Learning via Memory Tuning and Adversarial Probing](https://arxiv.org/abs/2602.20751) *(2026)* — Alternates memory-bank updates with adversarial probing to expose new quality gaps.
- [Reinforcing Chain-of-Thought Reasoning with Self-Evolving Rubrics](https://arxiv.org/abs/2602.10885) *(2026)* — Rewards reasoning with self-proposed criteria that evolve alongside the policy.
- [Compute as Teacher: Turning Inference Compute Into Reference-Free Supervision](https://arxiv.org/abs/2509.14234) *(2025)* — Rewards the fraction of self-proposed binary auditable criteria an independent judge marks satisfied.
- [LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiable RL](https://arxiv.org/abs/2607.04412) *(2026)* — Appends difficulty-raising constraints to prompts so criteria-based reward stays discriminative as the policy improves.

### Process, step, and token-level rubric credit

- [Step-wise Rubric Rewards for LLM Reasoning](https://arxiv.org/abs/2605.17291) *(2026)* — Attributes each criterion to the reasoning step responsible, decoupled from outcome scoring.
- [Rubrics to Tokens: Bridging Response-level Rubrics and Token-level Rewards in Instruction Following Tasks](https://arxiv.org/abs/2604.02795) *(2026)* — Pushes response-level criteria scores down to token-level reward assignment.
- [Rubric-Guided Process Reward for Stepwise Model Routing](https://arxiv.org/abs/2605.29310) *(2026)* — Routes reasoning steps to specialist sub-models using per-step criteria rewards.
- [Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards](https://arxiv.org/abs/2510.07774) *(2025)* — Grades whole reasoning trajectories against problem-specific criteria to penalize unjustified leaps.
- [Rethinking Reward Supervision: Rubric-Conditioned Self-Distillation](https://arxiv.org/abs/2606.19327) *(2026)* — Distills criteria-conditioned teacher judgments into the policy without an online verifier.
- [Rubric-Guided Self-Distillation: Post-Training Without Rubric Verifiers](https://arxiv.org/abs/2606.12507) *(2026)* — Distills a rubric-conditioned policy into an unconditioned student, with no verifier even at training time.
- [CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization](https://arxiv.org/abs/2607.25659) *(2026)* — Contrasts criteria-conditioned against criteria-free scoring on replayed rollouts to redistribute token-level credit.
- [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277) *(2025)* — Step-level process reward model for web navigation trained on annotated per-step checklists.
- [Chaining the Evidence: Robust Reinforcement Learning for Deep Search Agents with Citation-Aware Rubric Rewards](https://arxiv.org/abs/2601.06021) *(2026)* — Decomposes search questions into single-hop criteria scored on citations and evidence chains.
- [CriPO: Enhancing Rubric-based RL via Self-Distillation](https://arxiv.org/abs/2607.18082) *(2026)* — On-policy self-distillation fixes unexplored and suppressed criteria.

## Rubric Construction

Where criteria come from is its own research problem. The four-way split below follows [the survey](https://openreview.net/forum?id=FnSimngGYk).

### Direct generation

- [RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation](https://arxiv.org/abs/2601.08430) *(2026)* — Coarse-to-fine generation combining principle-guided synthesis and multi-model aggregation.
- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454) *(2026)* — Co-generates questions, references, and weighted criteria from raw documents in one pass.
- [Qworld: Question-Specific Evaluation Criteria for LLMs](https://arxiv.org/abs/2603.23522) *(2026)* — Builds per-question criteria via a recursive expansion tree of scenarios and binary checks.
- [SedarEval: Automated Evaluation using Self-Adaptive Rubrics](https://arxiv.org/abs/2501.15595) *(2025)* — Generates per-question rubrics carrying explicit scoring and deduction points, then trains a matching evaluator.
- [Rubric Is All You Need: Enhancing LLM-based Code Evaluation With Question-Specific Rubrics](https://arxiv.org/abs/2503.23989) *(2025)* — Grades code with per-problem criteria rather than one question-agnostic rubric.
- [Configurable Preference Tuning with Rubric-Guided Synthetic Data](https://arxiv.org/abs/2506.11702) *(2025)* — Generates synthetic preference data from structured criteria so behavior is modulated by prompt directives.
- [AutoLibra: Agent Metric Induction from Open-Ended Human Feedback](https://arxiv.org/abs/2505.02820) *(2025)* — Turns free-text feedback on agent trajectories into concrete clustered evaluation metrics.
- [RubricRAG: Towards Interpretable and Reliable LLM Evaluation via Domain Knowledge Retrieval for Rubric Generation](https://arxiv.org/abs/2603.20882) *(2026)* — Retrieves criteria from related queries at inference time to ground evaluation.
- [Many Voices, One Reward: Multi-Role Rubric Generation for LLM Judging and Reward Modeling](https://arxiv.org/abs/2607.01830) *(2026)* — Elicits criteria from complementary evaluator roles into one auditable scorer.
- [Automated Rubrics for Reliable Evaluation of Medical Dialogue Systems](https://arxiv.org/abs/2601.15161) *(2026)* — Retrieval-augmented multi-agent pipeline decomposes medical evidence into atomic-fact criteria per instance.
- [Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling](https://arxiv.org/abs/2602.06795) *(2026)* — Builds granular reasoning-error taxonomies to train domain-adaptive classifiers.
- [Rubric-as-Experts: Case-Specific MQM Rubrics for Translation Quality Evaluation](https://arxiv.org/abs/2606.21559) *(2026)* — Instantiates case-specific criteria from a generic translation-quality framework.
- [Two-Level Meta-Rubrics for Evaluating Open-Ended Generation: GAMUT, a Benchmark for Factual Completeness](https://arxiv.org/abs/2607.19322) *(2026)* — An expressive meta-rubric compiles into a flat binary machine-gradable checklist.
- [PREFINE: Personalized Story Generation via Simulated User Critics and User-Specific Rubric Generation](https://arxiv.org/abs/2510.21721) *(2025)* — Simulated user critics generate personalized criteria steering story generation.
- [EvalLM: Interactive Evaluation of Large Language Model Prompts on User-Defined Criteria](https://arxiv.org/abs/2309.13633) *(2023)* — An interactive workbench lets developers author and revise evaluation criteria while diagnosing prompts.

### Contrastive generation

- [OpenRubrics: Towards Scalable Synthetic Rubric Generation for Reward Modeling and LLM Alignment](https://arxiv.org/abs/2510.07743) *(2025)* — Mines hard rules and implicit principles by contrasting preferred against rejected responses.
- [Auto-Rubric: Learning From Implicit Weights to Explicit Rubrics for Reward Modeling](https://arxiv.org/abs/2510.17314) *(2025)* — Distills implicit preferences into explicit compressed criteria from few preference pairs.
- [CDRRM: Contrast-Driven Rubric Generation for Reliable and Interpretable Reward Modeling](https://arxiv.org/abs/2603.08035) *(2026)* — Generates criteria by contrasting response pairs, then scores against the result.
- [C2: Scalable Rubric-Augmented Reward Modeling from Binary Preferences](https://arxiv.org/abs/2604.13618) *(2026)* — Trains a cooperative generator-verifier pair from binary preferences alone.
- [Learning Query-Specific Rubrics from Human Preferences for DeepResearch Report Generation](https://arxiv.org/abs/2602.03619) *(2026)* — Trains criteria generators by RL on human preference data over research reports.
- [Support Vector Rubrics: Closing the Gap Between Self-Generated and Human Rubrics](https://arxiv.org/abs/2606.08077) *(2026)* — Recasts rubric construction as max-margin boundary learning over preference data.
- [CritiQ: Mining Data Quality Criteria from Human Preferences](https://arxiv.org/abs/2502.19279) *(2025)* — Mines explicit data-quality criteria from preference judgments instead of hand-crafted rules.

### Iterative refinement

- [Rethinking Rubric Generation for Improving LLM Judge and Reward Modeling for Open-ended Tasks](https://arxiv.org/abs/2602.05125) *(2026)* — Decomposes coarse criteria into finer ones and reweights by inter-criterion correlation.
- [HD-Eval: Aligning Large Language Model Evaluators Through Hierarchical Criteria Decomposition](https://arxiv.org/abs/2402.15754) *(2024)* — Iteratively decomposes evaluation into finer criteria, pruning insignificant ones by preference-guided attribution.
- [Generating and Refining Dynamic Evaluation Rubrics for LLM-as-a-Judge](https://arxiv.org/abs/2605.30568) *(2026)* — A meta-judge reward signal iteratively fine-tunes a criteria generator without annotation.
- [Confusion-Aware Rubric Optimization for LLM-based Automated Grading](https://arxiv.org/abs/2603.00451) *(2026)* — Diagnoses grading errors via confusion-matrix analysis, then synthesizes targeted fixes.
- [OptimSyn: Influence-Guided Rubrics Optimization for Synthetic Data Generation](https://arxiv.org/abs/2604.00536) *(2026)* — Uses gradient-based influence estimates to optimize synthetic-data criteria.
- [Feedback-to-Rubrics: Can We Learn Expert Criteria from Inline Comments?](https://arxiv.org/abs/2605.29857) *(2026)* — Iteratively refines criteria by observing comment-wise mismatches against accumulated human feedback.
- [AdaRubric: Task-Adaptive Rubrics for Reliable LLM Agent Evaluation and Reward Learning](https://arxiv.org/abs/2603.21362) *(2026)* — Generates task-adaptive criteria on the fly without manual design.
- [iRULER: Intelligible Rubric-Based User-Defined LLM Evaluation for Revision](https://arxiv.org/abs/2602.12779) *(2026)* — Scaffolds writing review by user-defined criteria, refining them through a rubric-of-rubrics loop.
- [ARISE: Agentic Rubric-Guided Iterative Survey Engine for Automated Scholarly Paper Generation](https://arxiv.org/abs/2511.17689) *(2025)* — Reviewer agents grade drafted surveys against a behaviorally anchored rubric inside a refinement loop.
- [Automated Refinement of Essay Scoring Rubrics for Language Models via Reflect-and-Revise](https://arxiv.org/abs/2510.09030) *(2025)* — Models iteratively refine their own scoring criteria by reflecting on discrepancies with human scores.
- [LLM-based Automated Grading with Human-in-the-Loop](https://arxiv.org/abs/2504.05239) *(2025)* — Poses clarifying questions to human experts to dynamically refine grading criteria.
- [Redefining Quality Criteria and Distance-Aware Score Modeling for Image Editing Assessment](https://arxiv.org/abs/2604.12175) *(2026)* — Optimizes the evaluation-criteria prompts themselves via probabilistic feedback instead of hand-written metric definitions.
- [Learnable Assessment Skills for LLM-based Automated Scoring: Rubric Construction via Iterative Optimization](https://arxiv.org/abs/2605.29274) *(2026)* — Optimizes a reusable instruction for building rubrics from scoring errors, learning item-agnostic construction rules rather than one rubric per item.

### Online and co-evolving generation

- [Online Rubrics Elicitation from Pairwise Comparisons](https://arxiv.org/abs/2510.07284) *(2025)* — Curates criteria live during training from current-versus-reference policy comparisons.
- [QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards](https://arxiv.org/abs/2606.03968) *(2026)* — Constructs queries and criteria jointly to reduce hallucinated or ungrounded criteria.
- [Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training](https://arxiv.org/abs/2602.01511) *(2026)* — Treats criteria generation as a latent RL action alternated against judge training.
- [RUBRIC-ARROW: Alternating Pointwise Rubric Reward Modeling for LLM Post-training in Non-verifiable Domains](https://arxiv.org/abs/2605.29156) *(2026)* — Alternating training jointly optimizes a generator and a criteria-conditioned pointwise judge.
- [RLAC: Reinforcement Learning with Adversarial Critic for Free-Form Generation Tasks](https://arxiv.org/abs/2511.01758) *(2025)* — An adversarial critic hunts likely failure modes instead of checking exhaustive checklists.
- [ARCO: Adaptive Rubrics with Co-Evolution for Multi-Step LLM-Based Agents](https://arxiv.org/abs/2606.21262) *(2026)* — Co-evolves criteria alongside the agent policy across multi-step trajectories.
- [MIRA: Mid-training Rubric Anchoring for Source-Aware Data Selection](https://arxiv.org/abs/2605.30288) *(2026)* — Discovers per-source criteria from a teacher's judgments, then distills them into scorers.
- [Auto-Prompt Ensemble for LLM Judge](https://arxiv.org/abs/2510.06538) *(2025)* — Learns auxiliary evaluation dimensions from a judge's own failure cases, ensembled by confidence.
- [CARMO: Dynamic Criteria Generation for Context-Aware Reward Modelling](https://arxiv.org/abs/2410.21545) *(2024)* — Generates query-specific criteria to ground reward scores instead of reusing a static rubric.
- [GrowLoop: Self-Evolving Conversation Evaluation Seeded by Human](https://arxiv.org/abs/2605.28882) *(2026)* — Rubric-case co-evolution grows conversation evaluation criteria from minimal human seeds as models improve.
- [Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents](https://arxiv.org/abs/2607.12790) *(2026)* — Evolves compositions of typed drawback detectors into an inspectable grading expression validated against anchored references.
- [Co-Evolving LLM Evaluators and Policies via DynamicRubric](https://arxiv.org/abs/2607.20083) *(2026)* — Generates weighted binary criteria conditioned on the candidate response set, keeping score gaps informative.

## Checklists, Principles, Constitutions, and Specs

Structurally rubrics under different names.

### Checklist feedback as reward

- [Checklists Are Better Than Reward Models For Aligning Language Models](https://arxiv.org/abs/2507.18624) *(2025)* — Scores instruction-derived checklist items with judges plus verifier programs.
- [IF-CRITIC: Towards a Fine-Grained LLM Critic for Instruction-Following Evaluation](https://arxiv.org/abs/2511.01014) *(2025)* — Decomposes instructions into constraint checklists for a constraint-level critic.
- [TICKing All the Boxes: Generated Checklists Improve LLM Evaluation and Generation](https://arxiv.org/abs/2410.03608) *(2024)* — Auto-generated per-instruction checklists raise agreement over holistic scoring.
- [AutoChecklist: Composable Pipelines for Checklist Generation and Scoring with LLM-as-a-Judge](https://arxiv.org/abs/2603.07019) *(2026)* — Modular generator-refiner-scorer pipeline with several criteria-derivation strategies.
- [RocketEval: Efficient Automated LLM Evaluation via Grading Checklist](https://arxiv.org/abs/2503.05142) *(2025)* — Reframes evaluation as instance-specific checklist grading by lightweight judges, reweighted against human labels.
- [RubRIX: Rubric-Driven Risk Mitigation in Caregiver-AI Interactions](https://arxiv.org/abs/2601.13235) *(2026)* — Scores caregiving responses across five clinician-validated ethical-care risk dimensions, guiding iterative refinement.
- [Checklist Engineering Empowers Multilingual LLM Judges](https://arxiv.org/abs/2507.06774) *(2025)* — Training-free checklist prompting brings small multilingual judges to frontier-judge agreement.
- [CheckEval: A reliable LLM-as-a-Judge framework for evaluating text generation using checklists](https://arxiv.org/abs/2403.18771) *(2024)* — Replaces subjective Likert scoring with decomposed binary checklist questions to cut rating variance.
- [CM2: Reinforcement Learning with Checklist Rewards for Multi-Turn and Multi-Step Agentic Tool Use](https://arxiv.org/abs/2602.12268) *(2026)* — Decomposes each turn into binary checklist criteria with grounded evidence.
- [EvoIdeator: Evolving Scientific Ideas through Checklist-Grounded Reinforcement Learning](https://arxiv.org/abs/2603.21728) *(2026)* — Evolves research ideas against checklist-grounded span-level rewards rather than global scalar scores.
- [P-Check: Advancing Personalized Reward Model via Learning to Generate Dynamic Checklist](https://arxiv.org/abs/2601.02986) *(2026)* — Trains a generator synthesizing per-user dynamic checklists for personalized reward.
- [WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild](https://arxiv.org/abs/2406.04770) *(2024)* — Grades real user tasks with per-query generated checklists.

### Constitutions and principle-following

- [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) *(2022)* — Self-critique and revision against written principles replace human harm labels.
- [Collective Constitutional AI: Aligning a Language Model with Public Input](https://arxiv.org/abs/2406.07814) *(2024)* — Crowdsources constitution principles from public deliberation before preference training.
- [Specific versus General Principles for Constitutional AI](https://arxiv.org/abs/2310.13798) *(2023)* — Compares narrow written principles against a single broad one for suppressing subtle harmful behaviors.
- [Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming](https://arxiv.org/abs/2501.18837) *(2025)* — Trains input and output classifiers from an explicit allowed-content constitution.
- [Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks](https://arxiv.org/abs/2601.04603) *(2026)* — Constitution-conditioned classifiers as production defenses at lower latency cost.
- [C3AI: Crafting and Evaluating Constitutions for Constitutional AI](https://arxiv.org/abs/2502.15861) *(2025)* — Selects and structures constitutional principles before tuning, then tests whether models follow them.
- [Inverse Constitutional AI: Compressing Preferences into Principles](https://arxiv.org/abs/2406.06560) *(2024)* — Reverse-engineers the principle set that best reconstructs a preference dataset.
- [Decoding Human Preferences in Alignment: An Improved Approach to Inverse Constitutional AI](https://arxiv.org/abs/2501.17112) *(2025)* — Improves principle extraction from preferences via better generation, clustering, and embedding.
- [Principle-Driven Self-Alignment of Language Models from Scratch with Minimal Human Supervision](https://arxiv.org/abs/2305.03047) *(2023)* — Bootstraps an aligned assistant by applying written principles in context, then fine-tuning on the outputs.
- [SALMON: Self-Alignment with Instructable Reward Models](https://arxiv.org/abs/2310.05910) *(2023)* — Trains a reward model that follows arbitrary judging principles specified at RL time.
- [RewardAnything: Generalizable Principle-Following Reward Models](https://arxiv.org/abs/2506.03637) *(2025)* — Follows arbitrary natural-language reward principles at inference time without retraining.
- [Improving alignment of dialogue agents via targeted human judgements](https://arxiv.org/abs/2209.14375) *(2022)* — Breaks dialogue safety into many natural-language rules rated separately.
- [Reflect: Transparent Principle-Guided Reasoning for Constitutional Alignment at Scale](https://arxiv.org/abs/2601.18730) *(2026)* — Aligns purely at inference time via constitution-conditioned drafting then self-revision.
- [Beyond Preferences: Learning Alignment Principles Grounded in Human Reasons and Values](https://arxiv.org/abs/2601.18760) *(2026)* — Extracts principles from the stated reasons behind preferences rather than labels alone.
- [Latent Principle Discovery for Language Model Self-Improvement](https://arxiv.org/abs/2505.16927) *(2025)* — Mines and clusters implicit principles from self-improvement traces.

### Specs and instruction hierarchies

- [OpenAI Model Spec](https://model-spec.openai.com/) — Public behavioral specification with worked examples, used as a target for training and evaluation.
- [Claude's Constitution](https://www.anthropic.com/constitution) — Anthropic's published statement of intended values and behavior, written to shape training directly.
- [Rule Based Rewards for Language Model Safety](https://arxiv.org/abs/2411.01111) *(2024)* — Composable judge-scored propositions replace human safety labels as the RL reward.
- [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339) *(2024)* — Trains models to reason explicitly over safety-specification text before answering.
- [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208) *(2024)* — Trains on generated demonstrations so models prioritize higher-privilege instructions when sources conflict.
- [IHEval: Evaluating Language Models on Following the Instruction Hierarchy](https://arxiv.org/abs/2502.08745) *(2025)* — Benchmarks whether models correctly prioritize conflicting instructions by privilege.
- [Reasoning Up the Instruction Ladder for Controllable Language Models](https://arxiv.org/abs/2511.04694) *(2025)* — Trains explicit reasoning over instruction-privilege conflicts before responding.
- [AutoRule: Reasoning Chain-of-thought Extracted Rule-based Rewards Improve Preference Learning](https://arxiv.org/abs/2506.15651) *(2025)* — Extracts explicit rules from reasoning traces to build rule-based preference rewards.

### Instruction and constraint verification

- [Instruction-Following Evaluation for Large Language Models](https://arxiv.org/abs/2311.07911) *(2023)* — Scores outputs against programmatically verifiable constraints like counts and keywords.
- [FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models](https://arxiv.org/abs/2310.20410) *(2023)* — Stacks constraint types incrementally to measure fine-grained degradation.
- [Benchmarking Complex Instruction-Following with Multiple Constraints Composition](https://arxiv.org/abs/2407.03978) *(2024)* — Defines a taxonomy of constraint types and dimensions verified by rule-augmented evaluators.
- [VCIFBench: Evaluating Complex Instruction Following for Video Understanding](https://arxiv.org/abs/2606.04588) *(2026)* — Benchmarks constraint-rich video instructions across content, format, style, and structure.
- [InFoBench: Evaluating Instruction Following Ability in Large Language Models](https://arxiv.org/abs/2401.03601) *(2024)* — Decomposes each instruction into yes/no sub-questions for a decomposed following ratio.
- [Generalizing Verifiable Instruction Following](https://arxiv.org/abs/2507.02833) *(2025)* — Adds many held-out verifiable constraint types to test generalization.
- [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://arxiv.org/abs/2506.09942) *(2025)* — Combines rule-based constraint checking with judge-based checks as one RL reward.
- [RECAST: Expanding the Boundaries of LLMs' Complex Instruction Following with Multi-Constraint Data](https://arxiv.org/abs/2505.19030) *(2025)* — Builds multi-constraint data with per-constraint verifiable reward functions.
- [MDP-GRPO: Stabilized Group Relative Policy Optimization for Multi-Constraint Instruction Following](https://arxiv.org/abs/2606.06058) *(2026)* — Stabilizes group-relative RL under sparse discrete multi-constraint rewards.
- [Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following](https://arxiv.org/abs/2601.04954) *(2026)* — Finds verification precision, not constraint diversity, bounds generalization gains.
- [M-IFEval: Multilingual Instruction-Following Evaluation](https://arxiv.org/abs/2502.04688) *(2025)* — Extends objective judgment-free verifiable constraints to French, Japanese, and Spanish.
- [The SIFo Benchmark: Investigating the Sequential Instruction Following Ability of Large Language Models](https://arxiv.org/abs/2406.19999) *(2024)* — Verifies an entire instruction chain by checking only the final-step output.
- [AdvancedIF: Rubric-Based Benchmarking and Reinforcement Learning for Advancing LLM Instruction Following](https://arxiv.org/abs/2511.10507) *(2025)* — Chains criteria generation, verifier fine-tuning, and reward shaping into one pipeline.
- [DIALEVAL: Automated Type-Theoretic Evaluation of LLM Instruction Following](https://arxiv.org/abs/2603.03321) *(2026)* — Decomposes instructions into typed predicates whose satisfaction semantics differ by predicate type.

### Question decomposition and atomic-claim verification

- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) *(2023)* — Decomposes long-form text into atomic facts scored against a retrieval source.
- [QA-LIGN: Aligning LLMs through Constitutionally Decomposed QA](https://arxiv.org/abs/2506.08123) *(2025)* — Decomposes a scalar reward into per-principle question checks in a draft-critique-revise loop.
- [DecomposeRL: Learning to Ask Useful, Informative, and Diverse Questions for Semi-Supervised, Traceable Claim Verification](https://arxiv.org/abs/2605.27858) *(2026)* — Learns a question-decomposition policy rewarded by downstream verdict correctness.
- [Verifiable Rewards Beyond Math and Code: Lightweight Corpus-Grounded Process Supervision for Factual Question Answering](https://arxiv.org/abs/2605.29648) *(2026)* — Grounds factual reward in corpus-verified subclaims for lightweight process supervision.
- [Self-Alignment for Factuality: Mitigating Hallucinations in LLMs via Self-Evaluation](https://arxiv.org/abs/2402.09267) *(2024)* — Uses self-evaluated confidence on generated claims as a factuality training signal.
- [Agent-as-Judge for Factual Summarization of Long Narratives](https://arxiv.org/abs/2501.09993) *(2025)* — Extracts a character knowledge graph to check summary facts individually, flagging missing or erroneous ones.

## Rubric-Conditioned Reward Models

Scorers that consume or emit criteria. A reward model with several heads, or one that lands credit at token level, is not in scope here just for being fine-grained — granularity in *where* reward lands is not explicitness about *what standard* is applied. For general and dense reward models see [Adjacent collections](#adjacent-collections).

### Rubric- and criteria-conditioned reward models

- [R3: Robust Rubric-Agnostic Reward Models](https://arxiv.org/abs/2505.13388) *(2025)* — Produces rubric-agnostic scores with explicit reasoning traces justifying each judgment.
- [mR3: Multilingual Rubric-Agnostic Reward Reasoning Models](https://arxiv.org/abs/2510.01146) *(2025)* — Extends rubric-agnostic reward reasoning across dozens of languages via curriculum selection.
- [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507) *(2025)* — Uses causal criteria augmentations isolating quality attributes from superficial features.
- [Multidimensional Rubric-oriented Reward Model Learning via Geometric Projection Reference Constraints](https://arxiv.org/abs/2511.16139) *(2025)* — Aligns a medical reward model's scoring gradients with clinical reasoning via geometric projection constraints.
- [Rationale Matters: Learning Transferable Rubrics via Proxy-Guided Critique for VLM Reward Models](https://arxiv.org/abs/2603.16600) *(2026)* — Trains a proxy agent whose scoring accuracy becomes the RL reward for rubric generation.
- [A Rubric-Supervised Critic from Sparse Real-World Outcomes](https://arxiv.org/abs/2603.03800) *(2026)* — Learns a critic from sparse traces using behavioral-feature criteria, enabling rerank.
- [Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models](https://arxiv.org/abs/2602.04649) *(2026)* — A rationale-consistency metric catches models reaching right verdicts by unfaithful reasoning.
- [Preference-Aware Rubric Learning for Personalized Evaluation](https://arxiv.org/abs/2605.31545) *(2026)* — Learns individualized criteria adapting reward to a specific user's preferences.
- [Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization](https://arxiv.org/abs/2604.07343) *(2026)* — Evaluates reward models against individually tailored criteria, not one universal rubric.
- [EVALUESTEER: Measuring Reward Model Steerability Towards Values and Preferences](https://arxiv.org/abs/2510.06370) *(2025)* — Benchmarks whether reward models track a stated user value and style profile.
- [Retro*: Optimizing LLMs for Reasoning-Intensive Document Retrieval](https://arxiv.org/abs/2509.24869) *(2025)* — Scores document relevance against explicitly defined criteria, yielding interpretable fine-grained relevance.
- [Skill-RM: Unifying Heterogeneous Evaluation Criteria via Agent Skill](https://arxiv.org/abs/2606.03980) *(2026)* — Reformulates reward computation as an agentic skill orchestrating verifiers, checklists, and rubrics.
- [Beyond Holistic Scores: Automatic Trait-Based Quality Scoring of Argumentative Essays](https://arxiv.org/abs/2602.04604) *(2026)* — Scores essays on rubric-aligned traits via ordinal regression rather than one holistic number.
- [Rationale Behind Essay Scores: Enhancing S-LLM's Multi-Trait Essay Scoring with Rationale Generated by LLMs](https://arxiv.org/abs/2410.14202) *(2024)* — Generates trait-specific rationales that a smaller model uses to predict multi-trait scores.
- [CRACQ: A Multi-Dimensional Approach To Automated Document Assessment](https://arxiv.org/abs/2510.02337) *(2025)* — Scores documents on five named traits rather than collapsing them into one judgment.
- [YESciEval: Robust LLM-as-a-Judge for Scientific Question Answering](https://arxiv.org/abs/2505.14279) *(2025)* — Combines fine-grained criteria assessment with reinforcement learning to mitigate evaluator optimism bias.
- [Reward Modeling for Scientific Writing Evaluation](https://arxiv.org/abs/2601.11374) *(2026)* — Cost-efficient reward models reasoning over task-dependent multi-faceted criteria.
- [ToolRM: Towards Agentic Tool-Use Reward Modeling](https://arxiv.org/abs/2510.26167) *(2025)* — Builds tool-use preference data by rule-based scoring across multiple sampled dimensions.
- [Think Twice: Branch-and-Rethink Reasoning Reward Model](https://arxiv.org/abs/2510.23596) *(2025)* — Writes out instance-critical evaluation dimensions, then rereads the response targeting exactly those.
- [CE-RM: A Pointwise Generative Reward Model Optimized via Two-Stage Rollout and Unified Criteria](https://arxiv.org/abs/2601.20327) *(2026)* — Pointwise generative reward model scored against unified query-based criteria instead of pairwise preference.
- [P-GenRM: Personalized Generative Reward Model with Test-time User-based Scaling](https://arxiv.org/abs/2602.12116) *(2026)* — Derives per-user scoring rubrics from preference signals, transferring them across clustered user prototypes.
- [AutoSCORE: Enhancing Automated Scoring with Multi-Agent Large Language Models via Structured Component Recognition](https://arxiv.org/abs/2509.21910) *(2025)* — Structured component recognition makes automated criteria scoring decomposable.

### Multi-attribute and multi-objective reward models

- [Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts](https://arxiv.org/abs/2406.12845) *(2024)* — Trains many absolute-rating objectives then gates them per context with a router.
- [HelpSteer2: Open-source dataset for training top-performing reward models](https://arxiv.org/abs/2406.08673) *(2024)* — Multi-attribute preference data scoring several named attributes separately.
- [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704) *(2024)* — Projects hidden states into five named attributes combined by a weighted sum.
- [Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards](https://arxiv.org/abs/2402.18571) *(2024)* — Represents preferences as reward-space unit vectors for arithmetic trade-off control.
- [Beyond One-Preference-Fits-All Alignment: Multi-Objective Direct Preference Optimization](https://arxiv.org/abs/2310.03708) *(2023)* — Folds multiple weighted objectives directly into an implicit preference-trained reward.
- [Multi-Objective Reinforcement Learning from AI Feedback](https://arxiv.org/abs/2406.07295) *(2024)* — Decomposes AI feedback into multiple objectives rather than one scalar reward.
- [Projection Optimization: A General Framework for Multi-Objective and Multi-Group RLHF](https://arxiv.org/abs/2502.15145) *(2025)* — Recasts non-linear multi-objective aggregation as a series of tractable linear sub-problems.
- [General Preference Reinforcement Learning](https://arxiv.org/abs/2605.18721) *(2026)* — Replaces the scalar reward with a multi-dimensional preference embedding normalized per axis.
- [Bradley-Terry and Multi-Objective Reward Modeling Are Complementary](https://arxiv.org/abs/2507.07375) *(2025)* — Jointly trains a single-objective head and fine-grained multi-attribute heads to curb reward hacking.
- [PARM: Multi-Objective Test-Time Alignment via Preference-Aware Autoregressive Reward Model](https://arxiv.org/abs/2505.06274) *(2025)* — One autoregressive reward model conditioned on preference-dimension vectors replaces per-dimension models.
- [UniARM: Towards a Unified Autoregressive Reward Model for Multi-Objective Test-Time Alignment](https://arxiv.org/abs/2602.09538) *(2026)* — Modulates shared preference-dimension features by mixture-of-adapters to fix cross-objective entanglement.
- [Interpreting Language Reward Models via Contrastive Explanations](https://arxiv.org/abs/2411.16502) *(2024)* — Generates counterfactual edits to explain which attributes drive a reward score.
- [Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards](https://arxiv.org/abs/2306.04488) *(2023)* — Interpolates weights of policies tuned on separate rewards to trace a Pareto front.
- [Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging](https://arxiv.org/abs/2310.11564) *(2023)* — Models personalization as multi-objective alignment, merging separately tuned preference policies post hoc.
- [Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment](https://arxiv.org/abs/2402.19085) *(2024)* — Conditions generation on explicit per-objective preference tokens to make the alignment tax steerable.
- [ENCORE: Entropy-guided Reward Composition for Multi-head Safety Reward Models](https://arxiv.org/abs/2503.20995) *(2025)* — Downweights high-entropy rule heads when composing per-rule safety ratings into one score.

### Fine-grained, dense, and span-level rewards

- [Fine-Grained Human Feedback Gives Better Rewards for Language Model Training](https://arxiv.org/abs/2306.01693) *(2023)* — Sentence-level rewards from separate factuality, relevance, and completeness models.
- [Sentence-level Reward Model can Generalize Better for Aligning LLM from Human Preference](https://arxiv.org/abs/2503.04793) *(2025)* — Aggregates sentence-level scores to improve out-of-distribution generalization.

### Self-rewarding and self-generated criteria

- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) *(2024)* — The model judges its own generations via judge prompting, improving policy and reward together.
- [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) *(2024)* — Adds a meta-judge that critiques the model's own judgments, not just its responses.
- [Self-Generated Critiques Boost Reward Modeling for Language Models](https://arxiv.org/abs/2411.16646) *(2024)* — Augments a scalar reward head with self-generated critiques to sharpen prediction.
- [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) *(2024)* — Bootstraps a judge purely from synthetic contrasting responses with no human labels.
- [Process-based Self-Rewarding Language Models](https://arxiv.org/abs/2503.03746) *(2025)* — Extends self-rewarding with step-wise self-evaluation where holistic judging fails.
- [CREAM: Consistency Regularized Self-Rewarding Language Models](https://arxiv.org/abs/2410.12735) *(2024)* — Regularizes self-rewarding with a consistency term to curb accumulated reward-estimate bias.
- [Toward Evaluative Thinking: Meta Policy Optimization with Evolving Reward Models](https://arxiv.org/abs/2504.20157) *(2025)* — Co-evolves a generative reward model alongside the policy via meta-level optimization.

## Criteria Compilers and Programmatic Rubric Graders

Reward-model versus verifier is not a boundary this list observes. What matters is whether the target is expressed as inspectable criteria — a program running several named predicates, acceptance conditions, or partial-credit rules. A monolithic correctness check (answer equals reference, proof checks, tests pass) is verification but not a rubric, and lives in the RLVR lists under [Adjacent collections](#adjacent-collections).

- [Reinforcement Learning with Robust Rubric Rewards](https://arxiv.org/abs/2605.30244) *(2026)* — Routes each criterion to a deterministic verifier or judge, limiting evidence exposure.
- [An Efficient Rubric-based Generative Verifier for Search-Augmented LLMs](https://arxiv.org/abs/2510.14660) *(2025)* — Treats atomic information nuggets as structured criteria, distilling a compact verifier.
- [The Art of Building Verifiers for Computer Use Agents](https://arxiv.org/abs/2604.06240) *(2026)* — A practical playbook for constructing programmatic verifiers grading interface trajectories.
- [Time To Impeach LLM-as-a-Judge: Programs are the Future of Evaluation](https://arxiv.org/abs/2506.10403) *(2025)* — Synthesizes executable auditable judging programs in place of opaque model scores.
- [Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems](https://arxiv.org/abs/2502.19328) *(2025)* — Routes a preference model alongside verifiable factuality and instruction-following checks through a reward agent.
- [When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K Causal Reasoning in LLMs](https://arxiv.org/abs/2608.03506) *(2026)* — A training-free symbolic verifier scores causal traces against named causal axioms.
- [CHiL(L)Grader: Calibrated Human-in-the-Loop Short-Answer Grading](https://arxiv.org/abs/2603.11957) *(2026)* — Routes low-confidence gradings to humans while adapting the grader to evolving criteria.
- [PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating and Training Large Language Models](https://arxiv.org/abs/2605.20873) *(2026)* — Taxonomy-driven synthesis instantiating planning problems with instance-level automatic verification checklists.
- [Cited but Not Verified: Parsing and Evaluating Source Attribution in LLM Deep Research Agents](https://arxiv.org/abs/2605.06635) *(2026)* — Parses citations and scores sources on link validity, relevance, and factuality separately.
- [LLM-as-a-Judge for Scalable Test Coverage Evaluation: Accuracy, Operational Reliability, and Cost](https://arxiv.org/abs/2512.01232) *(2025)* — A production criteria-driven judge grading acceptance tests, benchmarked on accuracy, reliability, and cost.
- [EDIT: Evidence-Diagnosed Intervention Training for Rule-Faithful LLM Grading](https://arxiv.org/abs/2606.06350) *(2026)* — Locates grading errors via posterior mark drift, then revises steps against an explicit mark scheme.
- [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/abs/2605.19769) *(2026)* — Builds executable state checkers as first-class verifiers, outperforming a judge model.
- [CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents](https://arxiv.org/abs/2605.25624) *(2026)* — Adversarially coupled agents co-synthesize task, environment, and reward together.
- [TRON: Targeted Rule-Verifiable Online Environments for Visual Reasoning RL](https://arxiv.org/abs/2606.01599) *(2026)* — Generator-verifier programs produce difficulty-controlled visual tasks with exact rewards.
- [Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185) *(2026)* — PDI-Bench lifts tracked objects to world space to score three named geometric failure dimensions.
- [Taming Camera-Controlled Video Generation with Verifiable Geometry Reward](https://arxiv.org/abs/2512.02870) *(2025)* — Scores segment-wise camera-pose alignment between estimated generated and reference 3D trajectories.
- [SPATIALALIGN: Aligning Dynamic Spatial Relationships in Video Generation](https://arxiv.org/abs/2602.22745) *(2026)* — Geometric verifier checks whether prompted dynamic spatial relationships actually hold in generated video.
- [RLGF: Reinforcement Learning with Geometric Feedback for Autonomous Driving Video Generation](https://arxiv.org/abs/2509.16500) *(2025)* — Hierarchical geometric reward separates point-line-plane alignment from scene occupancy coherence.
- [CreFlow: Corrective Reflow for Sparse-Reward Embodied Video Diffusion RL](https://arxiv.org/abs/2605.14274) *(2026)* — Composes manipulation requirements as linear temporal logic constraints returning localized per-constraint violations.
- [RLAR: An Agentic Reward System for Multi-task Reinforcement Learning on Large Language Models](https://arxiv.org/abs/2603.00724) *(2026)* — A reward agent synthesizes programmatic verifiers per query, tracking distribution shift during training.
- [JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR](https://arxiv.org/abs/2604.25419) *(2026)* — Rewards only plurality-voted answers that a formal proof checker independently confirms.
- [Diagnosing Under-Development of Irreversible Processes in Video Generation](https://arxiv.org/abs/2608.00617) *(2026)* — Null-tests irreversibility metrics, surfacing a computable directional-progress plus stasis-rate protocol.
- [Inference-Time Scaling for Joint Audio-Video Generation](https://arxiv.org/abs/2606.03183) *(2026)* — Adaptive reward weighting calibrates heterogeneous verifier variances online for best-of-N joint audio-video selection.
- [RAPO++: Cross-Stage Prompt Optimization for Text-to-Video Generation via Data Alignment and Test-Time Scaling](https://arxiv.org/abs/2510.20206) *(2025)* — Closed-loop prompt optimizer refining against semantic, spatial, temporal, and optical-flow feedback signals.
- [Codifying the Judge: Scalable Evaluation via Program Distillation](https://arxiv.org/abs/2607.22561) *(2026)* — Distills judge decision logic into a committee of inspectable, editable scoring programs with fallback.
- [VerifiAgent: a Unified Verification Agent in Language Model Reasoning](https://arxiv.org/abs/2504.00406) *(2025)* — Pairs completeness and consistency meta-checks with reasoning-type-selected verification tools instead of one fixed verifier.
- [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391) *(2026)* — Scales training-free verification along criteria decomposition, repeated evaluation, and score granularity.

## Process Reward Models and Step-Level Criteria

Step-level scoring alone does not qualify — a binary "this step is correct" label is not a criteria set. Entries here carry an explicit criteria tree, error taxonomy, checklist, or independently weighted process components. General PRM literature is in [Adjacent collections](#adjacent-collections).

- [Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning](https://arxiv.org/abs/2601.17223) *(2026)* — Checks intermediate steps with deterministic verifiers for risk-of-bias assessment in evidence synthesis.
- [Dynamic and Generalizable Process Reward Modeling](https://arxiv.org/abs/2507.17849) *(2025)* — Stores multi-dimensional reward criteria in an explicit tree, selecting per step by Pareto dominance.
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124) *(2025)* — Grades process reward models on explicit simplicity, soundness, and sensitivity error dimensions.
- [Error Typing for Smarter Rewards: Improving Process Reward Models with Error-Aware Hierarchical Supervision](https://arxiv.org/abs/2505.19706) *(2025)* — Classifies math and consistency error types per step before estimating step correctness.
- [Socratic-PRMBench: Benchmarking Process Reward Models with Systematic Reasoning Patterns](https://arxiv.org/abs/2505.23474) *(2025)* — Tests step-level error detection across an explicit taxonomy of six reasoning patterns.
- [DeepCritic: Deliberate Critique with Large Language Models](https://arxiv.org/abs/2505.00662) *(2025)* — Trains step-wise critics performing multi-perspective verification instead of a shallow single pass.
- [RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System](https://arxiv.org/abs/2602.02488) *(2026)* — Co-trains a step-wise generative reward model with the policy via consistency feedback.
- [ExpRL: Exploratory RL for LLM Mid-Training](https://arxiv.org/abs/2606.17024) *(2026)* — A reference-conditioned judge scores rollouts against a problem-specific rubric for dense mid-training reward.
- [ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents](https://arxiv.org/abs/2601.12294) *(2026)* — Step-level benchmark isolating single-step from multi-step tool-agent failures via multi-model-verified action pairs.
- [SEVA: Self-Evolving Verification Agent with Process Reward for Fact Attribution](https://arxiv.org/abs/2606.29713) *(2026)* — Decomposes verification quality into independently weighted process components replacing an opaque binary label.

## Rubric-Conditioned Judges and Rubric-Specific Judge Science

The substrate rubric rewards are built on. Kept deliberately compact relative to its literature; for depth see the dedicated lists under [Adjacent collections](#adjacent-collections).

### Judge models and generative reward models

- [Prometheus: Inducing Fine-grained Evaluation Capability in Language Models](https://arxiv.org/abs/2310.08491) *(2023)* — Open evaluator trained against custom score rubrics as a frontier-judge substitute.
- [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](https://arxiv.org/abs/2405.01535) *(2024)* — Unifies direct assessment and pairwise ranking in one open judge model.
- [M-Prometheus: A Suite of Open Multilingual LLM Judges](https://arxiv.org/abs/2504.04953) *(2025)* — Extends the rubric-conditioned evaluator family to multilingual judging.
- [Prometheus-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation](https://arxiv.org/abs/2401.06591) *(2024)* — Carries the rubric-conditioned evaluator design into vision-language judgment.
- [RM-R1: Reward Modeling as Reasoning](https://arxiv.org/abs/2505.02387) *(2025)* — Reframes reward modeling as chain-of-rubrics reasoning refined with verifiable-reward RL.
- [Inference-Time Scaling for Generalist Reward Modeling](https://arxiv.org/abs/2504.02495) *(2025)* — Self-principled critique tuning lets reward models generate principles then scale by voting.
- [Incentivizing Agentic Reasoning in LLM Judges via Tool-Integrated Reinforcement Learning](https://arxiv.org/abs/2510.23038) *(2025)* — Trains a judge to call a code executor for constraint checks beyond text-only reasoning.
- [Learning to Align Multi-Faceted Evaluation: A Unified and Robust Framework](https://arxiv.org/abs/2502.18874) *(2025)* — ARJudge formulates criteria per instruction, refining code-driven alongside text-based analyses into one judgment.
- [CodeVisionary: An Agent-based Framework for Evaluating Large Language Models in Code Generation](https://arxiv.org/abs/2504.13472) *(2025)* — Distills each task's requirements into evaluation context before scoring, replacing static single-prompt code judging.

### Critic models and explainable metrics

- [TIGERScore: Towards Building Explainable Metric for All Text Generation Tasks](https://arxiv.org/abs/2310.00752) *(2023)* — Instruction-tuned metric produces error-localized natural-language critique scores.
- [INSTRUCTSCORE: Explainable Text Generation Evaluation with Finegrained Feedback](https://arxiv.org/abs/2305.14282) *(2023)* — Fine-tunes a diagnostic metric from model critiques guided by a human-authored error taxonomy.
- [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) *(2026)* — Adapts the critic-as-judge pattern to reward interface-agent trajectories at scale.

### Judge behavior science: bias

- [Self-Preference Bias in Rubric-Based Evaluation of Large Language Models](https://arxiv.org/abs/2604.06996) *(2026)* — Shows criteria-based judges still favor same-family outputs despite itemized structure.
- [Am I More Pointwise or Pairwise? Revealing Position Bias in Rubric-Based LLM-as-a-Judge](https://arxiv.org/abs/2602.02219) *(2026)* — Shows criteria-based judging behaves like multiple choice, with bias over score options and criterion order.
- [When Can You Debias an LLM Judge? Identifiability Limits, a Test, and Designs for Top-k Ranking](https://arxiv.org/abs/2607.02104) *(2026)* — Derives identifiability limits on debiasing and a test for reliable top-k ranking.
- [Assistant-Guided Mitigation of Teacher Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2505.19176) *(2025)* — An unbiased assistant supplements teacher-distilled data to remove teacher bias.
- [Comparing Developer and LLM Biases in Code Evaluation](https://arxiv.org/abs/2603.24586) *(2026)* — Finds judges favor longer explanations that real developers do not want.
- [Great Models Think Alike and this Undermines AI Oversight](https://arxiv.org/abs/2502.04313) *(2025)* — A chance-adjusted similarity metric shows judges favor models resembling themselves.

### Judge behavior science: reliability and calibration

- [Time to REFLECT: Can We Trust LLM Judges for Evidence-based Research Agents?](https://arxiv.org/abs/2605.19196) *(2026)* — A failure taxonomy plus controlled interventions expose where judges misread research-agent traces.
- [Beyond the Illusion of Consensus: From Surface Heuristics to Knowledge-Grounded Evaluation in LLM-as-a-Judge](https://arxiv.org/abs/2603.11027) *(2026)* — Traces illusory judge consensus to shared rubric structure, proposing domain-grounded criteria instead.
- [Can LLM be a Personalized Judge?](https://arxiv.org/abs/2406.11657) *(2024)* — Finds persona-conditioned judges unreliable, adding verbal uncertainty so they abstain when unsure.
- [Beyond Single-Point Judgment: Distribution Alignment for LLM-as-a-Judge](https://arxiv.org/abs/2505.12301) *(2025)* — Trains judges to match the full human rating distribution rather than a point estimate.
- [Limits to scalable evaluation at the frontier: LLM as Judge won't beat twice the data](https://arxiv.org/abs/2410.13341) *(2024)* — Proves debiasing cannot halve ground-truth labels when the judge is no more accurate than the model.
- [Evaluating Judges as Evaluators: The JETTS Benchmark of LLM-as-Judges as Test-Time Scaling Evaluators](https://arxiv.org/abs/2504.15253) *(2025)* — Benchmarks judges against process and outcome reward models across reranking, search, and refinement.
- [An Empirical Study of LLM-as-a-Judge for LLM Evaluation: Fine-tuned Judge Model is not a General Substitute for GPT-4](https://arxiv.org/abs/2403.02839) *(2024)* — Finds fine-tuned judges overfit in-domain, generalizing worse than a prompted frontier judge.
- [Aligning Large Language Models by On-Policy Self-Judgment](https://arxiv.org/abs/2402.11253) *(2024)* — Judge-augmented fine-tuning lets one model score its own on-policy samples without a separate reward model.
- [Scaling Generative Verifiers For Natural Language Mathematical Proof Verification And Selection](https://arxiv.org/abs/2511.13027) *(2025)* — Finds proof verifiers reward procedural style over mathematical validity at long-context scale.

### Judge behavior science: adversarial robustness

- [Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment](https://arxiv.org/abs/2402.14016) *(2024)* — Short universal adversarial phrases transfer across prompts to inflate scores.
- [Optimization-based Prompt Injection Attack to LLM-as-a-Judge](https://arxiv.org/abs/2403.17710) *(2024)* — A gradient-optimized injected sequence forces the judge to pick the attacker's response.
- [Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections](https://arxiv.org/abs/2504.18333) *(2025)* — Measures how content-author versus system-prompt injection attacks transfer across judge models.
- [Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks](https://arxiv.org/abs/2505.13348) *(2025)* — Formalizes comparative-undermining and justification-manipulation injection attacks against judge decisions.
- [On the Adversarial Robustness of Multimodal LLM Judges](https://arxiv.org/abs/2606.15608) *(2026)* — First framework evaluating multimodal judge robustness, introducing a transferable score-inflating attack.
- [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://arxiv.org/abs/2410.07137) *(2024)* — Constant content-free responses exploit length and style bias to top major benchmarks.
- [A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness](https://arxiv.org/abs/2603.06594) *(2026)* — Audits harmfulness judges against human labels, finding accuracy near chance under red-teaming shift.
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403) *(2026)* — Systematizes judge security into attacks on judges, attacks via judges, and judge-based defenses.
- [Helpful Agent Meets Deceptive Judge: Understanding Vulnerabilities in Agentic Workflows](https://arxiv.org/abs/2506.03332) *(2025)* — Web-evidence-grounded adversarial critiques flip correct agent answers, exposing judge feedback as an attack surface.
- [One Token to Fool LLM-as-a-Judge](https://arxiv.org/abs/2507.08794) *(2025)* — Content-free master-key tokens elicit false positive rewards from reference-based generative verifiers.
- [Reliable to Expressive: A Curriculum for Rubric-Following Safety Judges](https://arxiv.org/abs/2606.09165) *(2026)* — Trains judges on instance-conditioned dynamic rubrics so verdicts survive reformulation of the criteria.

### Multi-agent, debate, and ensemble judges

- [Multi-Agent Debate for LLM Judges with Adaptive Stability Detection](https://arxiv.org/abs/2510.12697) *(2025)* — Judges debate under a statistical stopping rule instead of static majority voting.
- [Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Discussions](https://arxiv.org/abs/2405.20267) *(2024)* — Candidate models debate head-to-head while a judge committee votes.
- [Wider and Deeper LLM Networks are Fairer LLM Evaluators](https://arxiv.org/abs/2308.01862) *(2023)* — Arranges judges as a multi-layer network of diverse evaluator neurons rather than independent votes.
- [Emergence of Biased Consensus in Multi-Agent LLM Debates](https://arxiv.org/abs/2608.02827) *(2026)* — Shows debate among homogeneous judges converges on shared bias rather than cancelling it.
- [Who can we trust? LLM-as-a-jury for Comparative Assessment](https://arxiv.org/abs/2602.16610) *(2026)* — Adds a per-judge discriminator parameter so jury aggregation infers rankings and judge reliability together.
- [Leveraging LLMs as Meta-Judges: A Multi-Agent Framework for Evaluating LLM Judgments](https://arxiv.org/abs/2504.17087) *(2025)* — Builds an expert rubric, then uses multi-agent meta-judges to score and filter weak judgments.
- [Approximating Human Preferences Using a Multi-Judge Learned System](https://arxiv.org/abs/2510.25884) *(2025)* — Learns an aggregator over rubric-conditioned judge scores to model persona-based human preferences.
- [RoPoLL: Robust Panel of LLM Judges](https://arxiv.org/abs/2606.30931) *(2026)* — Replaces jury mean aggregation with a geometric median bounding bias under contaminated judges.
- [DialogGuard: Multi-Agent Psychosocial Safety Evaluation of Sensitive LLM Responses](https://arxiv.org/abs/2512.02282) *(2025)* — Compares four judge pipelines scoring five psychosocial-risk dimensions against one shared three-level rubric.
- [SAGEval: The frontiers of Satisfactory Agent based NLG Evaluation for reference-free open-ended text](https://arxiv.org/abs/2411.16077) *(2024)* — Critiquing agent rectifies evaluator scores against eight predefined aspects, proposing new criteria where coverage gaps appear.
- [Multi-Agent-as-Judge: Aligning LLM-Agent-Based Automated Evaluation with Multi-Dimensional Human Evaluation](https://arxiv.org/abs/2507.21028) *(2025)* — Derives evaluator personas carrying distinct dimensions from domain documents, then debates them into per-dimension feedback.
- [MADRAG: Multi-Agent Debate with Retrieval-Augmented Generation for Training-Free Analytic Essay Scoring](https://arxiv.org/abs/2606.06754) *(2026)* — Advocate and skeptic agents debate before a judge calibrated by rubric-aligned exemplar retrieval.
- [Efficient LLM Safety Evaluation through Multi-Agent Debate](https://arxiv.org/abs/2511.06396) *(2025)* — Critic, defender, and judge agents debate a jailbreak response under one shared safety rubric.
- [Who Judges the Judge? LLM Jury-on-Demand: Building Trustworthy LLM Evaluation Systems](https://arxiv.org/abs/2512.01786) *(2025)* — Predicts per-instance judge reliability to assemble and weight a jury dynamically.
- [AGACCI : Affiliated Grading Agents for Criteria-Centric Interface in Educational Coding Contexts](https://arxiv.org/abs/2507.05321) *(2025)* — Distributes rubric-grading roles across specialized agents scoring programming assignments against expert binary criteria.
- [EduPanel: A Three-Agent LLM Judge for Teaching Videos -- Reliability, Complementarity, and Human Trust Calibration](https://arxiv.org/abs/2607.18529) *(2026)* — Splits rubric-grounded teaching-quality judgment across specialized agents conditioned on the intended learner.

### Efficient judges

- [Reinforcement Learning-based Knowledge Distillation with LLM-as-a-Judge](https://arxiv.org/abs/2604.02621) *(2026)* — Distills a judge's single-token reward signal into student models over unlabeled data.
- [Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge](https://arxiv.org/abs/2605.10805) *(2026)* — Routes each case between reasoning and non-reasoning judges to balance cost.
- [RTLC -- Research, Teach-to-Learn, Critique](https://arxiv.org/abs/2605.13695) *(2026)* — Three-stage Feynman-inspired prompting lifts judge accuracy with no fine-tuning.
- [You Only Judge Once: Multi-response Reward Modeling in a Single Forward Pass](https://arxiv.org/abs/2604.10966) *(2026)* — Scores multiple image and video candidates in a single vision-language forward pass.

## Reward Hacking and Robustness

### Rubric-specific hacking and attack surface

- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) *(2026)* — A cross-family judge panel separates verifier failure from rubric-design limitation.
- [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923) *(2026)* — Injects known judge biases into a controllable environment to reproduce hacking onset.
- [Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges](https://arxiv.org/abs/2602.13576) *(2026)* — Shows criteria-based judges can be stealthily manipulated into drifting preferences.
- [RIFT: A Rubric Failure Mode Taxonomy and Automated Diagnostics](https://arxiv.org/abs/2604.01375) *(2026)* — Taxonomizes how criteria grading fails and provides automated diagnostics.
- [PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges](https://arxiv.org/abs/2605.30803) *(2026)* — Audits criteria sets on structural adequacy, reliability, preference fit, and robustness.
- [EST-PRM: Stress-Testing Process Reward Models Before They Become Load-Bearing](https://arxiv.org/abs/2606.00437) *(2026)* — Step inflation and reordering preserve correctness while fooling step-level scoring.
- [Examining Reasoning LLMs-as-Judges in Non-Verifiable LLM Post-Training](https://arxiv.org/abs/2603.12246) *(2026)* — Finds policies trained against reasoning judges learn outputs that deceive the judge itself.

### Reward model over-optimization and mitigations

- [WARM: On the Benefits of Weight Averaged Reward Models](https://arxiv.org/abs/2401.12187) *(2024)* — Averages fine-tuned reward models in weight space rather than ensembling predictions.
- [Helping or Herding? Reward Model Ensembles Mitigate but do not Eliminate Reward Hacking](https://arxiv.org/abs/2312.09244) *(2023)* — Shows prediction ensembles only partially reduce downstream over-optimization.
- [Reward Model Ensembles Help Mitigate Overoptimization](https://arxiv.org/abs/2310.02743) *(2023)* — Shows ensembling learned reward models measurably slows proxy-reward over-optimization.
- [ODIN: Disentangled Reward Mitigates Hacking in RLHF](https://arxiv.org/abs/2402.07319) *(2024)* — Splits reward into length and quality heads, discarding the length head before RL.
- [Regularizing Hidden States Enables Learning Generalizable Reward Model for LLMs](https://arxiv.org/abs/2406.10216) *(2024)* — Adds hidden-state regularization to reduce overfitting-driven reward hacking.
- [RRM: Robust Reward Model Training Mitigates Reward Hacking](https://arxiv.org/abs/2409.13156) *(2024)* — A causal reformulation isolates prompt-independent artifacts so the model ignores length cues.
- [Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms](https://arxiv.org/abs/2406.02900) *(2024)* — Extends over-optimization scaling laws to direct alignment objectives.
- [Inference-Time Reward Hacking in Large Language Models](https://arxiv.org/abs/2506.19248) *(2025)* — Shows best-of-N against a proxy reward can overoptimize and subvert alignment at inference.
- [Adversarial Training of Reward Models](https://arxiv.org/abs/2504.06141) *(2025)* — Trains the reward model against an adversary searching for exploits during training.
- [Teach a Reward Model to Correct Itself: Reward Guided Adversarial Failure Discovery for Robust Reward Modeling](https://arxiv.org/abs/2507.06419) *(2025)* — The reward model adversarially finds its own failure modes then retrains on them.
- [Beyond Reward Hacking: Causal Rewards for Large Language Model Alignment](https://arxiv.org/abs/2501.09620) *(2025)* — Enforces counterfactual invariance so rewards stay stable under irrelevant changes.
- [One Bias After Another: Mechanistic Reward Shaping and Persistent Biases in Language Reward Models](https://arxiv.org/abs/2603.03291) *(2026)* — Correcting one reward-model bias tends to induce a different persistent bias.
- [Elephant in the Room: Unveiling the Impact of Reward Model Quality in Alignment](https://arxiv.org/abs/2409.19024) *(2024)* — Traces how reward-model quality itself drives downstream alignment outcomes.
- [Multimodal Reward Hacking in Reinforcement Learning](https://arxiv.org/abs/2607.09492) *(2026)* — Finds keyword-based visual checks increase hacking while semantic judge verification reduces it.

### Specification gaming and reward tampering

- [Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models](https://arxiv.org/abs/2406.10162) *(2024)* — Shows reward tampering generalizes from minor sycophancy to outright tampering.
- [Honesty to Subterfuge: In-Context Reinforcement Learning Can Make Honest Models Reward Hack](https://arxiv.org/abs/2410.06491) *(2024)* — In-context reflection alone pushes honest models into specification gaming.
- [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) *(2025)* — Optimizing against a reasoning monitor produces obfuscated hacking that evades it.
- [Specification Self-Correction: Mitigating In-Context Reward Hacking Through Test-Time Refinement](https://arxiv.org/abs/2507.18742) *(2025)* — Has the model rewrite its own tainted specification to close the exploited loophole.
- [Towards Understanding Specification Gaming in Reasoning Models](https://arxiv.org/abs/2605.02269) *(2026)* — Catalogs reasoning models exploiting their training specification instead of solving the task.
- [Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964) *(2026)* — Tests tool-using agents for shortcuts like skipping verification or tampering with eval code.
- [SoliReward: Mitigating Susceptibility to Reward Hacking and Annotation Noise in Video Generation Reward Models](https://arxiv.org/abs/2512.22170) *(2025)* — Hardens a video reward model against both criteria gaming and noisy human annotation.
- [reWordBench: Benchmarking and Improving the Robustness of Reward Models with Transformed Inputs](https://arxiv.org/abs/2503.11751) *(2025)* — Shows reward models degrade under meaning-preserving rewrites, fixed by paraphrase-invariant training.
- [Evaluating Robustness of Reward Models for Mathematical Reasoning](https://arxiv.org/abs/2410.01729) *(2024)* — Shows single-comparison math benchmarks overstate reward-model robustness and hide overoptimization.
- [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149) *(2026)* — Finds verifiable-reward training abandons rule induction for shortcuts passing imperfect verifiers.
- [Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition](https://arxiv.org/abs/2604.05279) *(2026)* — Splits a sycophancy signal into five reward terms disentangling pressure capitulation from evidence blindness.
- [Calibration Collapse Under Sycophancy Fine-Tuning: How Reward Hacking Breaks Uncertainty Quantification in LLMs](https://arxiv.org/abs/2604.10585) *(2026)* — Shows sycophancy fine-tuning is reward hacking that breaks uncertainty calibration.
- [Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges](https://arxiv.org/abs/2604.13602) *(2026)* — Unifies reward hacking under a proxy-compression account spanning verbosity to alignment faking.

## Multimodal Rubric Rewards

Criteria-decomposed rewards outside text. For single-scalar visual preference scorers see [Foundations](#single-scalar-preference-scorers-for-generative-models).

### Criteria-decomposed image rewards

- [VisionReward: Fine-Grained Multi-Dimensional Human Preference Learning for Image and Video Generation](https://arxiv.org/abs/2412.21059) *(2024)* — Decomposes preference into weighted yes/no judgment questions across many dimensions.
- [MJ-Bench: Is Your Multimodal Reward Model Really a Good Judge for Text-to-Image Generation?](https://arxiv.org/abs/2407.04842) *(2024)* — Scores reward models on alignment, safety, quality, and bias sub-criteria separately.
- [A-Bench: Are LMMs Masters at Evaluating AI-generated Images?](https://arxiv.org/abs/2406.03070) *(2024)* — Probes whether multimodal judges assess generated-image quality as human experts do.
- [RubricRL: Simple Generalizable Rewards for Text-to-Image Generation](https://arxiv.org/abs/2511.20651) *(2025)* — One reasoning model auto-builds prompt-adaptive criteria, replacing evaluator ensembles.
- [AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment](https://arxiv.org/abs/2605.17602) *(2026)* — Rule-based criteria reward model built for robustness against reward hacking.
- [DyCoRM: Dynamic Criterion-Aware Reward Modeling for Text-to-Image Generation](https://arxiv.org/abs/2605.25876) *(2026)* — Grounds task-relevant criteria per prompt before criterion-aware preference comparison.
- [SpatialReward: Verifiable Spatial Reward Modeling for Fine-Grained Spatial Consistency in Text-to-Image Generation](https://arxiv.org/abs/2603.22228) *(2026)* — A prompt decomposer, separate expert detectors, and a reasoning model jointly verify spatial-layout criteria.
- [FineGRAIN: Evaluating Failure Modes of Text-to-Image Models with Vision Language Model Judges](https://arxiv.org/abs/2512.02161) *(2025)* — Localizes and categorizes fine-grained failure modes rather than emitting one score.
- [Z-Reward: Beyond Scalar Rewards by Internalizing Reasoning into Score Distributions](https://arxiv.org/abs/2606.09076) *(2026)* — Models visual preference as a distribution over rubric scores, distilling a reasoning teacher into a compact student.
- [Qwen-Image-2.0-RL Technical Report](https://arxiv.org/abs/2606.27608) *(2026)* — Composite pointwise reward models with chain-of-thought scoring drive diffusion RLHF.
- [RationalRewards: Reasoning Rewards Scale Visual Generation Both Training and Test Time](https://arxiv.org/abs/2604.11626) *(2026)* — Emits explicit multi-dimensional critiques before scoring, serving both training reward and test-time refinement.
- [Beyond Thumbs Up/Down: Untangling Challenges of Fine-Grained Feedback for Text-to-Image Generation](https://arxiv.org/abs/2406.16807) *(2024)* — Tests whether fine-grained feedback actually beats coarse binary preference for image reward models.
- [Automatic Evaluation for Text-to-image Generation: Task-decomposed Framework, Distilled Training, and Meta-evaluation Benchmark](https://arxiv.org/abs/2411.15488) *(2024)* — Decomposes image evaluation into sub-tasks to distill a frontier judge into an open model.
- [Enhancing Reward Models for High-quality Image Generation: Beyond Text-Image Alignment](https://arxiv.org/abs/2507.19002) *(2025)* — Separates content and aesthetic scores after finding alignment-only rewards penalize detailed images.
- [PoSh: Using Scene Graphs To Guide LLMs-as-a-Judge For Detailed Image Descriptions](https://arxiv.org/abs/2510.19060) *(2025)* — Uses scene graphs as structured criteria guiding judges toward span-localized description errors.
- [FiRe: Fine-grained Multimodal Reasoning for Enhanced Image Generation](https://arxiv.org/abs/2604.13491) *(2026)* — Decomposes prompts into visual requirements, self-judges each, then locally refines the image.
- [Judge Anything: MLLM as a Judge Across Any Modality](https://arxiv.org/abs/2503.17489) *(2025)* — Evaluates multimodal judging across any-to-any modality tasks using human judgments and detailed criteria.
- [Unified Personalized Reward Model for Vision Generation](https://arxiv.org/abs/2602.02380) *(2026)* — Instantiates fine-grained criteria per request rather than scoring against one fixed evaluation rubric.
- [AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities](https://arxiv.org/abs/2607.24821) *(2026)* — Grades audio-video edits against thousands of checklist items plus a separate realism rubric.
- [Evaluation-Verification Reward for Consistent Multi-Reference Image Editing](https://arxiv.org/abs/2607.29025) *(2026)* — Splits multi-reference edit evaluation into distinct visual criteria, each checked by a grounding verifier.
- [ReasonEdit: Towards Interpretable Image Editing Evaluation via Reinforcement Learning](https://arxiv.org/abs/2605.07477) *(2026)* — Reinforcement-trains an interpretable edit evaluator against explanation logicality, accuracy, and usefulness.
- [FilmBench: A Film-Grade Benchmark for Cinematic Video Generation](https://arxiv.org/abs/2607.24241) *(2026)* — Scores generated video against a three-level taxonomy of cinematic craft criteria.
- [RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning](https://arxiv.org/abs/2603.09160) *(2026)* — Applies criteria-guided reward specifically to dense image captioning.
- [Visual Preference Optimization with Rubric Rewards](https://arxiv.org/abs/2604.13029) *(2026)* — Builds instance-specific essential-and-additional checklists to filter visual preference pairs.
- [Leveraging Verifier-Based Reinforcement Learning in Image Editing](https://arxiv.org/abs/2604.27505) *(2026)* — Splits each editing instruction into principles checked separately before aggregating an interpretable reward.
- [Editor's Choice: Evaluating Abstract Intent in Image Editing through Atomic Entity Analysis](https://arxiv.org/abs/2605.14842) *(2026)* — Decomposes abstract editing instructions into entity-level checks correlating with human judgment.
- [A Unified Agentic Framework for Evaluating Conditional Image Generation](https://arxiv.org/abs/2504.07046) *(2025)* — Breaks each evaluation into named sub-questions, answering every one with a dedicated vision tool.
- [Personalized Reward Modeling for Text-to-Image Generation](https://arxiv.org/abs/2511.19458) *(2025)* — Generates user-conditioned evaluation dimensions per request, personalizing reward without user-specific training.
- [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558) *(2026)* — Reward model writes case-specific evaluation metrics instead of scoring against a fixed reference.
- [PICABench: How Far Are We from Physically Realistic Image Editing?](https://arxiv.org/abs/2510.17681) *(2025)* — Grades edits across eight physical-effect sub-dimensions using per-case region-level judge questions.
- [OneReward: Unified Mask-Guided Image Generation via Multi-Task Human Preference Learning](https://arxiv.org/abs/2508.21066) *(2025)* — Single reward model takes the evaluation criterion as an explicit input alongside the task.
- [Human-Aligned MLLM Judges for Fine-Grained Image Editing Evaluation: A Benchmark, Framework, and Analysis](https://arxiv.org/abs/2602.13028) *(2026)* — Decomposes edit evaluation into twelve interpretable factors spanning preservation, edit quality, and instruction fidelity.
- [GRADE: Benchmarking Discipline-Informed Reasoning in Image Editing](https://arxiv.org/abs/2603.12264) *(2026)* — Scores discipline reasoning, visual consistency, and logical readability separately across ten academic domains.
- [Evaluating Image Editing with LLMs: A Comprehensive Benchmark and Intermediate-Layer Probing Approach](https://arxiv.org/abs/2603.19775) *(2026)* — Separately rates perceptual quality, editing alignment, and content preservation via an intermediate-layer probing evaluator.
- [CV-Arena: An Open Benchmark for Instructional Computer Vision Problem Solving with Human-AI Collaborative Preferences](https://arxiv.org/abs/2606.00931) *(2026)* — A logic-gated multi-dimensional judge filters clear failures, routing only close comparisons to experts.
- [MIEScore: Human-Aligned Evaluation for Multi-Source Image Editing](https://arxiv.org/abs/2608.02059) *(2026)* — Rates multi-source edits on visual quality, instruction following, and attribute preservation separately.

### Question decomposition for text-to-image

Three parallel lineages independently invented "decompose the prompt into checkable criteria."

**Question-answering family**

- [TIFA: Accurate and Interpretable Text-to-Image Faithfulness Evaluation with Question Answering](https://arxiv.org/abs/2303.11897) *(2023)* — Auto-generates per-prompt question-answer pairs and scores faithfulness by answer accuracy.
- [Divide, Evaluate, and Refine: Evaluating and Improving Text-to-Image Alignment with Iterative VQA Feedback](https://arxiv.org/abs/2307.04749) *(2023)* — Decomposes prompts into sub-questions and refines generation from the feedback.
- [Davidsonian Scene Graph: Improving Reliability in Fine-grained Evaluation for Text-to-Image Generation](https://arxiv.org/abs/2310.18235) *(2023)* — A dependency graph of atomic questions fixing reliability gaps in question-based evaluation.
- [Evaluating Text-to-Visual Generation with Image-to-Text Generation](https://arxiv.org/abs/2404.01291) *(2024)* — Scores alignment by the probability a model answers yes to a caption-matching question.

**Object-detection checklist family**

- [GenEval: An Object-Focused Framework for Evaluating Text-to-Image Alignment](https://arxiv.org/abs/2310.11513) *(2023)* — Detection-based checklist scoring counting, position, and color binding as separate checks.
- [T2I-CompBench++: An Enhanced and Comprehensive Benchmark for Compositional Text-to-image Generation](https://arxiv.org/abs/2307.06350) *(2023)* — Splits compositional evaluation into attribute binding, relationships, numeracy, and complex compositions.
- [GenEval 2: Addressing Benchmark Drift in Text-to-Image Evaluation](https://arxiv.org/abs/2512.16853) *(2025)* — Updates the object-focused checklist as generators saturate the original.

**Reasoning family**

- [LLMScore: Unveiling the Power of Large Language Models in Text-to-Image Synthesis Evaluation](https://arxiv.org/abs/2305.11116) *(2023)* — Decomposes images into global and region-level descriptions scored by multi-granularity reasoning.
- [Factuality Matters: When Image Generation and Editing Meet Structured Visuals](https://arxiv.org/abs/2510.05091) *(2025)* — Grades structured-visual factuality through a multi-round question-answering protocol instead of aesthetic preference.
- [Evaluating Hallucination in Text-to-Image Diffusion Models with Scene-Graph based Question-Answering Agent](https://arxiv.org/abs/2412.05722) *(2024)* — Extracts scene-graph questions whose answers score consistency while recording each hallucination type.
- [TIIF-Bench: How Does Your T2I Model Follow Your Instructions?](https://arxiv.org/abs/2506.02161) *(2025)* — Pairs each prompt with attribute-specific yes/no checklists verified by a purpose-trained evaluator.

### Multimodal judges and reward models

- [MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark](https://arxiv.org/abs/2402.04788) *(2024)* — First systematic benchmark of multimodal judges across scoring, comparison, and ranking.
- [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://arxiv.org/abs/2502.10391) *(2025)* — Large multimodal preference set with a critique-based reward model scored across dimensions.
- [Multimodal RewardBench: Holistic Evaluation of Reward Models for Vision Language Models](https://arxiv.org/abs/2502.14191) *(2025)* — Expert-annotated benchmark spanning correctness, reasoning, and safety.
- [Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image](https://arxiv.org/abs/2512.16899) *(2025)* — Extends reward evaluation to models judging interleaved text-and-image output.
- [VLRMBench: A Comprehensive and Challenging Benchmark for Vision-Language Reward Models](https://arxiv.org/abs/2503.07478) *(2025)* — Tests process understanding, outcome assessment, and critique generation together.
- [VL-RewardBench: A Challenging Benchmark for Vision-Language Generative Reward Models](https://arxiv.org/abs/2411.17451) *(2024)* — Stress-tests generative reward models on hallucination detection where scorers fail.
- [ViLBench: A Suite for Vision-Language Process Reward Modeling](https://arxiv.org/abs/2503.20271) *(2025)* — Benchmark and data suite for step-level reward models in vision-language reasoning.
- [Multi-Crit: Benchmarking Multimodal Judges on Pluralistic Criteria-Following](https://arxiv.org/abs/2511.21662) *(2025)* — Tests whether judges follow multiple potentially conflicting user-specified criteria.
- [Advancing Multimodal Judge Models through a Capability-Oriented Benchmark and MCTS-Driven Data Generation](https://arxiv.org/abs/2603.00546) *(2026)* — Organizes judge evaluation by capability and synthesizes harder training data by search.
- [Omni-RRM: Advancing Omni Reward Modeling via Automatic Rubric-Grounded Preference Synthesis](https://arxiv.org/abs/2602.00846) *(2026)* — Synthesizes criteria-grounded preference justifications spanning text, image, video, and audio.
- [VLFeedback: A Large-Scale AI Feedback Dataset for Large Vision-Language Models Alignment](https://arxiv.org/abs/2410.09421) *(2024)* — Multi-aspect feedback annotating helpfulness, visual faithfulness, and safety separately, used to train Silkie.
- [Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling](https://arxiv.org/abs/2606.02578) *(2026)* — Uses visual perturbations to correct judges rewarding plausible text over visual truth.
- [ARM-Thinker: Reinforcing Multimodal Generative Reward Models with Agentic Tool Use and Visual Reasoning](https://arxiv.org/abs/2512.05111) *(2025)* — Reward model invokes cropping and retrieval tools to ground each judgment in verifiable evidence.
- [Visual-ERM: Reward Modeling for Visual Equivalence](https://arxiv.org/abs/2603.13224) *(2026)* — Generative reward model judging vision-to-code output in rendered pixel space rather than by text rules.
- [Unified Multimodal Chain-of-Thought Reward Model through Reinforcement Fine-Tuning](https://arxiv.org/abs/2505.03318) *(2025)* — Long chain-of-thought reward model writes out task-relevant dimensions, scoring each before aggregating.
- [MJ1: Multimodal Judgment via Grounded Verification](https://arxiv.org/abs/2603.07990) *(2026)* — Routes every verdict through an explicit observation-to-claim-to-verification chain rather than scoring the response directly.

### Multimodal reasoning rubrics

- [AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning](https://arxiv.org/abs/2510.14738) *(2025)* — Self-aggregates criteria checkpoints from successful trajectories without human annotation.
- [Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria](https://arxiv.org/abs/2605.08354) *(2026)* — Externalizes implicit preferences into prompt-specific independently verifiable criteria.
- [DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification](https://arxiv.org/abs/2605.09269) *(2026)* — Plans criteria and verifies against them in a single generative pass.
- [Learning What Matters: Dynamic Dimension Selection and Aggregation for Interpretable Vision-Language Reward Modeling](https://arxiv.org/abs/2604.05445) *(2026)* — Selects which dimensions matter per instance for interpretable rewards.
- [VisualPRM: An Effective Process Reward Model for Multimodal Reasoning](https://arxiv.org/abs/2503.10291) *(2025)* — Step-level process reward model built for multimodal chain-of-thought reasoning.
- [Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models](https://arxiv.org/abs/2603.16253) *(2026)* — Adds explicit visual-premise verification to reduce ungrounded step scoring.
- [Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583) *(2026)* — Grounds process errors at token level by extracting image-related claims for verification.
- [Judging the Judges: Can Large Vision-Language Models Fairly Evaluate Chart Comprehension and Reasoning?](https://arxiv.org/abs/2505.08468) *(2025)* — Pairwise and pointwise criteria for grading chart comprehension.
- [Multimodal Reinforcement Learning with Adaptive Verifier for AI Agents](https://arxiv.org/abs/2512.03438) *(2025)* — Selects per-sample scoring functions grading answer accuracy, spatiotemporal grounding, and reasoning quality separately.

### Video

Judging whether a generated video follows its prompt and stays self-consistent is a first-class use case for this list. Entries here are the criteria-decomposed cut — multi-dimensional, checklist, or claim-level scoring — as distinct from single-scalar video preference scorers.

#### Per-dimension benchmarks and suites

- [VBench: Comprehensive Benchmark Suite for Video Generative Models](https://arxiv.org/abs/2311.17982) *(2023)* — Splits video generation quality into sixteen disentangled dimensions, each validated against human annotation.
- [VBench++: Comprehensive and Versatile Benchmark Suite for Video Generative Models](https://arxiv.org/abs/2411.13503) *(2024)* — Extends the per-dimension suite with trustworthiness axes such as bias and safety.
- [VBench-2.0: Advancing Video Generation Benchmark Suite for Intrinsic Faithfulness](https://arxiv.org/abs/2503.21755) *(2025)* — Shifts the dimension set from surface fidelity toward intrinsic faithfulness criteria.
- [EvalCrafter: Benchmarking and Evaluating Large Video Generation Models](https://arxiv.org/abs/2310.11440) *(2023)* — Scores video generators on seventeen objective metrics regressed onto human opinion.
- [FETV: A Benchmark for Fine-Grained Evaluation of Open-Domain Text-to-Video Generation](https://arxiv.org/abs/2311.01813) *(2023)* — Categorizes prompts along content and challenge axes to expose per-category failures.
- [VideoPhy: Evaluating Physical Commonsense for Video Generation](https://arxiv.org/abs/2406.03520) *(2024)* — Grades generated video against physical-law criteria rather than perceptual quality.
- [TC-Bench: Benchmarking Temporal Compositionality in Text-to-Video and Image-to-Video Generation](https://arxiv.org/abs/2406.08656) *(2024)* — Verifies prompted state transitions with per-prompt temporal criteria instead of aggregate motion scores.
- [T2V-CompBench: A Comprehensive Benchmark for Compositional Text-to-video Generation](https://arxiv.org/abs/2407.14505) *(2024)* — Splits compositional generation into per-category criteria with a dedicated evaluator each.
- [WorldModelBench: Judging Video Generation Models As World Models](https://arxiv.org/abs/2502.20694) *(2025)* — Judges generated video against instruction-following and physical-law criteria as a world model.
- [WorldSimBench: Towards Video Generation Models as World Simulators](https://arxiv.org/abs/2410.18072) *(2024)* — Pairs explicit-criteria perceptual scoring with embodied action-level task verification.
- [WorldReasonBench: Human-Aligned Stress Testing of Video Generators as Future World-State Predictors](https://arxiv.org/abs/2605.10434) *(2026)* — Expert pairwise comparisons meta-evaluate reward models judging world-model video rollouts.
- [Q-Eval-100K: Evaluating Visual Quality and Alignment Level for Text-to-Vision Content](https://arxiv.org/abs/2503.02357) *(2025)* — Separates visual quality from text alignment as independently annotated opinion scores.
- [Benchmarking Multi-dimensional AIGC Video Quality Assessment: A Dataset and Unified Model](https://arxiv.org/abs/2407.21408) *(2024)* — Scores generated video on spatial quality, temporal quality, and text alignment separately.
- [Thinking in Video: Can Video Generators Really Reason About the Real World?](https://arxiv.org/abs/2607.17523) *(2026)* — Dual-judge audit separates explicit causal perception from the implicit perception-prediction gap.
- [AIGCBench: Comprehensive Evaluation of Image-to-Video Content Generated by AI](https://arxiv.org/abs/2401.01651) *(2024)* — Splits image-to-video evaluation into control alignment, motion, temporal consistency, and quality dimensions.
- [FiVE: A Fine-grained Video Editing Benchmark for Evaluating Emerging Diffusion and Rectified Flow Models](https://arxiv.org/abs/2503.13684) *(2025)* — Adds a VLM-judged edit-success check beside per-dimension preservation and consistency scores.
- [MMGR: Multi-Modal Generative Reasoning](https://arxiv.org/abs/2512.14691) *(2025)* — Scores generative reasoning on physical, logical, spatial, and temporal abilities rather than perceptual quality.
- [RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986) *(2026)* — Grades reasoning alignment, temporal consistency, physical rationality, and visual quality as separate metrics.
- [WorldJen: An End-to-End Multi-Dimensional Benchmark for Generative Video Models](https://arxiv.org/abs/2605.03475) *(2026)* — Replaces binary visual question answering with per-dimension Likert questionnaires graded at native resolution.
- [MBench: A Comprehensive Benchmark on Memory Capability for Video World Models](https://arxiv.org/abs/2606.00793) *(2026)* — Decomposes world-model memory into entity, environment, and causal consistency across twelve sub-dimensions.
- [KeyFrame-Compass: Towards Comprehensive Evaluation of Keyframe-Conditioned Video Generation](https://arxiv.org/abs/2607.14202) *(2026)* — Decomposes keyframe execution into presence, fidelity, ordering, localization, persistence, and uniqueness metrics.
- [UI2V-Bench: An Understanding-based Image-to-video Generation Benchmark](https://arxiv.org/abs/2509.24427) *(2025)* — Scores image-to-video on spatial understanding, attribute binding, category understanding, and reasoning separately.

#### Reward models and judges for generated video

- [VideoScore: Building Automatic Metrics to Simulate Fine-grained Human Feedback for Video Generation](https://arxiv.org/abs/2406.15252) *(2024)* — Trains an evaluator on five separately annotated quality dimensions rather than one score.
- [VideoScore2: Think before You Score in Generative Video Evaluation](https://arxiv.org/abs/2509.22799) *(2025)* — Produces reasoning traces before scoring visual quality, alignment, and physical plausibility separately.
- [GRADEO: Towards Human-Like Evaluation for Text-to-Video Generation via Multi-Step Reasoning](https://arxiv.org/abs/2503.02341) *(2025)* — Trains a video evaluator on multi-dimensional multi-step reasoning to produce explainable scores.
- [MJ-VIDEO: Fine-Grained Benchmarking and Rewarding Video Preferences in Video Generation](https://arxiv.org/abs/2502.01719) *(2025)* — Stacked aspect-routing and criteria-scoring expert layers predict twenty-eight fine-grained video preference scores.
- [VR-Thinker: Boosting Video Reward Models through Thinking-with-Image Reasoning](https://arxiv.org/abs/2510.10518) *(2025)* — Reward model actively re-selects frames as visual evidence while forming its judgment.
- [VideoDPO: Omni-Preference Alignment for Video Diffusion Generation](https://arxiv.org/abs/2412.14167) *(2024)* — Builds preference pairs from a composite multi-dimension score rather than human labels.
- [Refining Multidimensional Video Reward Models via Disentangled Influence Functions](https://arxiv.org/abs/2605.28203) *(2026)* — Uses influence functions to find which training samples corrupt each reward dimension.
- [ReWorld: Multi-Dimensional Reward Modeling for Embodied World Models](https://arxiv.org/abs/2601.12428) *(2026)* — Extends multi-dimension reward modeling to embodied world-model rollouts.
- [VQ-Insight: Teaching VLMs for AI-Generated Video Quality Understanding via Progressive Visual Reinforcement Learning](https://arxiv.org/abs/2506.18564) *(2025)* — Trains a reasoning video-quality judge by staged RL over multi-dimension, preference, and temporal rewards.
- [Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling](https://arxiv.org/abs/2605.05922) *(2026)* — Separates the reasoning trace from the final regression score.
- [Exploring Video Quality Assessment on User Generated Contents from Aesthetic and Technical Perspectives](https://arxiv.org/abs/2211.04894) *(2022)* — DOVER disentangles aesthetic preference from technical distortion perception into separately modeled branches.
- [Improving Video Generation with Human Feedback](https://arxiv.org/abs/2501.13918) *(2025)* — VideoReward trains a reward model on preferences annotated across named quality dimensions.
- [HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361) *(2026)* — Layers a coarse VLM quality pass over pose-based anatomical and 3D-motion-stability checks.
- [Towards A Better Metric for Text-to-Video Generation](https://arxiv.org/abs/2401.07781) *(2024)* — T2VScore separates text-video alignment from a mixture-of-experts video quality score, each human-calibrated.
- [AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078) *(2026)* — Hierarchical aesthetic rubric of fifteen sub-criteria trains a chain-of-thought video reward model.
- [AIGVE-MACS: Unified Multi-Aspect Commenting and Scoring Model for AI-Generated Video Evaluation](https://arxiv.org/abs/2507.01255) *(2025)* — Emits a language comment alongside a numerical score for each of nine annotated aspects.
- [CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](https://arxiv.org/abs/2605.11723) *(2026)* — Coarse-to-fine anomaly reward model attributes defects to grounded spatiotemporal regions rather than one score.
- [Omni-Judge: Can Omni-LLMs Serve as Human-Aligned Judges for Text-Conditioned Audio-Video Generation?](https://arxiv.org/abs/2602.01623) *(2026)* — Chain-of-thought omni-LLM judge scored against nine named perceptual and cross-modal alignment metrics.
- [Thinking with Frames: Generative Video Distortion Evaluation via Frame Reward Model](https://arxiv.org/abs/2601.04033) *(2026)* — REACT scores structural distortions frame-by-frame against an explicit taxonomy with per-instance attribution.
- [FantasyTalking2: Timestep-Layer Adaptive Preference Optimization for Audio-Driven Portrait Animation](https://arxiv.org/abs/2508.11255) *(2025)* — Talking-Critic scores named preference dimensions fused by timestep-layer adaptive multi-expert optimization.
- [VideoGen-Eval: Agent-based System for Video Generation Evaluation](https://arxiv.org/abs/2503.23452) *(2025)* — Agentic evaluator pairing LLM content structuring with MLLM judging and per-dimension patch tools.
- [Multi-Dimensional Quality Assessment for AI-Generated Human-Centric Videos: Dataset and Model](https://arxiv.org/abs/2607.16742) *(2026)* — Mixture-of-experts rater unifies dimensional scoring, pairwise comparison, and category-specific question answering.
- [VlogReward: Learning Multi-Dimensional Evaluation for Vlog Editing](https://arxiv.org/abs/2607.22632) *(2026)* — Six-dimension vlog-editing taxonomy trains a reward model emitting scores plus actionable refinement feedback.
- [Aligning Anime Video Generation with Human Feedback](https://arxiv.org/abs/2504.10044) *(2025)* — AnimeReward assigns a dedicated vision-language model to each named appearance and consistency dimension.

#### Question and claim decomposition

- [ETVA: Evaluation of Text-to-Video Alignment via Fine-grained Question Generation and Answering](https://arxiv.org/abs/2503.16867) *(2025)* — Parses prompts into scene graphs to generate atomic questions answered by multi-stage video reasoning.
- [Plan-and-Verify Video Reward Reasoning with Spatio-Temporal Scene Graph Grounding](https://arxiv.org/abs/2606.11838) *(2026)* — Decomposes prompts into atomic claims verified individually against a persistent spatio-temporal scene graph.
- [Claim-Level Rubric Rewards for Video Caption Reinforcement Learning](https://arxiv.org/abs/2607.05150) *(2026)* — Decomposes video captions into individually verifiable claims scored as reward.
- [FingER: Content Aware Fine-grained Evaluation with Reasoning for AI-Generated Videos](https://arxiv.org/abs/2504.10358) *(2025)* — Auto-generates entity-level questions across five perspectives, each answered by a reasoning model.
- [VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310) *(2026)* — Dynamically generates per-video visual questions whose VLM answers form actionable semantic-gradient feedback.
- [Physics Question Scene Graph: Fine-grained Evaluation of Physical Plausibility in Text-to-Video Generation](https://arxiv.org/abs/2606.25306) *(2026)* — Hierarchical question graph judges object-, action-, and physics-level plausibility, localizing the violated property.
- [Diffusion-DRF: Free, Rich, and Differentiable Reward for Video Diffusion Fine-Tuning](https://arxiv.org/abs/2601.04153) *(2026)* — Replaces the scalar reward with a frozen VLM answering prompt-decomposed dense visual questions.
- [Self-Correcting Text-to-Video Generation with Misalignment Detection and Localized Refinement](https://arxiv.org/abs/2411.15115) *(2024)* — VideoRepair localizes misalignments via fine-grained MLLM question answering before targeted regeneration.
- [Neuro-Symbolic Evaluation of Text-to-Video Models using Formal Verification](https://arxiv.org/abs/2411.16718) *(2024)* — Compiles prompts into temporal-logic specifications model-checked against an automaton abstraction of the video.
- [VGIF-Score: Interpretable and Diagnostic Evaluation of Spatio-Temporal Instruction Following in Video Generation](https://arxiv.org/abs/2607.13527) *(2026)* — Parses prompts into a spatio-temporal dependency graph whose questions short-circuit to localize the violated constraint.

#### Physics and identity criteria

- [PhysCorr: Dual-Reward DPO for Physics-Constrained Text-to-Video Generation with Automated Preference Selection](https://arxiv.org/abs/2511.03997) *(2025)* — Scores intra-object stability and inter-object interaction separately to drive physics-aware preference optimization.
- [What about gravity in video generation? Post-Training Newton's Laws with Verifiable Rewards](https://arxiv.org/abs/2512.00425) *(2025)* — Computes Newtonian kinematic and mass-conservation rewards programmatically from optical-flow proxies.
- [PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation](https://arxiv.org/abs/2605.14269) *(2026)* — Recovers body meshes into a physics simulator to score kinematics, contact balance, and dynamic feasibility.
- [MagicID: Hybrid Preference Optimization for ID-Consistent and Dynamic-Preserved Video Customization](https://arxiv.org/abs/2503.12689) *(2025)* — Builds preference pairs from separately defined identity-preservation and motion-dynamics rewards.
- [ID-Crafter: VLM-Grounded Online RL for Compositional Multi-Subject Video Generation](https://arxiv.org/abs/2511.00511) *(2025)* — Composite online reward covering instruction fulfillment, visual quality, and multi-subject identity preservation.
- [PhyGround: Benchmarking Physical Reasoning in Generative World Models](https://arxiv.org/abs/2605.10806) *(2026)* — Operationalizes thirteen physical laws as observable sub-questions enabling per-law diagnostics of generated video.

#### Post-training recipes and agentic loops

- [VISTA: A Test-Time Self-Improving Video Generation Agent](https://arxiv.org/abs/2510.15831) *(2025)* — Three specialized critique agents score visual, audio, and contextual fidelity inside an iterative loop.
- [HunyuanVideo 1.5 Technical Report](https://arxiv.org/abs/2511.18870) *(2025)* — Post-training reward model scores text alignment, image alignment, quality, and motion as separate axes.
- [Waver: Wave Your Way to Lifelike Video Generation](https://arxiv.org/abs/2508.15761) *(2025)* — Quality judge predicts an overall label alongside separately scored defect dimensions.
- [LongCat-Video Technical Report](https://arxiv.org/abs/2510.22200) *(2025)* — Multi-reward GRPO sums group-normalized advantages from three reward models, resisting the hacking single-reward training induces.
- [A Systematic Post-Train Framework for Video Generation](https://arxiv.org/abs/2604.25427) *(2026)* — Four-stage pipeline whose GRPO stage scores perceptual quality and temporal coherence separately.
- [Hierarchical Fine-grained Preference Optimization for Physically Plausible Video Generation](https://arxiv.org/abs/2508.10858) *(2025)* — PhysHPO aligns four separately defined hierarchical preference levels rather than one global judgment.
- [AlignHuman: Improving Motion and Fidelity via Timestep-Segment Preference Optimization for Audio-Driven Human Animation](https://arxiv.org/abs/2506.11144) *(2025)* — Trains one expert LoRA per named dimension, each activated in different denoising-timestep intervals.
- [FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159) *(2026)* — Multi-agent MLLM judge scores three named talking-head axes as a composite GRPO reward.
- [PISCES: Annotation-free Text-to-Video Post-Training via Optimal Transport-Aligned Rewards](https://arxiv.org/abs/2602.01624) *(2026)* — Separates a distributional quality reward from a token-level semantic correspondence reward.
- [TempAct: Advancing Temporal Plausibility in Autoregressive Video Generation via Planner-Executor RL](https://arxiv.org/abs/2606.28016) *(2026)* — Hierarchical planner-executor reward stack assigns credit to plan- and execution-level components separately.
- [PAVXploreRL: Physical-Action-Visual World Model Reinforcement Learning with Action Exploration](https://arxiv.org/abs/2607.16602) *(2026)* — Optimizes physical plausibility, action adherence, and visual fidelity as three explicit reward-driven objectives.
- [Seedance 1.0: Exploring the Boundaries of Video Generation Models](https://arxiv.org/abs/2506.09113) *(2025)* — Backpropagates a composite of three separately trained reward models through the predicted clean video.
- [LongCat-Video-Avatar 1.5 Technical Report](https://arxiv.org/abs/2605.26486) *(2026)* — Multi-reward GRPO whose per-frame and temporally partitioned terms localize specific avatar defects.
- [InfLVG: Reinforce Inference-Time Consistent Long Video Generation with GRPO](https://arxiv.org/abs/2505.17574) *(2025)* — Context-selection policy trained on named semantic-alignment, cross-scene-consistency, and artifact-reduction reward components.
- [WorldCycle: Self-Verifiable Reinforcement Learning for Long-Horizon Video World Models](https://arxiv.org/abs/2608.04964) *(2026)* — Reversible action cycles yield annotation-free spatial-closure and temporal-consistency rewards without ground-truth futures.
- [VIVA: VLM-Guided Instruction-Based Video Editing with Reward Optimization](https://arxiv.org/abs/2512.16906) *(2025)* — Weights separate instruction-following, source-preservation, and preference rewards for instruction-based video editing.

#### Rewards for video understanding

- [Incentivizing Vision Language Models to Search for Long Video Question Answering](https://arxiv.org/abs/2607.02959) *(2026)* — Compiles questions into temporal-logic evidence checklists for dense verifiable reward.
- [TimeThink: Reasoning with Time for Video LLMs](https://arxiv.org/abs/2607.05089) *(2026)* — Combines step-wise temporal process rewards with joint process-outcome optimization.
- [Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models](https://arxiv.org/abs/2605.07872) *(2026)* — Benchmark plus reward models for long-reasoning video preference judgment.
- [VideoRewardBench: Comprehensive Evaluation of Multimodal Reward Models for Video Understanding](https://arxiv.org/abs/2509.00484) *(2025)* — Evaluates reward models on video-understanding judgment, distinct from generation.
- [A Benchmark for Omni-Modal Reasoning in Long Videos](https://arxiv.org/abs/2512.16978) *(2025)* — Weighted criterion-level grading across vision, speech, and ambient audio.

### Audio, speech, and music

An emerging area: one 2020 anchor, then almost everything from late 2025 onward.

- [AGAV-Rater: Adapting Large Multimodal Model for AI-Generated Audio-Visual Quality Assessment](https://arxiv.org/abs/2501.18314) *(2025)* — Adapts a multimodal model to rate audio-visual quality jointly rather than per track.
- [Workflow-Based Evaluation of Music Generation Systems](https://arxiv.org/abs/2507.01022) *(2025)* — Scores generated music on a standardized per-criterion scale inside an evaluator workflow.
- [SCORE: Scaling audio generation using Standardized COmposite REwards](https://arxiv.org/abs/2509.19831) *(2025)* — Normalizes and combines several perceptual reward components into one composite signal.
- [PrismAudio: Decomposed Chain-of-Thoughts and Multi-dimensional Rewards for Video-to-Audio Generation](https://arxiv.org/abs/2511.18833) *(2025)* — Four specialized reasoning rewards drive multi-dimensional video-to-audio training.
- [MR-FlowDPO: Multi-Reward Direct Preference Optimization for Flow-Matching Text-to-Music Generation](https://arxiv.org/abs/2512.10264) *(2025)* — Combines text-alignment, semantic-consistency, and production-quality rewards for flow-matching music models.
- [Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models](https://arxiv.org/abs/2603.11661) *(2026)* — Uses online audio-language-model feedback as a fine-grained reward.
- [AnyAudio-Judge: A Dynamic Rubric-Based Benchmark and Evaluator for Audio Instruction Following](https://arxiv.org/abs/2606.03116) *(2026)* — Adaptively decomposes audio captions into verifiable binary criteria across domains.
- [CMI-RewardBench: Evaluating Music Reward Models with Compositional Multimodal Instruction](https://arxiv.org/abs/2603.00610) *(2026)* — Benchmarks music reward models across musicality, text alignment, and compositional instruction dimensions.
- [AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models](https://arxiv.org/abs/2605.24652) *(2026)* — Integrates ten human-centric dimensions spanning visual quality, audio quality, and cross-modal consistency.
- [Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning](https://arxiv.org/abs/2608.02831) *(2026)* — Self-evolving audio-grounded criteria supervise audio reasoning beyond text-only rubrics.
- [AcoustiTrace: When Plausible Sound Violates Physics](https://arxiv.org/abs/2608.02035) *(2026)* — Attributes audio-video violations to eight acoustic-process dimensions grounded in measurable physical quantities.
- [Dual-Axis Generative Reward Model Toward Semantic and Turn-taking Robustness in Interactive Spoken Dialogue Models](https://arxiv.org/abs/2604.14920) *(2026)* — Taxonomy-trained reward model scores spoken-dialogue semantics and turn-taking timing separately for online RL.
- [MMAE: A Massive Multitask Audio Editing Benchmark](https://arxiv.org/abs/2606.07229) *(2026)* — Decomposes free-form audio editing instructions into thousands of verifiable instruction-following and consistency criteria.

### 3D generation

- [3DGen-Bench: Comprehensive Benchmark Suite for 3D Generative Models](https://arxiv.org/abs/2503.21745) *(2025)* — Establishes a 3D preference arena plus a reward model for automatic evaluation.
- [End-to-End Fine-Tuning of 3D Texture Generation using Differentiable Rewards](https://arxiv.org/abs/2506.18331) *(2025)* — Back-propagates differentiable reward through a 3D texture generation pipeline.
- [CREward: A Type-Specific Creativity Reward Model](https://arxiv.org/abs/2511.19995) *(2025)* — Scores 3D asset creativity along geometry, material, and texture axes separately.
- [VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271) *(2026)* — Scores multi-view consistency by cross-frame reprojection error from a geometry foundation model.
- [World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://arxiv.org/abs/2604.24764) *(2026)* — Lifts clips to a 3D representation to score meta-view plausibility, re-render fidelity, and trajectory alignment.
- [Geo-Align: Video Generation Alignment via Metric Geometry Reward](https://arxiv.org/abs/2605.23903) *(2026)* — Extracts camera trajectories with a metric-3D estimator, penalizing rotation and translation deviation separately.
- [Epipolar Geometry Improves Video Generation Models](https://arxiv.org/abs/2510.21615) *(2025)* — Uses classical epipolar-consistency error as a geometric verifier ranking videos into preference pairs.
- [GeoFlow: Enforcing Implicit Geometric Consistency in Video Generation](https://arxiv.org/abs/2605.18365) *(2026)* — Separates rigid camera-induced flow from dynamic object motion, checking each region's consistency.

## Agent, GUI, and Embodied Verification

The densest 2026 area. Verification mechanisms here — environment-state probing, milestone rewards, executable checkers — are architecturally distinct from text judging.

### GUI and computer-use agents

- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596) *(2025)* — Benchmarks outcome and process reward models at trajectory and step level.
- [Agentic Reward Modeling: Verifying GUI Agent via Progressive Trajectory-Grounded Interaction](https://arxiv.org/abs/2602.00575) *(2026)* — A verifier agent probes the environment for evidence rather than passively observing.
- [Adaptive Milestone Reward for GUI Agents](https://arxiv.org/abs/2602.11524) *(2026)* — Anchors trajectories to milestones distilled from successful runs for credit assignment.
- [AgentV-RL: Scaling Reward Modeling with Agentic Verifier](https://arxiv.org/abs/2604.16004) *(2026)* — Turns reward modeling into tool-augmented deliberation with forward and backward verifiers.
- [Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/abs/2607.25904) *(2026)* — Proposes completion conditions then verifies them by invoking system and app tools.
- [OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models](https://arxiv.org/abs/2607.28609) *(2026)* — Standardized cross-platform protocol replacing hand-written per-task verifiers.
- [MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux](https://arxiv.org/abs/2601.13060) *(2026)* — Reflows automated feedback so interface agents self-improve while cutting annotation cost.
- [SeekJudge: A Practical Reward Framework for Reinforcement Learning in Computer-Use Agents](https://arxiv.org/abs/2607.23263) *(2026)* — Role-specialized agents seek trajectory evidence to emit step-level verdicts replacing brittle rule-based supervision.
- [Orcust: Stepwise-Feedback Reinforcement Learning for GUI Agent](https://arxiv.org/abs/2509.17917) *(2025)* — Constrains stepwise GUI rewards by environment-verifiable and model-derived principles rather than outcome alone.

### Embodied and robotic verification

- [VL-CheckList: Evaluating Pre-trained Vision-Language Models with Objects, Attributes and Relations](https://arxiv.org/abs/2207.00221) *(2022)* — Early checklist diagnostic splitting evaluation into object, attribute, and relation checks.
- [Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation](https://arxiv.org/abs/2508.13998) *(2025)* — Two-stage reinforced fine-tuning with a specialized multi-task reward for manipulation.
- [Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition](https://arxiv.org/abs/2505.11175) *(2025)* — Verifies generated reasoning steps against grounded criteria during skill acquisition.
- [Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation](https://arxiv.org/abs/2512.23703) *(2025)* — Multi-view process reward model driving continuous self-improvement in manipulation.
- [Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents](https://arxiv.org/abs/2605.12620) *(2026)* — Scores candidate actions with a learned verifier before execution.
- [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](https://arxiv.org/abs/2602.12281) *(2026)* — Shows compute spent on a verifier can beat compute spent on more policy training.
- [Reward as An Agent for Embodied World Models](https://arxiv.org/abs/2606.19990) *(2026)* — An agentic reward framework actively evaluates generated behaviors to resist reward hacking.
- [RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models](https://arxiv.org/abs/2605.03821) *(2026)* — Defines robot-centric judge dimensions for aligning video world models via RL.
- [RDA: Reward Design Agent for Reinforcement Learning](https://arxiv.org/abs/2606.01672) *(2026)* — Vision-language agent revises executable reward code from visual trajectory critiques instead of coarse success rates.

### Rubric rewards for agents, tool use, and software engineering

- [Agentic Rubrics as Contextual Verifiers for SWE Agents](https://arxiv.org/abs/2601.04171) *(2026)* — A repo-grounded checklist scores code patches without executing tests.
- [Beyond Verifiable Rewards: Rubric-Based GRM for Reinforced Fine-Tuning SWE Agents](https://arxiv.org/abs/2604.16335) *(2026)* — A human-designed criteria reward model filters and scores trajectories for fine-tuning.
- [SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling](https://arxiv.org/abs/2604.14820) *(2026)* — Criteria-based process reward plus memory-augmented RL for long-horizon coding.
- [StitchCUDA: An Automated Multi-Agents End-to-End GPU Programing Framework with Rubric-based Agentic Reinforcement Learning](https://arxiv.org/abs/2603.02637) *(2026)* — Trains a coder agent on combined criteria and execution rewards inside a planner-coder-verifier pipeline.
- [Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents](https://arxiv.org/abs/2605.23590) *(2026)* — Criteria act as per-step collaborators giving dense feedback inside the reasoning-action loop.
- [ARBOR: Online Process Rewards via a Reusable Rubric Buffer for Search Agents](https://arxiv.org/abs/2606.03239) *(2026)* — A reusable criteria buffer supplies online process rewards for multi-hop search.
- [RUBAS: Rubric-Based Reinforcement Learning for Agent Safety](https://arxiv.org/abs/2606.04051) *(2026)* — Multi-dimensional criteria rewards spanning tool-use, argument, and response safety.
- [VideoWeaver: Evaluating and Evolving Skills for Agentic Long Video Generation](https://arxiv.org/abs/2606.08091) *(2026)* — Agent-as-judge grounds scores in execution traces and intermediate files across sixteen task categories.
- [LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards](https://arxiv.org/abs/2605.31584) *(2026)* — Criteria rewards supervise long-context reasoning learned from search trajectories.
- [Step-DeepResearch Technical Report](https://arxiv.org/abs/2512.20491) *(2025)* — A checklist-style judger hardens an autonomous research agent across a staged training pipeline.
- [Agent-as-a-Judge: Evaluate Agents with Agents](https://arxiv.org/abs/2410.10934) *(2024)* — Uses agentic systems to evaluate agentic code generation against hierarchical annotated task requirements.
- [Willful Disobedience: Automatically Detecting Failures in Agentic Traces](https://arxiv.org/abs/2603.23806) *(2026)* — Extracts behavioral rules from agent prompts, then checks traces for specification compliance.
- [LH-Bench: Skill-Grounded Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks](https://arxiv.org/abs/2603.22744) *(2026)* — Expert-grounded criteria give judges the domain context that model-authored rubrics lack.
- [PRBench: End-to-end Paper Reproduction in Physics Research](https://arxiv.org/abs/2603.27646) *(2026)* — Grades end-to-end physics paper reproduction against detailed scoring rubrics and verified ground truth.
- [Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards](https://arxiv.org/abs/2601.22511) *(2026)* — Trains small agentic models entirely in synthetic environments graded by criteria.
- [CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents](https://arxiv.org/abs/2606.22883) *(2026)* — Validates synthesized terminal tasks against explicit criteria for correctness and coverage.
- [Auto-Eval Judge: Towards a General Agentic Framework for Task Completion Evaluation](https://arxiv.org/abs/2508.05508) *(2025)* — Decomposes tasks into sub-tasks validated by aspect-specific modules, targeting domain-independent agent evaluation.
- [Online Agent-as-a-Judge: Situation-Generating Evaluation for Interactive Agents](https://arxiv.org/abs/2606.08200) *(2026)* — An in-world evaluator agent provokes situations so authored social criteria become observable rather than waiting.
- [SkillCoach: Self-Evolving Rubrics for Evaluating and Enhancing Agentic Skill-Use](https://arxiv.org/abs/2607.01874) *(2026)* — Derives skill-grounded process rubrics scoring selection, following, composition, and reflection separately.
- [AgentAuditor: Human-Level Safety and Security Evaluation for LLM Agents](https://arxiv.org/abs/2506.00641) *(2025)* — Retrieves structured reasoning experiences from memory to guide training-free evaluation of agent safety risks.
- [Guideline-Grounded Evidence Accumulation for High-Stakes Agent Verification](https://arxiv.org/abs/2603.02798) *(2026)* — Scores step-wise alignment with expert clinical guidelines, calibrating aggregated ratings into correctness probabilities.
- [Human-on-the-Bridge: Scalable Evaluation for AI Agents](https://arxiv.org/abs/2606.16871) *(2026)* — Experts curate juror personas, scoring guidelines, and audit rules upfront for repeated adversarial evaluation.
- [SRR-Judge: Step-Level Rating and Refinement for Enhancing Search-Integrated Reasoning in Search Agents](https://arxiv.org/abs/2602.07773) *(2026)* — Rates each search-agent step against four named criteria inside a rate-and-refine loop.
- [Aligning Agents via Planning: A Benchmark for Trajectory-Level Reward Modeling](https://arxiv.org/abs/2604.08178) *(2026)* — Tests trajectory judges on four tool-use task families against deliberately confusable hard negatives.
- [WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models](https://arxiv.org/abs/2604.18224) *(2026)* — Checklist-guided judging of web editing plus an agent judge executing generated sites in-browser.
- [AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking](https://arxiv.org/abs/2604.23581) *(2026)* — Grades each workflow node against typed quality metrics, attributing failures through a hierarchical error taxonomy.

### Rubric rewards for deep research

- [DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research](https://arxiv.org/abs/2511.19399) *(2025)* — Criteria co-evolve with the policy to absorb newly discovered evidence.
- [DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents](https://arxiv.org/abs/2606.17029) *(2026)* — Evidence-tree supervision gives dense efficient rewards for research agents.
- [Deep Research as Rubric for Reinforcement Learning](https://arxiv.org/abs/2606.01091) *(2026)* — Uses the research process itself as the criteria structure for the reward.
- [QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks](https://arxiv.org/abs/2605.24218) *(2026)* — Rubric-tree synthesis decomposes queries into verifiable leaves for dense reward.
- [AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research Agents](https://arxiv.org/abs/2605.11732) *(2026)* — Repurposes the generator as a scoring agent that evaluates critic outputs into quality signals.
- [Self-Evolving Deep Research via Joint Generation and Evaluation](https://arxiv.org/abs/2606.04507) *(2026)* — Shared-parameter evaluator and solver co-evolve, with a meta-harness policing which evaluation dimensions stay valid.
- [Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification](https://arxiv.org/abs/2601.15808) *(2026)* — Derives verification criteria from an automatically constructed failure taxonomy, feeding critiques back at test time.

## Rubric Quality and Meta-Evaluation

Whether criteria-based judging is reliable at all.

- [RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following](https://arxiv.org/abs/2603.25133) *(2026)* — Meta-evaluates judges at the individual criterion level rather than the aggregate score.
- [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://arxiv.org/abs/2606.29920) *(2026)* — Meta-evaluates judge reliability at rubric scoring specifically on long, complex agentic outputs.
- [Autorubric: Unifying Rubric-based LLM Evaluation](https://arxiv.org/abs/2603.00077) *(2026)* — Unifies binary, ordinal, and nominal criteria under one framework with bias mitigation.
- [RubricBench: Aligning Model-Generated Rubrics with Human Standards](https://arxiv.org/abs/2603.01562) *(2026)* — Benchmarks model-generated criteria against expert-annotated ones over curated pairs.
- [SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation](https://arxiv.org/abs/2603.29186) *(2026)* — Synthetic degradation pairs across ten aspects meta-evaluate automatic text-to-long-video evaluation systems.
- [Physics-IQ Verified](https://arxiv.org/abs/2606.18943) *(2026)* — Audits a physics benchmark's ground truth and reweights its scoring to equal-weight sample-level criteria.
- [Rethinking Reward Signals in Video GRPO: When Scores Become Targets](https://arxiv.org/abs/2511.19356) *(2025)* — Diagnoses Goodhart saturation and shortcut exploitation per reward component, then adaptively reweights them.
- [VF-Eval: Evaluating Multimodal LLMs for Generating Feedback on AIGC Videos](https://arxiv.org/abs/2505.23693) *(2025)* — Decomposes judge quality on generated video into four separately scored feedback tasks.
- [CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation](https://arxiv.org/abs/2607.29252) *(2026)* — Builds compact task-adaptive criteria banks via a measurability posterior.
- [Rubric-Conditioned LLM Grading: Alignment, Uncertainty, and Robustness](https://arxiv.org/abs/2601.08843) *(2025)* — Finds alignment holds for binary criteria but degrades as granularity increases.
- [Agreement Metrics for LLM-as-Judge Evaluation: What to Report and Why](https://arxiv.org/abs/2606.00093) *(2026)* — Defines which agreement statistics criteria-based judging papers should report.
- [Judge Reliability Harness: Stress Testing the Reliability of LLM Judges](https://arxiv.org/abs/2603.05399) *(2026)* — Perturbs formatting, phrasing, and verbosity to stress-test judge consistency.
- [From Rubrics to Reliable Scores: Evidence-Grounded Text Evaluation with LLM Judges](https://arxiv.org/abs/2601.08654) *(2026)* — Locks human criteria into fixed specifications executed with extractive evidence grounding.
- [JudgmentBench: Comparing Rubric and Preference Evaluation for Quality Assessment](https://arxiv.org/abs/2605.25240) *(2026)* — Compares criteria-based scoring against pairwise preference on expert-annotated tasks.
- [Learning to Judge: LLMs Designing and Applying Evaluation Rubrics](https://arxiv.org/abs/2602.08672) *(2026)* — Studies models both authoring and applying their own evaluation criteria.
- [Is this Idea Novel? An Automated Benchmark for Judgment of Research Ideas](https://arxiv.org/abs/2603.10303) *(2026)* — Benchmarks automated novelty judgment, including criteria-based scoring, against expert human verdicts.
- [On Predicting the Post-training Potential of Pre-trained LLMs](https://arxiv.org/abs/2605.11978) *(2026)* — Predicts a base model's post-training ceiling from its criteria-satisfying likelihood gap.
- [Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist](https://arxiv.org/abs/2407.08733) *(2024)* — Tests robustness with a checklist of task variants rather than single-answer accuracy.
- [Do We Need a Detailed Rubric for Automated Essay Scoring using Large Language Models?](https://arxiv.org/abs/2505.01035) *(2025)* — Tests how criteria detail affects scoring accuracy, finding simplified rubrics often suffice.
- [GroUSE: A Benchmark to Evaluate Evaluators in Grounded Question Answering](https://arxiv.org/abs/2409.06595) *(2024)* — Unit tests built from named generator failure modes reveal which ones judges overlook.
- [Beyond the Leaderboard: Rethinking Medical Benchmarks for Large Language Models](https://arxiv.org/abs/2508.04325) *(2025)* — A lifecycle checklist for auditing medical benchmarks themselves rather than the models.
- [Same Verdict, Different Reasons: LLM-as-a-Judge and Clinician Disagreement on Medical Chatbot Completeness](https://arxiv.org/abs/2604.16383) *(2026)* — Stress-tests three criteria granularities against clinicians, finding near-chance discrimination.
- [Quantifying the Statistical Effect of Rubric Modifications on Human-Autorater Agreement](https://arxiv.org/abs/2605.06283) *(2026)* — Analyzes how holistic versus decomposed criteria edits shift human-autorater agreement.
- [Does Context Matter? ContextualJudgeBench for Evaluating LLM-based Judges in Contextual Settings](https://arxiv.org/abs/2503.15620) *(2025)* — A judge benchmark built on conditional criteria ordering for retrieval-grounded settings.
- [Do You Need a Frontier Model as a Citation Verifier? Benchmarking Rubric LLMs for Deep-Research Source Attribution](https://arxiv.org/abs/2607.08700) *(2026)* — Benchmarks judges scoring citation relevance and factual support, finding cheaper models calibrate adequately.

## Rubric-Graded Benchmarks

Three strata cut across domain: **expert-authored** criteria written once by specialists, **dynamically generated** criteria synthesized per query at evaluation time, and **meta-evaluation** of whether criteria-based judging works at all.

| Name | Year | Domain | What the criteria grade |
|---|---|---|---|
| [HealthBench](https://arxiv.org/abs/2505.08775) | 2025 | Medical dialogue | Physician-written weighted criteria per conversation |
| [HealthBench Professional](https://arxiv.org/abs/2604.27470) | 2026 | Clinical chat | Rubric grading of real clinician-authored transcripts |
| [ClinConsensus](https://arxiv.org/abs/2603.02097) | 2026 | Chinese medical QA | Physician-calibrated criteria coverage |
| [Rethinking Evidence Hierarchies](https://arxiv.org/abs/2508.00081) | 2025 | Medical dialogue | Critique of the evidence hierarchy behind physician criteria |
| [HealthBench in Action](https://arxiv.org/abs/2509.02594) | 2025 | Clinical queries | Physician-rubric grading applied to a deployed assistant |
| [From Feedback to Checklists](https://arxiv.org/abs/2507.17717) | 2025 | Clinical notes | Checklists derived from aggregated physician feedback |
| [LiveMedBench](https://arxiv.org/abs/2602.10367) | 2026 | Medical QA | Automated criteria over contamination-free live cases |
| [MedDialogRubrics](https://arxiv.org/abs/2601.03023) | 2026 | Medical consultation | Clinician-refined criteria over synthetic multi-turn cases |
| [QuarkMedBench](https://arxiv.org/abs/2603.13691) | 2026 | Medical QA | Per-query criteria from multi-model consensus, hierarchically weighted |
| [PanCanBench](https://arxiv.org/abs/2603.01343) | 2026 | Oncology QA | Question-specific expert criteria over real patient questions |
| [Med-RewardBench](https://arxiv.org/abs/2508.21430) | 2025 | Medical multimodal | Six clinically critical dimensions over expert cases |
| [GAPS](https://arxiv.org/abs/2510.13734) | 2025 | Clinical QA | Agent-synthesized guideline-anchored criteria, ensemble-judged |
| [PaperBench](https://arxiv.org/abs/2504.01848) | 2025 | Research replication | Hierarchical criteria decomposing paper reproduction |
| [SWE Atlas](https://arxiv.org/abs/2605.08366) | 2026 | Agentic coding | Code quality and design beyond issue resolution |
| [WebDevJudge](https://arxiv.org/abs/2510.18560) | 2025 | Web development | Structured query-grounded criteria as judge ground truth |
| [OSWorld](https://arxiv.org/abs/2404.07972) | 2024 | Computer use | Per-task verifiable criteria with partial credit |
| [DeepResearch Bench](https://arxiv.org/abs/2506.11763) | 2025 | Research reports | Report quality and citation accuracy criteria |
| [DeepResearch Bench II](https://arxiv.org/abs/2601.08536) | 2026 | Research reports | Binary criteria from expert investigative articles |
| [ResearchRubrics](https://arxiv.org/abs/2511.07685) | 2025 | Deep research | Expert-written criteria measuring rubric adherence |
| [ResearchQA](https://arxiv.org/abs/2509.00496) | 2025 | Scholarly QA | Survey-mined criteria on citations, explanations, limitations |
| [DEER](https://arxiv.org/abs/2512.17776) | 2025 | Expert reports | Fine-grained criteria under a multi-dimension taxonomy |
| [ResearcherBench](https://arxiv.org/abs/2507.16280) | 2025 | Deep research | Expert-designed criteria plus factual and citation checks |
| [Dr. Bench](https://arxiv.org/abs/2510.02190) | 2025 | Deep research | Semantic quality, topical focus, retrieval trustworthiness |
| [DRACO](https://arxiv.org/abs/2602.11685) | 2026 | Cross-domain research | Task-specific criteria on accuracy, completeness, presentation, citations |
| [MiroEval](https://arxiv.org/abs/2603.28407) | 2026 | Multimodal research | Per-query criteria plus atomic-claim factuality |
| [Expert Consulting Benchmark](https://arxiv.org/abs/2605.17554) | 2026 | Consulting | Deterministic verifiers plus an expert criterion set |
| [ProfBench](https://arxiv.org/abs/2510.18941) | 2025 | Professional reasoning | Criteria requiring expertise to answer and to grade |
| [UpBench](https://arxiv.org/abs/2511.12306) | 2025 | Real labor-market tasks | Expert-decomposed acceptance criteria with per-criterion feedback |
| [FrontierScience](https://arxiv.org/abs/2601.21165) | 2026 | Expert science tasks | Granular criteria grading the process, not just final answers |
| [GIM](https://arxiv.org/abs/2605.18663) | 2026 | Cross-domain integration | Rubric-decomposed scoring, several independently judged criteria per item |
| [COMPOSITE-Stem](https://arxiv.org/abs/2604.09836) | 2026 | Doctoral STEM | Criterion-based rubrics with an LLM-jury protocol beside exact match |
| [PRBench (Professional Reasoning)](https://arxiv.org/abs/2511.11562) | 2025 | Legal and finance | Large expert-authored criteria sets |
| [GreekBarBench](https://arxiv.org/abs/2505.17267) | 2025 | Legal (Greek bar) | Three-dimensional scoring rubric with span-based grounding |
| [oab-bench](https://arxiv.org/abs/2504.21202) | 2025 | Legal (Brazilian bar) | The same evaluation guidelines human examiners apply |
| [LLMEval-Med](https://arxiv.org/abs/2506.04078) | 2025 | Clinical scenarios | Expert checklists inside a physician-refined judge pipeline |
| [$OneMillion-Bench](https://arxiv.org/abs/2603.07980) | 2026 | Multi-domain expert | Accuracy, coherence, professional compliance |
| [PLawBench](https://arxiv.org/abs/2601.16669) | 2026 | Legal practice | Expert-designed criteria across legal scenarios |
| [LexRubric](https://arxiv.org/abs/2606.09389) | 2026 | Legal tasks | Atomic criteria under a six-dimensional framework |
| [Magis-Bench](https://arxiv.org/abs/2605.08437) | 2026 | Legal reasoning | Criteria-based magistrate-level grading |
| [Legal Issue Tree Rubrics](https://arxiv.org/abs/2512.01020) | 2025 | Legal traces | Tree-structured criteria for issue-spotting |
| [FinResearchBench II](https://arxiv.org/abs/2607.12252) | 2026 | Financial reports | Consensus-derived gold criteria |
| [WritingBench](https://arxiv.org/abs/2503.05244) | 2025 | Generative writing | Query-specific dynamic criteria via a critic model |
| [Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation](https://arxiv.org/abs/2606.01629) | 2026 | Long-form output | Meta-eval of judge reliability on document-length text |
| [HelloBench](https://arxiv.org/abs/2409.16191) | 2024 | Long text | Hierarchical checklist across five task types |
| [DeepSynth-Eval](https://arxiv.org/abs/2601.03540) | 2026 | Survey writing | Factual-coverage plus structural-constraint checklists |
| [MoReBench](https://arxiv.org/abs/2510.16380) | 2025 | Moral reasoning | Pluralistic criteria on the reasoning process |
| [FLASK](https://arxiv.org/abs/2307.10928) | 2023 | General alignment | Per-skill ratings across alignment competencies |
| [BiGGen Bench](https://arxiv.org/abs/2406.05761) | 2024 | General | Per-instance criteria across many capabilities |
| [LMUnit](https://arxiv.org/abs/2412.13091) | 2024 | General | Natural-language criteria as pass/fail unit tests |
| [IFEval](https://arxiv.org/abs/2311.07911) | 2023 | Instructions | Programmatically verifiable constraints |
| [InFoBench](https://arxiv.org/abs/2401.03601) | 2024 | Instructions | Per-instruction yes/no decomposition |
| [FollowBench](https://arxiv.org/abs/2310.20410) | 2023 | Instructions | Multi-level constraint difficulty ladder |
| [M-IFEval](https://arxiv.org/abs/2502.04688) | 2025 | Multilingual instructions | Verifiable constraints in three languages |
| [CoDI-Eval](https://arxiv.org/abs/2401.00690) | 2024 | Controllable generation | Explicit constraint attributes graded automatically for compliance |
| [XIFBench](https://arxiv.org/abs/2503.07539) | 2025 | Multilingual instructions | Categorized content, style, format, and numerical constraints |
| [SIFo](https://arxiv.org/abs/2406.19999) | 2024 | Sequential instructions | Final-step verification of an instruction chain |
| [LLMBar](https://arxiv.org/abs/2310.07641) | 2023 | Judge meta-eval | Judge accuracy on instruction-following pairs |
| [RewardBench](https://arxiv.org/abs/2403.13787) | 2024 | Reward models | Chosen-rejected accuracy across categories |
| [RewardBench 2](https://arxiv.org/abs/2506.01937) | 2025 | Reward models | Harder best-of-N-style discrimination |
| [JudgeBench](https://arxiv.org/abs/2410.12784) | 2024 | Judges | Objectively verifiable correctness pairs |
| [RM-Bench](https://arxiv.org/abs/2410.16184) | 2024 | Reward models | Subtle content edits versus stylistic bias |
| [IF-RewardBench](https://arxiv.org/abs/2603.04738) | 2026 | Judges | Preference-graph instruction-following ranking |
| [MCJudgeBench](https://arxiv.org/abs/2605.03858) | 2026 | Judges (instructions) | Per-constraint gold labels over multi-constraint instructions |
| [UEval](https://arxiv.org/abs/2601.22155) | 2026 | Unified multimodal generation | Human-validated per-question criteria for image and text output |
| [XpertBench](https://arxiv.org/abs/2604.02368) | 2026 | Expert tasks | Granular per-task criteria under a dedicated judge |
| [JobBench](https://arxiv.org/abs/2605.26329) | 2026 | Delegated work | Chained all-or-nothing criteria |
| [Long-Horizon-Terminal-Bench](https://arxiv.org/abs/2607.08964) | 2026 | Terminal agents | Subtask-level partial-credit grading |
| [TRAJECT-Bench](https://arxiv.org/abs/2510.04550) | 2025 | Tool use | Step-by-step trajectory diagnosis |
| [MCP-Universe](https://arxiv.org/abs/2508.14704) | 2025 | Tool use | Execution-based evaluators against live servers |
| [ASTRA-bench](https://arxiv.org/abs/2603.01357) | 2026 | Tool use | Personal-context-aware planning criteria |
| [AgentBoard](https://arxiv.org/abs/2401.13178) | 2024 | Multi-turn agents | Fine-grained subgoal-completion progress |
| [MultiChallenge](https://arxiv.org/abs/2501.17399) | 2025 | Multi-turn chat | Four per-turn challenge categories |
| [PresentBench](https://arxiv.org/abs/2603.07244) | 2026 | Slide generation | Binary checklist items on content and layout |
| [GDP.pdf](https://arxiv.org/abs/2607.11192) | 2026 | Professional PDF QA | A rubric of atomic criteria reported beside strict pass rates |
| [TechImage-Bench](https://arxiv.org/abs/2512.12220) | 2025 | Technical images | Binary criteria mined from textbooks |
| [Video-Bench](https://arxiv.org/abs/2504.04907) | 2025 | Video generation | Multimodal judges applied across every evaluation dimension |
| [EvalVerse](https://arxiv.org/abs/2605.23271) | 2026 | Cinematic video | Expert-calibrated taxonomy following the filmmaking pipeline |
| [VABench](https://arxiv.org/abs/2512.09299) | 2025 | Audio-video generation | Fifteen dimensions spanning cross-modal similarity, sync, and lip-speech |
| [MSAVBench](https://arxiv.org/abs/2605.20183) | 2026 | Multi-shot audio-video | Video, audio, shot, and reference dimensions with instance-wise rubrics |
| [VEFX-Bench](https://arxiv.org/abs/2604.16272) | 2026 | Video editing and VFX | Instruction following, rendering quality, edit exclusivity scored separately |
| [Apple-pi](https://arxiv.org/abs/2607.16401) | 2026 | Physical reasoning video | Perception, formulation, and deduction stages scored separately |
| [VideoScience-Bench](https://arxiv.org/abs/2512.02942) | 2025 | Scientific video | Five physics- and chemistry-grounded consistency dimensions |
| [AV-Phys Bench](https://arxiv.org/abs/2605.07061) | 2026 | Audio-video physics | Five semantic and physical-commonsense dimensions across both modalities |
| [AIGVE-Bench](https://arxiv.org/abs/2503.14064) | 2025 | Video generation | Nine critical quality dimensions under a five-category method taxonomy |
| [WorldScore](https://arxiv.org/abs/2504.00983) | 2025 | World generation | Controllability, quality, and dynamics across 3D, 4D, and video |
| [Stable Cinemetrics](https://arxiv.org/abs/2509.26555) | 2025 | Professional video | Seventy-six filmmaking control nodes scored by auto-generated questions |
| [AVGen-Bench](https://arxiv.org/abs/2604.08540) | 2026 | Text-to-audio-video | Aesthetics separated from fine-grained semantic controllability per task |
| [AIGVE-60K](https://arxiv.org/abs/2505.12098) | 2025 | Video generation | Twenty fine-grained task dimensions with paired opinion and QA labels |
| [T2VEval-Bench](https://arxiv.org/abs/2501.08545) | 2025 | Text-to-video | Overall impression, text consistency, realness, and technical quality |
| [TDVE-DB](https://arxiv.org/abs/2505.19535) | 2025 | Text-driven video editing | Edited quality, editing alignment, and structural consistency rated separately |
| [VideoPhy-2](https://arxiv.org/abs/2503.06800) | 2025 | Action-centric physics | Semantic adherence, physical commonsense, and physical-rule grounding |
| [Physion-Eval](https://arxiv.org/abs/2603.19607) | 2026 | Physical realism | Expert reasoning traces localizing twenty-two named physical-failure categories |
| [TiViBench](https://arxiv.org/abs/2511.13704) | 2025 | Image-to-video reasoning | Structural, spatial, symbolic, and action-planning reasoning dimensions |
| [SafeGen-Bench](https://arxiv.org/abs/2606.01481) | 2026 | Video safety | Ten malicious categories spanning risky temporal sequences and behaviors |
| [T2VPhysBench](https://arxiv.org/abs/2505.00337) | 2025 | Text-to-video physics | Twelve enumerated physical laws each scored separately by humans |
| [VideoVerse](https://arxiv.org/abs/2510.08398) | 2025 | World-model video | Ten per-prompt dimensions targeting event-level temporal causality |
| [IVEBench](https://arxiv.org/abs/2510.11647) | 2025 | Instruction-guided video editing | Video quality, instruction compliance, and video fidelity |
| [LoCoT2V-Bench](https://arxiv.org/abs/2510.26412) | 2025 | Long-form text-to-video | Five dimensions including a human-expectation realization degree |
| [V-ReasonBench](https://arxiv.org/abs/2511.16668) | 2025 | Video generation reasoning | Structured, spatial, pattern-based, and physical reasoning scored apart |
| [RULER-Bench](https://arxiv.org/abs/2512.02622) | 2025 | Rule-based video reasoning | Per-video checklists spanning six cognitive rule categories |
| [VIPER](https://arxiv.org/abs/2512.24952) | 2025 | Generative video reasoning | Hierarchical rubric grading intermediate frame-reasoning validity |
| [WorldBench](https://arxiv.org/abs/2601.21282) | 2026 | World-model physics | One isolated physical concept per diagnostic test |
| [UniEditBench](https://arxiv.org/abs/2604.15871) | 2026 | Image and video editing | Structural fidelity, text alignment, background consistency, and naturalness |
| [WorldMark](https://arxiv.org/abs/2604.21686) | 2026 | Interactive video world models | Direction accuracy, purity, response latency, and motion stability |
| [BRITE](https://arxiv.org/abs/2605.00873) | 2026 | Implausible-scenario video | Human-verified question-answer criteria covering audio-visual consistency |
| [Edit-Compass](https://arxiv.org/abs/2605.13062) | 2026 | Image editing | Structured-reasoning scoring rubrics across progressively harder editing categories |
| [LongAV-Compass](https://arxiv.org/abs/2605.26244) | 2026 | Minute-scale audio-visual | Within-segment quality, cross-segment consistency, and narrative coherence |
| [DirectorBench](https://arxiv.org/abs/2605.30090) | 2026 | Long-form video generation | Forty checkpoint criteria across script, visual, audio, and stability |
| [CoVEBench](https://arxiv.org/abs/2606.08415) | 2026 | Complex video editing | Checklist items covering requested edits and preservation constraints |
| [MultiRef-Compass](https://arxiv.org/abs/2607.14189) | 2026 | Multi-reference audio-video | Four dimensions decomposed into fourteen auditable sub-metrics |
| [CultureVidBench](https://arxiv.org/abs/2608.01942) | 2026 | Cultural text-to-video | Fourteen cultural aspects scored for faithfulness and rendering |
| [WorldExam](https://arxiv.org/abs/2608.02603) | 2026 | Video world models | Visual quality, control adherence, spatial consistency, and world reactivity |
| [OmniEdit-Bench](https://arxiv.org/abs/2608.05049) | 2026 | Instruction-based video editing | Preservation, realism, and consistency gated on edit accuracy |
| [GAUGE](https://arxiv.org/abs/2608.05948) | 2026 | Physical fidelity | Task-specific physical observables calibrated from real-world trajectories |
| [Mind2Web 2](https://arxiv.org/abs/2506.21506) | 2025 | Agentic search | Tree-structured per-task rubrics grading correctness and source attribution |
| [FinResearchBench](https://arxiv.org/abs/2507.16248) | 2025 | Financial research agents | Extracted logic trees of the research outcome per task type |
| [UniGenBench++](https://arxiv.org/abs/2510.18701) | 2025 | Text-to-image semantics | Ten primary and twenty-seven sub-criteria over bilingual prompt themes |
| [T2AV-Compass](https://arxiv.org/abs/2512.21094) | 2025 | Text-to-audio-video | Signal-level video, audio, and cross-modal scores plus judged instruction following |
| [AJ-Bench](https://arxiv.org/abs/2604.18240) | 2026 | Agent-as-a-judge | Judge information acquisition, state verification, and process verification |
| [ICE-Bench](https://arxiv.org/abs/2503.14482) | 2025 | Image creation and editing | Six dimensions from aesthetics to controllability across thirty-one tasks |
| [EdiVal-Agent](https://arxiv.org/abs/2509.13399) | 2025 | Multi-turn image editing | Instruction following, content consistency, and visual quality per turn |
| [VinaBench](https://arxiv.org/abs/2503.20871) | 2025 | Visual narratives | Annotated commonsense and discourse constraints for faithfulness and consistency |
| [DEVIL](https://arxiv.org/abs/2407.01094) | 2024 | Text-to-video dynamics | Dynamics range, controllability, and dynamics-based quality scored separately |
| [DynamicEval](https://arxiv.org/abs/2510.07441) | 2025 | Dynamic-camera text-to-video | Background scene consistency and foreground object consistency measured separately |
| [ViDiC](https://arxiv.org/abs/2512.03405) | 2025 | Video difference captioning | Dual similarity and difference checklists across seven comparison categories |
| [SVBench](https://arxiv.org/abs/2512.21507) | 2025 | Social reasoning in video | Five interpretable social-reasoning dimensions over thirty psychology paradigms |
| [MechVerse](https://arxiv.org/abs/2605.14843) | 2026 | Mechanical motion in video | Part identity, motion primitive, and inter-part coupling constraints per clip |
| [BlueFin](https://arxiv.org/abs/2605.30907) | 2026 | Financial spreadsheet agents | Expert-validated granular rubric criteria per task, graded by a judge |
| [V2V-Bench](https://arxiv.org/abs/2606.05665) | 2026 | Video-to-video generation | Eleven dimensions across temporal alignment, structural fidelity, and semantic alignment |
| [StrongREJECT](https://arxiv.org/abs/2402.10260) | 2024 | Safety | Detailed harmfulness rubric for jailbreak responses |
| [Claw-Eval](https://arxiv.org/abs/2604.06132) | 2026 | Autonomous agents | Trajectory-aware safety and robustness criteria |
| [RefGrader](https://arxiv.org/abs/2510.09021) | 2025 | Math proofs | Problem-specific criteria for partial credit |
| [Beyond Score Prediction](https://arxiv.org/abs/2607.19219) | 2026 | Essay feedback | Binary criteria grading feedback quality |
| [LiveCodeBench Pro](https://arxiv.org/abs/2506.11928) | 2025 | Competitive programming | Olympiad-medalist expert judgment |

## Datasets

| Name | Year | What it contains |
|---|---|---|
| [Feedback Collection / Prometheus](https://arxiv.org/abs/2310.08491) | 2023 | Customized score rubrics with graded responses for evaluator training |
| [EditHF-1M](https://arxiv.org/abs/2603.14916) | 2026 | Image-editing preferences rated on visual quality, instruction alignment, and attribute preservation |
| [Preference Collection / Prometheus 2](https://arxiv.org/abs/2405.01535) | 2024 | Criteria-graded preference pairs for judge training |
| [HelpSteer](https://arxiv.org/abs/2311.09528) | 2023 | Multi-attribute helpfulness ratings across named dimensions |
| [HelpSteer2](https://arxiv.org/abs/2406.08673) | 2024 | Compact multi-attribute preference pairs |
| [HelpSteer2-Preference](https://arxiv.org/abs/2410.01257) | 2024 | Attribute ratings complemented with pairwise preferences |
| [HelpSteer3-Preference](https://arxiv.org/abs/2505.11475) | 2025 | Human-annotated multilingual preference pairs |
| [PKU-SafeRLHF](https://arxiv.org/abs/2406.15513) | 2024 | Preference pairs decoupling helpfulness and harmlessness across harm categories and severity |
| [RubricHub](https://arxiv.org/abs/2601.08430) | 2026 | Large multi-domain automatically generated criteria |
| [ARES](https://arxiv.org/abs/2605.23454) | 2026 | Questions, references, and weighted criteria synthesized together |
| [Pick-a-Pic](https://arxiv.org/abs/2305.01569) | 2023 | Open crowd-sourced image preference pairs |
| [VLFeedback](https://arxiv.org/abs/2410.09421) | 2024 | Multi-aspect AI-feedback annotations for vision-language alignment |
| [MM-RLHF](https://arxiv.org/abs/2502.10391) | 2025 | Multimodal preference data with dimension-level critique |
| [DataRubrics](https://arxiv.org/abs/2506.01789) | 2025 | Criteria-based quality scoring applied to datasets themselves |

## Human Annotation Rubrics and Protocols

Rubrics shaping human labels rather than model rewards. A small literature, but the place where inter-rater disagreement gets studied honestly.

- [When LLM Essays Outscore Student Essays: What a Korean Writing Rubric Rewards and Where Readers Disagree](https://arxiv.org/abs/2601.19913) *(2026)* — A sixteen-criterion rubric shows where human readers diverge while applying shared criteria.
- [Diverging Preferences: When do Annotators Disagree and do Models Know?](https://arxiv.org/abs/2410.14632) *(2024)* — A taxonomy of disagreement sources shows most divergence traces to task underspecification or style.
- [Using Natural Language Explanations to Rescale Human Judgments](https://arxiv.org/abs/2305.14770) *(2023)* — Rescores annotator Likert ratings against a shared scoring guide using their written explanations.
- [Rubric-Guided Fine-tuning of SpeechLLMs for Multi-Aspect, Multi-Rater L2 Reading-Speech Assessment](https://arxiv.org/abs/2603.16889) *(2026)* — Models multiple raters explicitly rather than collapsing them to one consensus label.

## Domain-Specific Rubric RL

- [InfiMed-ORBIT: Aligning LLMs on Open-Ended Complex Tasks via Rubric-Based Incremental Training](https://arxiv.org/abs/2510.15859) *(2025)* — Case-conditioned criteria act as adaptive guides for incremental clinical RL.
- [Baichuan-M2: Scaling Medical Capability with Large Verifier System](https://arxiv.org/abs/2509.02208) *(2025)* — Pairs a patient simulator with a clinical criteria generator producing multi-dimensional metrics for medical RL.
- [Health-SCORE: Towards Scalable Rubrics for Improving Health-LLMs](https://arxiv.org/abs/2601.18706) *(2026)* — A scalable criteria framework for health models, usable as an RL reward and as an in-context prompt.
- [LLM-Driven Rubric-Based Assessment of Algebraic Competence in Multi-Stage Block Coding Tasks with Design and Field Evaluation](https://arxiv.org/abs/2510.06253) *(2025)* — Aligns five predefined criteria dimensions per problem segment, field-tested in classrooms.
- [QED-Nano: Teaching a Tiny Model to Prove Hard Theorems](https://arxiv.org/abs/2604.04898) *(2026)* — Trains a small theorem prover with criteria-based rewards plus an iterative summarize-and-refine cache.
- [ClinAlign: Scaling Healthcare Alignment from Clinician Preference](https://arxiv.org/abs/2602.09653) *(2026)* — Distills physician-refined criteria into reusable clinical principles for offline alignment and self-revision.
- [Quark Medical Alignment: A Holistic Multi-Dimensional Alignment and Collaborative Optimization Paradigm](https://arxiv.org/abs/2602.11661) *(2026)* — Splits medical alignment into four categories, each driven by observable metrics yielding fine-grained supervision.
- [Benchmarking and Learning Real-World Customer Service Dialogue](https://arxiv.org/abs/2510.22143) *(2025)* — Distills expert dialogue patterns, then trains with criteria-aware staged exploration for service agents.
- [Improving Heart-Focused Medical Question Answering in LLMs via Variance-Aware Rubric Rewards with GRPO](https://arxiv.org/abs/2606.05174) *(2026)* — Variance-aware criteria weighting targeting cardiology question answering.
- [OralGPT-Plus: Learning to Use Visual Tools via Reinforcement Learning for Panoramic X-ray Analysis](https://arxiv.org/abs/2603.06366) *(2026)* — Criteria-scored rewards train agentic reasoning over dental radiographs.
- [WaferSAGE: Large Language Model-Powered Wafer Defect Analysis via Synthetic Data Generation and Rubric-Guided Reinforcement Learning](https://arxiv.org/abs/2604.27629) *(2026)* — Converts generated defect descriptions into structured criteria that drive group-relative RL for wafer inspection.
- [CodeUltraFeedback: An LLM-as-a-Judge Dataset for Aligning Large Language Models to Coding Preferences](https://arxiv.org/abs/2403.09032) *(2024)* — Grades coding responses along five named preference dimensions, producing scores and feedback for alignment.
- [Kardia-R1: Unleashing LLMs to Reason toward Understanding and Empathy for Emotional Support via Rubric-as-Judge Reinforcement Learning](https://arxiv.org/abs/2512.01282) *(2025)* — Criteria-as-judge RL trains empathetic reasoning for emotional-support dialogue.
- [MUSE: Multi-Domain Chinese User Simulation via Self-Evolving Profiles and Rubric-Guided Alignment](https://arxiv.org/abs/2604.13828) *(2026)* — Criteria-based reward drives multi-turn RL optimizing a user simulator.
- [Rewarding Creativity: A Human-Aligned Generative Reward Model for Reinforcement Learning in Storytelling](https://arxiv.org/abs/2601.07149) *(2026)* — Generative reward model trained to match human judgments of storytelling quality.
- [From Correctness to Preference: A Framework for Personalized Agentic Reinforcement Learning](https://arxiv.org/abs/2605.23382) *(2026)* — Decouples a generic task-quality reward from a personalized-preference reward for user-conditioned agentic RL.
- [Training AI Co-Scientists Using Rubric Rewards](https://arxiv.org/abs/2512.23707) *(2025)* — Extracts goal-specific criteria from papers so a policy can self-grade research plans.
- [Beyond Score Prediction: LLM-Based Essay Scoring and Feedback Generation via Reinforcement Learning with Rubric Rewards](https://arxiv.org/abs/2607.19219) *(2026)* — Binary criteria grade the quality of generated essay feedback, not just the score.

## Frontier-Lab Post-Training Recipes

Of the open frontier recipes checked against their primary sources, only Kimi K2 explicitly documents a rubric mechanism — a grep of the full TeX finds zero occurrences of "rubric" or "checklist" in the DeepSeek-V3 and Tulu 3 reports, so neither is listed here. Several other labs are widely assumed to use criteria-based rewards but do not describe them in terms this list can verify.

- [Kimi K2: Open Agentic Intelligence](https://arxiv.org/abs/2507.20534) *(2025)* — Pairs verifiable-reward RL with a self-critique rubric using core, prescriptive, and human criteria.

## Surveys

- [The Rules of the Game: A Survey of Rubrics for Large Language Models](https://openreview.net/forum?id=FnSimngGYk) *(2026)* — The dedicated rubric survey, organizing the field into construction, training, and evaluation.
- [From Holistic Evaluation to Structured Criteria: Rubrics Across the Evolving LLM Landscape](https://arxiv.org/abs/2606.08625) *(2026)* — Traces the shift from single-score judging toward criteria-decomposed evaluation.
- [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) *(2024)* — Surveys reliability strategies spanning consistency, bias mitigation, and scenario adaptation.
- [LLMs-as-Judges: A Comprehensive Survey on LLM-based Evaluation Methods](https://arxiv.org/abs/2412.05579) *(2024)* — Organizes judging around functionality, methodology, applications, and meta-evaluation.
- [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://arxiv.org/abs/2411.16594) *(2024)* — Frames the field around what to judge, how to judge, and how to validate judgments.
- [Meta-Judging with Large Language Models: Concepts, Methods, and Challenges](https://arxiv.org/abs/2601.17312) *(2026)* — Surveys meta-judge methods, organizing conceptual foundations, mechanisms, training, and failure modes.
- [A Comprehensive Survey of Reward Models: Taxonomy, Applications, Challenges, and Future](https://arxiv.org/abs/2504.12328) *(2025)* — Taxonomizes reward models by preference collection, architecture, and downstream usage.
- [Sailing by the Stars: A Survey on Reward Models and Learning Strategies for Learning from Rewards](https://arxiv.org/abs/2505.02686) *(2025)* — Organizes the field around learning-from-rewards strategies across training and inference.
- [A Survey on Progress in LLM Alignment from the Perspective of Reward Design](https://arxiv.org/abs/2505.02666) *(2025)* — Frames alignment progress around reward-signal design rather than policy optimization.
- [Enhancing Large Language Model Reasoning with Reward Models: An Analytical Survey](https://arxiv.org/abs/2510.01925) *(2025)* — Surveys reward-model roles across training-time RL and inference-time search.
- [A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models](https://arxiv.org/abs/2510.08049) *(2025)* — Surveys process-reward data construction, architectures, and use in search and RL.
- [Reward Models in Deep Reinforcement Learning: A Survey](https://arxiv.org/abs/2506.15421) *(2025)* — Systematic review of reward model foundations and methodologies across RL settings.
- [Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation](https://arxiv.org/abs/2602.09305) *(2026)* — Surveys design choices and open challenges for reasoning-focused reward models.
- [GUI Agents with Reinforcement Learning: Toward Digital Inhabitants](https://arxiv.org/abs/2604.27955) *(2026)* — Surveys interface-agent RL via an offline, online, and hybrid taxonomy of training strategies.

## Tooling, Frameworks, and Leaderboards

### RL and post-training libraries with rubric-reward support

- [verifiers](https://github.com/PrimeIntellect-ai/verifiers) — RL environment and eval library whose `Rubric` abstraction combines multiple reward functions into one score.
- [prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) — Agentic RL training at scale built on the same environment, rubric, and grading-harness abstraction.
- [ART](https://github.com/OpenPipe/ART) — Agent Reinforcement Trainer whose RULER component ranks trajectories against a shared rubric with no hand-written reward.
- [slime](https://github.com/THUDM/slime) — Post-training and RL-scaling framework where custom reward computation and verifier feedback plug into the rollout loop.
- [NeMo-RL](https://github.com/NVIDIA-NeMo/RL) — Scalable RL post-training toolkit supporting custom reward functions and reward shaping.
- [AReaL](https://github.com/inclusionAI/AReaL) — Fully asynchronous RL system for LLM agents with pluggable reward backends.
- [OpenEnv](https://github.com/huggingface/OpenEnv) — Gymnasium-style interface for RL post-training environments.

### Rubric-specific libraries and released weights

- [OpenRubrics](https://github.com/wanghaoyu0408/OpenRubrics) — Code for the OpenRubrics family: large-scale prompt-rubric pairs plus rubric-conditioned reward-model training.
- [r3 / mr3](https://github.com/rubricreward) — Robust rubric-agnostic reward models and their multilingual reasoning successor, code and weights.
- [prometheus-eval](https://github.com/prometheus-eval/prometheus-eval) — Toolkit and released judge weights taking an explicit score rubric as input for absolute or relative grading.
- [OpenRubricRL](https://github.com/anikal2001/OpenRubricRL) — Early-stage pipeline converting human-written rubrics into LLM-based reward functions.
- [Skywork-Critic](https://huggingface.co/Skywork) — Released judge model weights with no accompanying paper; listed for practitioners rather than citation.

### Judge and eval harnesses with criteria graders

- [Define success criteria and build evaluations](https://platform.claude.com/docs/en/build-with-claude/develop-tests) — Anthropic's practitioner guide to multidimensional success criteria and code-, human-, or model-graded evals.
- [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) — Evaluation framework with built-in model-graded scorers and a custom scorer API.
- [DeepEval](https://github.com/confident-ai/deepeval) — Pytest-style eval framework whose G-Eval and DAG metrics implement custom-criteria judging.
- [promptfoo](https://github.com/promptfoo/promptfoo) — Prompt and agent testing CLI whose `llm-rubric` assertion grades output against a free-text rubric.
- [autoevals](https://github.com/braintrustdata/autoevals) — Judge and heuristic scorer library supporting custom rubric-style grading prompts.
- [RAGAS](https://github.com/explodinggradients/ragas) — Retrieval-augmented evaluation toolkit offering criteria-based discrete metrics.
- [Opik](https://github.com/comet-ml/opik) — Observability and eval platform with judge metrics plus custom-metric authoring.
- [Phoenix](https://github.com/Arize-ai/phoenix) — Observability platform whose evals package supports custom criteria evaluators.
- [Weave](https://github.com/wandb/weave) — Development and evaluation toolkit supporting custom scorers.
- [OpenAI Evals](https://github.com/openai/evals) — Open eval framework and registry supporting model-graded eval templates.

### Hosted graders

- [OpenAI Graders API](https://developers.openai.com/api/docs/guides/graders) — A `score_model` grader accepting an explicit judge prompt with criteria, used in evals and fine-tuning.
- [Vertex AI Gen AI Evaluation Service](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/determine-eval) — Managed rubric-based metrics plus custom metric authoring.

### Leaderboards

- [RewardBench](https://github.com/allenai/reward-bench) — Reward-model evaluation benchmark and public leaderboard.
- [Judge Arena](https://huggingface.co/spaces/AtlaAI/judge-arena) — Live leaderboard comparing LLM judges head-to-head.

## Blogs, Explainers, and Living Documents

Widely cited entry points that have no arXiv version.

- [Specification gaming examples in AI](https://docs.google.com/spreadsheets/d/e/2PACX-1vRPiprOaC3HsCf5Tuum8bRfzYUiKLRqJmbOoC-32JorNdfyTiRRsR7Ea5eWtvsWzuxo8bjOxCG84dAg/pubhtml) — Krakovna et al.'s living catalog of real specification-gaming incidents.
- [Reward Hacking in Reinforcement Learning](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/) — Lilian Weng's survey-style explainer, the most common entry point into the topic.

## Project Pages, Repos, and Useful Links

### Adjacent collections

- [Rubrics_Survey](https://github.com/RUC-NLPIR/Rubrics_Survey) — Companion to the dedicated rubric survey; construction, training, and evaluation taxonomy, text-only.
- [Awesome-Rubrics](https://github.com/FreedomIntelligence/Awesome-Rubrics) — Survey-companion rubric list covering data, training, inference-time supervision, and reward-hacking risks.
- [Rubric-RMs-Survey](https://github.com/EADMO/Rubric-RMs-Survey) — Narrower companion focused on analytic rubrics for holistic reward modeling.
- [Awesome-LLMs-as-Judges](https://github.com/CSHaitao/Awesome-LLMs-as-Judges) — Judge-focused survey companion.
- [Awesome-LLM-as-a-judge](https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge) — Second judge-focused survey companion.
- [Awesome-LLM-Judges](https://github.com/haizelabs/Awesome-LLM-Judges) — Judge list including some tooling links.
- [awesome-RLHF](https://github.com/opendilab/awesome-RLHF) — The standard RLHF resource list.
- [awesome-RLVR](https://github.com/opendilab/awesome-RLVR) — Verifiable-reward-focused list.
- [Awesome-LLM-RLVR](https://github.com/smiles724/Awesome-LLM-RLVR) — Second, actively updated verifiable-reward list.
- [Awesome-Process-Reward-Models](https://github.com/RyanLiu112/Awesome-Process-Reward-Models) — Process-reward-model focused.
- [awesome-reward-models](https://github.com/JLZhong23/awesome-reward-models) — General reward-model list.
- [Awesome-LLM-Eval](https://github.com/onejune2018/Awesome-LLM-Eval) — Broad evaluation list with strong tooling coverage.
- [awesome-evals](https://github.com/benchflow-ai/awesome-evals) — Agent-evaluation focused.
- [Awesome RM for Video Generation](https://github.com/chrisliu298/awesome-rm-for-video-generation) — sibling list: the reward *signal* for video generation.
- [Awesome RL for Video Generation](https://github.com/chrisliu298/awesome-rl-for-video-generation) — sibling list: the optimization *method* for video generation.

## Contributing

Contributions welcome! Please open a PR if you know of papers, datasets, benchmarks, or tools related to rubric rewards. See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed criteria, section placement, and formatting guidelines.

- **Inclusion criteria:** The work should define, train, apply, evaluate, or critique an explicit criteria-based reward, judge, or verifier for a modern generative model, or directly enable one.
- **Entry format:** `[Title](url) *(Year)* — One-line description.` See [CONTRIBUTING.md](CONTRIBUTING.md) for full examples.

## Citation

```bibtex
@software{awesome-rubric-rewards,
  title = {{Awesome Rubric Rewards}},
  author = {Liu, Chris Yuhao and others},
  year = {2026},
  doi = {10.5281/zenodo.21831038},
  url = {https://github.com/chrisliu298/awesome-rubric-rewards},
  version = {v1.0.0}
}
```

---

*Repository last updated: 2026-08-07. Literature systematically searched through August 2026. Coverage: rubrics as RL reward signals, rubric construction and refinement, checklists and constitutions, rubric-conditioned reward models, criteria compilers and programmatic rubric graders, criteria-based process rewards, rubric-conditioned judges, reward hacking and robustness, multimodal and agentic criteria-based rewards, rubric-graded benchmarks, datasets, and tooling. Scope is the criteria artifact: general reward models, judges, process reward models, and verifiers without one live in the [adjacent collections](#adjacent-collections).*
