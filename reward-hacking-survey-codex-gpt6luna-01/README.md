# Reward-hacking survey draft

This directory contains the Stage 1 AI-generated survey draft and supporting research notes. It does not contain a verification program or claim that human verification is complete. Preserve `survey/references_ai_original.bib` as the original draft bibliography during subsequent review.

## Files

- `survey/survey_ai_original.tex`: ACM-format initial survey draft.
- `survey/references_ai_original.bib`: BibTeX bibliography used by the draft.
- `research/selected_papers.md`: selected source metadata, relevance, and inspection scope.
- `research/taxonomy.md`: method classification and criteria.
- `research/claims_to_verify.md`: claims for later independent checking.
- `process/research_log.md`: actual search and drafting actions.
- `process/ai_drafting_summary.md`: scope, decisions, and unresolved questions.

## Compile

Compile from `survey/` with the ACM class from the supplied template directory on TeX's search path (or copy/link `acmart.cls` into the build environment):

```sh
TEXINPUTS="../../ACM_Template//:" pdflatex survey_ai_original.tex
bibtex survey_ai_original
TEXINPUTS="../../ACM_Template//:" pdflatex survey_ai_original.tex
TEXINPUTS="../../ACM_Template//:" pdflatex survey_ai_original.tex
```

The template copy used is The class is in the sibling directory `../../ACM_Template` from `survey/`; add that directory to `TEXINPUTS` as shown below. The source keeps the ACM `sigconf` class and does not alter the class to evade page limits. Check the instructor's required author/header fields and resulting page layout before submission.

Compilation depends on a local LaTeX installation.
