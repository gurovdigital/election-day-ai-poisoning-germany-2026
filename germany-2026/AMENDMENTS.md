# Amendments

## Version 4

Version 4, October 2026. Technical identifiers removed. The measurements, the counts and the findings are the same as in the earlier versions.

`python3 scripts/verify.py wave1` gives the same output on versions 3 and 4, line for line, and ends with `VERIFY: OK`. `python3 scripts/verify.py wave2` does the same and ends with `VERIFY (raw exports withheld): OK`.

Files in this package that changed in version 4 (paths relative to `germany-2026/`):

| File | SHA-256 before (version 3) | SHA-256 after |
|---|---|---|
| `FINDINGS.md` | `3a07f130ac201f6a7bb3268976ffc7505aec54f012e3a85abfb64fc154043129` | `7be64ccff1b656f8485d581aeb574e360f4733774c2a0cc327f8d990fffab3a6` |
| `PROTOCOL.md` | `c4317cd809b24474d0a94fc286652edfaa521eb51f2cef47c767a4fc0cd346f1` | `993f8f84618cdae7ac1a16aa13da16a2c03f9f3b45f324749187c5db75dd0944` |
| `README.md` | `dc46ed427dbbae91415aaa62a38bcba80e39c01c430c2d66d03b12eb2691d0a7` | `dfcfa0718a0d5f8773f46d374f9040bc37e0765a78f271bc4a888068ea1f6222` |
| `RUN-LOG.md` | `17824a82156a39d0bcfebd247d33d5a39d6682cf3d3e3e7b050104398d3e7cd6` | `95bc2d63a8a2072c17592a2896ba6b74884723df6003d8c9dc409ff2f4639fa4` |
| `pilot/answers_classified.jsonl` | `45b02d3a2e496759bfecd4d9bcecdc8ca23a5e23b00c57c6c6c2d7aec326835c` | `9531aa0fb7c38b785a68631d68aef2c57defc1b66289e8e7463afb116f657c47` |
| `pilot/ledger.csv` | `039bd0cfbf2428913d0ca9522f9cb39d322289b92c32fd4e1197ac1db19b09fd` | `6fa1ad9431537d7c746de5d131bcaf261b7d60360c357520dcd18b7bed52ce7d` |
| `pilot/responses.jsonl` | `30af4b7acc5e171f063a8c1ca7a98674a93325dd3809c35365c7df5efc76b4c3` | `69a85861f619b420559fb1212ea51287160f2f2eb5778708dd20636892e30792` |
| `scripts/board_merge.py` | `638554927d809d142dfa744dd338a4c2408b224d539631d04b14868effa319c2` | `c740e1740801729a10ed551882c32c40272baafe367d355b4f0ee01eca52e98e` |
| `scripts/ingest.py` | `a92c1395ed39f977042ce93241f727051c4798c6b0f77a12342ebf0121513009` | `68ce92b7a6507dd418b04109fbe3e9b5c4321d4dedb04a6ac0b2c318aa9642ad` |
| `scripts/run_wave.py` | `d476e9c9ee91c56a41b3e5479f35df2adf3bf62adab8dede36544393d31e55fa` | file removed |
| `scripts/supplement.py` | `ef008fef12e8dc47b8a2f743fc7f9fe56e906fe2fc6837f08fc46b049d2a2f22` | file removed |
| `study.json` | `4a173de342340c5049d9fb67676a6300c186d9915474d7ac27c241ec14951e10` | `f9f714120bf8185f9f444672c950aa57d6695d32ede85c89a9b63e3e56ee9efb` |
| `wave1/answers_classified.jsonl` | `2fd35f913fac4b4f51e87a6e971c3611a64b7fc5bf497a5e7ffabd8e9a3137e0` | `c2ac13adc2bae0a4e8145bdb0cf5fa8ecac009be489f0066d697945dd83851c9` |
| `wave1/ledger.csv` | `4a36b5448da5b3f1ed5d1ff0719a92358eba47096dc25ce41e632f04ae9ac42c` | `2f604e685c716ae927806f54818b59e111414d7a1f229895a0b5ee33a6017f8a` |
| `wave1/responses.jsonl` | `731ecf620de003396bb217e2f47a927cbd797117a3d6170f814677671f61b1b4` | `871ce3e132f3ff58333b8b6c05050998cf022ba3fcc6e55876d9297186472d55` |

Files in the repository outside this folder:

| File | SHA-256 before (version 3) | SHA-256 after |
|---|---|---|
| `CITATION.cff` | `820eb90e61305e6c44bdcda63fa92199451f1e37b1754db90483f53634f479df` | `8a1d9d540b6b0b614e74faf62de69e8a079a8057000448aa0100ff16fa5b8fc1` |
| `README.md` | `8a470477d37ebb3e6fdb40fc1f78064e77fde98e80dc413cc2e22395021f8a42` | `b571732e840cad3cf03ab462d7b73fa6a5d43dad9fe7625fd2bb227d8c716dbd` |

## Version 3

Version 3, October 2026. This version follows a stricter security and compliance standard. The measurements, the counts and the findings are the same as in the earlier versions.

This file is new in version 3. It lists every file that differs from versions 1 and 2.

### What we changed

1. We removed one file with network diagnostic output: `wave1/manual/rt_access_check_20260922T2333Z.txt`. The result it supported is stated in `RUN-LOG.md`, entry C3, and stays as it is.
2. We removed account cost data and account console links:
   - `PROTOCOL.md`: one value in line 3 and the text of section 7, which now reads `[removed: account cost data]`;
   - `wave1/ledger.csv` and `pilot/ledger.csv`: the two columns with the cost and the console link of each run;
   - `responses.jsonl` and `answers_classified.jsonl` in `wave1/` and `pilot/`: the cost field of each row;
   - `wave1/run.log` and `wave1/supplement.log`: the cost and the link at the end of each line, and the cost total in the last line of `run.log`;
   - `README.md`: the word "cost" in the description of the ledger and the sentence with the console address.
3. We replaced a local file path in `scripts/run_wave.py` and in `README.md`. The script now reads the path of the token file from the environment variable `STUDY_TOKEN_FILE`.
4. We changed four scripts so that they no longer write the cost and the console link: `run_wave.py`, `ingest.py`, `supplement.py` and `board_merge.py`. They write the same files as before, without these fields, and `ingest.py` runs on the ledger of this package.
5. In the saved copies of third-party pages and in the CheckFirst list we replaced each third-party e-mail address, IP address and API key in place with a marker: `[removed: e-mail address]`, `[removed: IP address]` or `[removed: API key]`. Nothing else in these files changed. In `lists/checkfirst_pravda_wikipedia_results.csv` the markers are in the column `user` only; the column `domain`, which the scripts read, is the same.
6. We updated the SHA-256 lines of the edited pages in `lists/CHECKSUMS-de.txt` and added an entry to `RUN-LOG.md`. The freeze hashes at the top of `RUN-LOG.md` are kept as they were written on 20 September 2026.
7. `scripts/verify.py` is the version that runs on Python 3.9. It has been on GitHub since 24 September 2026; the earlier archives on Zenodo held the first version.
8. From version 3 the scripts are licensed under `MIT OR EUPL-1.2`, at your choice. The data and the documentation stay under CC BY 4.0. The licence texts are in the repository (`LICENSE-MIT`, `LICENSE`, `LICENSE-DATA.md`).

Run ids and dataset ids are unchanged. They are the provenance of each answer.

### How we checked that the figures are the same

We ran `python3 scripts/verify.py wave1` on the files of version 2 and on the files of version 3. The output is the same, line for line:

```
[1] 64 raw exports hash-verified: OK
[2] ledger runs: 64 (SUCCEEDED 64); runs in responses: 56; rows: 492; per surface: {'copilot': 100, 'gemini': 100, 'perplexity': 100, 'chatgpt_search': 100, 'google_ai_overviews': 92}; runs with <10 items: ['6W33tOdevcMJnkJse', '7AfAf1bh89zA1FKcc', 'ByN0qGWTHPVw2Q9oI', 'EymlH9VVmYKFt4Hs7', 'FgxPjCeGFT0Lv6YID', 'Hlr8Xwtb6efoyHgF1', 'L55TjfbYFqJoVj1s6', 'LnUWvnw7hN4d0TGD8', 'OOy1WQAqBecFfcsoz', 'cjLGlyLJA9cE5wh6J', 'gzICasszt9eU2iEO6', 's5J95j9oUyG66NVpR', 'sbzMxV6FcAzTJWMnF', 'tuJPC8FctNV5uR1xn', 'zggHWaeiRURO2ZzFx']
   runs that legitimately returned 0 items (no AI Overview on Google's side): 8
[3] recomputed: (1) answers citing ru_state/ru_network = 20/492; (2) ru citations = 25/4819, ru domains = 1/263; (3) zero-citation answers = 17/492; .ru/.su/.by flag = ['anti-spiegel.ru', 'interfax.ru', 'kremlin.ru']
[4] RESULTS.md headline fractions found: [('20', '492'), ('25', '4819'), ('1', '263'), ('17', '492')]
VERIFY: OK
```

We also ran `ingest.py`, `classify.py`, `annotate.py` and `manual_summary.py` on both versions. They produce the same result files. The only difference is the removed cost field.

### Files in this package

Paths are relative to `germany-2026/`. 72 files changed and 1 file was removed. "SHA-256 before" is the hash of the file in versions 1 and 2.

| File | Kind of content removed or changed | Count | SHA-256 before | SHA-256 after |
|---|---|---|---|---|
| `PROTOCOL.md` | account cost data | 2 | `019eb908f5139e29e7290c8895ccf7d3d1cd28dc44d74b2746febcc9a3953ff4` | `c4317cd809b24474d0a94fc286652edfaa521eb51f2cef47c767a4fc0cd346f1` |
| `README.md` | account cost data; account console links; local file path | 1; 1; 1 | `defe0aa98551e9708cd662d96cbdb53e3e90488ee320a31e20742155563f466d` | `bb4b91ccab50e3140c739720943308dcdd2001b801511f6691bb3cb8ccd70b9a` |
| `RUN-LOG.md` | amendment entry added, nothing removed | 1 | `6ee45da658a9de8076d5f0ee3e79dbd9fa9ad2e0f258b89b3d4d1127ac37fe27` | `4a1c2d79f865671e46ca6536748e64755dbff811f7c71b98d270074f507f795e` |
| `lists/CHECKSUMS-de.txt` | checksum records updated | 53 | `81ee533401c1252a98e86c4b018c05338a4546360de4778fd005f47b81ab9fad` | `9f688924a0f5388d2e27e357c082be4495b57a68ddbace5c30774913fc346db7` |
| `lists/bva_domainverwaltung.html` | third-party e-mail addresses | 5 | `196ef35cba8537b0e3b75657c9b53fc3e5ce4ea5a8cea82f9869289cc3795735` | `b1b5459aab7fa46d74e6999381b8d2f03ded9ba21feb4f7cd4912dbec536e142` |
| `lists/checkfirst_pravda_wikipedia_results.csv` | third-party IP addresses | 140 | `7253e14ed9e67057f8f8e423cb1a33d0df0d24bfd01d55314324ace109d72559` | `73ddcfddf882a4b3338cdb73d7180f5603a25821fb341c4ac7b7a22b25a75f48` |
| `lists/presserat_selbstverpflichtung.html` | third-party e-mail addresses; third-party API keys | 5; 1 | `95ab92d3375d5795eb0b7f4ad73e9f7ab4611506ea3a4e1092dbde31ceecb9c8` | `f7d5ff84e2a81abb57b8e12ca716bde802930d78ab91855fc51070caba7bf5f1` |
| `lists/sources_impressum/3sat_impressum.html` | third-party e-mail addresses; third-party API keys | 4; 1 | `2e4e02d99e113706e0b461da743d43df4fddbcfe5d5b8d574d22a97d25127336` | `731e970a9921959b721a62d051849521edc963b71fa1ecaf358595dbca64591e` |
| `lists/sources_impressum/ardsounds_impressum.html` | third-party e-mail addresses; third-party API keys | 72; 1 | `50db2f3639cf3927162dbd1123b7e1bd3aba78ba6d4274ad2347256245e75db6` | `e1ec19ca2e50cb80c2945afa3b3166bab2236f57509107d1df06e9642d2aeb4e` |
| `lists/sources_impressum/br_impressum.html` | third-party e-mail addresses | 4 | `1ab97615c8bed3469ac6c139355b69c9e4374680aa543421c24c4fa54113298c` | `4ec0e4ea7619c3cb0508e8a2a8b1aa208cacfcf1b0b032b3e31968cc260ead5c` |
| `lists/sources_impressum/butenunbinnen_impressum.html` | third-party e-mail addresses | 2 | `227e5f145242a3d224713435abbe4c6b131109b813df5fe01530358047508aca` | `edb937afbe2d9ea04f860b3a4e4ea9b199a734dbd1f6b1eab3affe0576b9f3b8` |
| `lists/sources_impressum/butenunbinnen_impressum2.html` | third-party e-mail addresses | 2 | `b695b9f242417ff7971a03a85ac183f1a689a5352b798b98f4780e777684a24b` | `99d9dc0f338da3db364abc0f8fa5fd51612077a985f3281eb2d23197d16f53fa` |
| `lists/sources_impressum/daserste_ardmediathek_impressum.html` | third-party e-mail addresses; third-party API keys | 72; 1 | `f780f9c9401c92279357a45c82169e8abc6bc72a721473f19372938ee5690fea` | `e96eee12dd38e2dfa53e72cb7fe6378291ab2d9d8afee9301146c8f40420392f` |
| `lists/sources_impressum/deutschlandradio_impressum.html` | third-party e-mail addresses | 4 | `d70817c3232f89e42ba3761f4b96d220a557030109a82c6dd69d80bba19e7752` | `c7746cc8e48e87946eace306e71708c6caafbb426189c8616c87e8d1a6156bc9` |
| `lists/sources_impressum/funk_impressum.html` | third-party e-mail addresses | 8 | `4d62c7e55ea19d1e4477e523e52b73f89e8a141aab5f861f3737b790f7ec4356` | `b981b2942650270c650a327fb2714e4183f8470a2b42e9caca5834587986ca6d` |
| `lists/sources_impressum/hessenschau_impressum.html` | third-party e-mail addresses | 3 | `cdea36432e47d65639b4a068c4dce4e083061b5c33225c43c618cb2dc3621f53` | `0c33d7b650241aadc25d65e9aecaf8848a19f90f119168c89cbeaf475a454cad` |
| `lists/sources_impressum/hr_impressum_full.html` | third-party e-mail addresses | 3 | `cdea36432e47d65639b4a068c4dce4e083061b5c33225c43c618cb2dc3621f53` | `0c33d7b650241aadc25d65e9aecaf8848a19f90f119168c89cbeaf475a454cad` |
| `lists/sources_impressum/kika_impressum.html` | third-party e-mail addresses | 7 | `2c219a701ff7d2b4dddc7fde25b87ca095fff27b1998008953d16fea3288da67` | `f0043c564712a32a79382cfc94fb3cfd2e02f917cba49e5902bb5ebbf780bd91` |
| `lists/sources_impressum/rbb24_impressum.html` | third-party e-mail addresses | 18 | `6f654be00cc9328c8e1b216a915b3ef1d8d2ef2089daad6ca722a93f58fba4a8` | `0d37ecf8136bd14fe56e1ae5485acdb1b3b63cb51ddb0eda7262914bb81f064b` |
| `lists/sources_impressum/sportschau_impressum.html` | third-party e-mail addresses | 8 | `15fcbd44da85de5fbf358d02a464dddef4af54c687d452ba72b4e1fad196209a` | `31226b6b32ddf4d5b46dbded222ca28f4f97895d88f92949b3754a8b81d347f3` |
| `lists/sources_impressum/swr_impressum.html` | third-party e-mail addresses | 4 | `5f014fbffaafbec9ef4ca62f5b295de045ec8ee54e9f616ef90449bb4ac39db8` | `5cfb32fafbbd42affc7623e5d6bb44c25524e2c566e5bdd721f95c575afb892c` |
| `lists/sources_impressum/tagesschau_impressum.html` | third-party e-mail addresses | 6 | `e7531503b360ef7d901e0264e54143a9c6ee86c81be962db17b0cdad40edb8b6` | `6733b57a8629386d6acc0a3e59fefd325c521de96fdb98ae8a817b56e63bf631` |
| `lists/sources_impressum/zdfheute_home.html` | third-party API keys | 4 | `d496328d224b6c9881d2d0d20ca8f79398cd920c96408398cf52ab31b05f5012` | `53d471bcb52b8bb236c154c857fb62fe50b4a58639615abd3d4cadf9b565d376` |
| `lists/sources_impressum/zdfheute_impressum.html` | third-party e-mail addresses; third-party API keys | 26; 9 | `80b515d6822114bf45ab671d2981e2e17efe7b3c8cda63bc2be7fcc30fa9f810` | `731051e5bcaa30ec632ad05ccc7de21e336a8d5f3d7ba4fec5191aed70acf322` |
| `lists/sources_media/bdzv_entries/bdzv_die-welt.html` | third-party e-mail addresses | 8 | `8a3818d3f7e824c7531604fe6728d1580a7aa96e025ee719091a33c25db8fc0e` | `1bac1c0eae315d8287e387dbca1c308729bcf4dd2402950824679fd040307c15` |
| `lists/sources_media/bdzv_entries/bdzv_frankfurter-allgemeine-zeitung.html` | third-party e-mail addresses | 8 | `9a0f29c7549bc55456507bf7eaf7c875a911398bc1c4099a568c61076f842367` | `3611a3b5d91e47d0a768d039e6a98093ee10da0f602bb0f9df75608695afddc3` |
| `lists/sources_media/bdzv_entries/bdzv_handelsblatt.html` | third-party e-mail addresses | 6 | `eec800a362f73cd503cd40b5de9e3440d604f4a93f0fd84e9490f3d15289719b` | `d6d6ae04235a0b69a68faca176c3e392dcf0c9246fa42e5468930c88c1d9fda5` |
| `lists/sources_media/bdzv_entries/bdzv_leipziger-volkszeitung.html` | third-party e-mail addresses | 8 | `9b5b5ab9d592a27877bce4dee64a30dec82db638e60db9a43fc46553d2fc1f06` | `82017a666ef1b93837c6b2d3da5e4fbb3f932ff9c825bc407fbee138d5488032` |
| `lists/sources_media/bdzv_entries/bdzv_ostsee-zeitung.html` | third-party e-mail addresses | 8 | `d8347cb80896badf1c9b11717bf24aa7f5e0504f6438a0206a6b476089d723d1` | `9dab87c88113f40619eea1fa964c88443579aeac201ca0d805b86437823abfdc` |
| `lists/sources_media/bdzv_entries/bdzv_sueddeutsche-zeitung.html` | third-party e-mail addresses | 8 | `b43dce8af030843d755aafbfda17aabd23c9f788c0c22489ef4c559ac3807598` | `6be53b68f312c17b8187bef82277ec951795199263fba67c4fc7a2a5acb99f9b` |
| `lists/sources_media/bdzv_entries/bdzv_volksstimme.html` | third-party e-mail addresses | 10 | `4babf7896d8c8c2846ccc25b4d8afa4c380174909f65efd9197d2b500a5ced4b` | `23adbbdeeb5375fb97015152ace997c37a0ccbdabafc0e5edf21a8d33e1ec6ed` |
| `lists/sources_media/bdzv_mitgliederverlage.html` | third-party e-mail addresses | 4 | `044bf48e05847223bc22a999f741fb73fad5869104e6b6b38f6bb6561555ce6b` | `e5ba6106849b15bc95d9d04ce541dbbda23cb8840fe7efe2dfd9bbe9f79698c3` |
| `lists/sources_media/berliner-zeitung.html` | third-party e-mail addresses | 3 | `77c047d86297faf645039d4f0fe89d6f6210162a2f12119f4f9c1e9ab941d3f5` | `ccd62e6e2c122a66d0fdf0d255ba7b7abbf7752d44e2a8fe962760345cf04f63` |
| `lists/sources_media/bild.html` | third-party API keys | 1 | `a45e5c649b6ed1158360c58bd341c32bcd88dae584f98ee28f477d0be0c82fc8` | `e27a68906589e46ef819543ad5cb9a21fb093f83f805b139d8da48114060f823` |
| `lists/sources_media/faz.html` | third-party e-mail addresses; third-party API keys | 28; 1 | `659efef624760469c8c96eb8b6b94aa91060717303961c0a06a029e3f535e8b8` | `7b414a1ff265814f9afa82835e3b16ffc0cfdd32a46278bf533944c6edd6b6ab` |
| `lists/sources_media/focus.html` | third-party e-mail addresses | 12 | `dbb3333416ed8d6b6510a103ad91d20bf7be64240e641d2da8683f6fd478e73a` | `a6d98aa97e6af879d8d162a462387b3e49f4d36a1909f5155858750702f19769` |
| `lists/sources_media/fr.html` | third-party e-mail addresses; third-party API keys | 12; 1 | `1a847fcdca0ac2950a007219f5476d2912ec2f682fd1696e3a23e9e1a87a9439` | `b323e72188f425b8a9a325a2f43f98558729d28e4f5eb21d46f9e0925430676c` |
| `lists/sources_media/handelsblatt.html` | third-party e-mail addresses | 33 | `d084e8e97465a86b7c74bbe1dd4bc4bade912dd92b0dc391cdb9722a3f49892f` | `f4bb44b20c2d997b4719a2dd1f75052291b413989163c198e6bc5b89368c03c4` |
| `lists/sources_media/joyn_impressum_prosieben-domain-confirm.html` | third-party e-mail addresses | 46 | `1726ffbf1d52c7dc8e36793138f0a1e5268f86574ba66868f421ff9234067a18` | `12fc8459af91e22c208db32e5a74670856b44084e3fbc60b08a2a665a0c8af72` |
| `lists/sources_media/morgenpost.html` | third-party e-mail addresses; third-party API keys | 14; 1 | `f2be9a1f5d49749e840236fcd61856659d2d99e1a56ab99decbface650162ac5` | `918a294065e592c8bdbf5942791b2650acb8dd0e19b3b9818e477dfe49e73858` |
| `lists/sources_media/mvfp_F.html` | third-party e-mail addresses | 2 | `c8034422867b87ddd238c7e47bb0e5389a5e40895be15a1d4789696744a501c4` | `ec624cbf6e9503b1b991eb2d0f991fe1976dc65bf2c6618a8e6570c21d332d9e` |
| `lists/sources_media/mvfp_S.html` | third-party e-mail addresses | 2 | `2b2e0275e027da99e71e93a85bf09ecf9768c31f928517be96bf8c9ba18e34cb` | `5642f5204d1ef5ca7585aee94a60f70238d270b07f67d5c6734d7e825cd0f09d` |
| `lists/sources_media/mz.html` | third-party e-mail addresses | 12 | `8a1bc424ed49b11bf918e5dae9fae71269653bd2dd3fc1c0ab4357e5c64a697e` | `c67e5d0aa42475a7817604ffcf54685d12bfe391db6fff9c825a6d734939a12f` |
| `lists/sources_media/nordkurier.html` | third-party e-mail addresses; third-party API keys | 4; 1 | `41595ca42cfb218ece677a6860d2bb9febbe0f15b85499edd9b8c58cd045107b` | `0863ee883e41911562b4e2765b6447f90ab57db661c6833abaeea11deecfa240` |
| `lists/sources_media/reuters_dnr2025_germany.html` | third-party e-mail addresses | 2 | `73e4260914bab56949699d0168f54fc87d757be62c1b82c8b43dc834abc2c94d` | `6730693ab73e4f0a7a08e026bc626c3527eb7b12bd8e6da0798e2fc56aa52739` |
| `lists/sources_media/rtl.html` | third-party e-mail addresses | 70 | `2a1bd497a3e6513156d76c732b1866a57ba266370a96c7de5e987dae9da7618b` | `253f820462d16e2750650e26994345811b7f26c68716448af000b5c25f8607a2` |
| `lists/sources_media/stern.html` | third-party e-mail addresses | 43 | `6e3b76b763a215889b41c7d9743c6c69de9bc625778d34be98b0982c590bd54a` | `593584c8c25a42b52cd19657a9d0152ac7cff1fed42bab974f425f63934012cf` |
| `lists/sources_media/sueddeutsche.html` | third-party e-mail addresses | 22 | `84039f1e606cab652d27a517d97508db8b49cd3dba80269e4f135abdd3eaba50` | `a6fa52e57d9f5f5c23f53592b6454fd3e85a4481b705d7105c53dae1313e9e7d` |
| `lists/sources_media/t-online.html` | third-party e-mail addresses | 22 | `1cc7447cc2a0e5e1cf071fc783df0376ddf0443a391eccf237f5db0511e503e7` | `eaeeaf104e238c03c477249a3abda15cdd0e1e5ffdc621952aeed737cb8ec37a` |
| `lists/sources_media/tagesspiegel.html` | third-party e-mail addresses | 13 | `cf2a3d791813e61c5d494f31d4d7250232e335fac596cabbd7a20cc0cc3cc12f` | `77c67c70909ec431f7412b300d8c9abdd479b9bf1522c74c6817994ac3524260` |
| `lists/sources_media/taz.html` | third-party e-mail addresses | 5 | `cf6889d61c570744dac122630e7294d650c110a18709b22e83eae15d659e5bd4` | `7372e30bb25e635415bcbcbe8032aba80ed56d19eac23774f7ee0f68561223dd` |
| `lists/sources_media/volksstimme.html` | third-party e-mail addresses | 10 | `86d29171ae4282316e5818817975bedb131f940f0148455fa0a271357e050d5d` | `418e34ff85aa5e82221d1fc6ce13943360ec250ab8e76eaf01527ecf2c06a3af` |
| `lists/sources_media/welt.html` | third-party e-mail addresses | 58 | `3c9c6cdb5cb81d443a3b3bc763e45535a601950f3470e252b4791a508da2562a` | `349713be61a39527470dc4e3210b25ee65b25cb08ed028f5429b0108da3be01f` |
| `lists/sources_watchlist/cemas_telegram-rt-ukraine.html` | third-party e-mail addresses | 7 | `557bdc9c5181d35ccf4170791fc81af29c040e4df43ffc71108fc0235aa21587` | `ff667423789320e326a15e5d6ffe54636da2ba0ba5d652a128af147a29e7cb0c` |
| `lists/sources_watchlist/correctiv_report24-wochenblick-2021.html` | third-party e-mail addresses | 5 | `4fe37a4c71a45f1f898918f434d4a18199d464f23b689db4e3ca439a82303ff9` | `6fe2a273556cf1a9a0912816664123aa8402e483c5a975819bc5fd110212a12f` |
| `lists/sources_watchlist/correctiv_storm1516-german-election-en.html` | third-party e-mail addresses | 4 | `a119b092451e26821c69efba53c336c3db951547eecd4bb051db9809ac29af81` | `14457e749da624f1b1a023185a7ce38a44d41ad30c6ff98945dc480415a122d1` |
| `lists/sources_watchlist/laender-analysen_ra456_alternative-medien-kreml.html` | third-party e-mail addresses | 2 | `4896d316abcb1d9fc238096c2664919efb56db39bac8a008874191c52fd18ebe` | `e680e89f6c87fe8aab0758dc043878f4882b3a9c39fd70794739c62871072b2a` |
| `lists/sources_watchlist/medienwoche_weltwoche-putins-nuetzliche-idioten.html` | third-party e-mail addresses | 2 | `919d14494875a74bdaec25d0f0bcc216f3a1efcaf4cb0e63315faee28c1a5cf5` | `4788648ff9ef6313d807db26b46b68c8380acb5858d34c9b22dddee6918474ff` |
| `lists/sources_watchlist/nachdenkseiten_author-15_warweg.html` | third-party e-mail addresses | 3 | `8629abb27392c9aa5b4f3933d2092fe0deeb236eaeb61057c3ad96437644ee39` | `dcc7256decf33d56c827eb82d69e1b9529f92920a3626c81e2c86a94c80d32ed` |
| `pilot/answers_classified.jsonl` | account cost data | 1 | `118d22dea61919fa1d7db3f90a18ac28cfaaf3065ec5982c948bcc547219e7ab` | `45b02d3a2e496759bfecd4d9bcecdc8ca23a5e23b00c57c6c6c2d7aec326835c` |
| `pilot/ledger.csv` | account cost data; account console links | 1; 1 | `536cb6876e40fde2be71d2957ec79c8da42be289d9632b0e8bbd984e181e0116` | `039bd0cfbf2428913d0ca9522f9cb39d322289b92c32fd4e1197ac1db19b09fd` |
| `pilot/responses.jsonl` | account cost data | 1 | `9c5e4c456cf65a87016706d0d17610d8269ea17e4950cb2b04f677d4f81db4b5` | `30af4b7acc5e171f063a8c1ca7a98674a93325dd3809c35365c7df5efc76b4c3` |
| `scripts/board_merge.py` | script code that wrote account cost data and console links | 1 | `d5794f588af2cd28149899c776f49760e50c8e774324de18914f3efa5651862b` | `638554927d809d142dfa744dd338a4c2408b224d539631d04b14868effa319c2` |
| `scripts/ingest.py` | script code that wrote account cost data and console links | 1 | `965972d489a1e40a88cb7cbad420a46c9a011c9f8afbea87fe36cd16be0d4ecf` | `a92c1395ed39f977042ce93241f727051c4798c6b0f77a12342ebf0121513009` |
| `scripts/run_wave.py` | local file path; script code that wrote account cost data and console links | 2; 9 | `63138a126cea5950ea3264bc78c7d596443ad62e5cb93042ceffd295f70c0aad` | `d476e9c9ee91c56a41b3e5479f35df2adf3bf62adab8dede36544393d31e55fa` |
| `scripts/supplement.py` | script code that wrote account cost data and console links | 1 | `99f81b30c5624f552029d625995e70e367e77a27d2f6915cabf05f59324094af` | `ef008fef12e8dc47b8a2f743fc7f9fe56e906fe2fc6837f08fc46b049d2a2f22` |
| `scripts/verify.py` | nothing removed: the version that runs on Python 3.9, on GitHub since 24 September 2026 | 0 | `2449a2e2a5fe689c29a19e739af5cf1940fa2e088ea2d0df103a11f72d2a298a` | `141bdf3f96ac4a6b57853a8f47361988c4bcb64393e41cbc96e351a7377ec8db` |
| `wave1/answers_classified.jsonl` | account cost data | 492 | `a8bccc7646749edb3371a459d29d31f2a120b8bf3da1e8eca3ff7213f33cdad8` | `2fd35f913fac4b4f51e87a6e971c3611a64b7fc5bf497a5e7ffabd8e9a3137e0` |
| `wave1/ledger.csv` | account cost data; account console links | 64; 64 | `4dade33bd7114e61ba7f29a83111ae8697cfffa67befb135f5ff1ea1137f7c43` | `4a36b5448da5b3f1ed5d1ff0719a92358eba47096dc25ce41e632f04ae9ac42c` |
| `wave1/manual/rt_access_check_20260922T2333Z.txt` | network diagnostic output | 1 | `d48de12ff157a4c7335e7e3221eae9ed2dec9f6e336fed6cacefa44c8652a7ec` | file removed |
| `wave1/responses.jsonl` | account cost data | 492 | `c46fbabe70caf0d29287d9c7f68bd199591f47cd75578aa571ae8817a606d26a` | `731ecf620de003396bb217e2f47a927cbd797117a3d6170f814677671f61b1b4` |
| `wave1/run.log` | account cost data; account console links | 51; 50 | `eee599898f30aa37290d1e411264199f330fc662528612c20cf52d6282add716` | `d4b6fc4524fdfb32ce53b5792e5b38d830d9a2cebc524289193990efc9f50281` |
| `wave1/supplement.log` | account cost data; account console links | 14; 14 | `f9784154b07031c4002781f31931df5c7004ee3fd6bddfe1db8308f633fb6950` | `58b8b1b92e8a392feb836c06b3c3b47e5b05615b3a859bbcf96db12099f371ed` |

### Files in the repository outside this folder

| File | Change | Count | SHA-256 before | SHA-256 after |
|---|---|---|---|---|
| `CITATION.cff` | licence list, version number and release date updated; nothing removed | 3 | `bf8b05e8095ec80aec01b3d8cadc00314032759df1306cb8cab006f8fbf6387d` | `820eb90e61305e6c44bdcda63fa92199451f1e37b1754db90483f53634f479df` |
| `LICENSE-DATA.md` | licence sentence updated; nothing removed | 1 | `c91071de95a6c6e18551bb6b9bab63290fa3782d90991d6fa1beaffea0b3cae9` | `dc7ad3c2ecba228412d11eeba6f63bb7a67cbde1421e97e71aa339ea2203124e` |
| `LICENSE-MIT` | new file: the MIT licence text for the scripts | 1 | new file | `12626fe7823ff13075d266b88584bf81f75e4935d24f43af5a126a3c1c32a109` |
| `README.md` | version note added; licence sentence, archive paragraph and version number updated; nothing removed | 4 | `a06a47d4881b243d3deba5f60c1c339a79824d81563bfa15766229c2df1cb0e6` | `c4cdb340b7ce538bd068c08f4d0f813f3ee38aadbd5b861f54370f20fd91fb11` |
