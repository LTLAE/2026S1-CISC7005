# Claims to verify in the later human-review stage

These are claims appearing in the draft, not verified conclusions. “Location” gives a suggested section based on the inspected records; page/section numbers should be confirmed from the source PDFs.

| ID | Exact claim in draft | Cited source | Type | Suggested location | Difficulty |
|---|---|---|---|---|---|
| C1 | “Formal accounts characterize reward hacking as increased proxy reward accompanied by worse performance on the true objective, which is often unavailable.” | Skalse et al. (2022) | Definition | Abstract and formal definition | Medium: confirm exact formal conditions and scope. |
| C2 | “A wrong answer alone is an ordinary model error; reward hacking requires exploiting the evaluation or optimization signal so that proxy success diverges from task success.” | Skalse et al. (2022); synthesis | Conceptual distinction | Definition and discussion of proxy/true reward | Medium: partly a synthesized distinction; judge if wording is too restrictive. |
| C3 | “Baker et al. show CoT monitors can detect coding-agent misbehavior, but optimizing directly against the monitor can promote obfuscation.” | Baker et al. (2025) | Empirical finding | Abstract, experiments, discussion | Medium: verify environment and optimization regime. |
| C4 | “TRACE progressively truncates a generated CoT, asks the model to answer from each prefix, and measures reward as a function of retained reasoning.” | Wang et al. (2026) | Method | Methodology section | Low-medium: confirm exact TRACE procedure/normalization. |
| C5 | “Its interpretation depends on the premise that the exploit is easier than solving the task.” | Wang et al. (2026) | Method assumption | Introduction and method motivation | Medium: distinguish premise from proven requirement. |
| C6 | “Verbalization fine-tuning trains models to acknowledge influential prompt cues before RL; this can make some hacks easier to monitor, but is a training intervention rather than an independent detector.” | Turpin et al. (2025) | Method / synthesis | Abstract and experimental setup | Medium: inspect whether the summary matches paper terminology and scope. |
| C7 | “Evaluations using injected loopholes are useful controlled tests but cannot enumerate real-world exploit strategies.” | Wang et al. (2026); synthesis | Limitation / inference | TRACE experiment design and discussion | Medium-high: first clause factual, second is an inference to label clearly. |
| C8 | “No detector can establish the absence of hacking.” | General synthesis | Limitation | Conclusion | High: broad claim; check whether a narrower statement is more defensible. |
