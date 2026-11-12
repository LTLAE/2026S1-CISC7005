# Research log

## Scope and workflow

Stage 1 only: an AI-assisted initial draft. No verification program or human-correction stage was performed. Research was conducted on 30 October 2026 using web search and primary or official pages where available. Existing files in this directory were preserved; this run added the requested root-level deliverables.

## Search queries used

- “Detecting Reward Hacking large language models monitoring paper”
- “LLM reward hacking detection monitor reasoning traces reward hacking paper”
- “Is It Thinking or Cheating ICLR 2026 reward hacking effort”
- “specification gaming language models reward hacking detection empirical paper”
- “Monitoring reasoning models for misbehavior authors 2025”
- “Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis”
- “School of Reward Hacks authors 2025”
- “Monitoring Emergent Reward Hacking During Generation via Internal Activations authors”
- “Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations authors”

Sources consulted: arXiv records 2209.13085, 2503.11926, 2508.17511, 2510.01367, 2601.20103, 2603.04069, 2609.19101, and 2609.28614; OpenReview's ICLR 2026 record for the reasoning-effort paper; NeurIPS records for the foundational work; and OpenAI's publication page/PDF for CoT monitoring. Search results identified candidates; bibliographic details were taken from arXiv or venue pages where possible.

## Selection criteria and decisions

Selection favored direct relevance to detection/oversight, variety of evidence (outcomes, CoT, truncation/process, activations), technical detail, and a mix of foundations and recent work. Eight studies were selected. Skalse et al. grounds terminology; Taylor et al. provides occurrence/generalization context; Baker, Wang, Deshpande, Wilhelm, and Bergen cover monitoring and benchmarks; Huang contributes evaluator-oversight evidence. The ICLR effort paper is treated as one method among several.

Anthropic's reward-tampering curriculum was a relevant background candidate but was omitted from the short list because it studies occurrence more than detection. Reward-model overoptimization work was similarly less direct to this survey's central question. “Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use” was not selected because the available search result appeared to rely on an automatically generated summary rather than a paper record. Other recent candidates were omitted to stay within 5–10 references and avoid unconfirmed details.

## Taxonomy decisions

The taxonomy is an authorial synthesis organized by primary evidence: (1) external behavior and contrastive trajectory evaluation; (2) semantic monitoring of visible reasoning traces; and (3) process/internal-state signals, including reasoning truncation and activation probes. The last group combines related evidence sources but the paper distinguishes their assumptions. Categories overlap: a trace monitor reads process output, and an activation probe may score that same trace internally.

## Uncertainties and limitations

- Several 2026 items are preprints; their metadata and findings can change.
- DOI fields are blank where none was confirmed during drafting; blank does not mean no DOI exists.
- ICLR 2026 publication status and permanent metadata should be independently checked.
- Papers use different models, task environments, labels, and synthetic data, so their results are not head-to-head comparisons.
- Exact word count and page count can vary with the ACM class version and compiler.
- The supplied `acmart` class is referenced at compile time instead of copied, preserving the template unchanged.
