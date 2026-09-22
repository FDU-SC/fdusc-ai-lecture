# Roofline model + why LLM decoding is memory-bandwidth-bound

Verified research notes. Compiled 2026-09-19. All non-obvious claims carry a URL/DOI.
Methods used: `web_search` and `web_fetch` only (no bash network, no PDF tooling).
Quoted text is verbatim from the cited page; quotes are in `"..."`.

---

## ITEM 1 — The Roofline model original paper

### (a) Exact citation

**The version to cite (peer-reviewed, archival):**

- Authors: **Samuel Williams** (Lawrence Berkeley National Laboratory), **Andrew Waterman** (University of California, Berkeley), **David Patterson** (University of California, Berkeley)
- Title: **"Roofline: An Insightful Visual Performance Model for Multicore Architectures"**
- Journal: **Communications of the ACM**
- Volume **52**, Issue **4**, pages **65–76**
- Month/Year: **April 2009**
- DOI: **10.1145/1498765.1498785** — ✅ **VERIFIED** (exact match to the DOI supplied in the task)
- URL: https://doi.org/10.1145/1498765.1498785 · ACM DL landing page: https://dl.acm.org/doi/10.1145/1498765.1498785
- ISSN 0001-0782 (print) / 1557-7317 (electronic)

Verified against the Crossref REST API record for the DOI (deposited by ACM; publisher "Association for Computing Machinery (ACM)", `container-title: ["Communications of the ACM"]`, `volume: "52"`, `issue: "4"`, `page: "65-76"`, `published-print: 2009-04`, `type: journal-article`):
https://api.crossref.org/works/10.1145/1498765.1498785

⚠️ **TITLE CORRECTION — the lecturer's title is wrong.** The task states the title as
"...for **Multiclass Computing** Architectures". The real title is
**"...for Multicore Architectures"**. Crossref stores the title as `"Roofline"` with the
subtitle `"an insightful visual performance model for multicore architectures"`; the
commonly-cited full form is *"Roofline: An Insightful Visual Performance Model for
Multicore Architectures"*. Independently confirmed by Semantic Scholar (venue `CACM`, year 2009):
https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/1498765.1498785

**The earlier 2008 version (a technical report, NOT a conference paper):**

- Authors: Samuel Webb Williams, Andrew Waterman, David A. Patterson
- Title: **"Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures"**
- Institution: EECS Department, University of California, Berkeley
- **Technical Report No. UCB/EECS-2008-134**, dated **October 17, 2008**
- Landing page (with BibTeX): https://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/EECS-2008-134.html
- PDF: http://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/Archive/EECS-2008-134.pdf
- Note the 2008 title says "Floating-Point Programs and Multicore Architectures"; the 2009 CACM title drops "Floating-Point Programs".

**Second 2008/2009-adjacent record (LBNL report, same title as the tech report):**

- DOI **10.2172/1407078**, type `report`, issuer recorded by Crossref as dated **2009-09-01**, same three authors, title "Roofline: An Insightful Visual Performance Model for Floating-Point Programs and Multicore Architectures".
- Metadata: https://api.crossref.org/works/10.2172/1407078 (retrieved via Crossref search) · landing page https://www.osti.gov/biblio/1407078 (⚠️ page itself unreachable from this environment — see FETCH FAILURES)
- Semantic Scholar lists a green open-access copy of the CACM article at https://www.osti.gov/servlets/purl/1407073 (a PDF).

**Is there a 2008 SC conference version? — ❌ NOT FOUND; probably does not exist.**
A Crossref bibliographic search over the whole of 2008 (`filter=from-pub-date:2008-01-01,until-pub-date:2008-12-31`) plus queries for "Roofline", "Roofline Williams Waterman Patterson" and "Roofline insightful visual performance model" returned **no** SC/SC08 roofline paper by these authors. What exists and is sometimes confused with it is a *different* SC08 paper that **uses** the model: K. Datta et al., "Stencil computation optimization and auto-tuning on state-of-the-art multicore architectures", Proc. ACM/IEEE SC08 — cited as reference `e_1_2_2_12_1` in the CACM paper's own reference list (visible in the Crossref record above).

**Recommendation for the lecturer:** cite the **CACM 52(4):65–76, April 2009, DOI 10.1145/1498765.1498785** version. Mention the **UCB/EECS-2008-134 tech report (17 Oct 2008)** only if the 2008 priority date matters. Do **not** cite an "SC 2008 Roofline paper" — I could not verify one.

### (b) The Roofline formula

The standard statement of the model:

```
attainable performance = min( peak floating-point performance ,
                              arithmetic intensity × peak memory bandwidth )
```

- **Arithmetic intensity** = **FLOPs performed ÷ bytes of DRAM (HBM) traffic**.
- The x-axis of the Roofline plot is arithmetic intensity; the y-axis is attainable performance (GFLOP/s). The "ridge point" where the two roofs meet is the machine balance point.

Sources for the formula/definition (secondary, because the primary body text was inaccessible to me — see (c)):
- NERSC documentation, "Roofline Performance Model": *"Arithmetic Intensity (AI) is the ratio of total floating-point operations (FLOPs) performed by a given code or code section, to the total data movement (Bytes) required to support those FLOPs."* — https://docs.nersc.gov/tools/performance/roofline/ — and it links the Roofline model directly to the CACM paper DOI.
- Same page, on the device/HBM level: `AI (HBM) = flop_count_dp / ((dram_read_transactions + dram_write_transactions)*32)` — i.e. the *DRAM-traffic* form of arithmetic intensity requested in the task.
- FlashAttention (peer-reviewed, primary for the *term* "arithmetic intensity"): *"This is commonly measured by the arithmetic intensity [85], which is the number of arithmetic operations per byte of memory access."* — https://arxiv.org/html/2205.14135v2

⚠️ **Terminology caveat I could NOT resolve:** I could not open the Roofline paper body, so I cannot verify whether Williams et al. 2009 write "arithmetic intensity" or "operational intensity" (the tech report/earlier literature is widely said to use "operational intensity"). Do not attribute either exact term to the paper without checking the body.

### (c) Verbatim quote of the paper's core idea

**❌ I could NOT read the body of the paper, so I cannot supply a verbatim core-idea sentence from the article text.** Details:
- `https://dl.acm.org/doi/fullHtml/10.1145/1498765.1498785` returned **HTTP 403** ("Just a moment..." Cloudflare interstitial) on **4 separate attempts**.
- `https://cacm.acm.org/research/roofline-an-insightful-visual-performance-model-for-multicore-architectures/` returned **HTTP 403** (Cloudflare "Sorry, you have been blocked").
- The two open-access full texts are **PDFs** (`http://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/Archive/EECS-2008-134.pdf` and `https://www.osti.gov/servlets/purl/1407073`), and my fetch tool rejects PDFs (`unsupported content type "application/pdf"`). I therefore could not read the tech report either.

**The one verbatim sentence I *can* verify from the paper** is its abstract, retrieved via the Crossref API for the DOI:

> "The Roofline model offers insight on how to improve the performance of software and hardware."

Source: abstract field of https://api.crossref.org/works/10.1145/1498765.1498785 (the same one-sentence abstract appears in the ACM DL record).

---

## ITEM 2 — Transformer/LLM inference is memory-bandwidth-bound, especially autoregressive decoding

### Best citable peer-reviewed source (recommended)

**Leviathan, Kalman & Matias, "Fast Inference from Transformers via Speculative Decoding", ICML 2023 (Oral), arXiv:2211.17192** — peer-reviewed ✅

Verbatim (Section 1):

> "We additionally observe that inference from large models is often not bottlenecked on arithmetic operations, but rather on memory bandwidth and communication, so additional computation resources might be available."

and, later in the same section:

> "Therefore, in common situations where memory bandwidth is the bottleneck, and compute resources are available, it may be a good default to accelerate sampling from autoregressive models like Transformers."

URLs: https://arxiv.org/html/2211.17192v2 · abstract page https://arxiv.org/abs/2211.17192 (abstract page lists `Comments: ICML 2023 Oral`).

### Pope et al., "Efficiently Scaling Transformer Inference" — peer-reviewed ✅ (MLSys 2023)

Venue confirmed: *Proceedings of Machine Learning and Systems 5 (MLSys 2023)* — https://proceedings.mlsys.org/paper_files/paper/2023/hash/c4be71ab8d24cdfb45e3d06dbfca2780-Abstract-mlsys2023.html (arXiv:2211.05102, https://arxiv.org/abs/2211.05102)

Verbatim (Section 1, on generative inference / decoding):

> "The large memory footprint gives rise to a large amount of memory traffic to load the parameters and KV cache from high-bandwidth memory (HBM) into the compute cores for each step, and hence a large total memory bandwidth required to meet a given latency target."

Verbatim (Section 2, "Memory costs"):

> "At small batch sizes and sequence lengths, the time to load weights dominates."

Verbatim (Section 2.1):

> "The on-chip memory needs to load this KV cache from off-chip memory once for every token generated during which the computational core of the chip is essentially idle."

URLs: https://arxiv.org/html/2211.05102v1 · MLSys PDF https://proceedings.mlsys.org/paper_files/paper/2023/file/c4be71ab8d24cdfb45e3d06dbfca2780-Paper-mlsys2023.pdf

⚠️ Caveat: I read Sections 1–3.2 of the HTML; the literal string "memory-bandwidth-bound" did **not** appear in the portion I retrieved. I did not retrieve the whole paper, so I cannot claim the exact hyphenated phrase is absent.

### Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need" (2019) — ⚠️ PREPRINT, NOT peer-reviewed

arXiv:1911.02150; the abstract page lists **no** conference/journal (`Comments` field absent). Verbatim from the abstract:

> "While training these layers is generally fast and simple, due to parallelizability across the length of the sequence, incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors."

("paralleization" is a typo present in the original.) It says **"memory-bandwidth cost"**, not the literal phrase "memory-bandwidth-bound", but it is an unambiguous attribution of incremental-decoding slowness to memory bandwidth.
URL: https://arxiv.org/abs/1911.02150

### FlashAttention (Dao, Fu, Ermon, Rudra, Ré) — peer-reviewed ✅ (NeurIPS 2022)

Venue confirmed: NeurIPS 2022 proceedings, https://proceedings.neurips.com.cn/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html (arXiv:2205.14135, https://arxiv.org/abs/2205.14135)

Verbatim (Section 1):

> "On modern GPUs, compute speed has out-paced memory speed [61, 62, 63], and most operations in Transformers are bottlenecked by memory accesses [43]."

Verbatim (Section 2.1):

> "As compute has gotten faster relative to memory speed [61, 62, 63], operations are increasingly bottlenecked by memory (HBM) accesses."

Verbatim (Section 2.1, arithmetic-intensity definition):

> "This is commonly measured by the arithmetic intensity [85], which is the number of arithmetic operations per byte of memory access."

URL: https://arxiv.org/html/2205.14135v2

⚠️ Caveat: FlashAttention's memory-bound framing is about attention/softmax **IO**, not about autoregressive decoding per se. It does **not** contain a sentence saying "decoding is memory-bandwidth-bound"; do not cite it for that specific claim.

### vLLM / PagedAttention

- Paper (Kwon et al., **SOSP 2023** — peer-reviewed ✅): arXiv:2309.06180, https://arxiv.org/abs/2309.06180. The **abstract** I read does not state that decoding is memory-bandwidth-bound (it is about KV-cache memory waste and throughput). I did not retrieve the body, so I cannot rule out such a sentence inside it.
- Project blog (❌ NOT peer-reviewed): *"In vLLM, we identify that the performance of LLM serving is bottlenecked by memory."* — https://vllm.ai/blog/2023-06-20-vllm — this is about serving being memory-*capacity*/memory bound, not a precise bandwidth-bound claim about decoding.

### NVIDIA technical blog — ❌ industry/technical blog, NOT peer-reviewed

Under the heading "Decode phase or generating the output", verbatim:

> "The speed at which the data (weights, keys, values, activations) is transferred to the GPU from memory dominates the latency, not how fast the computation actually happens. In other words, this is a memory-bound operation."

URL: https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ (Verma & Vaidya, 17 Nov 2023). This is the most on-the-nose "the decode phase is memory-bound" statement I found, but it is an **industry blog**, not peer-reviewed — mark it as such in slides.

### Summary table

| Source | Exact quote | Peer-reviewed? | URL |
|---|---|---|---|
| Leviathan, Kalman & Matias, *Fast Inference from Transformers via Speculative Decoding* (ICML 2023, Oral) | "We additionally observe that inference from large models is often not bottlenecked on arithmetic operations, but rather on memory bandwidth and communication, so additional computation resources might be available." | **Yes** (ICML 2023) | https://arxiv.org/html/2211.17192v2 |
| Pope et al., *Efficiently Scaling Transformer Inference* (MLSys 2023) | "The large memory footprint gives rise to a large amount of memory traffic to load the parameters and KV cache from high-bandwidth memory (HBM) into the compute cores for each step, and hence a large total memory bandwidth required to meet a given latency target." | **Yes** (MLSys 2023) | https://arxiv.org/html/2211.05102v1 |
| Pope et al. (MLSys 2023) | "At small batch sizes and sequence lengths, the time to load weights dominates." | **Yes** | https://arxiv.org/html/2211.05102v1 |
| Pope et al. (MLSys 2023) | "The on-chip memory needs to load this KV cache from off-chip memory once for every token generated during which the computational core of the chip is essentially idle." | **Yes** | https://arxiv.org/html/2211.05102v1 |
| Shazeer, *Fast Transformer Decoding* (2019) | "incremental inference (where such paralleization is impossible) is often slow, due to the memory-bandwidth cost of repeatedly loading the large "keys" and "values" tensors." | **No** (arXiv preprint only) | https://arxiv.org/abs/1911.02150 |
| Dao et al., *FlashAttention* (NeurIPS 2022) | "On modern GPUs, compute speed has out-paced memory speed ..., and most operations in Transformers are bottlenecked by memory accesses" | **Yes** (NeurIPS 2022) | https://arxiv.org/html/2205.14135v2 |
| Dao et al., *FlashAttention* (NeurIPS 2022) | "the arithmetic intensity ..., which is the number of arithmetic operations per byte of memory access" | **Yes** | https://arxiv.org/html/2205.14135v2 |
| NVIDIA Technical Blog, *Mastering LLM Techniques: Inference Optimization* | "The speed at which the data (weights, keys, values, activations) is transferred to the GPU from memory dominates the latency, not how fast the computation actually happens. In other words, this is a memory-bound operation." | **No** (industry blog) | https://developer.nvidia.com/blog/mastering-llm-techniques-inference-optimization/ |
| vLLM project blog | "In vLLM, we identify that the performance of LLM serving is bottlenecked by memory." | **No** (project blog) | https://vllm.ai/blog/2023-06-20-vllm |
| Williams, Waterman & Patterson, Roofline (CACM 2009) — abstract only | "The Roofline model offers insight on how to improve the performance of software and hardware." | **Yes** (CACM) | https://api.crossref.org/works/10.1145/1498765.1498785 |

---

## COULD NOT VERIFY

1. **No verbatim core-idea sentence from the Roofline paper body.** Both HTML full texts are Cloudflare-blocked and both open-access copies are PDFs my fetch tool cannot parse. Only the one-sentence abstract quote (above) is verifiable. If a verbatim body quote is required, someone with PDF/browser access must open https://www.osti.gov/servlets/purl/1407073 or the CACM article.
2. **"arithmetic intensity" vs "operational intensity" in the original Roofline paper** — could not check the body.
3. **No 2008 SC conference version of the Roofline paper exists in Crossref.** I could not find one; treat claims of an "SC 2008 Roofline paper" as unverified/likely confused with Datta et al., SC08 (stencil auto-tuning).
4. **LBNL report DOI 10.2172/1407078** — metadata came from Crossref only; the OSTI landing page could not be fetched. Its exact publication date/venue labeling is therefore only as reliable as Crossref's deposit (2009-09-01).
5. **Literal phrase "memory-bandwidth-bound" in Pope et al.** — not observed in the Sections 1–3.2 I retrieved; later sections not retrieved.
6. **vLLM/PagedAttention paper body** — only the abstract was retrieved; no memory-bandwidth-bound sentence verified there.
7. **Whether FlashAttention says anything about *decoding*** beyond "most operations in Transformers are bottlenecked by memory accesses" — not verified; its memory-bound discussion is about attention IO.
8. **Wikipedia "Roofline model"** and **jax-ml.github.io/scaling-book/roofline** (both would have been convenient secondary formula sources) were unreachable from this environment.

## FETCH FAILURES (recorded as required)

Network/tool failures, with the number of failed attempts:

| URL | Result | Attempts |
|---|---|---|
| https://dl.acm.org/doi/fullHtml/10.1145/1498765.1498785 | HTTP 403 (Cloudflare interstitial) | 4 |
| https://dl.acm.org/doi/10.1145/1498765.1498785 | HTTP 403 (Cloudflare) | 1 |
| https://cacm.acm.org/research/roofline-an-insightful-visual-performance-model-for-multicore-architectures/ | HTTP 403 (Cloudflare block page) | 1 |
| https://www.osti.gov/biblio/1407073 | `fetch failed` | 2 |
| https://www.osti.gov/pages/biblio/1407073 | `fetch failed` | 1 |
| https://www.osti.gov/biblio/1407078 | `fetch failed` | 1 |
| https://mags.acm.org/communications/200904?pg=68 | `fetch failed` | 3 |
| https://escholarship.org/uc/item/78h8v7mr | HTTP 403 (CloudFront) | 1 |
| https://escholarship.org/content/qt78h8v7mr/qt78h8v7mr.pdf | HTTP 403 (CloudFront) | 1 |
| https://scholar.archive.org/search?q=%22Roofline...%22 | `fetch failed` | 3 |
| https://jax-ml.github.io/scaling-book/roofline/ | `getaddrinfo EAI_AGAIN` (DNS) | 3 |
| https://en.wikipedia.org/wiki/Roofline_model | blocked: "resolves to a non-public IP address" | 1 |
| http://www2.eecs.berkeley.edu/Pubs/TechRpts/2008/Archive/EECS-2008-134.pdf | `unsupported content type "application/pdf"` (tool limitation) | 1 |
| https://api.semanticscholar.org/graph/v1/paper/search?... (roofline query) | HTTP 429 rate limit (later retried OK on a different endpoint) | 1 |
| https://api.semanticscholar.org/graph/v1/paper/arXiv:2205.14135?... | HTTP 429 rate limit | 2 (gave up; used NeurIPS proceedings + web search instead) |
| web_search call (2 queries) | `TypeError: fetch failed` (search backend) | 1, then retried successfully |
| web_search call (2 more queries) | `TypeError: fetch failed` (search backend) | 1, then retried successfully |

Succeeded normally: all `arxiv.org/abs/*` and `arxiv.org/html/*` pages, `api.crossref.org`, `www2.eecs.berkeley.edu` landing page, `docs.nersc.gov`, `proceedings.mlsys.org`, `researchr.org`, `vllm.ai/blog`, `developer.nvidia.com/blog`, `amcr.lbl.gov`.
