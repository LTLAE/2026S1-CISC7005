# Research log

## Scope and date

AI-assisted drafting completed 2026-10-30. The scope was reward-hacking detection and monitoring in LLMs, with foundational specification-gaming and reward-hacking definitions included only to establish terminology. The assigned ICLR 2026 reasoning-effort paper was treated as one contribution among several.

## Search queries used

- `reward hacking detection large language models specification gaming monitoring reasoning traces academic papers`
- `LLM reward model exploitation reward hacking detection process supervision chain of thought monitoring research paper`
- `deceptive behavior monitoring language models reward hacking paper OpenReview arXiv`
- `reward hacking in large language models monitor detector 2025 2026`
- `reward hacking language model monitoring chain of thought monitor 2025`
- `Skalse reward hacking defining and characterizing reward hacking paper`
- `Krakovna specification gaming examples AI paper 2020`
- Exact-title searches for each selected paper, authors, venue, DOI, and BibTeX metadata.

## Sources consulted

- arXiv records and paper identifiers for preprints: 2209.13085, 2503.11926, 2506.19248, 2506.22777, 2603.04069, 2604.13602, 2605.02964, and 2510.01367.
- OpenReview and conference pages returned by title searches for ICLR/ICML records.
- NeurIPS and PMLR search results for venue information.
- DeepMind Safety Research Blog for the foundational specification-gaming examples.
- Search-result snippets were used for initial discovery only; they are not a substitute for the later independent verification stage.

## Selection criteria

Papers were selected for direct relevance to detection, diversity of evidence, methodological significance, and availability of a public paper record. The set includes outcome auditing, tool-use benchmarks, CoT monitoring, self-reporting/verbalization, reasoning-effort tests, activation monitoring, a formal definition, and one broad survey for context.

## Inclusion and exclusion decisions

- Included Skalse et al. because a stable definition is necessary to distinguish reward hacking from ordinary error and generic deception.
- Included Krakovna et al. as a foundational example source, while explicitly labeling it a blog post.
- Included Baker et al. and Turpin et al. to represent process/CoT monitoring but did not assume that CoT is faithful.
- Included Khalaf et al. and Thaman to represent behavioral detection and controlled evaluation.
- Included Wilhelm et al. for online internal-activation monitoring.
- Included Wang et al. (TRACE) because it targets implicit reward hacking; it is not used as the taxonomy's default.
- Included Wang et al.'s 2026 survey only as contextual background, not as the sole evidence for empirical claims.
- Excluded mitigation-only papers unless their monitoring assumptions were directly relevant to detection.

## Taxonomy decisions

The final taxonomy uses the source of evidence rather than the training intervention: (1) behavioral/outcome-based detection, (2) CoT/process monitoring, and (3) white-box/representation monitoring. Benchmarks are treated as an enabling layer because a benchmark creates controlled opportunities for detection but is not itself a detector. Overlap is explicit: a benchmark can provide labels for an activation probe, and a behavioral audit can trigger a CoT investigation.

## Uncertainties and limitations

Several works are 2025--2026 preprints or workshop papers, and final venue, DOI, author-list, and proceedings metadata may have changed. The DeepMind source is a blog post with an uncertain contributor list. Search results sometimes reported conflicting OpenReview identifiers or quantitative findings; those details were deliberately omitted from the draft unless needed for the conceptual synthesis. The literature is new and fragmented, so the survey does not claim exhaustive coverage. The main text avoids unsupported numerical comparisons and preserves uncertain metadata in notes and BibTeX `note` fields.

## Drafting boundary

This is the original AI-assisted draft for Stage 1. No verification program was implemented, and no independent human verification or silent correction was performed. The inventories intentionally retain pending statuses for later checking.
