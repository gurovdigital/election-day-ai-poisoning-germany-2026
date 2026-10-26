# PROTOCOL - Germany AI answer-surface audit, state elections of 20 September 2026 (pre-registered)

Version 1.0 · written 20 September 2026 · status: awaiting Pavel Gurov's "пуск" - no wave run executed (one single-question pilot of the Copilot collector, run fdSIR679KtbFev1lG).
On approval this file is frozen: its SHA-256 and the UTC timestamp go into `RUN-LOG.md` before the first wave run. Any later change is a new version, logged, never a silent edit.

## 0. Question and analytical stance

**Research question.** When the consumer AI answer surfaces most used in Germany are asked, in German, questions that operationalise narratives documented as pushed by Kremlin campaigns (Storm-1516, Doppelgänger, the EUvsDisinfo case corpus), do their answers cite sources attributable - by published lists only - to the Russian state or to the Pravda / Portal Kombat network, and which outlets fill those presumed data voids instead?

**Stance.** Data voids are the mechanism; grooming is the exploitation. Each question is a presumed data void: a loaded phrasing that authoritative German pages rebut rather than answer. We count sources, not truth: the list of cited domains is a fact two coders reproduce; the quality of an answer is an opinion. Citation is not influence (declared limitation).

## 1. Fixed inputs (frozen with this protocol)

**Questions.** Q01-Q10, asked in German exactly as in `questions.csv` (approved by Pavel Gurov on 16 September 2026; SHA-256 in `CHECKSUMS-questions.txt`). Four target AfD voters (Storm-1516 fakes), three reach both flanks (Doppelgänger, EUvsDisinfo), three target the left flank (Doppelgänger). English and Russian columns are for readers only.

**Prompt language: German only** - the citizen's surface; the location of the collection is not configurable, language is the locale lever.

**Surfaces - class B (consumer products), collected through their consumer interfaces, configured in `study.json`:**

| # | Surface | Why |
|---|---|---|
| 1 | Google AI Overviews | widest passive exposure: Google 88.49% of German search (StatCounter, Aug 2026); AI Overviews live in Germany since 26 Mar 2025 |
| 2 | ChatGPT Search | 71% of German AI users (Bitkom 2026); 77.83% of chatbot referrals (StatCounter DE, Aug 2026) |
| 3 | Gemini | 50% of AI users; 9.85% of referrals |
| 4 | Microsoft Copilot | 43% of AI users; 3.82% of referrals (the first collector returned 0 items in two pilots on 9 Sep 2026, so a second one is used) |
| 5 | Perplexity | 5.44% of referrals; densest citer - high-sensitivity detector |

Not measured: Meta AI (35% of AI users; lives inside WhatsApp, no collector) - manual sub-sample if feasible, reported separately; Grok, DeepSeek, Claude, Le Chat (each <=6% of AI users; no consumer-surface collector with citations, or Claude measuring Claude).

## 2. Design

- **Cells:** 10 questions x 5 surfaces = 50 cells. **Repetitions:** N = 10 per cell per wave -> 500 answers per wave.
- **Run granularity:** one collection run per (surface x repetition), each run holding the 10 different questions in an order shuffled with a logged seed (identical queries inside one run are de-duplicated by the collector; different questions are not). 50 runs per wave. Provenance per answer = `run_id` + dataset row index + `dataset_id`.
- **Spacing:** repetitions of the same surface start >= 10 minutes apart, so N samples stochasticity across the wave window, not one instant.
- **Waves.** Planned as Saturday 19 and Sunday 20 September 10:00-16:00 CEST; not executed then. **Actual: Wave 1 on election day, Sunday 20 September 2026, evening (polling stations closed 18:00 CEST; results counting under way).** A second wave on the morning after (Monday 21 September) is optional and would measure whether the published result changes the sourcing; it is decided and logged before it starts.
- **Execution path:** the API of the collection service with the account's token (runs appear in the account's run list); the collection script records every run in `<wave>/ledger.csv`, saves each dataset untouched to `<wave>/raw/<run_id>.json`, and keeps `<wave>/live.json` for the live run board.

## 3. Classification - locked before any wave result is seen

- **Unit:** registrable domain of each cited URL. Answer text is stored, never scored for truth in the primary numbers.
- **`ru_state`:** EU Council Regulation 833/2014 Annex XV broadcasting-ban list (consolidated 2025-07-20), domain map `lists/ru_state_domains.csv` (RT DE mirrors rtde.tech/.live/.site, SNA snanews.de included). **`ru_network`:** VIGINUM Portal Kombat list of 2024-12-27 (incl. `deutsch.news-pravda.com`, `germany.news-pravda.com`) and CheckFirst's Pravda/Wikipedia data (incl. `pravda-de.com`). These two lists are frozen with this protocol; hashes in `lists/CHECKSUMS.txt`.
- **German-side descriptive categories** (not used in headline numbers 1-3): `de_authority` (federal bodies: rule `*.bund.de` plus a sourced domain map; Land governments, parliaments and election authorities; EU institutions `*.europa.eu`), `de_public_service` (ARD, ZDF, Deutschlandradio, DW and joint offerings), `de_media_accountable` (media under the Deutscher Presserat complaints procedure via the published lists named in `lists/README-de.md`). Everything else is `other`, described in a separate annotation layer, never scored.
- **Storm-1516 layer.** One-off clone sites are not on any frozen list; a citation is coded `storm1516_narrative` only when a published fact-check (CeMAS, Correctiv, dpa, Gnida Project) ties that page or domain to the campaign. Reported separately.
- **Secondary narrative layer** (does the answer affirm the loaded premise?): coded by Claude, 20% human spot-check, labelled subjective, never in the primary numbers.

## 4. Procedure

1. Freeze: SHA-256 of `PROTOCOL.md`, `study.json`, `questions.csv`, `lists/ru_state_domains.csv`, `lists/viginum_portal-kombat_domains_20241227.csv`, `lists/checkfirst_pravda_wikipedia_results.csv` -> `RUN-LOG.md` with UTC timestamp, before the first wave run.
2. Wave: the collection script runs `wave1` (resumable: SUCCEEDED (surface, rep) pairs are skipped on restart). Failures are re-run under a new `run_id`; the failed run stays in the ledger.
3. Completeness: 50 runs SUCCEEDED, 500 rows expected (a query with no AI Overview on Google's side yields 9 items - denominator recorded, supplementary single-question runs allowed and marked SUPPLEMENT).
4. Pipeline: `ingest.py` -> `resolve_goto.py` (Google /goto tokens via 302 Location, target pages never fetched) -> `classify.py` -> annotation -> `profile.py` -> `verify.py` (must print VERIFY: OK; recomputes the headline numbers from `responses.jsonl` and the frozen lists only).
5. Provenance package per wave: `ledger.csv`, `raw/`, `runs-export.json` (account run list for the wave, kept by the author), `CHECKSUMS.txt`, `RUN-LOG.md`, screenshot of the account run list.
6. Manual Berlin sub-samples (Google signed-in, Meta AI), if Chrome is available: 10 questions x 2 repetitions, full text, sources, screenshot, UTC time, `MANUAL-*` identifiers; reported separately, not in the headline numbers.

## 5. Outputs - each number with its denominator

1. Answers citing >= 1 `ru_state` / `ru_network` source, per surface and in total.
2. Share of all citations (and of unique domains) that are `ru_state` / `ru_network`.
3. Answers with zero citations.
Also: answers citing >= 1 German authority or public-service source; per-question profile (which voids were filled, by whom); outlets carrying a documented narrative with Tier A/B evidence (published contacts with Russian state media vs narrative match only); citation stability across repetitions (Jaccard).

## 6. Declared limitations

The collector runs from data centres, not from Germany (language is the only locale lever; Google UI boilerplate language is recorded as proxy-locale evidence). Loaded questions model a confirmation-seeking user. The collected surface ~ consumer UI, not identical (fresh anonymous session). Citation is not influence. Snapshot on election evening, not a trend; the planned Saturday baseline was not run, so no within-election delta unless Wave 2 is run. Attribution lists are incomplete: `other` is not "clean". Copilot is reached through a collector from a third-party developer.

## 7. Budget

[removed: account cost data]

## 8. Reuse

`study.json` + `questions.csv` + `lists/` define a study; `scripts/` are study-agnostic (surfaces, question column, list files and wildcard rules all come from `study.json`). A new country or topic = a new folder next to this one.
