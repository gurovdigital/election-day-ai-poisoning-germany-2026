# Election-Day AI Poisoning in Germany (20 September 2026)

Version 3, October 2026. This version follows a stricter security and compliance standard. The measurements, the counts and the findings are the same as in the earlier versions.

Data, source lists and scripts behind the research report by Pavel Gurov.

On 20 September 2026, election day in Berlin and Mecklenburg-Vorpommern, ten politically loaded questions in German were put to Google AI Overviews, ChatGPT Search, Gemini, Perplexity and Microsoft Copilot, ten times each (492 answers, 4,819 citations), and twice each to Meta AI from Berlin (20 answers). Perplexity cited Russia Today (RT) in 20 of 100 answers, Meta AI cited RT-linked blogs in 2 of 20 and Microsoft Copilot cited an RT-linked site in 3 of 100.

## Report

- English: [Election-Day AI Poisoning in Germany](report/Election-Day-AI-Poisoning-Germany-2026-EN.pdf)
- German: [KI-Vergiftung am Wahltag in Deutschland](report/Election-Day-AI-Poisoning-Germany-2026-DE.pdf)
- Online, English: [dosimeteraudit.org/research/election-day-ai-poisoning-germany](https://dosimeteraudit.org/research/election-day-ai-poisoning-germany)
- Online, German: [dosimeteraudit.org/research/ki-vergiftung-am-wahltag-deutschland](https://dosimeteraudit.org/research/ki-vergiftung-am-wahltag-deutschland)

## Check the numbers

Python 3.9 or later, nothing to install:

```
cd germany-2026
python3 scripts/verify.py wave1
```

The script checks the SHA-256 of every raw export against `wave1/CHECKSUMS.txt`, matches the runs against the ledger, and recomputes three figures from the raw answers using only the frozen EU and Pravda-network lists: answers citing Russian state media or the Pravda network (20 of 492), citations to them (25 of 4,819) and answers without any citation (17 of 492). It ends with `VERIFY: OK`.

The other figures in the report (RT-linked outlets, official and public-service sources, Meta AI) come from `scripts/classify.py`, `scripts/profile.py` and `scripts/manual_summary.py`, run on the same files.

## What is here

- `report/` - the report in English and German (PDF).
- `germany-2026/` - the verification package: every raw answer with its citations (`wave1/`, `pilot/`), the source lists with the evidence for each entry (`lists/`), the protocol, the run log with the freeze hashes (`PROTOCOL.md`, `RUN-LOG.md`) and the scripts (`scripts/`). Its own [README](germany-2026/README.md) describes the pipeline and how to run the same study for another country or topic. Re-running the data collection needs an Apify account; checking the numbers does not.

## Archive and history

The package is archived on Zenodo: https://doi.org/10.5281/zenodo.22925952 (all versions).

The folder `germany-2026/` is the same as `germany-2026-verification-package.zip` of version 3 on Zenodo. The file [germany-2026/AMENDMENTS.md](germany-2026/AMENDMENTS.md) lists every file that differs from versions 1 and 2, with its SHA-256 before and after.

## Citation

Gurov, P. (2026). *Election-Day AI Poisoning in Germany (20 September 2026): verification package* (Version 3) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.22925952

## Licence

Scripts: MIT OR EUPL-1.2, at your choice ([LICENSE-MIT](LICENSE-MIT), [LICENSE](LICENSE)). Report, data, lists and documentation: CC BY 4.0 ([LICENSE-DATA.md](LICENSE-DATA.md)).

## Contact

Pavel Gurov, Dosimeter, Berlin: [dosimeteraudit.org](https://dosimeteraudit.org), contact@dosimeteraudit.org
