# Primary-Source Verification Report — Training Scaling Laws Lecture

Compiled 2026-09-16. All fetches performed 2026-09-16.

## ACCESS CONSTRAINTS (affect what could be verified)

- `openai.com` **HTML pages** return `HTTP 403` with `cf-mitigated: challenge` (Cloudflare bot challenge) from this environment. Only `/robots.txt`, `/sitemap.xml`, `/news/rss.xml` are served. `web.archive.org` is unreachable (connections time out). Therefore **no OpenAI blog *body text* could be read directly**; where a quote is given it is marked secondary.
- `nytimes.com`, `podscripts.co`, `apple.com/podcasts`, `dwarkesh.com`, `snipd.com`, `muckrack.com`, `archive.today`, Google/Bing/DuckDuckGo/Brave web UIs are all unreachable or blocked. Reachable: `arxiv.org`, `storage.googleapis.com`, `deepmind.google`, `cdn.openai.com`, `openai.com/*.xml`, `arcprize.org`, `epoch.ai`, `anthropic.com`, `theverge.com`, `the-decoder.com`, `techcrunch.com`, `siliconrepublic.com`, `gigazine.net`, `36kr.com`, `mixed-news.com`, `neurips.cc`.

---

## TASK 1 — Silver & Sutton, "Welcome to the Era of Experience"

**Canonical URL — VERIFIED (primary; live document, author-hosted on Google DeepMind's media bucket)**
`https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf`
Fetched 2026-09-16: HTTP 200, 226,196 bytes, PDF v1.5, 11 pages. Authors on p.1: **David Silver, Richard S. Sutton**.

**Date — VERIFIED (primary, file metadata only).** `pdfinfo` reports `CreationDate: Thu Apr 10 23:30:54 2025 CST` and identical `ModDate`. **No publication date is printed anywhere in the document**; there is no dated announcement page. Caveat to state on a slide: "PDF metadata dates the distributed file to 10 Apr 2025."

**No canonical landing page found.** `https://deepmind.google/discover/blog/welcome-to-the-era-of-experience/` → **HTTP 404**. A grep of `https://deepmind.google/sitemap.xml` for `era-of-experience` → **0 matches**. It is **not on arXiv** (no arXiv listing found; arXiv:2508.05619 cites it only as "Preprint", MIT Press 2025).

**Status footnote — VERIFIED (primary, verbatim, p.1):**
> "This is a preprint of a chapter that will appear in the book Designing an Intelligence, published by MIT Press."

**Scaling quotes — VERIFIED (primary, verbatim from the PDF):**

1. > "In key domains such as mathematics, coding, and science, the knowledge extracted from human data is rapidly approaching a limit. The majority of high-quality data sources - those that can actually improve a strong agent's performance - have either already been, or soon will be consumed. The pace of progress driven solely by supervised learning from human data is demonstrably slowing, signalling the need for a new approach."

2. > "AI is at the cusp of a new period in which experience will become the dominant medium of improvement and ultimately dwarf the scale of human data used in today's systems."

3. > "Ultimately, experiential data will eclipse the scale and quality of human generated data."

4. (supporting, on the scalability of experiential learning) > "powerful RL agents such as AlphaZero ... exhibited impressive and potentially unlimited scalability with the size of the neural network, the quantity of interactive experience, and the duration of thinking time."

---

## TASK 2 — Ilya Sutskever, NeurIPS 2024

**Main quote — VERIFIED (secondary outlet quoting him directly, with photographs of his own slides).**

The Verge, Kylie Robison, "OpenAI cofounder Ilya Sutskever says the way AI is built is about to change" — URL dated `2024/12/13`, page timestamp **Dec 14, 2024, 12:34 AM UTC**:
`https://www.theverge.com/2024/12/13/24320811/what-ilya-sutskever-sees-openai-model-data-training`

Verbatim:
> "'Pre-training as we know it will unquestionably end,' Sutskever said onstage."

**Wording resolved:** the actual onstage wording per The Verge is **"Pre-training as we know it will unquestionably end"** — i.e. the longer form, *not* "Pre-training as we know it will end."

Other direct quotes from the same piece:
> "'We've achieved peak data and there'll be no more,' according to Sutskever. 'We have to deal with the data that we have. There's only one internet.'"

> "The more a system reasons, 'the more unpredictable it becomes,' according to Sutskever."

> "'They will understand things from limited data,' he said. 'They will not get confused.'"

Occasion context (verbatim from The Verge): "made a rare public appearance in Vancouver on Friday at the Conference on Neural Information Processing Systems (NeurIPS)." (Friday = 13 Dec 2024.)

**"Data is the fossil fuel" — VERIFIED (secondary, slide caption credited to NeurIPS).** Photograph caption in the same Verge piece:
> "Ilya Sutskever calls data the 'fossil fuel' of AI." — photo credit: "Ilya Sutskever/NeurIPS"

Editorial description in the same piece: "He compared the situation to fossil fuels: just as oil is a finite resource, the internet contains a finite amount of human-generated content." Additional secondary aggregation exists but was **not fetched**: officechai.com, "Data Is The Fossil Fuel Of AI, It Will Get Exhausted: Ilya Sutskever".

**"Compute and data were the two axes of scaling that have now plateaued" — COULD NOT VERIFY.** No source found, primary or secondary, carrying this phrasing or an equivalent two-axes claim. The Verge piece's scaling content is a *paraphrase* (not a quote):
> "He suggested that, just as evolution found a new scaling pattern for hominid brains, AI might similarly discover new approaches to scaling beyond how pre-training works today."

**Official NeurIPS award-speech record / transcript — COULD NOT VERIFY.** `neurips.cc` was reachable but pages fetched (`/Conferences/2024`, `/virtual/2024/index.html`, award pages) contained **0 occurrences of "Sutskever"**; `slideslive.com` and `blog.neurips.cc` are unreachable; the talk video/transcript could not be obtained. The only attribution of this as an "award speech" is the citing preprint's own reference [1]: *"Ilya Sutskever. Sequence to sequence learning with neural networks: What a decade. In Award speech in the 38th Conference on Neural Information Processing Systems (NeurIPS 2024), Vancouver, Canada, December 2024. Award speech stating 'Pre-training as we know it will unquestionably end'."* — that is the citing paper's characterization, not independent verification.

---

## TASK 3 — Dario Amodei's "~10% chance … stagnate due to insufficient data"

### 3a. The original podcast — COULD NOT VERIFY

**What the citing preprint actually claims (primary for the claim, verbatim from arXiv:2508.05619v1 references):**
> "[2] Kevin Roose and Casey Newton. Dario amodei on the paradoxes of a.i. safety and netflix's 'deep fake love'. Podcast Transcript, July 2023. URL https://www.nytimes.com/section/technology. Available at The New York Times."

**The cited episode exists — VERIFIED.**
Title: "Dario Amodei, C.E.O. of Anthropic, on the Paradoxes of A.I. Safety and Netflix's 'Deep Fake Love'"; podcast: **Hard Fork** (The New York Times), hosts Kevin Roose and Casey Newton; NYT transcript page path dates it **21 July 2023**:
`https://www.nytimes.com/2023/07/21/podcasts/dario-amodei-ceo-of-anthropic-on-the-paradoxes-of-ai-safety-and-netflixs-deep-fake-love.html`
(URL obtained via search; nytimes.com is unreachable from this environment, so the page itself could not be read. Apple Podcasts episode id 1000621870653; also mirrored at globalplayer.com/podcasts/episodes/7DritQZ/ — not fetchable.) Date is consistent with the preprint's "July 2023".

**The "10% chance that the scaling of AI systems could stagnate due to insufficient data" wording: COULD NOT VERIFY in any source.** No reachable transcript of the Hard Fork episode exists in this environment (nytimes.com, podscripts.co, snipd.com, musixmatch, podchaser, apple.com all blocked/unreachable), and no reachable outlet attributes a 10%-data-stagnation figure to Amodei in that episode.

**Two specific red flags to carry into the lecture:**
1. The preprint's citation URL is a **generic NYT section URL** (`nytimes.com/section/technology`), not an episode permalink — it does not resolve to the cited episode.
2. The preprint's acknowledgements (verbatim) state: *"Manus and Perplexity were helpful for literature search and citation validation."*

Recommended slide wording: *"A 7 Aug 2025 IBM preprint (arXiv:2508.05619v1) attributes to Amodei a '10% chance that the scaling of AI systems could stagnate due to insufficient data', citing a July 2023 NYT Hard Fork episode. The episode exists (21 Jul 2023); the quoted sentence could not be located in any accessible transcript. Treat as unconfirmed/secondhand."*

**Alternative candidate (also unverified):** the Dwarkesh Podcast episode "Dario Amodei (Anthropic CEO) - Scaling, Alignment, & AI Progress" has a clip titled "Scaling Plateaus Before We Reach Human Level Intelligence" (`share.snipd.com/chapter/c08fe78e-f0b7-4f0b-bcfa-ad245ad9f63c`) — snipd returns HTTP 403, so neither date nor transcript could be checked.

### 3b. 2025–2026 Amodei on whether pretraining scaling is still delivering — VERIFIED (secondary; third-party transcript service, not authoritative)

**Dwarkesh Podcast, "Dario Amodei — 'We are near the end of the exponential'" — published 13 February 2026** (runtime 02:22:20).
- quicklets.ai episode page states `PUBLISHED: FEB 13, 2026`: `https://quicklets.ai/podcasts/dwarkesh-podcast/dario-amodei-we-are-near-the-end-of-the-exponential`
- pod.wave.co page states "February 13, 2026 · 02:22:20 episode": `https://pod.wave.co/podcast/dwarkesh-podcast/dario-amodei-we-are-near-the-end-of-the-exponential`

Verbatim from the pod.wave.co summary:
> "Pretraining continues to yield improvements. Now, RL (Reinforcement Learning) is showing similarly reliable scaling, with models generalizing across broader tasks."

> "When I look at the exponential, it is roughly what I expected... The most surprising thing has been the lack of public recognition of how close we are to the end of the exponential." (00:46)

> "The 'big blob of compute hypothesis' outlined in his 2017 doc is holding up."

> "Critics, like Rich Sutton, worry that real intelligence should need less brute force data/computation. Dario responds: Human brains come with evolutionary priors—models start as blank slates and need to learn everything from scratch."

**CAVEAT: pod.wave.co and quicklets.ai are third-party AI transcription/summary services, not the publisher.** `dwarkesh.com` and `dwarkesh.substack.com` were unreachable, so the primary transcript could not be checked. Verify before quoting on a slide. Corroborating pointer: The Decoder (21 Jun 2026) writes "Anthropic CEO Dario Amodei recently made similar remarks" (in favour of continued scaling).

---

## TASK 4 — OpenAI o1 (Sept 2024) and o3 (Dec 2024)

### 4a. URLs and publication dates — VERIFIED (primary: OpenAI's own news feed)

Source: `https://openai.com/news/rss.xml` (fetched 2026-09-16, HTTP 200, 725,972 bytes, 1,194 items). Timestamps verbatim:

| Post | URL | RSS `pubDate` |
|---|---|---|
| Learning to reason with LLMs | `https://openai.com/index/learning-to-reason-with-llms` | `Thu, 12 Sep 2024 10:02:00 GMT` |
| Introducing OpenAI o1 | `https://openai.com/index/introducing-openai-o1-preview` | `Thu, 12 Sep 2024 10:03:00 GMT` |
| OpenAI o1 System Card | `https://openai.com/index/openai-o1-system-card` | `Thu, 05 Dec 2024 10:00:00 GMT` |
| OpenAI o1 and new tools for developers | `https://openai.com/index/o1-and-new-tools-for-developers` | `Tue, 17 Dec 2024 00:00:00 GMT` |
| OpenAI o3-mini | `https://openai.com/index/openai-o3-mini` | `Fri, 31 Jan 2025 11:00:00 GMT` |
| Introducing OpenAI o3 and o4-mini | `https://openai.com/index/introducing-o3-and-o4-mini` | `Wed, 16 Apr 2025 10:00:00 GMT` |

**IMPORTANT NEGATIVE FINDING — there is no December 2024 OpenAI blog post announcing o3.** In the same feed the only 20 Dec 2024 item is "Deliberative alignment: reasoning enables safer language models" (`https://openai.com/index/deliberative-alignment`, `Fri, 20 Dec 2024 10:00:00 GMT`). o3 was announced live in the final "12 Days of OpenAI" stream on 20 Dec 2024 (confirmed by ARC Prize below). Any slide citing an "o3 announcement blog post, Dec 2024" should be corrected.

### 4b. The o1 test-time/train-time compute claim — VERIFIED (secondary outlet quoting the OpenAI post verbatim), with a wording correction

Silicon Republic, Leigh Mc Gowran, **13 Sep 2024**: `https://www.siliconrepublic.com/machines/openai-o1-reasoning-ai-model-preview`

> "'Our large-scale reinforcement learning algorithm teaches the model how to think productively using its chain of thought in a highly data-efficient training process,' OpenAI said. 'We have found that the performance of o1 consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute).'"

**Correction to the wording in the brief:** the actual sentence reads "**We have found that the performance of o1 consistently improves** with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute)." The version supplied ("we have found that performance consistently improves…") drops "the performance of o1" and the preceding sentence. Because `openai.com/index/learning-to-reason-with-llms` returns HTTP 403 to this environment, this sentence is **secondhand-verified only** — the primary URL is correct, its body text was not readable.

Supporting OpenAI-employee quotes (secondary, The Decoder, 12 Sep 2024, updated 11 Dec 2024): `https://the-decoder.com/openais-new-o1-model-thinks-longer-to-give-smarter-answers/`
> "OpenAI o1 is trained with RL to 'think' before responding via a private chain of thought. The longer it thinks, the better it does on reasoning tasks." — Noam Brown

> "We're no longer bottlenecked by pretraining. We can now scale inference compute too." — Noam Brown

### 4c. o3 ARC-AGI high-compute claims — VERIFIED (primary: ARC Prize Foundation, benchmark owner)

François Chollet, "OpenAI o3 Breakthrough High Score on ARC-AGI-Pub", **published 20 Dec 2024**: `https://arcprize.org/blog/oai-o3-pub-breakthrough`

> "OpenAI's new o3 system - trained on the ARC-AGI-1 Public Training set - has scored a breakthrough 75.7% on the Semi-Private Evaluation set at our stated public leaderboard $10k compute limit. A high-compute (172x) o3 configuration scored 87.5%."

> "Update 12/20/2024: ARC Prize presented o3's performance results in person with OpenAI's Sam Altman (CEO) and Mark Chen (SVP Research) during the final '12 Days of OpenAI' event."

> "The low-efficiency score of 87.5% is quite expensive, but still shows that performance on novel tasks does improve with increased compute (at least up to this level.)"

Cost figures from the same post's results table: Semi-Private high-efficiency 75.7% ($2,680 total / $26 per task); Semi-Private low-efficiency 87.5% ($456,000 total / $4,560 per task); Public low-efficiency 91.5% ($760,000 total / $1,900 per task).

### 4d. o3 FrontierMath — VERIFIED (secondary only)

GIGAZINE, **25 Dec 2024, 09:45:00**: `https://www.gigazine.net/gsc_news/en/20241225-ai-frontiermath`
> "It has been revealed that the o3 model achieved a score of 25.2% on the FrontierMath problem dataset."
> "On December 20, 2024, OpenAI announced a new inference model, the o3 series."

It cites mathematician Kevin Buzzard's post, "Can AI do maths yet? Thoughts from a mathematician", **22 Dec 2024**: `https://xenaproject.wordpress.com/2024/12/22/can-ai-do-maths-yet-thoughts-from-a-mathematician/`

**COULD NOT VERIFY an Epoch AI primary page for the 25.2% figure.** `epoch.ai` is reachable (`https://epoch.ai/frontiermath` → HTTP 200) but no matching announcement post was located on it.

### 4e. Has test-time / inference scaling plateaued? (2025–2026)

**VERIFIED (secondary reporting on an Epoch AI analysis) — note this is an external analysis, NOT an OpenAI statement.**

TechCrunch, Kyle Wiggers, **12 May 2025, 3:36 PM PDT**: `https://techcrunch.com/2025/05/12/improvements-in-reasoning-ai-models-may-slow-down-soon-analysis-finds/`
> "An analysis by Epoch AI, a nonprofit AI research institute, suggests the AI industry may not be able to eke massive performance gains out of reasoning AI models for much longer. As soon as within a year, progress from reasoning models could slow down, according to the report's findings."

> "'If there's a persistent overhead cost required for research, reasoning models might not scale as far as expected,' writes You. 'Rapid compute scaling is potentially a very important ingredient in reasoning model progress, so it's worth tracking this closely.'" — Josh You, Epoch AI

> "OpenAI has said that it applied around 10x more computing to train o3 than its predecessor, o1, and Epoch speculates that most of this computing was devoted to reinforcement learning."

Corroboration: The Decoder, Maximilian Schreiner, **14 May 2025**: `https://the-decoder.com/compute-scaling-drives-reasoning-model-gains-but-cannot-last-forever/`
> "OpenAI says it trained o3 with ten times as much reasoning compute as o1—just four months after o1's release."

**No 2025–2026 OpenAI statement saying test-time scaling has plateaued was found.** (There is no such statement in OpenAI's own news feed; and openai.com HTML is unreadable here.)

---

## TASK 5 — Altman / Hassabis / LeCun, 2025–2026

### Sam Altman — VERIFIED (secondary outlet quoting him directly)
The Decoder, Matthias Bastian, **21 Jun 2026**: `https://the-decoder.com/sam-altman-says-a-whole-generation-of-researchers-held-ai-back-by-underestimating-what-scaling-could-do/`
> "Betting against LLMs scaling at this point feels quite misguided to me." — attributed "Sam Altman, OpenAI", said "At Stanford"; The Decoder cites its source as "Stanford Online".
> "So clearly, LLMs are capable of figuring out new knowledge," Altman said. For very long-horizon tasks requiring high judgment, LLMs "seem much worse than people."

German-language edition, same author, **21. Juni 2026**: `https://the-decoder.de/openai-chef-sam-altman-haelt-skalierung-grosser-sprachmodelle-fuer-lange-nicht-ausgereizt/` renders the same quote as "Zu diesem Zeitpunkt gegen die Skalierung von LLMs zu wetten, halte ich für ziemlich verfehlt."

Second outlet, same quote: Mixed Reality News, **Jul 08 2026**: `https://mixed-news.com/en/sam-altman-hits-back-at-ai-skeptics-who-called-llms-a-dead-end-as-science-focused-gpt-5-6-launch-looms/`
> "'Betting against LLMs scaling at this point feels quite misguided to me,' Altman said."

Scope note: this is about **LLM scaling generally**, not specifically pretraining.

### Demis Hassabis — PARTIALLY VERIFIED (episode title + date primary; substance unverified)
20VC (The Twenty Minute VC), episode: *"20VC: DeepMind's Demis Hassabis on Why AGI is Bigger than the Industrial Revolution | Why LLMs Will Not Commoditise & **We Have Not Hit Scaling Laws** | Bottlenecks in AI & The Energy Crisis Caused By AI | Whether AI Will Do More to Harm or Help Inequality"*.
**Release Date: 04/07/2026 (7 April 2026)**, verbatim from Libsyn's own directory listing: `https://directory.libsyn.com/episode/index/show/thetwentyminutevc/id/40750590`
Same page lists the agenda item verbatim: `00:06:00 — Have We Hit the Limits of Scaling Laws?`
→ The episode title asserts Hassabis's position that scaling limits have **not** been hit; **no verbatim quote or actual answer could be retrieved** (audio/transcript inaccessible; Apple Podcasts, teahose.com and podscan.fm blocked or JS-only).

Secondary and weaker (translated aggregator, no English direct quote): xix.ai, dated **2026-09-12**: `https://xix.ai/zh/ainews/deepmind-ceo-hassabis-predicts-agi-within-five-years-as-ai-sparks-tenfold-industrial-revolution.html` — reports Hassabis saying diminishing marginal returns on scaling do exist but "它还没有死" ("it is not dead yet"), and that competition has shifted from who has more money/compute to who can produce new ideas. Treat as low-confidence.

### Yann LeCun — VERIFIED (secondary; 36Kr English aggregation, not a first-person transcript)
36Kr (English), "Is the Pre-training Path to AGI Dead? Yann LeCun Uncovers the Cognitive Gap LLMs Can't Cross", **2025-07-04 14:42**: `https://eu.36kr.com/en/p/3364112069871367`
> "Yann LeCun said: Autoregressive models are terrible."

> "He believes that the current mainstream autoregressive models, whose core task is to generate text by predicting the next word, cannot in essence give rise to true intelligence. No matter how large the model scale is, this mechanism cannot achieve true understanding, reasoning, or human-like intelligence."

> "The era of the 'Pre-trained Scaling Myth' is coming to an end."

> "More importantly, this difference may not be bridged by the 'Scaling Law' of simply expanding the model scale and data volume."

Also located but **not fetched** (ain3xt.com returns HTTP 403 / Cloudflare): "Yann LeCun: The LLM Revolution Is Over, the Next Wave Is AI That Understands the Real World", dated 2026-01-29.

---

## SUMMARY TABLE

| # | Item | Status |
|---|---|---|
| 1 | Era of Experience PDF URL | VERIFIED (primary) |
| 1 | Era of Experience date | VERIFIED (primary, PDF metadata = 10 Apr 2025; no printed date) |
| 1 | Era of Experience scaling quotes | VERIFIED (primary, verbatim) |
| 2 | "Pre-training as we know it will unquestionably end" | VERIFIED (secondary, The Verge, 14 Dec 2024 UTC, direct quote) |
| 2 | "data is the fossil fuel" | VERIFIED (secondary, Verge slide caption credited to NeurIPS) |
| 2 | "two axes of scaling … plateaued" | COULD NOT VERIFY |
| 2 | Official NeurIPS award-speech transcript/video | COULD NOT VERIFY |
| 3 | Hard Fork episode existence + date (21 Jul 2023) | VERIFIED (secondary metadata) |
| 3 | Amodei "10% … stagnate due to insufficient data" | COULD NOT VERIFY |
| 3 | Amodei 2026: pretraining still yielding improvements | VERIFIED (secondary, third-party transcript service; 13 Feb 2026) |
| 4 | o1 / o3 blog URLs + dates | VERIFIED (primary, OpenAI RSS) |
| 4 | "no o3 blog post in Dec 2024" | VERIFIED (primary, OpenAI RSS) |
| 4 | o1 train-time/test-time compute sentence | VERIFIED (secondary, verbatim quote of the post; wording corrected) |
| 4 | o3 ARC-AGI 75.7% / 87.5% @172x | VERIFIED (primary, ARC Prize, 20 Dec 2024) |
| 4 | o3 FrontierMath 25.2% | VERIFIED (secondary, GIGAZINE 25 Dec 2024) |
| 4 | Reasoning/test-time scaling may slow | VERIFIED (secondary, TechCrunch 12 May 2025 re Epoch AI) |
| 4 | OpenAI's own statement of test-time plateau | COULD NOT VERIFY |
| 5 | Altman "Betting against LLMs scaling…" | VERIFIED (secondary, 21 Jun 2026) |
| 5 | Hassabis "We Have Not Hit Scaling Laws" | PARTIAL — title+date verified, quote not retrieved |
| 5 | LeCun pre-training scaling critique | VERIFIED (secondary, 36Kr EN 4 Jul 2025) |
