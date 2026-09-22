# Verified facts: the "Densing Law" and six laws-of-AI claims

Compiled 2026-09-19 for a technical lecture on AI history.
All quotes are verbatim from the source named. Every non-obvious number has a URL.
Uncertainty is flagged inline and collected in **COULD NOT VERIFY** at the end.

Environment note: in this session `bash` has **no network access** (`curl` to arXiv timed out, exit 124), so all
retrieval was done with `web_search` / `web_fetch` only. Intermittent `TypeError: fetch failed` responses were
retried; unrecoverable failures are listed under **FETCH FAILURES**.

---

# TASK A — The "Densing Law" of LLMs

## A.1 Identification: the lecturer was right about the paper, wrong about the author

| Field | Value |
| --- | --- |
| Title (preprint) | **Densing Law of LLMs** |
| arXiv ID | **2412.04315** — confirmed |
| v1 submitted | Thu, 5 Dec 2024, 16:31:13 UTC |
| v2 submitted | Fri, 6 Dec 2024, 11:39:27 UTC |
| arXiv DOI | 10.48550/arXiv.2412.04315 |
| Published title | **Densing law of LLMs** |
| Venue | **Nature Machine Intelligence**, vol. 7, issue 11, pp. **1823–1833** |
| Published online | **6 November 2025** (received 11 Jan 2025; accepted 22 Sep 2025) |
| Journal DOI | **10.1038/s42256-025-01137-0** |
| Cover | Tsinghua says it was the cover article of the 20 Nov 2025 issue |

Sources: <https://arxiv.org/abs/2412.04315> (v1/v2 dates, author list) ·
<https://api.crossref.org/works/10.1038/s42256-025-01137-0> (venue, volume, issue, pages, dates, DOI, published abstract) ·
<https://api.semanticscholar.org/graph/v1/paper/arXiv:2412.04315?fields=title,venue,externalIds,citationCount,publicationVenue,authors> (venue cross-check; 57 citations as of 2026-09)

### Authors

**v1 (7 authors):** Chaojun Xiao, Jie Cai, Weilin Zhao, Guoyang Zeng, Xu Han, Zhiyuan Liu, Maosong Sun.
**v2 / published (10 authors):** the same list **plus** Biyuan Lin, Jie Zhou, Zhi Zheng.
(Verified against the arXiv Atom API: `id_list=2412.04315v1` returns 7 authors, `id_list=2412.04315` returns 10.)

**Affiliations — Tsinghua University and ModelBest Inc., not HKU.**
The v2 HTML byline gives two affiliations: **Tsinghua University** and **ModelBest Inc.**, with
`{han-xu, liuzy, sms}@tsinghua.edu.cn` as corresponding contacts (Xu Han, Zhiyuan Liu, Maosong Sun).
Tsinghua's own news release names the group as Prof. **Sun Maosong**, Assoc. Prof. **Liu Zhiyuan** and
Assistant Research Fellow **Han Xu** (Dept. of Computer Science and Technology), "in collaboration with the
large model open-source community **OpenBMB**", and names **Xiao Chaojun** as first author.

> **Correction to the brief:** **Lingpeng Kong is not an author of this paper**, and no Hong Kong / HKU
> affiliation appears. The paper is a Tsinghua + ModelBest (面壁智能 / Mianbi Intelligence) + OpenBMB work.
> The "HKU / Lingpeng Kong" memory is a misattribution. Source: <https://www.tsinghua.edu.cn/en/info/1245/14611.htm>

## A.2 The exact claim, verbatim

### (a) arXiv v2 — abstract as rendered (HTML / ar5iv)

> "This paper introduces the concept of "capability density" as a new metric to evaluate the quality of the
> LLMs across different scales and describes the trend of LLMs in terms of both effectiveness and efficiency."
>
> "Our further analysis of recent open-source base LLMs reveals an empirical law (Densing Law) that the
> capability density of LLMs grows exponentially over time. More specifically, using some widely used
> benchmarks for evaluation, **the capability density of LLMs doubles approximately every three months.**"

Sources: <https://arxiv.org/html/2412.04315v2> · <https://ar5iv.labs.arxiv.org/html/2412.04315>

### (b) The formal "Densing Law" statement (arXiv v2, Highlights + §1.1)

> "**Densing Law.** The maximum capability density of LLMs exhibits an exponential growth trend over time.
> ln(ρ_max) = A·t + B. Here, ρ_max is the maximum capability density of LLMs at time t."

### (c) The precise 3.3-month figure (arXiv v2, Figure 1 caption + footnote)

> "A trend is fitted between maximum capability density and release date, revealing that **A ≈ 0.007** with
> **R² ≈ 0.93**. This indicates the maximum capability density of LLMs **doubles approximately every 3.3
> months**¹. That means, around three months, it is possible to achieve performance comparable to current
> state-of-the-art LLMs using a model with half the parameter size."
>
> Footnote 1: "**The capability density growth rate is affected by specific evaluation benchmarks and
> reference models.**"

Corollary 2 restates it: "Densing Law indicates that the density of LLMs doubles every **3.3** months."

**Unit of t (flag):** the paper writes `A ≈ 0.007` without stating the unit of `t` in the text I could reach.
The stated 3.3-month doubling is only self-consistent if **t is in days**: ln 2 / 0.007 ≈ 99 days ≈ 3.3
months. This unit is *inferred*, not quoted. Treat it as an inference.

### (d) The published Nature Machine Intelligence abstract (verbatim, via Crossref)

> "…we introduce the concept of **capability density** as a metric to evaluate the quality of the LLMs …
> Intuitively, capability density can be understood as the capability contained within each unit of model
> parameters. … Here we show an empirical observation, called the '**densing law**', that the capability
> density of LLMs grows exponentially over time. More specifically, using widely used benchmarks for
> evaluation, **the maximum capability density of open-source LLMs doubles approximately every 3.5 months.**
> This reveals that both parameter requirements and inference costs of LLMs for achieving equivalent
> performance decrease exponentially…"

Source: <https://api.crossref.org/works/10.1038/s42256-025-01137-0>

### (e) Terminology inconsistency — "capacity density" vs "capability density"

The **registered arXiv metadata abstract** (both `v1` and `v2`, via the arXiv Atom API) says
"**capacity density**":

> "This paper introduces the concept of ``\textit{capacity density}'' as a new metric …"

while the **rendered v2 paper** (HTML/ar5iv) and the **published Nature MI abstract** say
"**capability density**". Both spellings are therefore "in the paper". The body text, the Highlights and the
published version use **capability density**; the metadata/abstract string uses **capacity density**.
The lecturer's "capability density" matches the paper body and the published version.

## A.3 What "capability density" actually is — NOT performance ÷ log(parameters)

This is the part of the lecturer's framing that is **wrong**. The paper does not define density as
benchmark performance divided by log parameter count, nor as "performance per parameter" in any direct sense.

Verbatim definition (§2.1, eq. 1):

> "**ρ(M) = N̂(S_M) / N_M = f⁻¹(S_M) / N_M**"

where the **effective parameter size** is defined as:

> "the parameter size required by a reference model to achieve equivalent performance"

So: **density = (parameter count a reference model would need to match this model's score) ÷ (this model's
actual parameter count)**. Density is therefore **relative to a specific reference-model scaling curve** —
the paper's own abbreviation is "(relative) capability density" (footnote 2).

The pipeline (§2.1–§2.4):
1. Train small **reference models** (0.005B, 0.03B, 0.1B, 0.2B, 0.4B, 0.8B — Table 1) on the MiniCPM-3-4B
   corpus, 10–60 tokens/param, and fit a **conditional-loss power law**
   `L = a·N^(−α) + b·D^(−β)` (eq. 2), where `L = −log(P(answer | instruction))`.
2. Fit **loss → downstream score** with a sigmoid, `S = c/(1 + e^(−γ(L−l))) + d` (eq. 3), using well-trained
   MiniCPM-3 models and checkpoints (0.5B → tens of B).
3. Invert: `N̂(S_M) = ((L̂(S_M) − b·D₀^(−β)) / a)^(−1/α)` at a **fixed training-data size D₀ = 1T tokens**
   (eq. 4). Density is thus defined "at 1T tokens".

Two consequences the lecturer should state carefully:
- The metric is **not** a pure benchmark number; it is an **inverse-scaled effective parameter count**.
- Because D is pinned at D₀ = 1T tokens, density is **not** "capability per actual training compute".
- Because the reference set is MiniCPM-3-derived, densities are only comparable **within that reference frame**.

## A.4 Scope: which models, which benchmarks, what date range

- **arXiv version:** "we analyze **29** widely-used open-source pre-trained base models"; evaluation on
  **5** benchmarks — MMLU, BBH, MATH, HumanEval, MBPP — chosen "since the release of Llama-1, as most
  open-source models released before Llama-1 cannot achieve meaningful performance on our selected
  datasets". Date range is therefore ≈ **Feb 2023 (Llama-1) to the Dec 2024 writing**.
  *Caution:* the HTML renders "measured by their performance on 55 widely-used benchmarks". That "55" is a
  LaTeX artifact of "**5** widely-used benchmarks"; the paper lists exactly five, and says "Based on our
  evaluation on 5 widely-used benchmarks, MMLU, BBH, MATH, HumanEval, and MBPP". Do not repeat "55".
- **Not a single model family.** The set spans Llama-1/2/3, Falcon, MPT, Phi-1/1.5/3, Mistral, StableLM,
  TinyLlama, MiniCPM, etc. Evaluated models are **base (pre-trained) models only**, no instruction tuning.
- **Published Nature MI version (different numbers):** **51** open-source LLMs, **February 2023 – April
  2025**, R² = 0.934. Tsinghua's release: "from February 2023 to April 2025, the maximum capability density
  of open-source LLMs approximately doubles every **3.5 months**" and "an analysis of **51** open-source
  LLMs". Source: <https://www.tsinghua.edu.cn/en/info/1245/14611.htm>

## A.5 Explicit caveats the authors state

Quoted verbatim from the arXiv v2 text:

1. **Benchmark/reference dependence** (Figure 1 footnote 1): "The capability density growth rate is affected
   by specific evaluation benchmarks and reference models."
2. **Benchmark sensitivity** (§1.1): "It is worth noting that using different evaluation benchmarks may
   result in slight variations in the estimation and growth rate of model density. We encourage the
   community to develop more comprehensive evaluation benchmarks for LLMs to ensure more accurate
   measurements of density."
3. **Test-set contamination is unresolved** (§3.1): "Notably, many pre-trained models also introduce
   supervised finetuning datasets in the pre-training phase, leading to the test set contamination issue …
   Thus, the inaccurate density estimation remains to be solved, which we leave for future work."
4. **Base models only** (§3.1): "we only evaluate the density of pre-trained base models without further
   supervised fine-tuning and preference learning", because alignment "introduces excessive confounding
   factors" and because "The Scaling Law for the performance of LLMs with alignment remains an open question".
5. **Fixed data budget** (§2.4): effective parameter size is computed "defaultly us[ing] D = D₀ = 1T tokens".
6. **Density is relative** (footnote 2): "in this work, we use 'density' to refer to '(relative) capability
   density'"; the reference models are set to density 1 as the baseline.
7. **Corollary 3 caveat by construction:** the post-ChatGPT acceleration ("increased by 50%") is a
   comparison of fitted pre/post slopes on a short series, not an independent measurement.
8. **Could not retrieve §5 "Limitations and Future Directions" verbatim** — see COULD NOT VERIFY. The
   caveats above are from the abstract, Highlights, §1.1, §2.4 and §3.1, which I did read.

## A.6 Criticism, replication and follow-ups

- **No peer-reviewed criticism or formal replication of the Densing Law was found.** I pulled the full
  Semantic Scholar citation list for 2412.04315 (57 citing works, retrieved 2026-09) and scanned all titles:
  none is a critique, refutation or replication of the density metric. Searches for
  `"densing law" critique/flawed/overestimates`, `"capability density" criticism`, and
  `densing law replication` returned only the paper itself, press coverage, and unrelated work.
  **State this as a negative finding, not as proof that criticism does not exist.**
  Source: <https://api.semanticscholar.org/graph/v1/paper/arXiv:2412.04315/citations?fields=title,venue,year,externalIds&limit=100>
- **Refinement 1 (by the authors, in-paper):** the published version changes the headline numbers from
  ~3.0–3.3 months / 29 models to **3.5 months / 51 models**, i.e. the *published* claim is slightly weaker
  than the *preprint* figure caption. The published abstract says **"doubles approximately every 3.5 months"**.
- **Refinement 2 (secondary, flagged, and partly REFUTED):** a Chinese tech-media article (36kr / 新智元,
  2026-04-13) claims the paper re-measured on the contamination-filtered **MMLU-CF** benchmark with R² rising
  to 0.953, and claims independent confirmation by **METR ("AI capabilities double every 88.6 days", report
  dated 2026-04-03)** and by a Meta "scaling ladder" (Muse Spark, 2026-04-08). Source (secondary, low
  confidence): <https://eu.36kr.com/en/p/3765157269684738>
  **The METR part of that claim does not match METR's published paper.** METR's primary work, Kwa, West,
  Becker et al., "Measuring AI Ability to Complete Long Tasks" (arXiv 2503.14499), reports a **different
  metric** (the *50% task-completion time horizon*) and a **different number**:
  > "frontier AI time horizon has been doubling approximately every seven months since 2019"
  > "time horizon has doubled every **212 days** with a 95% bootstrapped confidence interval 171–249 days"
  The same paper also warns that a 2024-only fit gives ~3 months, and that this makes extrapolation
  fragile: "restricting our data further to 2024-only models produced a different trend with time horizon
  doubling about every three months, so any extrapolation into the future would not be robust."
  So: METR measures **task-duration horizon**, not parameter efficiency — conflating it with the Densing Law
  is a category error, and "88.6 days" is **not** METR's published doubling time.
  Source: <https://ar5iv.labs.arxiv.org/html/2503.14499>
  MMLU-CF itself is a real peer-reviewed artifact cited by the Nature paper: Zhao, Q. et al. "MMLU-CF: a
  contamination-free multi-task language understanding benchmark", ACL 2025, DOI 10.18653/v1/2025.acl-long.656.
- **Conflation warning for the lecture (do not skip this).** A very plausible source of a "doubling every
  ~3.x months" memory is *not* the Densing Law but the much older OpenAI result: Amodei & Hernandez,
  "AI and Compute" (2018), which found AI **training compute** doubling roughly every **3.4 months**
  (2012–2018). METR's related-work section restates it: "Amodei and Hernandez 2018 observed that AI
  training compute usage has been increasing exponentially, doubling approximately every 3.4 months between
  2012 and 2018". That is a different quantity (training compute, not parameter efficiency) on a different
  period (2012–2018, not 2023–2025). Source: <https://ar5iv.labs.arxiv.org/html/2503.14499> (quoting
  Amodei & Hernandez 2018); primary: <https://openai.com/index/ai-and-compute/>
- **Related follow-up (preprint, not a critique):** Mingdeng Du, "Tiered Super-Moore's Law: Price Evolution,
  Production Frontiers, and Market Competition in Large Language Model Inference Services", arXiv 2603.28576
  (March 2026) — measures LLM token-price decline directly (economy-tier price half-life **1.10 years**,
  mid-tier 1.55 years, flagship R² = 0.031) and a **~600-fold** token-price decline since GPT-3 (2020). It
  refines the *inference-cost corollary* of the Densing Law rather than the density law itself.
  <https://ar5iv.labs.arxiv.org/html/2603.28576> (preprint; **not peer-reviewed**)
- **In-paper cost corollary, for reference:** arXiv v2 claims "from January 2023 to the present, the
  inference cost of GPT-3.5-level models has decreased by **266.7 times**". Tsinghua's release restates it
  as $20/M tokens at end-2022 → ≈1/266th by August 2024. The Nature reference list cites a16z's
  "LLMflation" post for the inference-cost claim, i.e. the cost numbers rest on an **industry blog**, not a
  peer-reviewed measurement. Sources: arXiv v2 §1.1; <https://a16z.com/llmflation-llm-inference-cost/>

## A.7 Verdict on the lecturer's version

| Lecturer said | Verdict | Precise position |
| --- | --- | --- |
| "Densing Law of LLMs", arXiv 2412.04315 | ✅ correct | Title and ID confirmed |
| "capability density" | ✅ correct | Used in the paper body, Highlights and published abstract (arXiv *metadata* says "capacity density") |
| "doubles approximately every 3.3 months" | ⚠️ defensible but version-dependent | Preprint Fig. 1 caption / footnote: "**3.3 months**" (A ≈ 0.007, R² ≈ 0.93). Preprint abstract: "**approximately every three months**". **Published Nature MI abstract: "approximately every 3.5 months"** |
| "performance per parameter" / "benchmark performance divided by log of parameter count" | ❌ wrong | Density = effective parameter size ÷ actual parameter size, where effective size is the inverse of a fitted reference scaling law (loss `aN^−α + bD^−β`, then sigmoid loss→score), at D₀ = 1T tokens. No log-of-parameters divisor appears |
| "researchers including Lingpeng Kong (HKU group)" | ❌ wrong | Authors are Tsinghua + ModelBest + OpenBMB. **Lingpeng Kong is not an author**; no HKU affiliation. Corresponding authors: Xu Han, Zhiyuan Liu, Maosong Sun |
| "open-source base LLMs, several benchmarks, 2023 onwards" | ✅ correct | 29 models / 5 benchmarks (MMLU, BBH, MATH, HumanEval, MBPP) in the preprint; 51 models, Feb 2023–Apr 2025 in the published version |
| Later published in a venue? | ✅ yes | **Nature Machine Intelligence** 7(11):1823–1833, online 6 Nov 2025, DOI 10.1038/s42256-025-01137-0 |

**One-sentence verdict:** the lecturer has the paper, the term "capability density" and the ~3-month
doubling right, but has mis-stated the *definition* (it is effective-vs-actual parameter ratio, not
performance per parameter) and wrongly attributed it to Lingpeng Kong / HKU instead of Tsinghua + ModelBest;
and the number should be quoted as "**approximately every three months**" (preprint) or "**approximately
every 3.5 months**" (published), with "3.3 months" appearing only in the preprint's Figure 1 caption.

---

# TASK B — Laws-of-AI claims

## B.0 Laws table

| Law | Original author | Date | Exact original statement | AI relevance | URL |
| --- | --- | --- | --- | --- | --- |
| Goodhart's law | Charles Goodhart | presented July 1975; volume dated **1976** by the RBA; sentence best documented at p. 96 of the **1984** book | "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." | Benchmark/leaderboard gaming, reward hacking, proxy objectives in RLHF | <https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html> |
| The popular "measure/target" form | **Keith Hoskin (1996)** coined; **Marilyn Strathern (1997)** popularised — *not Goodhart himself* | 1996 / 1997 | "When a measure becomes a target, it ceases to be a good measure." | Same as above; the form usually quoted on slides | <https://forrt.org/glossary/english/goodhart_s_law/> |
| The Bitter Lesson | Richard S. ("Rich") Sutton | **13 March 2019** | "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective, and by a large margin." | Justifies scale/compute-first methods and search+learning over hand-built knowledge | <http://www.incompleteideas.net/IncIdeas/BitterLesson.html> |
| Amdahl's law | Gene M. Amdahl | 1967 (AFIPS Spring Joint Computer Conference) | *S* = 1 / ((1 − *p*) + *p*/*s*); as *s* → ∞, *S* → 1/(1 − *p*) | Serial fractions bound distributed training and inference speedup | <https://doi.org/10.1145/1465482.1465560> |
| Wright's law (learning curve) | Theodore Paul Wright | 1936 | *C*_n = *C*_1 · *n*^(−*b*); learning rate = 1 − 2^(−*b*) (constant % cost fall per doubling of cumulative production) | Hardware/inference cost declines; **no peer-reviewed Wright's-law fit to AI exists** | <https://doi.org/10.2514/8.155> |
| Roofline model | Williams, Waterman & Patterson | 2009 (CACM 52(4)) | attainable perf. = min(peak FLOP/s, arithmetic intensity × peak memory bandwidth) | Explains why autoregressive **decode** is memory-bandwidth-bound, not FLOP-bound | <https://doi.org/10.1145/1498765.1498785> |
| Zipf's law | George Kingsley Zipf | 1935 book / 1949 book | *f*(*r*) ∝ 1/*r*^α with α ≈ 1 | Why natural language is long-tailed and word-level vocabularies fail — the motivation for subword tokenizers | <https://pmc.ncbi.nlm.nih.gov/articles/PMC4176592/> |

---

## B.1 Goodhart's law — and a correction to the attribution

### (a) The original, in the monetary-policy context

Original sentence, as canonically quoted:

> "Any observed statistical regularity will tend to collapse once pressure is placed upon it for control
> purposes."

**Provenance is messier than "Goodhart 1975" suggests, and this matters for the slide:**

- The paper **was presented at the Reserve Bank of Australia's Conference in Monetary Economics, Sydney,
  July 1975**, and published in *Papers in Monetary Economics*, Vol. I (RBA). The RBA's **own** retrospective
  bibliography dates the volume **1976**: "*Papers in Monetary Economics*. Vol. I and II. Sydney : Reserve
  Bank of Australia, **1976**. Revised version of seven papers presented at the Conference in Monetary
  Economics, Sydney, July 1975". The same RBA page footnotes the Goodhart paper as "the first reference to
  what became known as 'Goodhart's Law'". <https://www.rba.gov.au/publications/rdp/1990/9013/conference-volumes.html>
- The sentence itself is most reliably **documented at page 96 of Goodhart's 1984 book *Monetary Theory and
  Practice***. McIntyre (DAMTP, Cambridge), quoting the Bank of England's own page on Goodhart:
  > "Professor Charles Goodhart FBA was Chief Adviser to the Bank of England. … giving his own statement of
  > the law, as published in his book *Monetary Theory and Practice*, page 96: 'Any observed statistical
  > regularity will tend to collapse once pressure is placed upon it for control purposes.'"
  <http://www.damtp.cam.ac.uk/user/mem2//papers/LHCE/goodhart.html>
- Many papers instead cite **1975**: e.g. Manheim & Garrabrant, "Categorizing Variants of Goodhart's Law",
  arXiv:1803.04585, ref. [1]: "Charles E. Goodhart *Problems of Monetary Management: The U.K. Experience*
  1975. *Papers in Monetary Economics*. Reserve Bank of Australia. I."; and El-Mhamdi & Hoang,
  arXiv:2410.09638, attribute the sentence to "[Goo75]".
- **Flag:** whether the sentence literally appears in the 1975/1976 conference version could **not** be
  verified (both primary texts inaccessible). Safe lecture wording: "Goodhart's law comes from his 1975
  RBA paper on UK monetary management; the famous wording is documented at p. 96 of his 1984
  *Monetary Theory and Practice*."

### (b) The popular form — who actually wrote it

> "When a measure becomes a target, it ceases to be a good measure."

**Citation (verified):** Strathern, Marilyn (1997). "'Improving ratings': audit in the British University
system." *European Review* **5**(3): **305–321**, July 1997. Cambridge University Press.
**DOI: `10.1002/(SICI)1234-981X(199707)5:3<305::AID-EURO184>3.0.CO;2-4`**
(Crossref-verified: container *European Review*, vol. 5, issue 3, pages 305-321, published-print 1997-07,
author Marilyn Strathern.) The page generally cited for the sentence is **p. 308** (FORRT glossary;
Reagle 2014). The lecturer's citation (1997, *European Review* 5(3):305–321) is **correct**.
<https://forrt.org/glossary/english/goodhart_s_law/> · <https://api.crossref.org/works/10.1002/(sici)1234-981x(199707)5:3%3C305::aid-euro184%3E3.0.co;2-4>

### ⚠️ CORRECTION: Strathern attributed it to **Keith Hoskin (1996)**, not directly to Goodhart

The brief states "Strathern herself attributed it to Goodhart." The best available evidence says her
immediate source was **Hoskin's 1996 book chapter**, which is what attached the phrasing to Goodhart's law:

- McIntyre (URL above): "Professor Marilyn Strathern FBA, **following Hoskin (1996, see below)**, has
  re-stated Goodhart's Law more succinctly and more generally: 'When a measure becomes a target, it ceases
  to be a good measure.'" McIntyre's Hoskin reference: *The 'awful idea of accountability': inscribing
  people into the measurement of objects*, in R. Munro & J. Mouritsen (eds.), *Accountability: Power, ethos
  and the technologies of managing*, London: International Thomson Business Press, 1996, pp. 265–282.
- Majka & El-Mhamdi, "The Strong, Weak and Benign Goodhart's law", arXiv:2505.23445: "From Charles
  Goodhart's remark in the context of monetary economics [5] to its **reformulation by Keith Hoskin** [9]
  and its **popularisation by Marylin Strathern** [16], Goodhart's law remained unformalised."
- Wikipedia (via mirror) describes the same chain: Hoskin wrote it in a 1996 chapter; "In a 1997 paper …
  Marilyn Strathern **cited Hoskins** expressing Goodhart's Law as 'When a measure becomes a target, it
  ceases to be a good measure'".
- **Could not verify:** the full text of Strathern (1997) is paywalled, so a verbatim attribution sentence
  written by Strathern herself could not be read. The Hoskin chapter PDF
  (<https://gwern.net/doc/statistics/decision/1996-hoskin.pdf>) is unreadable by the fetch tool.
- **Cleanest defensible slide attribution:** Hoskin (1996) formulated the measure/target phrasing;
  Strathern (1997) popularised it; both were restating **Goodhart's** law. Do not put the measure/target
  sentence in quotation marks under Goodhart's name alone.

### (c) Is the popular form misattributed to Goodhart himself? Yes, routinely

- Karwowski et al., "Goodhart's Law in Reinforcement Learning", arXiv:2310.09144, fold the two together:
  "an informal principle often stated as 'any observed statistical regularity will tend to collapse once
  pressure is placed upon it for control purposes' (Goodhart 1984), **or more simply: 'when a measure
  becomes a target, it ceases to be a good measure'**" — with no mention of Strathern or Hoskin.
- Wikipedia's lead attributes the measure/target sentence to "Goodhart's law … named after British
  economist Charles Goodhart", referencing only Goodhart (1975).
- For AI: the most useful treatments are Manheim & Garrabrant's four-variant taxonomy (regressional,
  extremal, causal, adversarial — arXiv:1803.04585) and the RL-specific formalisation in
  Karwowski et al. (arXiv:2310.09144). Goodhart is the right lens for **benchmark gaming, reward hacking
  and proxy-objective failure** in modern LLMs.

---

## B.2 The Bitter Lesson — Rich Sutton

- **Author:** Richard S. ("Rich") Sutton.
- **Exact date printed on the page: 13 March 2019.**
- **Where published:** Sutton's own site. The canonical, fetchable URL is
  **<http://www.incompleteideas.net/IncIdeas/BitterLesson.html>** (HTTP 200; `http://incompleteideas.net/...`
  serves identical text). **Only the `http://` form worked** — both `https://` variants failed repeatedly.
- **`sutton.cs.ualberta.ca` does NOT resolve** (`getaddrinfo ENOTFOUND`, 2 attempts). The brief's suggestion
  that it was published there could **not** be verified; no archive endpoint was reachable either.
  **Do not print an https canonical link or the ualberta host without rechecking.**

**Opening thesis sentence (verbatim):**

> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage
> computation are ultimately the most effective, and by a large margin."

**Closing sentence (verbatim):**

> "Building in our discoveries only makes it harder to see how the discovering process can be done."

**The numbered core argument (verbatim):**

> "The bitter lesson is based on the historical observations that 1) AI researchers have often tried to
> build knowledge into their agents, 2) this always helps in the short term, and is personally satisfying
> to the researcher, but 3) in the long run it plateaus and even inhibits further progress, and
> 4) breakthrough progress eventually arrives by an opposing approach based on scaling computation by
> search and learning."

**Misquote risk:** the most common corruption is dropping ", and by a large margin." from the opening
sentence; a copy on GitHub rewrites the numbered list as prose and silently drops clause 4. Quote from the
original page.

**AI relevance:** this is the canonical textual statement of the compute-first worldview — it underwrites
scaling laws, the transformer/LLM era, and search+learning systems (AlphaGo/AlphaZero, MuZero), and it is
the standard rebuttal to hand-engineered knowledge and feature engineering.

---

## B.3 Amdahl's law

**Citation (VERIFIED via Crossref — the brief's DOI is correct):**
Gene M. Amdahl, "Validity of the single processor approach to achieving large scale computing
capabilities", *AFIPS '67 (Spring): Proceedings of the April 18–20, 1967, Spring Joint Computer
Conference*, Atlantic City, NJ, 1967, pp. **483–485**.
**DOI: 10.1145/1465482.1465560** — <https://doi.org/10.1145/1465482.1465560>
(also confirmed via Semantic Scholar and Mendeley).

**Exact formulation:**

> **S = 1 / ((1 − p) + p/s)**

where *p* = the fraction of the work that can benefit from the improvement (0 ≤ p ≤ 1), *s* = the speedup
factor applied to that fraction, and (1 − *p*) = the fraction that remains serial (the bottleneck).
**Limit:** as *s* → ∞, **S → 1/(1 − p)** — a hard ceiling set by the serial fraction.
(Formula phrasing sourced from the Cornell Virtual Workshop, which uses the equivalent
S = 1/(F_s + F_p/N) with S → 1/F_s: <https://cvw.cac.cornell.edu/parallel/efficiency/amdahls-law>.)

**Could not verify:** the paper is closed access (Semantic Scholar reports openAccessPdf status CLOSED;
ACM DL returns 403 to the fetch tool), so **no verbatim sentence from the body is available and none is
invented here.** In particular, whether the 1967 paper itself prints the closed form above could not be
confirmed — the familiar closed form is a later standardisation of the argument. Only the abstract is
reproducible, and only from a secondary (Scopus-reproduced) source.

**Scaled-speedup counterpart (for contrast):** John L. Gustafson, "Reevaluating Amdahl's law",
*Communications of the ACM* **31**(5):532–533, May 1988, DOI **10.1145/42411.42415**.
Amdahl = fixed problem size / strong scaling; Gustafson = fixed run time / weak scaling.

**AI relevance:** the serial fraction bounds how much a training or serving job can be sped up by adding
accelerators — it is the standard explanation for diminishing returns in data/tensor/pipeline parallelism,
for the cost of synchronisation and all-reduce, and for why some inference steps (e.g. sampling loops)
resist parallelisation.

---

## B.4 Wright's law and its (non-)application to AI

### The 1936 original

**Citation (VERIFIED via Crossref, not from the paper body):**
Theodore Paul Wright, "Factors Affecting the Cost of Airplanes", *Journal of the Aeronautical Sciences*
**3**(4): **122–128**, February 1936 (AIAA; author affiliation Curtiss-Wright Corp.).
**DOI: 10.2514/8.155** — <https://doi.org/10.2514/8.155> (Crossref: <https://api.crossref.org/works/10.2514/8.155>)

**Statement and maths:**

> each **doubling of cumulative production** produces a **constant percentage reduction in unit cost**.
> *C*_n = *C*_1 · *n*^(−*b*), progress ratio = 2^(−*b*), **learning rate = 1 − 2^(−*b*)**, so *b* = −log₂(1 − LR).

(Form and the worked solar example LR = 1 − 2^(−0.31) = 19.3% from Our World in Data:
<https://ourworldindata.org/learning-curve>.)

**Could not verify:** the 1936 body is paywalled; AIAA returned **HTTP 403** for both the article and the
Vol. 3 No. 4 table of contents. **No verbatim Wright sentence is available and none is invented here.**
Anyone needing a direct quote must obtain AIAA access. Note also that the phenomenon travels under several
names (learning curve, experience curve, Henderson's law) — no primary source for the "Henderson's law"
label was found.

### Has Wright's law been applied credibly to AI compute or model costs?

**Headline negative finding: no peer-reviewed paper was found that fits Wright's law (cost vs *cumulative
production*) to AI/ML. All peer-reviewed AI cost work found is *time*-based, i.e. Moore's-law family, not
Wright's law.** Treat every "AI learning rate" claim with that distinction in hand.

| Source | What it claims | Rate | Peer-reviewed? | URL |
| --- | --- | --- | --- | --- |
| Epoch AI — Ho, Besiroglu, Erdil et al., "Algorithmic progress in language models", arXiv:2403.05812 | "the compute required to reach a set performance threshold has halved approximately every 8 months, with a 95% confidence interval of around 5 to 14 months" | ~8-month halving (CI 5–14), **vs time** | **Yes** — NeurIPS 37 (2024), pp. 58245–58283 | <https://arxiv.org/abs/2403.05812> |
| Epoch AI — dollar training cost (Cottier, 2023) | cost "grown by 0.49 orders of magnitude per year (90% CI 0.37–0.56)" | 0.49 OOM/yr **growth** | No (report) | <https://epoch.ai/publications/trends-in-the-dollar-training-cost-of-machine-learning-systems> |
| Epoch AI — "The rising costs of training frontier AI models", arXiv:2405.21015 | "grown precipitously at a rate of 2.4× per year since 2016 (90% CI: 2.0× to 2.9×)" | 2.4×/yr **growth** | No (preprint) | <https://arxiv.org/abs/2405.21015> |
| Epoch AI Data Insight (Mar 2025) | "the price to achieve GPT-4's performance … fell by 40× per year … ranging from 9× to 900× per year" | 9×–900×/yr | No | <https://epoch.ai/data-insights/llm-inference-price-trends> |
| Pilz, Heim & Brown, AAAI-25 | ImageNet-93% classifier >$1,000 (2017) → $5 (2021); accelerators doubled price-perf ~2 yr; vision algorithmic compute halved every 9 months | compute-efficiency (Moore/scaling family, **not** Wright's law) | **Yes** — DOI 10.1609/aaai.v39i26.34971 | <https://doi.org/10.1609/aaai.v39i26.34971> |
| Gogerty / Carbon Finance Lab (2025), "Wright's Law Across 98 Technologies" | "GPU cost per GFLOPS dropped **89.2%** every time cumulative shipments doubled" (13 points, 2003–2025) | **genuine Wright's-law learning rate ≈ 89.2%** | **No** (SSRN/industry; page R² = 0.9911 vs PDF snippets 0.9953 — inconsistent) | <https://carbonfinancelab.com/wrights-law/> |
| Gundlach, Lynch, Mertens & Thompson, arXiv:2511.23455 | "5× to 10× per year"; algorithmic ~"3× per year" | vs time | No (NeurIPS **workshop** only) | <https://arxiv.org/abs/2511.23455> |
| Our World in Data — Roser, "Learning curves" | solar "declined by 20% with each doubling of global cumulative capacity" | LR ≈ 20% (solar) — **OWID does NOT apply Wright's law to AI** | No (explainer) | <https://ourworldindata.org/learning-curve> |
| Dario Amodei, essays | **no doubling period or learning rate for AI training costs found** in the retrieved text | — | No (essays) | <https://darioamodei.com/essay/machines-of-loving-grace> |

**Amodei specifically:** his site lists only *Machines of Loving Grace* (Oct 2024) and *The Adolescence of
Technology* (Jan 2026). **An essay titled "Some High-level Thoughts on the Direction of AI" appears not to
exist on his site**; no doubling-period/learning-rate statement for training costs could be verified.
(If the lecture needs Amodei on cost trends, cite his 2025 Davos/blog remarks only after locating the
primary text.)

**Framing warning for the slide:** Epoch's ~8-month *efficiency* halving coexists with 2.4×/yr
training-cost **growth** — opposite directions, different quantities. And in AI, "learning rate" almost
always means the SGD step size, not Wright's progress ratio; never use the bare phrase.

---

## B.5 Roofline model and memory-bound decoding

### The original paper — note the title correction

**Citation (VERIFIED via Crossref):**
Samuel Williams, Andrew Waterman & David Patterson, "Roofline: An Insightful Visual Performance Model
for **Multicore** Architectures", *Communications of the ACM* **52**(4): **65–76**, April 2009.
**DOI: 10.1145/1498765.1498785** — <https://doi.org/10.1145/1498765.1498785>
⚠️ **The brief's title "…for Multiclass Computing Architectures" is wrong** — it is "**Multicore**".

**Earlier version:** UC Berkeley tech report **UCB/EECS-2008-134**, 17 Oct 2008, titled "Roofline: An
Insightful Visual Performance Model for **Floating-Point Programs and Multicore** Architectures"
(<https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-134.html>; also LBNL report DOI
10.2172/1407078). **No SC 2008 conference version was found.** Cite the CACM 2009 version.

**Formula:**

> attainable performance = **min**( peak floating-point performance, arithmetic intensity × peak memory
> bandwidth )

where **arithmetic intensity = FLOPs ÷ bytes of DRAM/HBM traffic**. The crossover point (the "ridge") is
peak FLOP/s ÷ peak bandwidth; below it a kernel is memory-bound, above it compute-bound.
(Definition corroborated by NERSC's roofline documentation: <https://docs.nersc.gov/tools/performance/roofline/>.)

**Could not verify:** the paper body is inaccessible — dl.acm.org and cacm.acm.org both return **HTTP 403**
(Cloudflare) and the open-access copies are PDFs the fetch tool rejects. The only verbatim line available
is the Crossref abstract sentence: "The Roofline model offers insight on how to improve the performance of
software and hardware." Whether the original says "arithmetic" vs "operational" intensity could not be
confirmed.

### Why transformer inference — especially decoding — is memory-bandwidth-bound

**Best peer-reviewed, on-the-nose quote** — Leviathan, Kalman & Matias, "Fast Inference from Transformers
via Speculative Decoding", **ICML 2023 (Oral)**, arXiv:2211.17192:

> "We additionally observe that inference from large models is often not bottlenecked on arithmetic
> operations, but rather on memory bandwidth and communication, so additional computation resources might
> be available."
<https://arxiv.org/html/2211.17192v2>

**Also peer-reviewed** — Pope et al., "Efficiently Scaling Transformer Inference", **MLSys 2023**,
arXiv:2211.05102:

> "The large memory footprint gives rise to a large amount of memory traffic to load the parameters and KV
> cache from high-bandwidth memory (HBM) into the compute cores for each step, and hence a large total
> memory bandwidth required to meet a given latency target."
>
> "At small batch sizes and sequence lengths, the time to load weights dominates."
<https://arxiv.org/html/2211.05102v1>

**Not peer-reviewed but commonly cited** — NVIDIA technical blog: "The speed at which the data (weights,
keys, values, activations) is transferred to the GPU from memory dominates the latency … In other words,
this is a memory-bound operation." <https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/>
And Noam Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", arXiv:1911.02150 (preprint):
"incremental inference … is often slow, due to the memory-bandwidth cost of repeatedly loading the large
'keys' and 'values' tensors."

**Be precise about the near-misses:** FlashAttention (Dao et al., NeurIPS 2022, arXiv:2205.14135) says only
that "most operations in Transformers are bottlenecked by memory accesses" — it does **not** claim decoding
is memory-bound. The vLLM paper (Kwon et al., SOSP 2023, arXiv:2309.06180) says serving is "bottlenecked by
memory" but does not give the decode-phase arithmetic-intensity argument.

**The mechanism, in one line for the slide:** during autoregressive decode each new token requires reading
the entire weight matrix and the KV cache from HBM while performing only O(1) FLOPs per weight, so
arithmetic intensity is on the order of a few FLOPs/byte — far below the ~100+ FLOPs/byte ridge of modern
GPUs — leaving throughput capped by memory bandwidth, whereas **prefill** performs large matmuls at high
arithmetic intensity and is compute-bound. That asymmetry is why batching, KV-cache compression,
quantisation and speculative decoding (all bandwidth-reduction tricks) are the standard decode
optimisations.

---

## B.6 Zipf's law and tokenizers

### Original formulation and origin

George Kingsley Zipf: *The Psycho-Biology of Language: An Introduction to Dynamic Philology* (Boston:
Houghton Mifflin, 1935 — some sources, including Piantadosi, cite it as **1936**; a London reprint also
exists, so do not state a single year without a caveat) and *Human Behavior and the Principle of Least
Effort: An Introduction to Human Ecology* (Cambridge, MA: Addison-Wesley, 1949).

**Formulation (verbatim from a peer-reviewed review):**

> "The *r*th most frequent word has a frequency *f*(*r*) that scales according to **f(r) ∝ 1/r^α** for
> **α ≈ 1** (Zipf, 1936, 1949)."

with Mandelbrot's generalisation "f(r) ∝ 1/(r+β)^α for α ≈ 1 and β ≈ 2.7". Same source, on the shape:
"there are few very high-frequency words that account for most of the tokens in text (e.g., 'a,' 'the,'
'I,' etc.) and many low-frequency words (e.g., 'accordion,' 'catamaran,' 'ravioli')."
Source: **Piantadosi, S. T. (2014), "Zipf's word frequency law in natural language: A critical review and
future directions", *Psychonomic Bulletin & Review* 21(5):1112–1130, DOI 10.3758/s13423-014-0585-6**,
<https://pmc.ncbi.nlm.nih.gov/articles/PMC4176592/>

**Could not verify:** neither book's text was fetchable (HathiTrust / Internet Archive copies failed), so
there is **no verbatim sentence from Zipf himself** here. The equation is quoted from Piantadosi.

### The tokenizer connection — a warning about a commonly repeated claim

**Verdict: the Zipf/long-tail connection is ABSENT from the retrievable text of the three papers usually
cited for it.** No sentence citing Zipf's law or "the long tail" was found in Sennrich, Haddow & Birch
(2016), "Neural Machine Translation of Rare Words with Subword Units" (arXiv:1508.07909 / ACL P16-1162);
Kudo (2018), "Subword Regularization" (arXiv:1804.10959); or Kudo & Richardson (2018), "SentencePiece"
(arXiv:1808.06226 — whose retrieved text **included the complete reference list**).
*Caveat:* the Sennrich and Kudo fetches truncated before their closing sections/bibliography, and PDFs are
unreadable by the fetch tool, so a mention there cannot be fully excluded. **Do not assert "BPE cites
Zipf's law" without checking §5/§6/references directly.**

What those papers *do* say — usable, verbatim, and the honest substitute:
- Sennrich et al. (2016), §1: "However, the translation of rare words is an open problem. The vocabulary of
  neural models is typically limited to 30 000–50 000 words, but translation is an open-vocabulary
  problem…" and "We show that open-vocabulary neural machine translation is possible by encoding (rare)
  words via subword units." §3.1: "A simple method to manipulate the trade-off between vocabulary size and
  text size is to use shortlists of unsegmented words, using subword units only for rare words."
- Kudo (2018), §1: "limiting vocabulary size increases the amount of unknown words, which makes the
  translation inaccurate especially in an open vocabulary setting."

**A citable source that DOES connect Zipf to tokenization:**
He, Y., Zeng, Q. & Jiang, M. (2025), "Pre-trained Models Perform the Best When Token Distributions Follow
Zipf's Law", *Proceedings of EMNLP 2025*, pp. 28009–28021, DOI **10.18653/v1/2025.emnlp-main.1421**,
<https://aclanthology.org/2025.emnlp-main.1421/> — abstract: "In this work, we propose a principled method
for determining the vocabulary size by analyzing token frequency distributions through Zipf's law. We show
that downstream task performance correlates with how closely token distributions follow power-law
behavior, and that aligning with Zipfian scaling improves both model efficiency and effectiveness."

**How to frame it for the lecture:** natural language is Zipfian/long-tailed, which is *why* a word-level
vocabulary is either unbounded or full of UNKs, and therefore *why* subword tokenization exists. Present
that as standard reasoning grounded in the Sennrich/Kudo "rare words / open-vocabulary" framing, and cite
He et al. (EMNLP 2025) for the explicit Zipf↔tokenizer link.

---

## COULD NOT VERIFY

- **arXiv §5 "Limitations and Future Directions" verbatim text.** The arXiv HTML/ar5iv fetch was truncated
  by the tool at ~§3.2 on repeated attempts; the PDF endpoint returns `unsupported content type
  "application/pdf"`, and `bash` has no network so the PDF could not be downloaded. The caveats in A.5 are
  from sections I did read, not from §5.
- **Section 5 / methods detail beyond §3.2** — same cause.
- **The unit of `t` in `ln(ρ_max) = A·t + B`** — not stated in the accessible text; "days" is inferred from
  ln 2 / 0.007 ≈ 99 days ≈ 3.3 months.
- **The Nature MI full text** — `nature.com`, `link.springer.com` and `preview-www.nature.com` all redirected
  to `idp.nature.com` / `idp.springer.com` identity providers and could not be fetched. The published
  *abstract*, volume/issue/pages, dates and DOI were obtained from the **Crossref API** instead, which is a
  reliable registry but is not the article body.
- **The claim that "the paper re-measured on MMLU-CF with R² = 0.953".** Only found in a secondary Chinese
  tech-media article (36kr / 新智元). The Nature reference list does cite MMLU-CF (Zhao et al., ACL 2025),
  but I could not confirm the 0.953 figure from the paper itself.
- **Independent verification claims: METR "88.6 days" (report dated 2026-04-03) and Meta "scaling ladder"
  (Muse Spark, 2026-04-08).** Reported only by 36kr / 新智元 (2026-04-13). The METR figure is **inconsistent
  with METR's published paper**, which gives 212 days (171–249) for the 50% time horizon — see A.6.
  No primary Meta source found. **Do not present these to the audience as verified.**
- **Any peer-reviewed criticism or replication of the Densing Law.** None found; this is a negative search
  result, not a guarantee of absence.

### Task B items that could NOT be verified

- **Goodhart 1975 vs. 1984.** Whether the famous sentence literally appears in the 1975/1976 RBA conference
  paper is **unsettled**: McIntyre (quoting the Bank of England) ties it to *Monetary Theory and Practice*
  **p. 96** (the 1984 reprint), while several arXiv papers tie it to the 1975 paper. Neither primary text was
  accessible. Do not assert either as certain.
- **Strathern's own verbatim attribution sentence.** The 1997 article is paywalled. Evidence indicates she
  credited **Hoskin (1996)**, not Goodhart directly — the opposite of the brief's premise. The exact
  punctuation and page (reported as p. 308) of the measure/target sentence could not be certified against
  print; secondary sources differ on the comma after "target".
- **The verbatim sentence in Hoskin (1996).** PDF unreadable by the fetch tool; HTML variant 404s.
- **A conflicting Goodhart citation.** An ECB 2007 publication snippet reads "Charles Goodhart (1981, page
  116) formulated his famous law…" — the PDF was unreadable, so this "1981, p. 116" attribution is unverified
  and recorded only as a known conflict.
- **Any verbatim text from Wright (1936).** AIAA is paywalled and returned HTTP 403. The learning-curve
  mathematics is sourced from OWID, not from Wright's body. A verbatim Wright quote requires AIAA access.
- **Any verbatim body text from Amdahl (1967).** Closed access; ACM DL returns 403. The paper's own abstract
  is reproducible only from a secondary (Scopus-reproduced) source, and whether the 1967 paper prints the
  closed form S = 1/((1−p) + p/s) could not be confirmed.
- **Any verbatim body text from the Roofline paper.** dl.acm.org and cacm.acm.org return 403; only the
  Crossref abstract sentence is quotable.
- **Whether a 2008 SC conference version of Roofline exists.** None found; the 2008 UC Berkeley tech report
  is the earlier version.
- **Verbatim text from Zipf (1935) or Zipf (1949).** HathiTrust and Internet Archive copies unfetchable;
  the equation is quoted from Piantadosi (2014).
- **Whether Sennrich et al. (2016) §5/§6/references or Kudo (2018) §5.2/§6/references mention Zipf.** Fetch
  truncation; PDFs unreadable. SentencePiece's complete text (incl. references) definitively contains no
  mention of Zipf.
- **Amodei essay "Some High-level Thoughts on the Direction of AI".** Appears not to exist on
  darioamodei.com; no Amodei doubling-period or learning-rate statement for AI training costs was verified.
- **"Henderson's law"** as a name for the experience curve: no primary source found.
- **Gogerty / Carbon Finance Lab R² value** for GPU cost vs cumulative shipments: the page says 0.9911 while
  unreadable PDF snippets say 0.9953 — inconsistent, so the fit quality is uncertain (the ~89.2% learning
  rate itself is reported consistently on the page).

### Environment limitations that caused these gaps

- `web_fetch` **cannot read PDFs** (`unsupported content type "application/pdf"`), which blocked AIAA, ACM,
  ECB, METR-progress-report and other primary PDFs.
- `bash` has **no network access** in this session (curl timed out, exit 124), so PDFs could not be
  downloaded and parsed locally.
- Publisher sites that block or redirect: `nature.com` / `link.springer.com` (→ identity-provider login),
  `dl.acm.org` and `cacm.acm.org` (HTTP 403, Cloudflare), `arc.aiaa.org` (HTTP 403),
  `*.wikipedia.org` (DNS-blocked), `arxiv.org/pdf/*` (content type rejected).
- `web_search` / `web_fetch` failed intermittently with `TypeError: fetch failed` or cross-origin-redirect
  errors; individual failures and retries are logged per-topic in the four notes files under
  `research/scratch/cv-facts/notes/` (`goodhart-zipf.md`, `bitter-lesson-amdahl.md`,
  `roofline-memory-bound.md`, `wrights-law-ai.md`).

## FETCH FAILURES (recorded per instructions)

| URL | Result |
| --- | --- |
| `https://www.nature.com/articles/s42256-025-01137-0` | `fetch failed` (×2), then cross-origin redirect to `https://idp.nature.com` |
| `https://link.springer.com/article/10.1038/s42256-025-01137-0` | `fetch failed`, then redirect to `idp.springer.com` |
| `https://link-hkg.springer.com/article/10.1038/s42256-025-01137-0` | redirect to `idp.springer.com` |
| `https://www.nature.com/natmachintell/volumes/7/issues/11` | redirect to `idp.nature.com` |
| `https://preview-www.nature.com/articles/s42256-025-01137-0` | redirect to `idp.nature.com` |
| `https://arxiv.org/abs/2412.04315v1` | `fetch failed` (×2) — used the Atom API instead |
| `https://arxiv.org/pdf/2412.04315v2` | `unsupported content type "application/pdf"` |
| `https://r.jina.ai/https://arxiv.org/html/2412.04315v2` | `fetch failed` (×2) |
| `https://ar5iv.labs.arxiv.org/html/2412.04315` | `fetch failed` first, succeeded on retry |
| `https://arxiv-org.ezproxy.obspm.fr/html/2412.04315v2` | redirect to `login.ezproxy.obspm.fr` |
| `https://www.themoonlight.io/en/review/densing-law-of-llms` | HTTP 429 (Vercel security checkpoint) |
| `https://metr.org/february-2026-progress-report.pdf` | `unsupported content type "application/pdf"` — could not check whether a later METR report revises the 212-day figure |
| `https://arxiv.org/abs/2412.04315` | succeeded (HTTP 200) |
| `https://arxiv.org/html/2412.04315v2` | succeeded, truncated ~§3.2 |
| `https://api.crossref.org/works/10.1038/s42256-025-01137-0` | succeeded (HTTP 200) |
| `https://www.tsinghua.edu.cn/en/info/1245/14611.htm` | succeeded (HTTP 200) |
| `bash`: `curl https://arxiv.org/abs/2412.04315` | timed out, exit 124 — **no network in bash** |
