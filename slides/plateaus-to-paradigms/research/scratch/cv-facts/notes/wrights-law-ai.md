# Wright's Law (the Learning Curve) and its Application to AI — Verified Facts

Compiled: 2026-09-19. Working dir: `/home/zecyel/slides/ch1`.
Evidence rule used here: every non-obvious number has a URL/DOI inline. Anything I could not
verify from a primary source is in **COULD NOT VERIFY** at the end. Every failing URL is logged in
**FETCH FAILURES**. No quote below is invented; where the source body was inaccessible I say so.

Notation used: **peer-reviewed** = journal/conference with editorial peer review; **preprint** =
arXiv/SSRN without (yet) verified peer review; **industry/informal** = company or independent blog report.

---

## PART 1 — The original 1936 paper

### (a) Exact citation — VERIFIED via Crossref (authoritative registry record)

Full Crossref metadata, retrieved from `https://api.crossref.org/works/10.2514/8.155` (HTTP 200):

| Field | Value (verbatim from Crossref) |
|---|---|
| Title | `Factors Affecting the Cost of Airplanes` |
| Author | T. P. WRIGHT (given: `T. P.`, family: `WRIGHT`), affiliation `Curtiss-Wright Corporation` |
| Journal | `Journal of the Aeronautical Sciences` |
| Volume | `3` |
| Issue | `4` |
| Pages | `122-128` |
| Year / month | published-print `1936-02` → **February 1936** |
| Publisher | `American Institute of Aeronautics and Astronautics (AIAA)` |
| ISSN | `1936-9956` (electronic) |
| DOI | `10.2514/8.155` |
| Type | `journal-article` |
| Cited-by count | `2275` (Crossref index snapshot dated 2026-09-17) |

- Crossref record: https://api.crossref.org/works/10.2514/8.155
- Canonical DOI link: https://doi.org/10.2514/8.155
- Publisher landing page (did NOT load for me — see FETCH FAILURES): https://arc.aiaa.org/doi/10.2514/8.155

Independent corroboration of the same volume/issue/pages: Our World in Data endnote 1 reads
"**Theodore Paul Wright (1936) – Factors affecting the cost of airplanes. J. Aeronaut. Sci., 3 (4)
(1936), pp. 122-128**" — https://ourworldindata.org/learning-curve

### (b) DOI — VERIFIED

`10.2514/8.155` is confirmed correct (Crossref resolves the record above; the DOI is also cited with
matching volume/pages in an independent bibliographic record at
https://m2.mtmt.hu/api/reference/40654901). URL: https://doi.org/10.2514/8.155

### (c) The exact statement of the law

**PRIMARY-SOURCE BODY NOT ACCESSED. I could not read the paper text, so I cannot give a verbatim
sentence from Wright (1936).** The paper is paywalled, and AIAA's site (arc.aiaa.org) returned HTTP
403 (Cloudflare interstitial "Just a moment...") for both the article page and the Vol. 3 No. 4 table
of contents. I did **not** invent or paraphrase-quote any sentence. Treat any "Wright wrote …" quote
you see elsewhere as unverified unless it cites a page image.

Standard mathematical form (this is the conventional formalisation, not a quotation from Wright):

- `C_n = C_1 · n^(−b)` — unit cost of the n-th cumulative unit, where `n` is **cumulative production
  quantity** and `b > 0` is the learning exponent.
- **Progress ratio** `PR = 2^(−b)` — the fraction of cost remaining after each doubling of cumulative
  production.
- **Learning rate** `LR = 1 − 2^(−b) = 1 − PR` — the percentage cost reduction per doubling.
- Inverse: `b = −log2(1 − LR) = −log2(PR)`.

Source for this exact algebraic form (independent research site, non-peer-reviewed, but explicit):
"**C(q) = C0 · q−b** … **LR = 1 − 2−b (learning rate)**" — https://carbonfinancelab.com/wrights-law/

A **peer-reviewed** statement of the same functional form, with the economics interpretation:
"An early hypothesis made by Theodore Wright in 1936 is that **cost decreases as a power law of
cumulative production**." — Nagy, Farmer, Bui & Trancik (2013), *PLOS ONE* 8(2): e52669,
DOI https://doi.org/10.1371/journal.pone.0052669

The distinction that has to be stressed in a lecture: Wright's law is cost **vs cumulative
production**, whereas Moore's law is cost/performance **vs time**. Nagy et al. (2013) state the
relation explicitly: "**Note that these methods forecast different things: Moore's law forecasts the
cost at a given time, Wright's law at a given cumulative production, and Goddard's law at a given
annual production.**" — https://doi.org/10.1371/journal.pone.0052669

**Worked numerical example of the learning-rate definition — VERIFIED, from Our World in Data**
(Max Roser, "Learning curves: What does it mean for a technology to follow Wright's Law?",
18 April 2023, https://ourworldindata.org/learning-curve):

> "The number of doublings of the capacity is: log2(578,553 / 0.3)=20.879
> The rate of change of the price at each doubling is: (106.09 / 0.37725) ^ (1/(20.879)) - 1=0.31=**31%**
> So the learning rate is 1-2^(-0.31)=0.193399911=**19.3%**"

And the prose definition, verbatim:

> "The relative price decline associated with each doubling of cumulative experience is the
> _learning rate_ of a technology."
> "The learning rate of solar panels is 20%. This means that with each doubling of the installed
> cumulative capacity, the price of solar panels declined by 20%."

Also for a technology actually following the law (verbatim OWID):

> "For more than four decades, the price of solar panels declined by 20% with each doubling of global
> cumulative capacity."

### (d) Alternative names: learning curve / experience curve / "Henderson's law"

- **"Learning curve"**: used interchangeably with Wright's law throughout the OWID article above
  ("The orange line that describes the relationship between these two metrics over time is called the
  _learning curve_ of that technology.") — https://ourworldindata.org/learning-curve
- **"Experience curve"**: the BCG/business-strategy name. BCG's own 1968 publication is titled
  "The Experience Curve" (Business Unit Strategy / Growth): https://www.bcg.com/publications/1968/business-unit-strategy-growth-experience-curve
  (I could get HTTP 200 only from the `/ja-jp/` mirror, and its body rendered empty because the page
  is JavaScript-driven, so I could **not** extract a verbatim BCG sentence — see FETCH FAILURES.)
  A BCG follow-up history piece exists at
  https://www.bcg.com/publications/1973/corporate-finance-strategy-portfolio-management-experience-curve-reviewed-part-ii-the-history
  (also not machine-readable for me).
- **"Henderson's law"**: I found **no reliable primary source** using this exact name for Wright's
  law. The experience curve is attributed to BCG founder Bruce Henderson, but I could not verify the
  label "Henderson's law" from a primary or peer-reviewed source. Flagged in COULD NOT VERIFY.
- Note the naming trap: in AI, "learning rate" almost always means the SGD step size
  (η), which is completely unrelated to the learning-curve "learning rate" used above. Flag this in
  the lecture.

---

## PART 2 — Applications to AI compute or model costs

### Classification summary

The literature splits into two distinct exercises, and they should not be conflated:

1. **Cost vs TIME** ("algorithmic progress", "compute efficiency", "price-performance trends").
   Almost all AI work lives here. It is *not* Wright's law.
2. **Cost vs CUMULATIVE PRODUCTION** (true Wright's law). For AI, this is essentially only found in
   non-peer-reviewed industry research.

### (a) Dario Amodei

**Result: NO explicit doubling period or learning rate for AI training costs could be verified from
Amodei's primary writings.**

- Amodei's official site lists exactly **two essays**: "The Adolescence of Technology" (January 2026)
  and "Machines of Loving Grace" (October 2024). It also lists short posts including "We Must Pace the
  Frontier" and "Policy on the AI Exponential". — https://darioamodei.com/
- **The title "Some High-level Thoughts on the Direction of AI" does not appear on Amodei's site.**
  I found no evidence that this is a real Amodei essay. Treat the premise as unverified.
- **"Machines of Loving Grace"** (October 2024): I fetched https://darioamodei.com/essay/machines-of-loving-grace
  (HTTP 200) and read the retrieved text. It is **an informal essay**, not a formal analysis. In the
  text I retrieved there is **no** statement of a training-cost doubling period or learning rate.
  The nearest cost statement is a market-mechanism claim, not a learning curve: "markets are typically
  good at bringing down the cost of high-value technologies over time" (in the "Inequality within
  countries" section).
  **Caveat:** the fetch tool truncated the page (last sections and the footnotes were not retrieved),
  so I cannot fully exclude such a statement in the unretrieved remainder.
- **"The Adolescence of Technology"** (January 2026, https://darioamodei.com/essay/the-adolescence-of-technology):
  also an **informal essay**. I searched the retrieved text for cost/training-cost/doubling/learning-rate
  claims; the only cost-related hits are about the cost of *training such systems* as an argument for
  correlated failure modes, and about classifier inference costs — **no doubling period, no learning
  rate**. Again, the fetch was truncated (33,586 bytes omitted).
- **Caution for the lecture:** Amodei's public framing is that training compute/cost is *rising*
  (e.g. frontier training runs costing hundreds of millions to billions), which is the **opposite**
  direction from a cost-learning curve. See Epoch AI's training-cost growth numbers below.
- I could **not** retrieve a transcript in which Amodei gives a "cost of training falls X× per year"
  figure (Dwarkesh transcript, Cockatoo transcript, Singjupost transcript all failed — see FETCH
  FAILURES). Any such quote should be treated as unverified until the primary transcript is obtained.

### (b) Epoch AI

All Epoch items below are **time-based** ("effective compute", "algorithmic progress",
"price-performance"), **not** Wright's-law fits against cumulative production.

**B1. "Algorithmic progress in language models" — the arXiv:2403.05812 candidate: VERIFIED.**
- arXiv:2403.05812, Ho, Besiroglu, Erdil, Owen, Rahman, Guo, Atkinson, Thompson, Sevilla;
  submitted 9 March 2024. https://arxiv.org/abs/2403.05812
- Verbatim from the abstract: "**we find that the compute required to reach a set performance
  threshold has halved approximately every 8 months, with a 95% confidence interval of around 5 to 14
  months, substantially faster than hardware gains per Moore's Law.**"
- Verbatim from Epoch's own publication page (12 March 2024):
  "**We find that the level of compute needed to achieve a given level of performance has halved
  roughly every 8 months, with a 95% confidence interval of 5 to 14 months.**"
  and, in the page summary line: "**occurring at a pace equivalent to doubling computational power
  every 5 to 14 months.**" — https://epoch.ai/publications/algorithmic-progress-in-language-models
- **Peer review status:** this work appears in *Advances in Neural Information Processing Systems 37*,
  pp. 58245–58283 — cited that way in a peer-reviewed-adjacent preprint's reference list
  (Gundlach et al., arXiv:2511.23455, reference [10]). It is also indexed in the NeurIPS proceedings
  via ACM DL (dlnext.acm.org/doi/10.5555/3737916.3739772). I could **not** fetch the NeurIPS page
  directly (ACM DL returned 403), so I classify it as **peer-reviewed (NeurIPS 2024) on strong
  secondary evidence, with the proceedings page itself unverified by me.** The arXiv version is a
  preprint.

**B2. "Trends in the dollar training cost of machine learning systems" (Ben Cottier, 31 Jan 2023) — non-peer-reviewed report.**
- Verbatim: "**I estimate that the cost of compute in US dollars for the final training run of ML
  systems has grown by 0.49 orders of magnitude (OOM) per year (90% CI: 0.37 to 0.56).**" (n=124
  systems, 2009–2022). Large-scale subset: "**0.2 OOMs/year (90% CI: 0.1 to 0.4 OOMs/year)**".
- URL: https://epoch.ai/publications/trends-in-the-dollar-training-cost-of-machine-learning-systems
- This is cost **growth vs time** — a direct counterpoint to naive "AI costs halve" claims, and NOT
  Wright's law.

**B3. "The rising costs of training frontier AI models" (Cottier, Rahman, Fattorini, Maslej, Besiroglu, Owen) — arXiv:2405.21015.**
- Verbatim abstract: "**the amortized cost to train the most compute-intensive models has grown
  precipitously at a rate of 2.4x per year since 2016 (90% CI: 2.0x to 2.9x).**"
- URL: https://arxiv.org/abs/2405.21015 ; DOI https://doi.org/10.48550/arXiv.2405.21015
- Status: arXiv preprint (v1 31 May 2024, v2 7 Feb 2025); I found no peer-reviewed venue.
  Cost **growth vs time**, not Wright's law.

**B4. Epoch Data Insight "LLM inference prices have fallen rapidly but unequally across tasks" (12 Mar 2025).**
- Verbatim: "**the price to achieve GPT-4's performance on a set of PhD-level science questions fell
  by 40x per year. The rate of decline varies dramatically depending on the performance milestone,
  ranging from 9x to 900x per year.**"
- URL: https://epoch.ai/data-insights/llm-inference-price-trends
- Status: non-peer-reviewed data insight. Price **vs time**, not vs cumulative production.

**B5. Epoch's "AI Benchmarking Hub"** (https://epoch.ai/benchmarks) is the underlying data source used
by the independent MIT analysis in (d) below.

**B6. No Wright's-law framing found.** Across the Epoch pages I retrieved, AI cost/efficiency progress
is framed as "algorithmic progress" / "effective compute" / "price-performance", i.e. vs time or vs
compute. I did not find an Epoch page fitting Wright's law to AI (cost vs cumulative production).

### (c) Our World in Data

- **Page:** "Learning curves: What does it mean for a technology to follow Wright's Law?" by Max
  Roser, 18 April 2023 — https://ourworldindata.org/learning-curve
- **Key verbatim numbers:**
  - "For more than four decades, the price of solar panels declined by **20%** with each doubling of
    global cumulative capacity."
  - "The learning rate of solar panels is **20%**."
  - Endnote 4, verbatim: "The authors find an average learning rate over many studies of **20.2%**
    (see Table 1 of their publication)" — citing de La Tour, Glachant & Ménière (2013), *Energy* 62,
    341–348. OWID's own fit: "The learning rate implied by the data that I'm presenting here is very
    similar (**19.3%**)".
  - Price decline 1976→2019: "$106 to $0.38 per watt in these four decades. A decline of **99.6%**."
  - "**Most technologies do not follow Wright's Law** – the prices of bicycles, fridges, or coal
    power plants do not decline exponentially as we produce more of them."
- **Cross-technology dataset:** OWID grapher "The cost of 66 different technologies over time"
  (https://ourworldindata.org/grapher/costs-of-66-different-technologies-over-time), source
  "Farmer and Lafond (2016) – with minor processing by Our World in Data", date range **1929–2013**,
  underlying paper DOI https://doi.org/10.1016/j.respol.2015.11.001.
- **Does OWID apply Wright's law to AI specifically? NO — not on the pages I retrieved.**
  The learning-curve article discusses solar, computing/Moore's law, batteries, the Model T and the
  66-technology database; it contains **no AI/LLM learning-rate figure**. Its companion article is
  "What is Moore's Law?" (https://ourworldindata.org/moores-law), which is a time-based law, not
  Wright's law. The 66-technology dataset (Farmer & Lafond 2016) predates modern LLMs. Caveat: I did
  not exhaustively crawl all of OWID.

### (d) Academic / peer-reviewed work applying Wright's law to AI or computation costs

**Finding: I found NO peer-reviewed paper that applies Wright's law (cost vs cumulative production) to
AI/ML training or inference costs.** The closest peer-reviewed works are time-based and are listed
below so the gap is explicit.

**D1. Peer-reviewed, but uses compute-efficiency/Moore-style TIME trends, NOT Wright's law.**
- Pilz, K. F., Heim, L., & Brown, N. (2025). "Increased Compute Efficiency and the Diffusion of AI
  Capabilities." *Proceedings of the AAAI Conference on Artificial Intelligence*, **39**(26),
  27582–27590. **DOI: https://doi.org/10.1609/aaai.v39i26.34971** (AAAI-25 Special Track on AI
  Alignment; published 2025-04-11). Landing page: https://ojs.aaai.org/index.php/AAAI/article/view/34971
- Verbatim: "**The cost of training an AI model to a given level of performance falls over time. In
  2017, training a classifier to 93% accuracy on ImageNet cost over $1,000; in 2021, it cost only $5
  — a reduction of over 99%.**"
- Verbatim: "**Between 2006 and 2021, the price performance of AI accelerators doubled approximately
  every two years.**"
- Verbatim: "**between 2012 and 2022, advances in image recognition algorithms halved the compute
  required for achieving 93% classification accuracy on the ImageNet dataset every nine months.**"
- Verbatim: "In 2020, OpenAI's GPT-3 cost at least $4.6 million in cloud compute to train; two years
  later, the company Mosaic claimed to achieve the same performance for a tenth of the price."
- Full text retrieved from https://ar5iv.labs.arxiv.org/html/2311.15377 (preprint version
  arXiv:2311.15377).
- **Flag:** this paper explicitly invokes "**Moore's Law**" for hardware and an "access effect /
  performance effect" model. It does **not** fit Wright's law and does not use "learning rate" in the
  Wright sense. It is the strongest peer-reviewed AI cost-decline paper, but it is a *time-based*
  claim, not a cumulative-production claim.

**D2. Peer-reviewed foundational Wright's-law paper, but NOT applied to AI.**
- Nagy, B., Farmer, J. D., Bui, Q. M., & Trancik, J. E. (2013). "Statistical Basis for Predicting
  Technological Progress." *PLOS ONE* **8**(2): e52669.
  **DOI: https://doi.org/10.1371/journal.pone.0052669** (peer-reviewed; PLOS ONE labels it
  "Peer-reviewed Research Article").
  Verbatim: "**Wright's law produces the best forecasts, but Moore's law is not far behind.**"
  Tested on "**62 different technologies**" grouped as Chemical, Hardware, Energy, Other — **AI/ML is
  not among them.** URL: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0052669
- Farmer, J. D. & Lafond, F. (2016). "How predictable is technological progress?" *Research Policy*
  **45**(3): 647–665. **DOI: https://doi.org/10.1016/j.respol.2015.11.001** (peer-reviewed). Same 62-
  technology basis; not applied to AI.

**D3. Peer-reviewed, AI-specific, but NOT Wright's law (time/parameter-scaling, not cumulative production).**
- Xiao, C. et al. "Densing Law of LLMs." arXiv:2412.04315 (https://arxiv.org/abs/2412.04315).
  Verbatim: "**the capacity density of LLMs doubles approximately every three months.**"
  Journal version reported as *Nature Machine Intelligence*: https://www.nature.com/articles/s42256-025-01137-0
  (I could not load the Nature page — it redirected to idp.nature.com — so the journal publication is
  flagged as unverified by me; the arXiv preprint is verified.) This is a law about model capability
  per parameter vs **time**, not cost vs cumulative production.

**D4. Non-peer-reviewed AI-specific Wright's-law work (the only true Wright's-law-on-AI fits found).**
- Gogerty / Carbon Finance Lab, "Experience Curves Extended: Wright's Law Across 98 Technologies"
  (2025). SSRN: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6198738
  Project site: https://carbonfinancelab.com/wrights-law/
  - Verbatim from the project site: "**GPU Compute: 89.2% cost decline per doubling**", with
    "Learning Rate **89.2%**", "R-squared **0.9911**", "Year Range **2003–2025**", "Data Points **13**",
    "Cost Metric **$/GFLOPS (2024 $)**".
  - Verbatim from the site's landmark list: "**GPU Compute 89.2% — The fastest learning rate ever
    measured. GPU cost per GFLOPS dropped 89.2% every time cumulative shipments doubled.**"
  - **Status: NON-peer-reviewed industry/independent research (SSRN preprint + commercial research
    site).** The PDF at
    https://carbonfinancelab.com/wrights-law/data/Gogerty_Wrights_Law_Extended_2025.pdf could not be
    read (unsupported content type `application/pdf`).
  - **Two red flags to state in the lecture:** (i) the site page reports **R² = 0.9911**, while search
    index snippets of the PDF report **R² = 0.9953** — an internal inconsistency; (ii) an 89.2%
    decline per doubling is extraordinarily high and rests on only **13 data points** over 2003–2025,
    so it should be presented as a striking claim requiring replication, not as settled fact.
  - The same site also contains an outright quote attributed to "Gogerty, 2025" ("The learning rate is
    not a property of the technology...") but since I could not read the paper body I do not treat
    that as verified.

**D5. Non-peer-reviewed AI-specific TIME-trend work (accepted to a workshop, not a peer-reviewed venue).**
- Gundlach, H., Lynch, J., Mertens, M., & Thompson, N. "The Price of Progress: Algorithmic Efficiency
  and the Falling Cost of AI Inference." arXiv:2511.23455, https://arxiv.org/abs/2511.23455
  (v1 28 Nov 2025; v2 23 Mar 2026 retitled "The Price of Progress: Price Performance and the Future
  of AI"). Verbatim v1 abstract: "**the price for a given level of benchmark performance has
  decreased remarkably fast, around 5× to 10× per year, for frontier models on knowledge, reasoning,
  math, and software engineering benchmarks.**" … "**we estimate that algorithmic efficiency progress
  is around 3× per year.**" Verbatim v2 abstract addition: "**the price of running frontier models is
  rising between 3× to 18× per year due to bigger models and larger reasoning demands.**"
  - Status: **preprint; footnote states it "was accepted to the NeurIPS 2025 Workshop"** — a workshop,
    not a peer-reviewed archival venue. Declining price is measured **vs time**, not vs cumulative
    production. This is a good caution against over-reading "5–10×/year" as a Wright's-law learning rate.

---

## Table — AI-related applications (cost/efficiency claims)

| Source | What it claims (verbatim where quoted) | Learning rate / doubling period | Peer-reviewed? | URL |
|---|---|---|---|---|
| Epoch AI — *Algorithmic progress in language models* (Ho, Besiroglu, Erdil, Owen, Rahman, Guo, Atkinson, Thompson, Sevilla), 2024 | "the compute required to reach a set performance threshold has halved approximately every 8 months, with a 95% confidence interval of around 5 to 14 months" | Halving every ~8 months (CI 5–14); equivalently "doubling computational power every 5 to 14 months". **Time-based algorithmic progress, NOT Wright's law** | Yes — NeurIPS 37 (2024), pp. 58245–58283 (proceedings page not directly fetched; strong secondary evidence) | https://arxiv.org/abs/2403.05812 ; https://epoch.ai/publications/algorithmic-progress-in-language-models |
| Epoch AI — *Trends in the dollar training cost of ML systems* (Cottier), 2023 | "the cost of compute in US dollars for the final training run of ML systems has grown by 0.49 orders of magnitude (OOM) per year (90% CI: 0.37 to 0.56)" | Cost **growth** 0.49 OOM/yr (all systems); 0.2 OOM/yr (large-scale). No learning rate; **opposite sign to a cost learning curve** | No — Epoch report | https://epoch.ai/publications/trends-in-the-dollar-training-cost-of-machine-learning-systems |
| Epoch AI — *The rising costs of training frontier AI models* (Cottier, Rahman, Fattorini, Maslej, Besiroglu, Owen), 2024–25 | "the amortized cost to train the most compute-intensive models has grown precipitously at a rate of 2.4x per year since 2016 (90% CI: 2.0x to 2.9x)" | Cost growth 2.4×/year — not a learning rate | No — arXiv preprint | https://arxiv.org/abs/2405.21015 |
| Epoch AI — Data Insight *LLM inference prices have fallen rapidly…*, 2025 | "the price to achieve GPT-4's performance on a set of PhD-level science questions fell by 40x per year … ranging from 9x to 900x per year" | 9×–900×/yr price decline (per milestone); **vs time, not cumulative production** | No — Epoch data insight | https://epoch.ai/data-insights/llm-inference-price-trends |
| Pilz, Heim & Brown, *Increased Compute Efficiency and the Diffusion of AI Capabilities*, AAAI-25 | "In 2017, training a classifier to 93% accuracy on ImageNet cost over $1,000; in 2021, it cost only $5 — a reduction of over 99%"; accelerators "doubled approximately every two years" (2006–2021); image-recognition compute "halved … every nine months" (2012–2022) | Doubling of accelerator price-performance ~2 yr; algorithmic compute halving ~9 mo in vision. **Compute-efficiency/Moore-style, NOT Wright's law** | Yes — AAAI 39(26):27582–27590, DOI 10.1609/aaai.v39i26.34971 | https://doi.org/10.1609/aaai.v39i26.34971 |
| Gogerty / Carbon Finance Lab — *Wright's Law Across 98 Technologies*, 2025 | "GPU cost per GFLOPS dropped 89.2% every time cumulative shipments doubled" (13 data points, 2003–2025) | **Genuine Wright's-law fit:** LR 89.2% per doubling (page: R²=0.9911; PDF snippets: R²=0.9953 — inconsistent) | No — SSRN preprint / industry research | https://carbonfinancelab.com/wrights-law/ ; https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6198738 |
| Gundlach, Lynch, Mertens & Thompson — *The Price of Progress…*, 2025/26 | price for a given benchmark performance "decreased … around 5× to 10× per year"; "algorithmic efficiency progress is around 3× per year" (hardware-adjusted) | 5–10×/yr overall; ~3×/yr algorithmic. **Vs time; NeurIPS *Workshop* only** | No — preprint (NeurIPS 2025 workshop) | https://arxiv.org/abs/2511.23455 |
| Xiao et al. — *Densing Law of LLMs*, 2024/25 | "the capacity density of LLMs doubles approximately every three months" | Doubling ~3 months, but of capability-per-parameter vs **time**; **not** Wright's law / not a cost learning rate | Reported in *Nature Machine Intelligence* (page not fetchable by me); arXiv preprint verified | https://arxiv.org/abs/2412.04315 ; https://www.nature.com/articles/s42256-025-01137-0 |
| Nagy, Farmer, Bui & Trancik — *Statistical Basis for Predicting Technological Progress*, PLOS ONE 2013 | "Wright's law produces the best forecasts, but Moore's law is not far behind"; tested on 62 technologies | Establishes Wright's law methodologically; **no AI technologies in the dataset** | Yes — DOI 10.1371/journal.pone.0052669 | https://doi.org/10.1371/journal.pone.0052669 |
| Our World in Data — *Learning curves…*, 2023 | "the price of solar panels declined by 20% with each doubling of global cumulative capacity"; "The learning rate of solar panels is 20%" | True Wright's-law **learning rate = 20% (solar)**. **No AI figure on OWID** | No — OWID explainer (rigorous, cites peer-reviewed literature) | https://ourworldindata.org/learning-curve |
| Dario Amodei — *Machines of Loving Grace* (Oct 2024); *The Adolescence of Technology* (Jan 2026) | Informal essays. **No doubling period or learning rate for training costs found in retrieved text.** "markets are typically good at bringing down the cost of high-value technologies over time" | n/a | No — informal essays | https://darioamodei.com/essay/machines-of-loving-grace ; https://darioamodei.com/essay/the-adolescence-of-technology |

---

## COULD NOT VERIFY

1. **Verbatim sentence from Wright (1936).** The paper is paywalled; AIAA returned HTTP 403 for both
   the article and the issue TOC. No quote is offered, and none should be attributed to Wright on the
   strength of this file. If the lecture needs a verbatim line, someone with AIAA access must supply
   the page image.
2. **Amodei essay titled "Some High-level Thoughts on the Direction of AI."** Not present on
   https://darioamodei.com/ (which lists only *The Adolescence of Technology* and
   *Machines of Loving Grace* as essays). Likely a non-existent/incorrect title.
3. **Any explicit Amodei statement of a doubling period or learning rate for AI training costs.**
   Not found in the retrieved (truncated) text of either essay, and no transcript could be retrieved.
   I cannot fully exclude it in the unretrieved portions of the essays.
4. **The name "Henderson's law."** No primary or peer-reviewed source found that uses this label.
   BCG's "experience curve" is attributable to Bruce Henderson, but the *label* is unverified.
5. **BCG 1968/1973 verbatim text.** bcg.com returned DNS failures; the `/ja-jp/` variant returned
   HTTP 200 with an empty (JS-rendered) body. Only the existence and titles are verified, from BCG URLs.
6. **NeurIPS 37 proceedings page for "Algorithmic progress in language models."** ACM DL returned 403;
   the proceedings citation (pp. 58245–58283) comes from a third paper's reference list. The
   arXiv preprint itself is fully verified.
7. **Nature Machine Intelligence publication of "Densing Law of LLMs."** The Nature URL 302s to an
   identity provider that the fetch tool refuses to follow; only the arXiv version is verified.
8. **Gogerty PDF internals.** The PDF could not be parsed, so the 89.2% learning rate, the R² value,
   and all verbatim quotations attributed to Gogerty (2025) rest on the project's HTML page and search
   snippets, not on the paper. The page says R² = 0.9911; search snippets of the PDF say 0.9953.
9. **Epoch AI "Performance per dollar improves around 30% each year"** (Rahman, 2024, used as the
   hardware-adjustment input in arXiv:2511.23455). Verified only as a citation inside another paper;
   the Epoch page itself was not fetched. Treat the "30%/year" figure as secondary.
10. **Whether any peer-reviewed paper fits Wright's law to AI specifically.** After multiple searches I
    found none. I state this as a negative finding of *my search*, not as proof of non-existence.

---

## FETCH FAILURES (all URLs that failed, with the failure mode; retried ≥3× where noted)

| URL | Failure |
|---|---|
| https://arc.aiaa.org/toc/jans/3/4 | HTTP 403 (Cloudflare interstitial "Just a moment...") |
| https://arc.aiaa.org/doi/10.2514/8.155 | HTTP 403 (Cloudflare). Retried. |
| https://www.darioamodei.com/essay/machines-of-loving-grace | DNS `EAI_AGAIN` (2 attempts; succeeded only via `darioamodei.com` without `www.`) |
| https://r.jina.ai/https://darioamodei.com/essay/machines-of-loving-grace | `TypeError: fetch failed` (2 attempts) |
| https://ojs.aaai.org/index.php/AAAI/article/download/34971/37126 | unsupported content type `application/pdf` |
| https://carbonfinancelab.com/wrights-law/data/Gogerty_Wrights_Law_Extended_2025.pdf | unsupported content type `application/pdf` |
| https://dl.acm.org/doi/10.1609/aaai.v39i26.34971 | HTTP 403 |
| https://www.nature.com/articles/s42256-025-01137-0 | cross-origin redirect to `idp.nature.com` not followed |
| https://en.wikipedia.org/wiki/Experience_curve_effects | blocked: hostname resolves to a non-public IP address |
| https://web.archive.org/web/20180131215735/https://en.wikipedia.org/wiki/Experience_curve_effects | `TypeError: fetch failed` (2 attempts) |
| http://web.archive.org/web/20230306215842/https://en.wikipedia.org/wiki/Experience_curve_effects | `TypeError: fetch failed` |
| https://www.dwarkesh.com/p/dario-amodei | `TypeError: fetch failed` (3 attempts) |
| https://singjupost.com/anthropic-ceo-dario-amodeis-interview-on-dwarkesh-podcast-transcript/ | `TypeError: fetch failed` (2 attempts) |
| https://www.cockatoo.com/content/dario-amodei-we-are-near-the-end-of-the-exponential | HTTP 200 but empty body (JS-rendered) |
| https://www.bcg.com/publications/1968/business-unit-strategy-growth-experience-curve | DNS `EAI_AGAIN` |
| https://www.bcg.com/publications/1973/...experience-curve-reviewed-part-ii-the-history | DNS `EAI_AGAIN` |
| https://www.bcg.com/ja-jp/publications/1968/business-unit-strategy-growth-experience-curve | HTTP 200 but empty body (JS-rendered) |
| https://wwwencyclopedia.thefreedictionary.com/Experience+curve+effects | HTTP 403 |
| https://zh.wikipedia.org/zh/%e7%bb%8f%e9%aa%8c%e5%ad%a6%e4%b9%a0%e6%9b%b2%e7%ba%bf | `TypeError: fetch failed` |
| https://darioamodei.com/archive | HTTP 404 (no archive page; essay list is on the homepage) |
| https://www.semanticscholar.org/paper/...Pilz-Heim... | HTTP 202 with empty body (no content returned) |

No `curl`/`wget`/`git`/`node`/build commands were run (bash has no network here, per instructions).

---

## Bottom line for the lecture

1. **The 1936 citation is solid**: Wright, T. P., "Factors Affecting the Cost of Airplanes,"
   *Journal of the Aeronautical Sciences* **3**(4): 122–128, February 1936, DOI `10.2514/8.155`.
   Verified from Crossref, not from the paper body.
2. **Definition:** `C_n = C_1 n^(−b)`, learning rate `LR = 1 − 2^(−b)`, progress ratio `2^(−b)`.
   Worked example (solar): LR = 1 − 2^(−0.31) = 19.3%.
3. **The 1936 paper body is paywalled and I could not read it.** No verbatim Wright quote exists in
   this file, by design.
4. **The Wright's-law-vs-time-line distinction is the key teaching point.** Nearly every "AI costs are
   falling fast" number (Epoch, OWID-adjacent, MIT's Price of Progress, AAAI compute-efficiency work)
   is a **time-based** trend — i.e. Moore's law family, or "algorithmic progress" — and **not**
   Wright's law. Epoch's 8-month compute halving and Epoch's 2.4×/year training-cost *growth* point in
   *opposite* directions and measure different things.
5. **No peer-reviewed paper was found that fits Wright's law to AI costs.** The only genuine
   Wright's-law-on-GPU figures found are from non-peer-reviewed industry research (Gogerty/Carbon
   Finance Lab, 89.2% per doubling, 13 data points) and should be presented with explicit caveats.
6. **"Learning rate" is used loosely in the AI literature** and usually means something else entirely
   (SGD step size, or a time-based annual improvement factor). Flag every such use.
