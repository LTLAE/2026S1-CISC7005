# Research log

## Actions taken

1. Read the supplied assignment prompt and inspected the ACM template directory (`acmart.cls`, `sample-sigconf.tex`, and its formatting conventions).
2. Located the core paper at `pre/13536_Is_it_Thinking_or_Cheating.pdf` and extracted its text. Read its abstract, introduction, problem statement, method setup, reported comparisons, limitations discussion, related-work discussion, and references. The paper reports TRACE as an ICLR 2026 paper.
3. Queried academic/web search for the TRACE record, formal reward-hacking definitions, CoT monitoring, monitorability, CoT faithfulness, and verbalization fine-tuning. Consulted OpenReview and arXiv records surfaced by those searches.
4. Selected eight references based on direct conceptual or methodological relevance, with TRACE as the central paper.
5. Drafted a compact ACM survey plus a synthesis taxonomy, claim checklist, and source log.
6. Compiled the LaTeX with the supplied `acmart.cls` using pdfLaTeX and BibTeX; the PDF is two pages including references. Visual inspection found no clipping. BibTeX produced missing-volume/page warnings for preprints and incomplete proceedings fields; the source log records unresolved metadata.

## Queries and sources consulted

Search queries included: “Is It Thinking or Cheating TRACE ICLR 2026”; “LLM reward hacking detection chain of thought monitoring specification gaming paper”; “reward hacking language models implicit reward hacking detection reasoning effort paper arxiv”; “Skalse reward hacking proxy reward formal definition paper”; “Monitoring reasoning models for misbehavior 2503.11926”; “Teaching models to verbalize reward hacking 2506.22777”; “When chain of thought is necessary language models struggle to evade monitors”; and “Correlated proxies new definition improved mitigation reward hacking”.

Sources: supplied TRACE PDF; ACM `acmart` template/sample; OpenReview TRACE record and ICLR paper PDF; arXiv records for Skalse et al., Baker et al., Turpin et al., Emmons et al., Lanham et al., Denison et al., and Laidlaw et al. Search-result summaries supplied some metadata and abstracts.

## Papers considered

Included the eight entries listed in `selected_papers.md`. Skalse and Laidlaw provide formal/background framing but are not classified as detectors. Lanham and Denison inform the limits and risks of interpreting CoT or reward-tampering behavior; they are supporting studies, not detector proposals.

Not included: broad surveys and general reward-model benchmark papers because the short survey emphasizes direct method diversity; general RLHF papers without a clear reward-hacking detection contribution; the recently surfaced activation-monitor and agent benchmark preprints because their full papers and metadata were not inspected in this drafting pass.

## Decisions and unresolved metadata

- The taxonomy is presented as this survey's synthesis, not an established field-wide classification.
- CoT monitoring, output/action audits, TRACE, and verbalization fine-tuning are kept distinct by evidence type and role.
- TRACE is described as detection, while verbalization fine-tuning and proxy regularization are not presented as detectors.
- Laidlaw venue/year indexing was inconsistent in returned records; bibliography retains a note for later checking.
- Full author lists for two supporting studies have not been confirmed.
- No independent human verification was performed.
