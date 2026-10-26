# Wave 2 - the same questions put to Perplexity again (7 October 2026)

## What was run and why

- In wave 1 (20 September 2026) Perplexity cited Russia Today in 20 of 100 answers.
- On 28 September 2026 Perplexity stated that all relevant domains associated with Russia Today and the linked outlets were blocked. The statement is published with the study: https://dosimeteraudit.org/research/election-day-ai-poisoning-germany
- Wave 2 puts the same questions to Perplexity again and counts the sources of the new answers.
- One platform only. The other platforms of wave 1 were not asked again.
- The same ten questions in German (`../questions.csv`), ten repetitions, 100 answers.
- The first repetition started on 6 October 2026 at 23:41 UTC (Coordinated Universal Time), which is 7 October, 01:41 Berlin time. The last one started on 7 October at 03:14 UTC (05:14 Berlin time).
- Repetitions 2, 3, 4, 8 and 9 started ten minutes after the one before, to within one second. The gaps before repetitions 5, 6, 7 and 10 were about 33, 17, 71 and 42 minutes, and the reason was not recorded.

## What is published

- `responses.jsonl` - one row per answer: wave, platform (`surface`), repetition (`rep`), place of the question in its repetition (`row_index`), start of the repetition in UTC, cut to whole seconds (`run_started_utc`), question, answer text, and the sources in the order they were returned, each with position, title, address and domain.
- `answers_classified.jsonl` - the same rows with the list category of every source and the flags computed from the categories.
- `domains.csv` - the cited domains with their category.
- `RESULTS.md` - the figures.
- `scripts/classify.py` writes the last three files from `responses.jsonl`, and anyone can run it again.
- `CHECKSUMS.txt` - SHA-256 of the files above, of `RAW-CHECKSUMS.txt` and of this README.
- `RAW-CHECKSUMS.txt` - SHA-256 of the ten raw exports, one per repetition (`raw-01.json` is repetition 1).

## What is not published

The ten raw exports and the run records stay with the author, because they carry data of the account used for the collection.

What this means for a reader:

- A reader can check that the published files are unchanged and that the figures follow from `responses.jsonl`.
- A reader cannot check that `responses.jsonl` matches the raw exports. The values in `RAW-CHECKSUMS.txt` fix the content of the raw exports from the day of publication on. They can be compared only if the raw exports are shown later, and they carry no outside time stamp.
- Before the files were written, `scripts/publish_wave.py` compared every question, answer text, source title and source address in the rows with the raw exports. This is the author's own check and a reader cannot repeat it.

## Check the numbers

```
cd germany-2026
python3 scripts/verify.py wave2
```

The script checks the SHA-256 of the published files against `CHECKSUMS.txt` and recomputes three figures from `responses.jsonl`, using only the frozen lists of Russian state media and of the Pravda network. It compares them with `RESULTS.md`, prints that the raw exports were not checked, and ends with `VERIFY (raw exports withheld): OK`.

## Figures

| measure | wave 2 | wave 1, Perplexity only |
|---|---|---|
| Answers citing Russian state media or the Pravda network | 0 of 100 | 20 of 100 (all Russia Today, rt.com) |
| Citations to such sources | 0 of 1,000 | 25 of 2,673 |
| Answers without any source | 0 of 100 | 0 of 100 |
| Sources per answer | 10 in every answer | 18 to 41 |
| Unique domains | 60 | 128 |
| Answers citing at least one authority or public-service source | 80 of 100 | 90 of 100 |

- The first three rows are the figures that `verify.py` recomputes.
- The last row is descriptive. It comes from `classify.py` and uses the authority list as amended during wave 1 (amendment A2 in `../RUN-LOG.md`).
- None of the seven outlets on the watchlist (`../lists/de_outlets_narrative_watchlist.csv`) is cited in wave 2. In wave 1 Perplexity cited two of them, nachdenkseiten.de and anti-spiegel.ru, each in 10 of 100 answers.

## Limits

**1. The two waves show source lists of different length.**

Every wave 2 answer shows exactly 10 sources. Wave 1 answers showed 18 to 41. In wave 1 Russia Today stood below the tenth source in 15 of the 20 answers that cited it, so a list cut to ten sources would remove it from those 15 answers without any blocking.

Comparing only the first 10 sources of every answer:

| source | wave 1, any position | wave 1, first 10 sources | wave 2 |
|---|---|---|---|
| rt.com (Russia Today) | 20 of 100 | 5 of 100 (all in question 10) | 0 of 100 |
| nachdenkseiten.de | 10 of 100 | 10 of 100 (all in question 7) | 0 of 100 |
| anti-spiegel.ru | 10 of 100 | 0 of 100 | 0 of 100 |

- The comparison that holds for Russia Today is 5 of 100 answers in wave 1 against 0 of 100 in wave 2.
- In the ten wave 1 answers to question 7, Russia Today stood at position 11. For these answers, and for anti-spiegel.ru, the two waves cannot be compared.
- The numbers come from the `position` of each source in `../wave1/responses.jsonl` (Perplexity rows) and in `responses.jsonl`.
- It is not known why the list is shorter. The platform may show fewer sources now, or the collection software, which had a newer version in wave 2, may return fewer. The files cannot tell which.

**2. The blocking itself was not measured.**

The statement by the company is the only source for the blocking. Wave 2 shows that Russia Today is not among the sources of these 100 answers. It does not show why.

**3. The sample is small.**

One platform, ten questions, ten repetitions, one night. Wave 2 says nothing about other questions, other days or the other platforms.

**4. The requests did not come from a browser in Germany.**

As in wave 1, software sent the requests from data centres. The country was not recorded.

**5. The new answers cite this study.**

In all ten answers to question 4, the second source is the German report of this study (a PDF on gurovdigital.com). Wave 1 had no such source. The page is on no list and changes no figure, but the repeat measurement partly reads the study that led to it.

**6. Nothing was frozen again for wave 2.**

- The protocol was frozen with SHA-256 hashes before the first request of wave 1.
- Wave 2 uses the questions, the lists and the counting script (`scripts/classify.py`) of wave 1. The questions, the three lists of Russian sources and the counting script still have the hashes of the freeze entry in `../RUN-LOG.md`.
- Wave 2 has no freeze of its own and no outside time stamp, and its entry in the run log was written after the run.
- The optional second wave named in `../PROTOCOL.md` (the morning after the election) is a different one. It was not run.
