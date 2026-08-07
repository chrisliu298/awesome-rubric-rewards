# 📋 Awesome Rubric Rewards

<p align="center">
  <a href="https://awesome.re"><img src="https://img.shields.io/badge/Awesome-%F0%9F%93%8B_Rubric_Rewards-000000?style=for-the-badge&labelColor=000000" alt="Awesome Rubric Rewards"></a>
</p>

<p align="center">
  <!-- entry-count-start --><a href="#contents"><img src="https://img.shields.io/badge/Entries-667-000000?style=for-the-badge&labelColor=000000" alt="Entries"></a><!-- entry-count-end -->
  <a href="https://github.com/chrisliu298/awesome-rubric-rewards/stargazers"><img src="https://img.shields.io/github/stars/chrisliu298/awesome-rubric-rewards?style=for-the-badge&logo=github&logoColor=white&label=Stars&labelColor=000000&color=000000" alt="GitHub Stars"></a>
  <a href="https://github.com/chrisliu298/awesome-rubric-rewards/network/members"><img src="https://img.shields.io/github/forks/chrisliu298/awesome-rubric-rewards?style=for-the-badge&logo=github&logoColor=white&label=Forks&labelColor=000000&color=000000" alt="GitHub Forks"></a>
  <a href="https://github.com/chrisliu298/awesome-rubric-rewards/commits"><img src="https://img.shields.io/github/last-commit/chrisliu298/awesome-rubric-rewards?style=for-the-badge&logo=github&logoColor=white&label=Last%20Commit&labelColor=000000&color=000000" alt="Last Commit"></a>
</p>

A curated collection of papers, datasets, benchmarks, and code for **rubric rewards**: rubrics, checklists, criteria sets, principles, constitutions, and scoring guides used to score, rank, verify, filter, or train modern generative models.

> **Rubric reward** = an explicit, decomposed, human-readable set of criteria applied to a model output to produce a reward, a preference label, or a quality score. Three properties separate it from an ordinary reward model: the criteria are *written down* rather than latent in weights, *decomposed* into many items rather than collapsed to one scalar, and *inspectable* so a person can read, audit, and edit them.

The organizing idea: **rubrics are how reinforcement learning escapes verifiable domains.** RLVR works wherever a checker already exists — a unit test, a math answer key. Rubrics manufacture a checker where none did, which is what makes RL tractable for writing, medicine, law, research, dialogue, and open-ended agentic work. Every entry here is either building that checker, using it as a reward, measuring whether it works, or documenting how it breaks.

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
- [Rubric-Conditioned and Fine-Grained Reward Models](#rubric-conditioned-and-fine-grained-reward-models)
  - [Rubric- and criteria-conditioned reward models](#rubric--and-criteria-conditioned-reward-models)
  - [Multi-attribute and multi-objective reward models](#multi-attribute-and-multi-objective-reward-models)
  - [Fine-grained, dense, and span-level rewards](#fine-grained-dense-and-span-level-rewards)
  - [Self-rewarding and self-generated criteria](#self-rewarding-and-self-generated-criteria)
- [Verifiers and Programmatic Graders](#verifiers-and-programmatic-graders)
- [Process Reward Models and Step-Level Criteria](#process-reward-models-and-step-level-criteria)
- [LLM-as-a-Judge](#llm-as-a-judge)
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
| Building a rubric-conditioned reward model | [R3](https://arxiv.org/abs/2505.13388), [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507) | [RM-R1](https://arxiv.org/abs/2505.02387), [C2](https://arxiv.org/abs/2604.13618), [mR3](https://arxiv.org/abs/2510.01146) |
| Worried about reward hacking | [Reward Hacking in Rubric-Based RL](https://arxiv.org/abs/2605.12474), [Rubrics as an Attack Surface](https://arxiv.org/abs/2602.13576) | [RIFT](https://arxiv.org/abs/2604.01375), [Reinforcement Learning with Robust Rubric Rewards](https://arxiv.org/abs/2605.30244) |
| Working on image or video generation | [VisionReward](https://arxiv.org/abs/2412.21059), [RubricRL](https://arxiv.org/abs/2511.20651) | [AutoRubric-T2I](https://arxiv.org/abs/2605.17602), [DeltaRubric](https://arxiv.org/abs/2605.09269), [Omni-RRM](https://arxiv.org/abs/2602.00846) |
| Working on agents or computer use | [Agentic Rubrics as Contextual Verifiers](https://arxiv.org/abs/2601.04171), [CM2](https://arxiv.org/abs/2602.12268) | [ARCO](https://arxiv.org/abs/2606.21262), [GUI-Shepherd](https://arxiv.org/abs/2509.23738), [The Art of Building Verifiers](https://arxiv.org/abs/2604.06240) |
| Evaluating with rubrics | [HealthBench](https://arxiv.org/abs/2505.08775), [PaperBench](https://arxiv.org/abs/2504.01848) | [ProfBench](https://arxiv.org/abs/2510.18941), [RubricEval](https://arxiv.org/abs/2603.25133), [PReMISE](https://arxiv.org/abs/2605.30803) |

## Start Here

The fastest reading path through the area:

1. **The founding trio.** [Rubrics as Rewards](https://arxiv.org/abs/2507.17746), [Reinforcement Learning with Rubric Anchors](https://arxiv.org/abs/2508.12790), and [Checklists Are Better Than Reward Models](https://arxiv.org/abs/2507.18624) landed within weeks of each other in mid-2025 and are the near-universal citation anchors. Almost every later paper cites at least one.
2. **Why rubrics instead of a reward model.** [Chasing the Tail](https://arxiv.org/abs/2509.21500) shows where scalar reward models fail on fine gradations; [The Invisible Leash](https://arxiv.org/abs/2507.14843) argues verifiable-reward RL stays anchored near the base prior.
3. **Where the criteria come from.** [OpenRubrics](https://arxiv.org/abs/2510.07743) mines them contrastively from preference pairs; [Auto-Rubric](https://arxiv.org/abs/2510.17314) distills them from implicit reward-model weights.
4. **Making the reward hold up.** [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507) and [R3](https://arxiv.org/abs/2505.13388) are the two most influential rubric-conditioned reward models.
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
| Human- or expert-authored | [Rubric Anchors](https://arxiv.org/abs/2508.12790), [HealthBench](https://arxiv.org/abs/2505.08775), [PRBench](https://arxiv.org/abs/2511.11562), [ComplexConstraints](https://arxiv.org/abs/2606.09118) |
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
| Trained rubric-conditioned reward model | [R3](https://arxiv.org/abs/2505.13388), [mR3](https://arxiv.org/abs/2510.01146), [Robust Reward Modeling via Causal Rubrics](https://arxiv.org/abs/2506.16507) |
| Process reward model, step-level | [Step-wise Rubric Rewards](https://arxiv.org/abs/2605.17291), [GUI-Shepherd](https://arxiv.org/abs/2509.23738), [VisualPRM](https://arxiv.org/abs/2503.10291) |
| Programmatic verifier or rule engine | [Rule Based Rewards](https://arxiv.org/abs/2411.01111), [IFEval](https://arxiv.org/abs/2311.07911), [TRON](https://arxiv.org/abs/2606.01599) |
| Execution or state check | [OpenComputer](https://arxiv.org/abs/2605.19769), [MCP-Universe](https://arxiv.org/abs/2508.14704), [Interactive Reward Agent](https://arxiv.org/abs/2607.25904) |
| Hybrid routing across the above | [RLR3](https://arxiv.org/abs/2605.30244), [SCRIBE](https://arxiv.org/abs/2601.03555), [StitchCUDA](https://arxiv.org/abs/2603.02637) |

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
| 3D | [DreamReward](https://arxiv.org/abs/2403.14613), [CREward](https://arxiv.org/abs/2511.19995) |
| GUI and computer use | [GUI-Shepherd](https://arxiv.org/abs/2509.23738), [OSReward](https://arxiv.org/abs/2607.28609), [CUARewardBench](https://arxiv.org/abs/2510.18596) |
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
- [ImplicitRM: Unbiased Reward Modeling from Implicit Preference Data](https://arxiv.org/abs/2603.23184) *(2026)* — Learns rewards from click-like implicit signals via stratification correcting action bias.
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
- [Improving Data and Reward Design for Scientific Reasoning in Large Language Models](https://arxiv.org/abs/2602.08321) *(2026)* — Builds fine-grained criteria for open-ended science answers and trains against them for stability.
- [RLBFF: Binary Flexible Feedback to bridge between Human Feedback & Verifiable Rewards](https://arxiv.org/abs/2509.21319) *(2025)* — Converts free-text human feedback into binary principles usable as verifiable-style rewards.
- [RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards](https://arxiv.org/abs/2605.10899) *(2026)* — Uses criteria as a shared interface across agent, judge, and memory in a meta-RL loop.
- [Reward and Guidance through Rubrics: Promoting Exploration to Improve Multi-Domain Reasoning](https://arxiv.org/abs/2511.12344) *(2025)* — Criteria-driven dense rewards widen exploration across several reasoning domains at once.

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
- [Chaining the Evidence: Robust Reinforcement Learning for Deep Search Agents with Citation-Aware Rubric Rewards](https://arxiv.org/abs/2601.06021) *(2026)* — Decomposes search questions into single-hop criteria scored on citations and evidence chains.
- [Enhancing Rubric-based RL via Self-Distillation](https://arxiv.org/abs/2607.18082) *(2026)* — On-policy self-distillation fixes unexplored and suppressed criteria.

## Rubric Construction

Where criteria come from is its own research problem. The four-way split below follows [the survey](https://openreview.net/forum?id=FnSimngGYk).

### Direct generation

- [RubricHub: A Comprehensive and Highly Discriminative Rubric Dataset via Automated Coarse-to-Fine Generation](https://arxiv.org/abs/2601.08430) *(2026)* — Coarse-to-fine generation combining principle-guided synthesis and multi-model aggregation.
- [ARES: Automated Rubric Synthesis for Scalable LLM Reinforcement Learning](https://arxiv.org/abs/2605.23454) *(2026)* — Co-generates questions, references, and weighted criteria from raw documents in one pass.
- [Qworld: Question-Specific Evaluation Criteria for LLMs](https://arxiv.org/abs/2603.23522) *(2026)* — Builds per-question criteria via a recursive expansion tree of scenarios and binary checks.
- [SedarEval: Automated Evaluation using Self-Adaptive Rubrics](https://arxiv.org/abs/2501.15595) *(2025)* — Generates per-question rubrics carrying explicit scoring and deduction points, then trains a matching evaluator.
- [Rubric Is All You Need: Enhancing LLM-based Code Evaluation With Question-Specific Rubrics](https://arxiv.org/abs/2503.23989) *(2025)* — Grades code with per-problem criteria rather than one question-agnostic rubric.
- [RubricRAG: Towards Interpretable and Reliable LLM Evaluation via Domain Knowledge Retrieval for Rubric Generation](https://arxiv.org/abs/2603.20882) *(2026)* — Retrieves criteria from related queries at inference time to ground evaluation.
- [Many Voices, One Reward: Multi-Role Rubric Generation for LLM Judging and Reward Modeling](https://arxiv.org/abs/2607.01830) *(2026)* — Elicits criteria from complementary evaluator roles into one auditable scorer.
- [Automated Rubrics for Reliable Evaluation of Medical Dialogue Systems](https://arxiv.org/abs/2601.15161) *(2026)* — Retrieval-augmented multi-agent pipeline decomposes medical evidence into atomic-fact criteria per instance.
- [Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling](https://arxiv.org/abs/2602.06795) *(2026)* — Builds granular reasoning-error taxonomies to train domain-adaptive classifiers.
- [Rubric-as-Experts: Case-Specific MQM Rubrics for Translation Quality Evaluation](https://arxiv.org/abs/2606.21559) *(2026)* — Instantiates case-specific criteria from a generic translation-quality framework.
- [Two-Level Meta-Rubrics for Evaluating Open-Ended Generation](https://arxiv.org/abs/2607.19322) *(2026)* — An expressive meta-rubric compiles into a flat binary machine-gradable checklist.
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

### Online and co-evolving generation

- [Online Rubrics Elicitation from Pairwise Comparisons](https://arxiv.org/abs/2510.07284) *(2025)* — Curates criteria live during training from current-versus-reference policy comparisons.
- [QUBRIC: Co-Designing Queries and Rubrics for RL Beyond Verifiable Rewards](https://arxiv.org/abs/2606.03968) *(2026)* — Constructs queries and criteria jointly to reduce hallucinated or ungrounded criteria.
- [Alternating Reinforcement Learning for Rubric-Based Reward Modeling in Non-Verifiable LLM Post-Training](https://arxiv.org/abs/2602.01511) *(2026)* — Treats criteria generation as a latent RL action alternated against judge training.
- [RUBRIC-ARROW: Alternating Pointwise Rubric Reward Modeling for LLM Post-training in Non-verifiable Domains](https://arxiv.org/abs/2605.29156) *(2026)* — Alternating training jointly optimizes a generator and a criteria-conditioned pointwise judge.
- [RLAC: Reinforcement Learning with Adversarial Critic for Free-Form Generation Tasks](https://arxiv.org/abs/2511.01758) *(2025)* — An adversarial critic hunts likely failure modes instead of checking exhaustive checklists.
- [ARCO: Adaptive Rubrics with Co-Evolution for Multi-Step LLM-Based Agents](https://arxiv.org/abs/2606.21262) *(2026)* — Co-evolves criteria alongside the agent policy across multi-step trajectories.
- [MIRA: Mid-training Rubric Anchoring for Source-Aware Data Selection](https://arxiv.org/abs/2605.30288) *(2026)* — Discovers per-source criteria from a teacher's judgments, then distills them into scorers.
- [CARMO: Dynamic Criteria Generation for Context-Aware Reward Modelling](https://arxiv.org/abs/2410.21545) *(2024)* — Generates query-specific criteria to ground reward scores instead of reusing a static rubric.

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

- [Rule Based Rewards for Language Model Safety](https://arxiv.org/abs/2411.01111) *(2024)* — Composable judge-scored propositions replace human safety labels as the RL reward.
- [Deliberative Alignment: Reasoning Enables Safer Language Models](https://arxiv.org/abs/2412.16339) *(2024)* — Trains models to reason explicitly over safety-specification text before answering.
- [The Instruction Hierarchy: Training LLMs to Prioritize Privileged Instructions](https://arxiv.org/abs/2404.13208) *(2024)* — Trains on generated demonstrations so models prioritize higher-privilege instructions when sources conflict.
- [IHEval: Evaluating Language Models on Following the Instruction Hierarchy](https://arxiv.org/abs/2502.08745) *(2025)* — Benchmarks whether models correctly prioritize conflicting instructions by privilege.
- [Reasoning Up the Instruction Ladder for Controllable Language Models](https://arxiv.org/abs/2511.04694) *(2025)* — Trains explicit reasoning over instruction-privilege conflicts before responding.
- [AutoRule: Reasoning Chain-of-thought Extracted Rule-based Rewards Improve Preference Learning](https://arxiv.org/abs/2506.15651) *(2025)* — Extracts explicit rules from reasoning traces to build rule-based preference rewards.

### Instruction and constraint verification

- [Instruction-Following Evaluation for Large Language Models](https://arxiv.org/abs/2311.07911) *(2023)* — Scores outputs against programmatically verifiable constraints like counts and keywords.
- [FollowBench: A Multi-level Fine-grained Constraints Following Benchmark for Large Language Models](https://arxiv.org/abs/2310.20410) *(2023)* — Stacks constraint types incrementally to measure fine-grained degradation.
- [InFoBench: Evaluating Instruction Following Ability in Large Language Models](https://arxiv.org/abs/2401.03601) *(2024)* — Decomposes each instruction into yes/no sub-questions for a decomposed following ratio.
- [Generalizing Verifiable Instruction Following](https://arxiv.org/abs/2507.02833) *(2025)* — Adds many held-out verifiable constraint types to test generalization.
- [VerIF: Verification Engineering for Reinforcement Learning in Instruction Following](https://arxiv.org/abs/2506.09942) *(2025)* — Combines rule-based constraint checking with judge-based checks as one RL reward.
- [RECAST: Expanding the Boundaries of LLMs' Complex Instruction Following with Multi-Constraint Data](https://arxiv.org/abs/2505.19030) *(2025)* — Builds multi-constraint data with per-constraint verifiable reward functions.
- [MDP-GRPO: Stabilized Group Relative Policy Optimization for Multi-Constraint Instruction Following](https://arxiv.org/abs/2606.06058) *(2026)* — Stabilizes group-relative RL under sparse discrete multi-constraint rewards.
- [Precision over Diversity: High-Precision Reward Generalizes to Robust Instruction Following](https://arxiv.org/abs/2601.04954) *(2026)* — Finds verification precision, not constraint diversity, bounds generalization gains.
- [M-IFEval: Multilingual Instruction-Following Evaluation](https://arxiv.org/abs/2502.04688) *(2025)* — Extends objective judgment-free verifiable constraints to French, Japanese, and Spanish.
- [The SIFo Benchmark: Investigating the Sequential Instruction Following Ability of Large Language Models](https://arxiv.org/abs/2406.19999) *(2024)* — Verifies an entire instruction chain by checking only the final-step output.
- [AdvancedIF: Rubric-Based Benchmarking and Reinforcement Learning for Advancing LLM Instruction Following](https://arxiv.org/abs/2511.10507) *(2025)* — Chains criteria generation, verifier fine-tuning, and reward shaping into one pipeline.

### Question decomposition and atomic-claim verification

- [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251) *(2023)* — Decomposes long-form text into atomic facts scored against a retrieval source.
- [QA-LIGN: Aligning LLMs through Constitutionally Decomposed QA](https://arxiv.org/abs/2506.08123) *(2025)* — Decomposes a scalar reward into per-principle question checks in a draft-critique-revise loop.
- [DecomposeRL: Learning to Ask Useful, Informative, and Diverse Questions for Semi-Supervised, Traceable Claim Verification](https://arxiv.org/abs/2605.27858) *(2026)* — Learns a question-decomposition policy rewarded by downstream verdict correctness.
- [Verifiable Rewards Beyond Math and Code: Lightweight Corpus-Grounded Process Supervision for Factual Question Answering](https://arxiv.org/abs/2605.29648) *(2026)* — Grounds factual reward in corpus-verified subclaims for lightweight process supervision.
- [Self-Alignment for Factuality: Mitigating Hallucinations in LLMs via Self-Evaluation](https://arxiv.org/abs/2402.09267) *(2024)* — Uses self-evaluated confidence on generated claims as a factuality training signal.

## Rubric-Conditioned and Fine-Grained Reward Models

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

### Multi-attribute and multi-objective reward models

- [Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts](https://arxiv.org/abs/2406.12845) *(2024)* — Trains many absolute-rating objectives then gates them per context with a router.
- [HelpSteer2: Open-source dataset for training top-performing reward models](https://arxiv.org/abs/2406.08673) *(2024)* — Multi-attribute preference data scoring several named attributes separately.
- [Nemotron-4 340B Technical Report](https://arxiv.org/abs/2406.11704) *(2024)* — Projects hidden states into five named attributes combined by a weighted sum.
- [Arithmetic Control of LLMs for Diverse User Preferences: Directional Preference Alignment with Multi-Objective Rewards](https://arxiv.org/abs/2402.18571) *(2024)* — Represents preferences as reward-space unit vectors for arithmetic trade-off control.
- [Beyond One-Preference-Fits-All Alignment: Multi-Objective Direct Preference Optimization](https://arxiv.org/abs/2310.03708) *(2023)* — Folds multiple weighted objectives directly into an implicit preference-trained reward.
- [Multi-Objective Reinforcement Learning from AI Feedback](https://arxiv.org/abs/2406.07295) *(2024)* — Decomposes AI feedback into multiple objectives rather than one scalar reward.
- [Projection Optimization: A General Framework for Multi-Objective and Multi-Group RLHF](https://arxiv.org/abs/2502.15145) *(2025)* — Recasts non-linear multi-objective aggregation as a series of tractable linear sub-problems.
- [General Preference Reinforcement Learning](https://arxiv.org/abs/2605.18721) *(2026)* — Replaces the scalar reward with a multi-dimensional preference embedding normalized per axis.
- [Interpreting Language Reward Models via Contrastive Explanations](https://arxiv.org/abs/2411.16502) *(2024)* — Generates counterfactual edits to explain which attributes drive a reward score.
- [Rewarded soups: towards Pareto-optimal alignment by interpolating weights fine-tuned on diverse rewards](https://arxiv.org/abs/2306.04488) *(2023)* — Interpolates weights of policies tuned on separate rewards to trace a Pareto front.
- [Personalized Soups: Personalized Large Language Model Alignment via Post-hoc Parameter Merging](https://arxiv.org/abs/2310.11564) *(2023)* — Models personalization as multi-objective alignment, merging separately tuned preference policies post hoc.
- [Controllable Preference Optimization: Toward Controllable Multi-Objective Alignment](https://arxiv.org/abs/2402.19085) *(2024)* — Conditions generation on explicit per-objective preference tokens to make the alignment tax steerable.
- [ENCORE: Entropy-guided Reward Composition for Multi-head Safety Reward Models](https://arxiv.org/abs/2503.20995) *(2025)* — Downweights high-entropy rule heads when composing per-rule safety ratings into one score.

### Fine-grained, dense, and span-level rewards

- [Fine-Grained Human Feedback Gives Better Rewards for Language Model Training](https://arxiv.org/abs/2306.01693) *(2023)* — Sentence-level rewards from separate factuality, relevance, and completeness models.
- [Dense Reward for Free in Reinforcement Learning from Human Feedback](https://arxiv.org/abs/2402.00782) *(2024)* — Extracts per-token reward from an existing model's attention weights at no extra cost.
- [RED: Unleashing Token-Level Rewards from Holistic Feedback via Reward Redistribution](https://arxiv.org/abs/2411.08302) *(2024)* — Redistributes one holistic preference score into token-level credit by attribution.
- [Sentence-level Reward Model can Generalize Better for Aligning LLM from Human Preference](https://arxiv.org/abs/2503.04793) *(2025)* — Aggregates sentence-level scores to improve out-of-distribution generalization.

### Self-rewarding and self-generated criteria

- [Self-Rewarding Language Models](https://arxiv.org/abs/2401.10020) *(2024)* — The model judges its own generations via judge prompting, improving policy and reward together.
- [Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge](https://arxiv.org/abs/2407.19594) *(2024)* — Adds a meta-judge that critiques the model's own judgments, not just its responses.
- [Self-Generated Critiques Boost Reward Modeling for Language Models](https://arxiv.org/abs/2411.16646) *(2024)* — Augments a scalar reward head with self-generated critiques to sharpen prediction.
- [Self-Taught Evaluators](https://arxiv.org/abs/2408.02666) *(2024)* — Bootstraps a judge purely from synthetic contrasting responses with no human labels.
- [Process-based Self-Rewarding Language Models](https://arxiv.org/abs/2503.03746) *(2025)* — Extends self-rewarding with step-wise self-evaluation where holistic judging fails.
- [CREAM: Consistency Regularized Self-Rewarding Language Models](https://arxiv.org/abs/2410.12735) *(2024)* — Regularizes self-rewarding with a consistency term to curb accumulated reward-estimate bias.
- [Toward Evaluative Thinking: Meta Policy Optimization with Evolving Reward Models](https://arxiv.org/abs/2504.20157) *(2025)* — Co-evolves a generative reward model alongside the policy via meta-level optimization.

## Verifiers and Programmatic Graders

Reward-model versus verifier is not a boundary this list observes. What matters is whether the target is expressed as inspectable criteria.

- [Generative Verifiers: Reward Modeling as Next-Token Prediction](https://arxiv.org/abs/2408.15240) *(2024)* — Trains verification as chain-of-thought generation, enabling majority-vote scaling.
- [Reinforcement Learning with Verifiable Rewards Implicitly Incentivizes Correct Reasoning in Base LLMs](https://arxiv.org/abs/2506.14245) *(2025)* — Binary correctness-verified group-relative RL extends reasoning boundaries.
- [Crossing the Reward Bridge: Expanding RL with Verifiable Rewards Across Diverse Domains](https://arxiv.org/abs/2503.23829) *(2025)* — Replaces binary rule checking with a soft generative reward for domains lacking reference answers.
- [Position: The Hidden Costs and Measurement Gaps of Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2509.21882) *(2025)* — Argues headline gains conflate policy improvement with budget and contamination confounds.
- [Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers](https://arxiv.org/abs/2510.00915) *(2025)* — Models verifier false-positive and false-negative rates as noise, deriving unbiased gradient corrections.
- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666) *(2026)* — Shows RL tolerates a noisy verifier without a large drop in final policy quality.
- [From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning](https://arxiv.org/abs/2505.22203) *(2025)* — Documents systematic failure modes of both rule-based and model-based verifiers.
- [Reinforcement Learning with Robust Rubric Rewards](https://arxiv.org/abs/2605.30244) *(2026)* — Routes each criterion to a deterministic verifier or judge, limiting evidence exposure.
- [An Efficient Rubric-based Generative Verifier for Search-Augmented LLMs](https://arxiv.org/abs/2510.14660) *(2025)* — Treats atomic information nuggets as structured criteria, distilling a compact verifier.
- [The Art of Building Verifiers for Computer Use Agents](https://arxiv.org/abs/2604.06240) *(2026)* — A practical playbook for constructing programmatic verifiers grading interface trajectories.
- [Time To Impeach LLM-as-a-Judge: Programs are the Future of Evaluation](https://arxiv.org/abs/2506.10403) *(2025)* — Synthesizes executable auditable judging programs in place of opaque model scores.
- [Agentic Reward Modeling: Integrating Human Preferences with Verifiable Correctness Signals for Reliable Reward Systems](https://arxiv.org/abs/2502.19328) *(2025)* — Routes a preference model alongside verifiable factuality and instruction-following checks through a reward agent.
- [When Many Answers Are Valid, Voting Fails: Symbolic Verification for Best-of-K Causal Reasoning in LLMs](https://arxiv.org/abs/2608.03506) *(2026)* — A training-free symbolic verifier scores causal traces against named causal axioms.
- [CHiL(L)Grader: Calibrated Human-in-the-Loop Short-Answer Grading](https://arxiv.org/abs/2603.11957) *(2026)* — Routes low-confidence gradings to humans while adapting the grader to evolving criteria.
- [EDIT: Evidence-Diagnosed Intervention Training for Rule-Faithful LLM Grading](https://arxiv.org/abs/2606.06350) *(2026)* — Locates grading errors via posterior mark drift, then revises steps against an explicit mark scheme.
- [OpenComputer: Verifiable Software Worlds for Computer-Use Agents](https://arxiv.org/abs/2605.19769) *(2026)* — Builds executable state checkers as first-class verifiers, outperforming a judge model.
- [CUA-Gym: Scaling Verifiable Training Environments and Tasks for Computer-Use Agents](https://arxiv.org/abs/2605.25624) *(2026)* — Adversarially coupled agents co-synthesize task, environment, and reward together.
- [TRON: Targeted Rule-Verifiable Online Environments for Visual Reasoning RL](https://arxiv.org/abs/2606.01599) *(2026)* — Generator-verifier programs produce difficulty-controlled visual tasks with exact rewards.
- [Golden Goose: A Simple Trick to Synthesize Unlimited RLVR Tasks from Unverifiable Internet Text](https://arxiv.org/abs/2601.22975) *(2026)* — Converts unverifiable web text into verifiable tasks via automatic answer construction.
- [Self-Distilled RLVR](https://arxiv.org/abs/2604.03128) *(2026)* — Turns a teacher's answer-aware rescoring into per-token advantage weights, dropping the KL term.
- [Reinforcing General Reasoning without Verifiers](https://arxiv.org/abs/2505.21493) *(2025)* — Skips rule-based checking by maximizing the policy's probability of the reference answer.
- [Co-Evolving LLM Coder and Unit Tester via Reinforcement Learning](https://arxiv.org/abs/2506.03136) *(2025)* — Co-trains a generator and a unit-test writer against each other without ground-truth tests.
- [Large Language Models are Better Reasoners with Self-Verification](https://arxiv.org/abs/2212.09561) *(2022)* — Backward-verifies candidate answers against their own premises to rerank solutions.
- [On the Self-Verification Limitations of Large Language Models on Reasoning and Planning Tasks](https://arxiv.org/abs/2402.08115) *(2024)* — Finds self-critique alone degrades accuracy while sound external verification helps.
- [The Invisible Leash: Why RLVR May or May Not Escape Its Origin](https://arxiv.org/abs/2507.14843) *(2025)* — Shows verifiable-reward RL mainly sharpens solutions the base model already reaches, narrowing exploration.

## Process Reward Models and Step-Level Criteria

- [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) *(2023)* — Step-level process supervision beats outcome supervision, with a large human step-label set.
- [Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations](https://arxiv.org/abs/2312.08935) *(2023)* — Automates step-quality labels via tree-search rollouts instead of manual annotation.
- [Let's reward step by step: Step-Level reward model as the Navigators for Reasoning](https://arxiv.org/abs/2310.10080) *(2023)* — Uses per-step scores to guide a heuristic greedy search rather than only rerank solutions.
- [What Are Step-Level Reward Models Rewarding? Counterintuitive Findings from MCTS-Boosted Mathematical Reasoning](https://arxiv.org/abs/2412.15904) *(2024)* — Finds removing a step's prose barely changes scores, revealing symbolic rather than linguistic tracking.
- [The Lessons of Developing Process Reward Models in Mathematical Reasoning](https://arxiv.org/abs/2501.07301) *(2025)* — Identifies label-noise and evaluation pitfalls, releasing a consensus-filtering recipe.
- [Process Reward Models That Think](https://arxiv.org/abs/2504.16828) *(2025)* — A generative process model reasons before emitting each step-level judgment.
- [GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning](https://arxiv.org/abs/2504.00891) *(2025)* — Scales verifier test-time compute by generating reasoning chains before each score.
- [Efficient Process Reward Model Training via Active Learning](https://arxiv.org/abs/2504.10559) *(2025)* — Cuts step-level annotation cost by actively selecting which steps to label.
- [The Bidirectional Process Reward Model](https://arxiv.org/abs/2508.01682) *(2025)* — Scores each step using both forward history and backward look-ahead context.
- [CoLD: Counterfactually-Guided Length Debiasing for Process Reward Models in Mathematical Reasoning](https://arxiv.org/abs/2507.15698) *(2025)* — Uses counterfactual step edits to remove a spurious preference for longer steps.
- [Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning](https://arxiv.org/abs/2601.17223) *(2026)* — Checks intermediate steps with deterministic verifiers for risk-of-bias assessment in evidence synthesis.
- [Dynamic and Generalizable Process Reward Modeling](https://arxiv.org/abs/2507.17849) *(2025)* — Stores multi-dimensional reward criteria in an explicit tree, selecting per step by Pareto dominance.
- [PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models](https://arxiv.org/abs/2501.03124) *(2025)* — Grades process reward models on explicit simplicity, soundness, and sensitivity error dimensions.
- [RLAnything: Forge Environment, Policy, and Reward Model in Completely Dynamic RL System](https://arxiv.org/abs/2602.02488) *(2026)* — Co-trains a step-wise generative reward model with the policy via consistency feedback.
- [ExpRL: Exploratory RL for LLM Mid-Training](https://arxiv.org/abs/2606.17024) *(2026)* — A reference-conditioned judge scores rollouts against a problem-specific rubric for dense mid-training reward.
- [ToolPRMBench: Evaluating and Advancing Process Reward Models for Tool-using Agents](https://arxiv.org/abs/2601.12294) *(2026)* — Step-level benchmark isolating single-step from multi-step tool-agent failures via multi-model-verified action pairs.
- [Entropy-Regularized Process Reward Model](https://arxiv.org/abs/2412.11006) *(2024)* — Adds entropy regularization to step-level reward modeling for multi-step mathematical reasoning.
- [Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning](https://arxiv.org/abs/2504.15275) *(2025)* — Traces process-reward hacking to summation-form credit assignment, replacing it with a min-form rule.

## LLM-as-a-Judge

The substrate rubric rewards are built on. Kept deliberately compact relative to its literature; for depth see the dedicated lists under [Adjacent collections](#adjacent-collections).

### Judge models and generative reward models

- [Prometheus: Inducing Fine-grained Evaluation Capability in Language Models](https://arxiv.org/abs/2310.08491) *(2023)* — Open evaluator trained against custom score rubrics as a frontier-judge substitute.
- [Prometheus 2: An Open Source Language Model Specialized in Evaluating Other Language Models](https://arxiv.org/abs/2405.01535) *(2024)* — Unifies direct assessment and pairwise ranking in one open judge model.
- [M-Prometheus: A Suite of Open Multilingual LLM Judges](https://arxiv.org/abs/2504.04953) *(2025)* — Extends the rubric-conditioned evaluator family to multilingual judging.
- [Prometheus-Vision: Vision-Language Model as a Judge for Fine-Grained Evaluation](https://arxiv.org/abs/2401.06591) *(2024)* — Carries the rubric-conditioned evaluator design into vision-language judgment.
- [JudgeLM: Fine-tuned Large Language Models are Scalable Judges](https://arxiv.org/abs/2310.17631) *(2023)* — Fine-tunes multi-scale judges whose position bias is countered via swap augmentation.
- [Generative Judge for Evaluating Alignment](https://arxiv.org/abs/2310.05470) *(2023)* — Trains on real user queries to emit both verdicts and natural-language critiques.
- [CritiqueLLM: Towards an Informative Critique Generation Model for Evaluation of Large Language Model Generation](https://arxiv.org/abs/2311.18702) *(2023)* — Synthesizes pointwise and reference-free pairwise critique training data.
- [Themis: A Reference-free NLG Evaluation Language Model with Flexibility and Interpretability](https://arxiv.org/abs/2406.18365) *(2024)* — Reference-free evaluator trained via multi-perspective consistency verification.
- [PandaLM: An Automatic Evaluation Benchmark for LLM Instruction Tuning Optimization](https://arxiv.org/abs/2306.05087) *(2023)* — Trains a dedicated judge to rank instruction-tuned outputs for hyperparameter selection.
- [CompassJudger-1: All-in-one Judge Model Helps Model Evaluation and Evolution](https://arxiv.org/abs/2410.16256) *(2024)* — Unifies scoring, pairwise comparison, and critique generation under one backbone.
- [RM-R1: Reward Modeling as Reasoning](https://arxiv.org/abs/2505.02387) *(2025)* — Reframes reward modeling as chain-of-rubrics reasoning refined with verifiable-reward RL.
- [JudgeLRM: Large Reasoning Models as a Judge](https://arxiv.org/abs/2504.00050) *(2025)* — Trains judgment-oriented reasoning models via outcome-driven RL rather than supervision.
- [J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning](https://arxiv.org/abs/2505.10320) *(2025)* — RL-trains a judge to reason before its verdict, rewarded on judgment accuracy.
- [Think-J: Learning to Think for Generative LLM-as-a-Judge](https://arxiv.org/abs/2505.14268) *(2025)* — Teaches a generative judge when and how to reason before rendering a verdict.
- [J4R: Learning to Judge with Equivalent Initial State Group Relative Policy Optimization](https://arxiv.org/abs/2505.13346) *(2025)* — Group-relative RL over equivalent initial states trains a judge robust to answer position.
- [Improve LLM-as-a-Judge Ability as a General Ability](https://arxiv.org/abs/2502.11689) *(2025)* — Two-stage supervised then preference training reaches strong judge accuracy on a fraction of the data.
- [FairJudge: An Adaptive, Debiased, and Consistent LLM-as-a-Judge](https://arxiv.org/abs/2602.06625) *(2026)* — Curriculum training treats judging as a policy explicitly optimized for rubric adherence.
- [Inference-Time Scaling for Generalist Reward Modeling](https://arxiv.org/abs/2504.02495) *(2025)* — Self-principled critique tuning lets reward models generate principles then scale by voting.
- [Reward Reasoning Model](https://arxiv.org/abs/2505.14674) *(2025)* — Generative reward model reasoning explicitly before emitting a scalar judgment.
- [Generative Reward Models](https://arxiv.org/abs/2410.12832) *(2024)* — Blends RLHF and RLAIF by training judges on self-generated reasoning traces.
- [Beyond Scalar Reward Model: Learning Generative Judge from Preference Data](https://arxiv.org/abs/2410.03742) *(2024)* — Trains a rationale-producing judge on self-generated contrastive judgments.
- [S2J: Bridging the Gap Between Solving and Judging Ability in Generative Reward Models](https://arxiv.org/abs/2509.22099) *(2025)* — Trains judges to draw on their own problem-solving ability to close the solve-judge gap.
- [REAL: Regression-Aware Reinforcement Learning for LLM-as-a-Judge](https://arxiv.org/abs/2603.17145) *(2026)* — Adds a regression objective so ordinal scoring errors are penalized proportionally.
- [Foundational Automatic Evaluators](https://arxiv.org/abs/2510.17793) *(2025)* — Scales iterative rejection-sampling fine-tuning to build reasoning-centric evaluators.
- [Foundational Autoraters: Taming Large Language Models for Better Automatic Evaluation](https://arxiv.org/abs/2407.10817) *(2024)* — Trains an autorater family across many human-judgment tasks, then distills it.

### Critic models and explainable metrics

- [Shepherd: A Critic for Language Model Generation](https://arxiv.org/abs/2308.04592) *(2023)* — Curated feedback data trains a compact critic to spot errors and suggest fixes.
- [CriticEval: Evaluating Large Language Model as Critic](https://arxiv.org/abs/2402.13764) *(2024)* — Benchmarks scalar and textual critique ability for scalable-oversight research.
- [LLM Critics Help Catch LLM Bugs](https://arxiv.org/abs/2407.00215) *(2024)* — An RLHF-trained critic catches naturally occurring code bugs that human reviewers missed.
- [TIGERScore: Towards Building Explainable Metric for All Text Generation Tasks](https://arxiv.org/abs/2310.00752) *(2023)* — Instruction-tuned metric produces error-localized natural-language critique scores.
- [INSTRUCTSCORE: Explainable Text Generation Evaluation with Finegrained Feedback](https://arxiv.org/abs/2305.14282) *(2023)* — Fine-tunes a diagnostic metric from model critiques guided by a human-authored error taxonomy.
- [xFinder: Large Language Models as Automated Evaluators for Reliable Evaluation](https://arxiv.org/abs/2405.11874) *(2024)* — Replaces brittle regex answer extraction with a dedicated small extractor model.
- [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](https://arxiv.org/abs/2603.19191) *(2026)* — Adapts the critic-as-judge pattern to reward interface-agent trajectories at scale.

### Judge behavior science: bias

- [Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge](https://arxiv.org/abs/2406.07791) *(2024)* — Introduces repetition-stability, position-consistency, and preference-fairness metrics.
- [Large Language Models are not Fair Evaluators](https://arxiv.org/abs/2305.17926) *(2023)* — Response order alone flips judge rankings, corrected by multi-evidence calibration.
- [Split and Merge: Aligning Position Biases in LLM-based Evaluators](https://arxiv.org/abs/2310.01432) *(2023)* — Splits answers into aligned segments before comparison, targeting position bias at its source.
- [Verbosity Bias in Preference Labeling by Large Language Models](https://arxiv.org/abs/2310.10076) *(2023)* — Documents systematic preference for longer responses regardless of quality.
- [Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators](https://arxiv.org/abs/2404.04475) *(2024)* — Regression-adjusts win rates to a counterfactual equal-length comparison.
- [Self-Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2410.21819) *(2024)* — Links self-preference to lower perplexity of the judge's own generation style.
- [LLM Evaluators Recognize and Favor Their Own Generations](https://arxiv.org/abs/2404.13076) *(2024)* — Links self-preference to a judge's ability to recognize its own text, establishing a causal path.
- [Do LLM Evaluators Prefer Themselves for a Reason?](https://arxiv.org/abs/2504.03846) *(2025)* — Uses verifiable domains to separate legitimate self-preference from harmful bias.
- [Beyond the Surface: Measuring Self-Preference in LLM Judgments](https://arxiv.org/abs/2506.02592) *(2025)* — Compares judge scores against gold judgments to isolate bias from genuine quality.
- [Quantifying and Mitigating Self-Preference Bias of LLM Judges](https://arxiv.org/abs/2604.22891) *(2026)* — Cognitive-load decomposition into sub-evaluations reduces self-preference bias.
- [Self-Preference Bias in Rubric-Based Evaluation of Large Language Models](https://arxiv.org/abs/2604.06996) *(2026)* — Shows criteria-based judges still favor same-family outputs despite itemized structure.
- [Am I More Pointwise or Pairwise? Revealing Position Bias in Rubric-Based LLM-as-a-Judge](https://arxiv.org/abs/2602.02219) *(2026)* — Shows criteria-based judging behaves like multiple choice, with bias over score options and criterion order.
- [BiasScope: Towards Automated Detection of Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2602.09383) *(2026)* — Discovers unknown judge biases by automated exploration rather than testing a predefined bias list.
- [Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector](https://arxiv.org/abs/2505.17100) *(2025)* — A plug-in detector flags biased verdicts and generates corrective reasoning without retraining the judge.
- [Style Over Substance: Evaluation Biases for Large Language Models](https://arxiv.org/abs/2307.03025) *(2023)* — Shows crowd and model evaluators both reward factual errors over brevity.
- [Style Outweighs Substance: Failure Modes of LLM Judges in Alignment Benchmarking](https://arxiv.org/abs/2409.15268) *(2024)* — Finds judge preferences uncorrelated with safety or knowledge, dominated by style.
- [Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation](https://arxiv.org/abs/2608.01666) *(2026)* — Isolates presentation style from scientific content to quantify stylistic bias.
- [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://arxiv.org/abs/2410.02736) *(2024)* — Applies principle-guided perturbations to quantify twelve distinct judge bias types.
- [Humans or LLMs as the Judge? A Study on Judgement Biases](https://arxiv.org/abs/2402.10669) *(2024)* — Ground-truth-free framework comparing misinformation, authority, and beauty bias.
- [OffsetBias: Leveraging Debiased Data for Tuning Evaluators](https://arxiv.org/abs/2407.06551) *(2024)* — Constructs a debiased preference dataset to fine-tune bias-resistant evaluators.
- [Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization](https://arxiv.org/abs/2603.08091) *(2026)* — Trains bias-aware judges via reinforcement learning against an explicit bias-type taxonomy.
- [Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines](https://arxiv.org/abs/2604.23178) *(2026)* — Compares debiasing techniques, finding style bias outweighs position bias.
- [Evaluating Scoring Bias in LLM-as-a-Judge](https://arxiv.org/abs/2506.22316) *(2025)* — Defines and quantifies three novel scoring biases: rubric order, score identifier, and reference-answer score.
- [When Can You Debias an LLM Judge? Identifiability Limits, a Test, and Designs for Top-k Ranking](https://arxiv.org/abs/2607.02104) *(2026)* — Derives identifiability limits on debiasing and a test for reliable top-k ranking.
- [Assistant-Guided Mitigation of Teacher Preference Bias in LLM-as-a-Judge](https://arxiv.org/abs/2505.19176) *(2025)* — An unbiased assistant supplements teacher-distilled data to remove teacher bias.
- [Comparing Developer and LLM Biases in Code Evaluation](https://arxiv.org/abs/2603.24586) *(2026)* — Finds judges favor longer explanations that real developers do not want.
- [Great Models Think Alike and this Undermines AI Oversight](https://arxiv.org/abs/2502.04313) *(2025)* — A chance-adjusted similarity metric shows judges favor models resembling themselves.

### Judge behavior science: reliability and calibration

- [Investigating Non-Transitivity in LLM-as-a-Judge](https://arxiv.org/abs/2502.14074) *(2025)* — Shows pairwise preferences violate transitivity, undermining ranking-based evaluation.
- [TrustJudge: Inconsistencies of LLM-as-a-Judge and How to Alleviate Them](https://arxiv.org/abs/2509.21117) *(2025)* — Distribution-sensitive scoring fixes score-comparison and transitivity violations.
- [The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2606.13685) *(2026)* — Repeated-trial testing finds verdicts flip often enough to require aggregation.
- [Overconfidence in LLM-as-a-Judge: Diagnosis and Confidence-Driven Solution](https://arxiv.org/abs/2508.06225) *(2025)* — Fuses judges into a risk-aware calibrated ensemble to correct diagnosed overconfidence.
- [Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge Models](https://arxiv.org/abs/2606.19544) *(2026)* — Shows agreement and consistency do not guarantee the judge measures the intended construct.
- [Through the Judge's Eyes: Inferred Thinking Traces Improve Reliability of LLM Raters](https://arxiv.org/abs/2510.25860) *(2025)* — Infers human annotators' latent reasoning from label-only ratings to guide model raters.
- [Who's Your Judge? On the Detectability of LLM-Generated Judgments](https://arxiv.org/abs/2509.25154) *(2025)* — Tests whether model-authored judgments are statistically distinguishable from human ones.
- [LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge](https://arxiv.org/abs/2506.09443) *(2025)* — Shows adversarial prompts reliably manipulate judge outcomes across many attack and defense pairings.
- [How to Evaluate Reward Models for RLHF](https://arxiv.org/abs/2410.14872) *(2024)* — Proposes benchmarks testing whether a reward model actually improves downstream policies.
- [Aligning with Human Judgement: The Role of Pairwise Preference in Large Language Model Evaluators](https://arxiv.org/abs/2403.16950) *(2024)* — Recasts evaluation as preference-based ranking rather than calibrating a judge's absolute scores.
- [How to Correctly Report LLM-as-a-Judge Evaluations](https://arxiv.org/abs/2511.21140) *(2025)* — A plug-in correction for judge sensitivity and specificity, yielding principled confidence intervals.
- [Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory](https://arxiv.org/abs/2602.00521) *(2026)* — Applies a graded response model to separate intrinsic judge consistency from human alignment.
- [An Empirical Study of LLM-as-a-Judge: How Design Choices Impact Evaluation Reliability](https://arxiv.org/abs/2506.13639) *(2025)* — Finds stated evaluation criteria drive judge reliability more than decoding or added reasoning.
- [Time to REFLECT: Can We Trust LLM Judges for Evidence-based Research Agents?](https://arxiv.org/abs/2605.19196) *(2026)* — A failure taxonomy plus controlled interventions expose where judges misread research-agent traces.
- [Beyond the Illusion of Consensus: From Surface Heuristics to Knowledge-Grounded Evaluation in LLM-as-a-Judge](https://arxiv.org/abs/2603.11027) *(2026)* — Traces illusory judge consensus to shared rubric structure, proposing domain-grounded criteria instead.
- [An Empirical Study of LLM-as-a-Judge for LLM Evaluation](https://arxiv.org/abs/2403.02839) *(2024)* — Finds fine-tuned judges overfit in-domain, generalizing worse than a prompted frontier judge.
- [Aligning Large Language Models by On-Policy Self-Judgment](https://arxiv.org/abs/2402.11253) *(2024)* — Judge-augmented fine-tuning lets one model score its own on-policy samples without a separate reward model.
- [PairJudge RM: Perform Best-of-N Sampling with Knockout Tournament](https://arxiv.org/abs/2501.13007) *(2025)* — A pairwise judge run as a knockout tournament replaces inconsistent pointwise best-of-N scoring.

### Judge behavior science: adversarial robustness

- [Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on Zero-shot LLM Assessment](https://arxiv.org/abs/2402.14016) *(2024)* — Short universal adversarial phrases transfer across prompts to inflate scores.
- [Optimization-based Prompt Injection Attack to LLM-as-a-Judge](https://arxiv.org/abs/2403.17710) *(2024)* — A gradient-optimized injected sequence forces the judge to pick the attacker's response.
- [Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections](https://arxiv.org/abs/2504.18333) *(2025)* — Measures how content-author versus system-prompt injection attacks transfer across judge models.
- [Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks](https://arxiv.org/abs/2505.13348) *(2025)* — Formalizes comparative-undermining and justification-manipulation injection attacks against judge decisions.
- [On the Adversarial Robustness of Multimodal LLM Judges](https://arxiv.org/abs/2606.15608) *(2026)* — First framework evaluating multimodal judge robustness, introducing a transferable score-inflating attack.
- [Cheating Automatic LLM Benchmarks: Null Models Achieve High Win Rates](https://arxiv.org/abs/2410.07137) *(2024)* — Constant content-free responses exploit length and style bias to top major benchmarks.
- [A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness](https://arxiv.org/abs/2603.06594) *(2026)* — Audits harmfulness judges against human labels, finding accuracy near chance under red-teaming shift.

### Multi-agent, debate, and ensemble judges

- [Multi-Agent Debate for LLM Judges with Adaptive Stability Detection](https://arxiv.org/abs/2510.12697) *(2025)* — Judges debate under a statistical stopping rule instead of static majority voting.
- [Auto-Arena: Automating LLM Evaluations with Agent Peer Battles and Committee Discussions](https://arxiv.org/abs/2405.20267) *(2024)* — Candidate models debate head-to-head while a judge committee votes.
- [Wider and Deeper LLM Networks are Fairer LLM Evaluators](https://arxiv.org/abs/2308.01862) *(2023)* — Arranges judges as a multi-layer network of diverse evaluator neurons rather than independent votes.
- [Emergence of Biased Consensus in Multi-Agent LLM Debates](https://arxiv.org/abs/2608.02827) *(2026)* — Shows debate among homogeneous judges converges on shared bias rather than cancelling it.
- [Who can we trust? LLM-as-a-jury for Comparative Assessment](https://arxiv.org/abs/2602.16610) *(2026)* — Adds a per-judge discriminator parameter so jury aggregation infers rankings and judge reliability together.

### Efficient judges

- [Reinforcement Learning-based Knowledge Distillation with LLM-as-a-Judge](https://arxiv.org/abs/2604.02621) *(2026)* — Distills a judge's single-token reward signal into student models over unlabeled data.
- [Reasoning Is Not Free: Robust Adaptive Cost-Efficient Routing for LLM-as-a-Judge](https://arxiv.org/abs/2605.10805) *(2026)* — Routes each case between reasoning and non-reasoning judges to balance cost.
- [RTLC: Research, Teach-to-Learn, Critique](https://arxiv.org/abs/2605.13695) *(2026)* — Three-stage prompting lifts judge accuracy with no fine-tuning.
- [You Only Judge Once: Multi-response Reward Modeling in a Single Forward Pass](https://arxiv.org/abs/2604.10966) *(2026)* — Scores multiple image and video candidates in a single vision-language forward pass.

## Reward Hacking and Robustness

### Rubric-specific hacking and attack surface

- [Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2605.12474) *(2026)* — A cross-family judge panel separates verifier failure from rubric-design limitation.
- [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning](https://arxiv.org/abs/2606.04923) *(2026)* — Injects known judge biases into a controllable environment to reproduce hacking onset.
- [Rubrics as an Attack Surface: Stealthy Preference Drift in LLM Judges](https://arxiv.org/abs/2602.13576) *(2026)* — Shows criteria-based judges can be stealthily manipulated into drifting preferences.
- [RIFT: A Rubric Failure Mode Taxonomy and Automated Diagnostics](https://arxiv.org/abs/2604.01375) *(2026)* — Taxonomizes how criteria grading fails and provides automated diagnostics.
- [PReMISE: Policy Rubrics as Measurement Specifications for LLM Judges](https://arxiv.org/abs/2605.30803) *(2026)* — Audits criteria sets on structural adequacy, reliability, preference fit, and robustness.
- [EST-PRM: Stress-Testing Process Reward Models Before They Become Load-Bearing](https://arxiv.org/abs/2606.00437) *(2026)* — Step inflation and reordering preserve correctness while fooling step-level scoring.

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

### Specification gaming and reward tampering

- [Sycophancy to Subterfuge: Investigating Reward-Tampering in Large Language Models](https://arxiv.org/abs/2406.10162) *(2024)* — Shows reward tampering generalizes from minor sycophancy to outright tampering.
- [Honesty to Subterfuge: In-Context Reinforcement Learning Can Make Honest Models Reward Hack](https://arxiv.org/abs/2410.06491) *(2024)* — In-context reflection alone pushes honest models into specification gaming.
- [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926) *(2025)* — Optimizing against a reasoning monitor produces obfuscated hacking that evades it.
- [Specification Self-Correction: Mitigating In-Context Reward Hacking Through Test-Time Refinement](https://arxiv.org/abs/2507.18742) *(2025)* — Has the model rewrite its own tainted specification to close the exploited loophole.
- [Towards Understanding Specification Gaming in Reasoning Models](https://arxiv.org/abs/2605.02269) *(2026)* — Catalogs reasoning models exploiting their training specification instead of solving the task.
- [Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use](https://arxiv.org/abs/2605.02964) *(2026)* — Tests tool-using agents for shortcuts like skipping verification or tampering with eval code.
- [SoliReward: Mitigating Susceptibility to Reward Hacking and Annotation Noise in Video Generation Reward Models](https://arxiv.org/abs/2512.22170) *(2025)* — Hardens a video reward model against both criteria gaming and noisy human annotation.
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
- [Unified Personalized Reward Model for Vision Generation](https://arxiv.org/abs/2602.02380) *(2026)* — Instantiates fine-grained criteria per request rather than scoring against one fixed evaluation rubric.
- [AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities](https://arxiv.org/abs/2607.24821) *(2026)* — Grades audio-video edits against thousands of checklist items plus a separate realism rubric.
- [Evaluation-Verification Reward for Consistent Multi-Reference Image Editing](https://arxiv.org/abs/2607.29025) *(2026)* — Splits multi-reference edit evaluation into distinct visual criteria, each checked by a grounding verifier.
- [ReasonEdit: Towards Interpretable Image Editing Evaluation via Reinforcement Learning](https://arxiv.org/abs/2605.07477) *(2026)* — Trains an image-edit reward model on human judgments of logicality, accuracy, and usefulness.
- [FilmBench: A Film-Grade Benchmark for Cinematic Video Generation](https://arxiv.org/abs/2607.24241) *(2026)* — Scores generated video against a three-level taxonomy of cinematic craft criteria.
- [RubiCap: Rubric-Guided Reinforcement Learning for Dense Image Captioning](https://arxiv.org/abs/2603.09160) *(2026)* — Applies criteria-guided reward specifically to dense image captioning.
- [Visual Preference Optimization with Rubric Rewards](https://arxiv.org/abs/2604.13029) *(2026)* — Builds instance-specific essential-and-additional checklists to filter visual preference pairs.

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

### Multimodal judges and reward models

- [MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark](https://arxiv.org/abs/2402.04788) *(2024)* — First systematic benchmark of multimodal judges across scoring, comparison, and ranking.
- [MM-RLHF: The Next Step Forward in Multimodal LLM Alignment](https://arxiv.org/abs/2502.10391) *(2025)* — Large multimodal preference set with a critique-based reward model scored across dimensions.
- [Multimodal RewardBench: Holistic Evaluation of Reward Models for Vision Language Models](https://arxiv.org/abs/2502.14191) *(2025)* — Expert-annotated benchmark spanning correctness, reasoning, and safety.
- [Multimodal RewardBench 2: Evaluating Omni Reward Models for Interleaved Text and Image](https://arxiv.org/abs/2512.16899) *(2025)* — Extends reward evaluation to models judging interleaved text-and-image output.
- [VLRMBench: A Comprehensive and Challenging Benchmark for Vision-Language Reward Models](https://arxiv.org/abs/2503.07478) *(2025)* — Tests process understanding, outcome assessment, and critique generation together.
- [VL-RewardBench: A Challenging Benchmark for Vision-Language Generative Reward Models](https://arxiv.org/abs/2411.17451) *(2024)* — Stress-tests generative reward models on hallucination detection where scorers fail.
- [ViLBench: A Suite for Vision-Language Process Reward Modeling](https://arxiv.org/abs/2503.20271) *(2025)* — Benchmark and data suite for step-level reward models in vision-language reasoning.
- [Multi-Crit: Benchmarking Multimodal Judges on Pluralistic Criteria-Following](https://arxiv.org/abs/2511.21662) *(2025)* — Tests whether judges follow multiple potentially conflicting user-specified criteria.
- [R1-Reward: Training Multimodal Reward Model Through Stable Reinforcement Learning](https://arxiv.org/abs/2505.02835) *(2025)* — Trains a multimodal reward model with stabilized RL rather than supervised fitting.
- [Skywork-VL Reward: An Effective Reward Model for Multimodal Understanding and Reasoning](https://arxiv.org/abs/2505.07263) *(2025)* — General-purpose multimodal reward model spanning understanding and reasoning.
- [BaseReward: A Strong Baseline for Multimodal Reward Model](https://arxiv.org/abs/2509.16127) *(2025)* — Distills which design choices actually matter for multimodal reward modeling.
- [Advancing Multimodal Judge Models through a Capability-Oriented Benchmark and MCTS-Driven Data Generation](https://arxiv.org/abs/2603.00546) *(2026)* — Organizes judge evaluation by capability and synthesizes harder training data by search.
- [Omni-RRM: Advancing Omni Reward Modeling via Automatic Rubric-Grounded Preference Synthesis](https://arxiv.org/abs/2602.00846) *(2026)* — Synthesizes criteria-grounded preference justifications spanning text, image, video, and audio.
- [VLFeedback: A Large-Scale AI Feedback Dataset for Large Vision-Language Models Alignment](https://arxiv.org/abs/2410.09421) *(2024)* — Multi-aspect feedback annotating helpfulness, visual faithfulness, and safety separately, used to train Silkie.
- [Mitigating Perceptual Judgment Bias in Multimodal LLM-as-a-Judge via Perceptual Perturbation and Reward Modeling](https://arxiv.org/abs/2606.02578) *(2026)* — Uses visual perturbations to correct judges rewarding plausible text over visual truth.

### Multimodal reasoning rubrics

- [AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning](https://arxiv.org/abs/2510.14738) *(2025)* — Self-aggregates criteria checkpoints from successful trajectories without human annotation.
- [Auto-Rubric as Reward: From Implicit Preferences to Explicit Multimodal Generative Criteria](https://arxiv.org/abs/2605.08354) *(2026)* — Externalizes implicit preferences into prompt-specific independently verifiable criteria.
- [DeltaRubric: Generative Multimodal Reward Modeling via Joint Planning and Verification](https://arxiv.org/abs/2605.09269) *(2026)* — Plans criteria and verifies against them in a single generative pass.
- [Learning What Matters: Dynamic Dimension Selection and Aggregation for Interpretable Vision-Language Reward Modeling](https://arxiv.org/abs/2604.05445) *(2026)* — Selects which dimensions matter per instance for interpretable rewards.
- [VisualPRM: An Effective Process Reward Model for Multimodal Reasoning](https://arxiv.org/abs/2503.10291) *(2025)* — Step-level process reward model built for multimodal chain-of-thought reasoning.
- [Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models](https://arxiv.org/abs/2603.16253) *(2026)* — Adds explicit visual-premise verification to reduce ungrounded step scoring.
- [Improving Vision-language Models with Perception-centric Process Reward Models](https://arxiv.org/abs/2604.24583) *(2026)* — Grounds process errors at token level by extracting image-related claims for verification.
- [Judging the Judges: Can Large Vision-Language Models Fairly Evaluate Chart Comprehension and Reasoning?](https://arxiv.org/abs/2505.08468) *(2025)* — Pairwise and pointwise criteria for grading chart comprehension.

### Video

The sibling lists [awesome-rm-for-video-generation](https://github.com/chrisliu298/awesome-rm-for-video-generation) and [awesome-rl-for-video-generation](https://github.com/chrisliu298/awesome-rl-for-video-generation) cover video reward modeling in depth. Only the criteria-decomposed cut appears here.

- [Claim-Level Rubric Rewards for Video Caption Reinforcement Learning](https://arxiv.org/abs/2607.05150) *(2026)* — Decomposes video captions into individually verifiable claims scored as reward.
- [Incentivizing Vision Language Models to Search for Long Video Question Answering](https://arxiv.org/abs/2607.02959) *(2026)* — Compiles questions into temporal-logic evidence checklists for dense verifiable reward.
- [TimeThink: Reasoning with Time for Video LLMs](https://arxiv.org/abs/2607.05089) *(2026)* — Combines step-wise temporal process rewards with joint process-outcome optimization.
- [Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models](https://arxiv.org/abs/2605.07872) *(2026)* — Benchmark plus reward models for long-reasoning video preference judgment.
- [Think, then Score: Decoupled Reasoning and Scoring for Video Reward Modeling](https://arxiv.org/abs/2605.05922) *(2026)* — Separates the reasoning trace from the final regression score.
- [VideoRewardBench: Comprehensive Evaluation of Multimodal Reward Models for Video Understanding](https://arxiv.org/abs/2509.00484) *(2025)* — Evaluates reward models on video-understanding judgment, distinct from generation.
- [A Benchmark for Omni-Modal Reasoning in Long Videos](https://arxiv.org/abs/2512.16978) *(2025)* — Weighted criterion-level grading across vision, speech, and ambient audio.

### Audio, speech, and music

An emerging area: one 2020 anchor, then almost everything from late 2025 onward.

- [BATON: Aligning Text-to-Audio Model with Human Preference Feedback](https://arxiv.org/abs/2402.00744) *(2024)* — Builds a human preference dataset for text-to-audio and aligns the generator to it.
- [AGAV-Rater: Adapting Large Multimodal Model for AI-Generated Audio-Visual Quality Assessment](https://arxiv.org/abs/2501.18314) *(2025)* — Adapts a multimodal model to rate audio-visual quality jointly rather than per track.
- [Workflow-Based Evaluation of Music Generation Systems](https://arxiv.org/abs/2507.01022) *(2025)* — Scores generated music on a standardized per-criterion scale inside an evaluator workflow.
- [SCORE: Scaling audio generation using Standardized COmposite REwards](https://arxiv.org/abs/2509.19831) *(2025)* — Normalizes and combines several perceptual reward components into one composite signal.
- [PrismAudio: Decomposed Chain-of-Thoughts and Multi-dimensional Rewards for Video-to-Audio Generation](https://arxiv.org/abs/2511.18833) *(2025)* — Four specialized reasoning rewards drive multi-dimensional video-to-audio training.
- [MR-FlowDPO: Multi-Reward Direct Preference Optimization for Flow-Matching Text-to-Music Generation](https://arxiv.org/abs/2512.10264) *(2025)* — Combines text-alignment, semantic-consistency, and production-quality rewards for flow-matching music models.
- [Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models](https://arxiv.org/abs/2603.11661) *(2026)* — Uses online audio-language-model feedback as a fine-grained reward.
- [AnyAudio-Judge: A Dynamic Rubric-Based Benchmark and Evaluator for Audio Instruction Following](https://arxiv.org/abs/2606.03116) *(2026)* — Adaptively decomposes audio captions into verifiable binary criteria across domains.
- [Reinforcement Learning with Evolving Rubrics as Rewards for Audio Reasoning](https://arxiv.org/abs/2608.02831) *(2026)* — Self-evolving audio-grounded criteria supervise audio reasoning beyond text-only rubrics.

### 3D generation

- [3DGen-Bench: Comprehensive Benchmark Suite for 3D Generative Models](https://arxiv.org/abs/2503.21745) *(2025)* — Establishes a 3D preference arena plus a reward model for automatic evaluation.
- [DreamCS: Geometry-Aware Text-to-3D Generation with Unpaired 3D Reward Supervision](https://arxiv.org/abs/2506.09814) *(2025)* — Trains an unpaired 3D preference reward model via a Cauchy-Schwarz divergence objective on annotated meshes.
- [End-to-End Fine-Tuning of 3D Texture Generation using Differentiable Rewards](https://arxiv.org/abs/2506.18331) *(2025)* — Back-propagates differentiable reward through a 3D texture generation pipeline.
- [CREward: A Type-Specific Creativity Reward Model](https://arxiv.org/abs/2511.19995) *(2025)* — Scores 3D asset creativity along geometry, material, and texture axes separately.

## Agent, GUI, and Embodied Verification

The densest 2026 area. Verification mechanisms here — environment-state probing, milestone rewards, executable checkers — are architecturally distinct from text judging.

### GUI and computer-use agents

- [GUI-Shepherd: Reliable Process Reward and Verification for Long-Sequence GUI Tasks](https://arxiv.org/abs/2509.23738) *(2025)* — Step-level process reward improving online RL for long-horizon interface trajectories.
- [CUARewardBench: A Benchmark for Evaluating Reward Models on Computer-using Agent](https://arxiv.org/abs/2510.18596) *(2025)* — Benchmarks outcome and process reward models at trajectory and step level.
- [Agentic Reward Modeling: Verifying GUI Agent via Progressive Trajectory-Grounded Interaction](https://arxiv.org/abs/2602.00575) *(2026)* — A verifier agent probes the environment for evidence rather than passively observing.
- [Adaptive Milestone Reward for GUI Agents](https://arxiv.org/abs/2602.11524) *(2026)* — Anchors trajectories to milestones distilled from successful runs for credit assignment.
- [AgentV-RL: Scaling Reward Modeling with Agentic Verifier](https://arxiv.org/abs/2604.16004) *(2026)* — Turns reward modeling into tool-augmented deliberation with forward and backward verifiers.
- [Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/abs/2607.25904) *(2026)* — Proposes completion conditions then verifies them by invoking system and app tools.
- [OSReward: Instituting Standardized Evaluation for Cross-Platform Computer-Use Reward Models](https://arxiv.org/abs/2607.28609) *(2026)* — Standardized cross-platform protocol replacing hand-written per-task verifiers.
- [MagicGUI-RMS: A Multi-Agent Reward Model System for Self-Evolving GUI Agents via Automated Feedback Reflux](https://arxiv.org/abs/2601.13060) *(2026)* — Reflows automated feedback so interface agents self-improve while cutting annotation cost.
- [IntentScore: Intent-Conditioned Action Evaluation for Computer-Use Agents](https://arxiv.org/abs/2604.05157) *(2026)* — Plan-aware reward model scoring candidate interface actions from offline data.

### Embodied and robotic verification

- [VL-CheckList: Evaluating Pre-trained Vision-Language Models with Objects, Attributes and Relations](https://arxiv.org/abs/2207.00221) *(2022)* — Early checklist diagnostic splitting evaluation into object, attribute, and relation checks.
- [Embodied-R1: Reinforced Embodied Reasoning for General Robotic Manipulation](https://arxiv.org/abs/2508.13998) *(2025)* — Two-stage reinforced fine-tuning with a specialized multi-task reward for manipulation.
- [Real-Time Verification of Embodied Reasoning for Generative Skill Acquisition](https://arxiv.org/abs/2505.11175) *(2025)* — Verifies generated reasoning steps against grounded criteria during skill acquisition.
- [Robo-Dopamine: General Process Reward Modeling for High-Precision Robotic Manipulation](https://arxiv.org/abs/2512.23703) *(2025)* — Multi-view process reward model driving continuous self-improvement in manipulation.
- [Think Twice, Act Once: Verifier-Guided Action Selection For Embodied Agents](https://arxiv.org/abs/2605.12620) *(2026)* — Scores candidate actions with a learned verifier before execution.
- [Scaling Verification Can Be More Effective than Scaling Policy Learning for Vision-Language-Action Alignment](https://arxiv.org/abs/2602.12281) *(2026)* — Shows compute spent on a verifier can beat compute spent on more policy training.
- [Reward as An Agent for Embodied World Models](https://arxiv.org/abs/2606.19990) *(2026)* — An agentic reward framework actively evaluates generated behaviors to resist reward hacking.
- [RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models](https://arxiv.org/abs/2605.03821) *(2026)* — Defines robot-centric judge dimensions for aligning video world models via RL.

### Rubric rewards for agents, tool use, and software engineering

- [Agentic Rubrics as Contextual Verifiers for SWE Agents](https://arxiv.org/abs/2601.04171) *(2026)* — A repo-grounded checklist scores code patches without executing tests.
- [Beyond Verifiable Rewards: Rubric-Based GRM for Reinforced Fine-Tuning SWE Agents](https://arxiv.org/abs/2604.16335) *(2026)* — A human-designed criteria reward model filters and scores trajectories for fine-tuning.
- [SWE-TRACE: Optimizing Long-Horizon SWE Agents Through Rubric Process Reward Models and Heuristic Test-Time Scaling](https://arxiv.org/abs/2604.14820) *(2026)* — Criteria-based process reward plus memory-augmented RL for long-horizon coding.
- [StitchCUDA: An Automated Multi-Agents End-to-End GPU Programing Framework with Rubric-based Agentic Reinforcement Learning](https://arxiv.org/abs/2603.02637) *(2026)* — Trains a coder agent on combined criteria and execution rewards inside a planner-coder-verifier pipeline.
- [Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents](https://arxiv.org/abs/2605.23590) *(2026)* — Criteria act as per-step collaborators giving dense feedback inside the reasoning-action loop.
- [ARBOR: Online Process Rewards via a Reusable Rubric Buffer for Search Agents](https://arxiv.org/abs/2606.03239) *(2026)* — A reusable criteria buffer supplies online process rewards for multi-hop search.
- [RUBAS: Rubric-Based Reinforcement Learning for Agent Safety](https://arxiv.org/abs/2606.04051) *(2026)* — Multi-dimensional criteria rewards spanning tool-use, argument, and response safety.
- [OpenReward: Learning to Reward Long-form Agentic Tasks via Reinforcement Learning](https://arxiv.org/abs/2510.24636) *(2025)* — Trains a reward model for long-form agentic tasks where terminal verification is sparse.
- [LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards](https://arxiv.org/abs/2605.31584) *(2026)* — Criteria rewards supervise long-context reasoning learned from search trajectories.
- [Step-DeepResearch Technical Report](https://arxiv.org/abs/2512.20491) *(2025)* — A checklist-style judger hardens an autonomous research agent across a staged training pipeline.
- [LH-Bench: Skill-Grounded Evaluation of Long-Horizon Agents on Subjective Enterprise Tasks](https://arxiv.org/abs/2603.22744) *(2026)* — Expert-grounded criteria give judges the domain context that model-authored rubrics lack.
- [PRBench: End-to-end Paper Reproduction in Physics Research](https://arxiv.org/abs/2603.27646) *(2026)* — Grades end-to-end physics paper reproduction against detailed scoring rubrics and verified ground truth.
- [Mock Worlds, Real Skills: Building Small Agentic Language Models with Synthetic Tasks, Simulated Environments, and Rubric-Based Rewards](https://arxiv.org/abs/2601.22511) *(2026)* — Trains small agentic models entirely in synthetic environments graded by criteria.
- [CLI-Universe: Towards Verifiable Task Synthesis Engine for Terminal Agents](https://arxiv.org/abs/2606.22883) *(2026)* — Validates synthesized terminal tasks against explicit criteria for correctness and coverage.

### Rubric rewards for deep research

- [DR Tulu: Reinforcement Learning with Evolving Rubrics for Deep Research](https://arxiv.org/abs/2511.19399) *(2025)* — Criteria co-evolve with the policy to absorb newly discovered evidence.
- [DEEPRUBRIC: Evidence-Tree Rubric Supervision for Efficient Reinforcement Learning of Deep Research Agents](https://arxiv.org/abs/2606.17029) *(2026)* — Evidence-tree supervision gives dense efficient rewards for research agents.
- [Deep Research as Rubric for Reinforcement Learning](https://arxiv.org/abs/2606.01091) *(2026)* — Uses the research process itself as the criteria structure for the reward.
- [QUEST: Training Frontier Deep Research Agents with Fully Synthetic Tasks](https://arxiv.org/abs/2605.24218) *(2026)* — Rubric-tree synthesis decomposes queries into verifiable leaves for dense reward.
- [AgentDisCo: Towards Disentanglement and Collaboration in Open-ended Deep Research Agents](https://arxiv.org/abs/2605.11732) *(2026)* — Repurposes the generator as a scoring agent that evaluates critic outputs into quality signals.

## Rubric Quality and Meta-Evaluation

Whether criteria-based judging is reliable at all.

- [RubricEval: A Rubric-Level Meta-Evaluation Benchmark for LLM Judges in Instruction Following](https://arxiv.org/abs/2603.25133) *(2026)* — Meta-evaluates judges at the individual criterion level rather than the aggregate score.
- [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://arxiv.org/abs/2606.29920) *(2026)* — Meta-evaluates judge reliability at rubric scoring specifically on long, complex agentic outputs.
- [Autorubric: Unifying Rubric-based LLM Evaluation](https://arxiv.org/abs/2603.00077) *(2026)* — Unifies binary, ordinal, and nominal criteria under one framework with bias mitigation.
- [RubricBench: Aligning Model-Generated Rubrics with Human Standards](https://arxiv.org/abs/2603.01562) *(2026)* — Benchmarks model-generated criteria against expert-annotated ones over curated pairs.
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
| [MiroEval](https://arxiv.org/abs/2603.28407) | 2026 | Multimodal research | Per-query criteria plus atomic-claim factuality |
| [Expert Consulting Benchmark](https://arxiv.org/abs/2605.17554) | 2026 | Consulting | Deterministic verifiers plus an expert criterion set |
| [ProfBench](https://arxiv.org/abs/2510.18941) | 2025 | Professional reasoning | Criteria requiring expertise to answer and to grade |
| [UpBench](https://arxiv.org/abs/2511.12306) | 2025 | Real labor-market tasks | Expert-decomposed acceptance criteria with per-criterion feedback |
| [FrontierScience](https://arxiv.org/abs/2601.21165) | 2026 | Expert science tasks | Granular criteria grading the process, not just final answers |
| [GIM](https://arxiv.org/abs/2605.18663) | 2026 | Cross-domain integration | Rubric-decomposed scoring, several independently judged criteria per item |
| [COMPOSITE-Stem](https://arxiv.org/abs/2604.09836) | 2026 | Doctoral STEM | Criterion-based rubrics with an LLM-jury protocol beside exact match |
| [PRBench](https://arxiv.org/abs/2511.11562) | 2025 | Legal and finance | Large expert-authored criteria sets |
| [$OneMillion-Bench](https://arxiv.org/abs/2603.07980) | 2026 | Multi-domain expert | Accuracy, coherence, professional compliance |
| [PLawBench](https://arxiv.org/abs/2601.16669) | 2026 | Legal practice | Expert-designed criteria across legal scenarios |
| [LexRubric](https://arxiv.org/abs/2606.09389) | 2026 | Legal tasks | Atomic criteria under a six-dimensional framework |
| [Magis-Bench](https://arxiv.org/abs/2605.08437) | 2026 | Legal reasoning | Criteria-based magistrate-level grading |
| [Legal Issue Tree Rubrics](https://arxiv.org/abs/2512.01020) | 2025 | Legal traces | Tree-structured criteria for issue-spotting |
| [FinResearchBench II](https://arxiv.org/abs/2607.12252) | 2026 | Financial reports | Consensus-derived gold criteria |
| [WritingBench](https://arxiv.org/abs/2503.05244) | 2025 | Generative writing | Query-specific dynamic criteria via a critic model |
| [Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation](https://arxiv.org/abs/2606.01629) | 2026 | Long-form output | Meta-eval of judge reliability on document-length text |
| [LitBench](https://arxiv.org/abs/2507.00769) | 2025 | Creative writing | Paired preference labels (not per-criterion) |
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
| [StrongREJECT](https://arxiv.org/abs/2402.10260) | 2024 | Safety | Detailed harmfulness rubric for jailbreak responses |
| [Claw-Eval](https://arxiv.org/abs/2604.06132) | 2026 | Autonomous agents | Trajectory-aware safety and robustness criteria |
| [RefGrader](https://arxiv.org/abs/2510.09021) | 2025 | Math proofs | Problem-specific criteria for partial credit |
| [Beyond Score Prediction](https://arxiv.org/abs/2607.19219) | 2026 | Essay feedback | Binary criteria grading feedback quality |
| [LiveCodeBench Pro](https://arxiv.org/abs/2506.11928) | 2025 | Competitive programming | Olympiad-medalist expert judgment |

## Datasets

| Name | Year | What it contains |
|---|---|---|
| [Feedback Collection / Prometheus](https://arxiv.org/abs/2310.08491) | 2023 | Customized score rubrics with graded responses for evaluator training |
| [Preference Collection / Prometheus 2](https://arxiv.org/abs/2405.01535) | 2024 | Criteria-graded preference pairs for judge training |
| [HelpSteer](https://arxiv.org/abs/2311.09528) | 2023 | Multi-attribute helpfulness ratings across named dimensions |
| [HelpSteer2](https://arxiv.org/abs/2406.08673) | 2024 | Compact multi-attribute preference pairs |
| [HelpSteer2-Preference](https://arxiv.org/abs/2410.01257) | 2024 | Attribute ratings complemented with pairwise preferences |
| [HelpSteer3-Preference](https://arxiv.org/abs/2505.11475) | 2025 | Human-annotated multilingual preference pairs |
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
- [AutoSCORE: Enhancing Automated Scoring with Multi-Agent Large Language Models via Structured Component Recognition](https://arxiv.org/abs/2509.21910) *(2025)* — Structured component recognition makes automated criteria scoring decomposable.
- [Rubric-Guided Fine-tuning of SpeechLLMs for Multi-Aspect, Multi-Rater L2 Reading-Speech Assessment](https://arxiv.org/abs/2603.16889) *(2026)* — Models multiple raters explicitly rather than collapsing them to one consensus label.

## Domain-Specific Rubric RL

- [InfiMed-ORBIT: Aligning LLMs on Open-Ended Complex Tasks via Rubric-Based Incremental Training](https://arxiv.org/abs/2510.15859) *(2025)* — Case-conditioned criteria act as adaptive guides for incremental clinical RL.
- [Baichuan-M2: Scaling Medical Capability with Large Verifier System](https://arxiv.org/abs/2509.02208) *(2025)* — Pairs a patient simulator with a clinical criteria generator producing multi-dimensional metrics for medical RL.
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

Of the open frontier recipes checked against their primary sources, only Kimi K2 explicitly documents a rubric mechanism. The other two are included as the closest documented neighbours — a self-voting constitutional-style reward and a verifiable-reward pipeline — not as rubric methods. Several other labs are widely assumed to use criteria-based rewards but do not describe them in terms this list can verify.

- [Kimi K2: Open Agentic Intelligence](https://arxiv.org/abs/2507.20534) *(2025)* — Pairs verifiable-reward RL with a self-critique rubric using core, prescriptive, and human criteria.
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) *(2024)* — Pairs a rule-based reward model with a self-rewarding scheme that votes using the model itself.
- [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124) *(2024)* — Open post-training recipe pairing verifiable-reward RL with a Bradley-Terry reward model.

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

*Repository last updated: 2026-08-07. Literature systematically searched through August 2026. Coverage: rubrics as RL reward signals, rubric construction and refinement, checklists and constitutions, rubric-conditioned and fine-grained reward models, verifiers and programmatic graders, process rewards, LLM-as-a-judge, reward hacking and robustness, multimodal and agentic criteria-based rewards, rubric-graded benchmarks, datasets, and tooling.*
