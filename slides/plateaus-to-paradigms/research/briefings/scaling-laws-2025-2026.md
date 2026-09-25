# Training Scaling Laws in Frontier AI, Jan 2025 – Sep 2026

*Verification labels: **[P]** primary (artifact fetched and inspected) · **[S]** secondary outlet quoting a named person · **[!]** could not verify. Raw evidence: `verify/VERIFICATION-REPORT.md`.*

---

## 1. Is pretraining scaling still delivering?

**Ilya Sutskever, NeurIPS 2024** (Vancouver, Fri 13 Dec 2024), onstage: *"Pre-training as we know it will unquestionably end."* Also: *"We've achieved peak data and there'll be no more… We have to deal with the data that we have. There's only one internet."* A slide photo captioned *"Ilya Sutskever calls data the 'fossil fuel' of AI"* is credited "Ilya Sutskever/NeurIPS." **[S]** [The Verge, 2024-12-13](https://www.theverge.com/2024/12/13/24320811/what-ilya-sutskever-sees-openai-model-data-training) (Kylie Robison; page timestamp 14 Dec 2024 00:34 UTC). The primary is his award talk *"Sequence to sequence learning with neural networks: What a decade"* — no published paper. No official NeurIPS transcript/video located. **[!]** The claim that he said "two axes of scaling have plateaued" is **unverified in any wording** **[!]** — do not put it on a slide.

**"The Era of Experience" (Silver & Sutton)** is **not on arXiv** (arXiv API: 0 results for `au:Sutton AND abs:"era of experience"`); `deepmind.google/discover/blog/welcome-to-the-era-of-experience/` is 404; the DeepMind sitemap has zero matching entries. Canonical source — [DeepMind-hosted PDF](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf), 11 pp, HTTP 200 **[P]**. PDF metadata `CreationDate = Thu Apr 10 23:30:54 2025 CST`; **no publication date is printed in the document**. Footnote verbatim: *"This is a preprint of a chapter that will appear in the book Designing an Intelligence, published by MIT Press."* Verbatim quotes: *"In key domains such as mathematics, coding, and science, the knowledge extracted from human data is rapidly approaching a limit… The pace of progress driven solely by supervised learning from human data is demonstrably slowing, signalling the need for a new approach."* · *"AI is at the cusp of a new period in which experience will become the dominant medium of improvement and ultimately dwarf the scale of human data used in today's systems."* · *"Ultimately, experiential data will eclipse the scale and quality of human generated data."* **[P]** Caveat: these are claims about **human data**, not about compute returns.

**Chinchilla/Kaplan successors.** [arXiv:2406.12907](https://arxiv.org/abs/2406.12907) (Pearce & Song, TMLR 2024) reconciles them: Kaplan `N_opt ∝ C^0.73` vs Chinchilla `N_opt ∝ C^0.50`, gap attributed mostly to Kaplan counting non-embedding params at small scale. **[P]** [arXiv:2509.23963](https://arxiv.org/abs/2509.23963) (Schaeffer et al., 28 Sep 2025) concludes Chinchilla remains *"a durable guide for scaling language models."* **[P]** [arXiv:2603.22339](https://arxiv.org/abs/2603.22339) (21 Mar 2026) argues Chinchilla Approach 2's parabolic IsoFLOP fit is systematically biased even on noise-free data, quantifying a parameter underallocation equal to 6.5% of Llama 3's `3.8×10^25`-FLOP budget (~$1.4M at 50% H100 MFU). **[P]**

Deliberate over-training is explicit in Llama 3 **[P]** ([arXiv:2407.21783](https://arxiv.org/abs/2407.21783)): *"While our scaling laws suggest our flagship model is an approximately compute-optimal size for our training budget, we also train our smaller models for much longer than is compute-optimal. The resulting models perform better than compute-optimal models at the same inference budget."* Also: *"IsoFLOPs curves become flatter around the minimum as the compute budget increases."*

## 2. Data walls

Villalobos et al. [arXiv:2211.04325](https://arxiv.org/abs/2211.04325) (v2, 4 Jun 2024): models "will be trained on datasets roughly equal in size to the available stock of public human text data **between 2026 and 2032**, or slightly earlier if models are overtrained." **[P]**

Muennighoff et al. [arXiv:2305.16264](https://arxiv.org/abs/2305.16264) (v5, 28 Jun 2025): *"training with up to 4 epochs of repeated data yields negligible changes to loss compared to having unique data. However, with more repetition, the value of adding compute eventually decays to zero."* **[P]**

Synthetic-data scaling: EMNLP 2025 [2025.emnlp-main.544](https://aclanthology.org/2025.emnlp-main.544/); data-quality scaling: ACL 2025 [2025.acl-long.1163](https://aclanthology.org/2025.acl-long.1163/). **[S]** (titles/venues from search results; abstracts not fetched).

## 3. RL / post-training scaling

DeepSeek-R1 [arXiv:2501.12948](https://arxiv.org/abs/2501.12948) (22 Jan 2025; v2 4 Jan 2026), *Nature* **645**:633–638 (2025), DOI `10.1038/s41586-025-09422-z`. Pure RL, no human-labeled reasoning trajectories. **[P]**

**ScaleRL — "The Art of Scaling Reinforcement Learning Compute for LLMs"** [arXiv:2510.13786](https://arxiv.org/abs/2510.13786) (Khatri, Madaan, Tiwari, Bansal, Duvvuri, Zaheer, Dhillon, Brandfonbrener, Agarwal; 15 Oct 2025). Verbatim: *"more than 400,000 GPU-hours"*; fits *"sigmoidal compute-performance curves"*; *"a single RL run scaled up to 100,000 GPU-hours."* Key negative result: *"Details such as loss aggregation, normalization, curriculum, and off-policy algorithm primarily modulate compute efficiency without materially shifting the asymptote."* **[P]** Strongest 2025 evidence RL is becoming predictable — but **sigmoidal, not a power-law exponent**.

2026: **IsoCompute Playbook** [arXiv:2603.12151](https://arxiv.org/abs/2603.12151) (12 Mar 2026) — compute-optimal parallel rollouts per problem *"increases predictably with compute budget and then saturates."* **[P]** **PrefixRL** [arXiv:2601.18795](https://arxiv.org/abs/2601.18795) (26 Jan 2026) — 2× faster to equal reward on hard problems. **[P]** Synthetic-curriculum RL for code: [arXiv:2603.24202](https://arxiv.org/abs/2603.24202) (25 Mar 2026). **[P]**

**No RL compute scaling exponent found.** GRPO successors (DAPO, GSPO, Dr. GRPO) appeared only in search snippets — IDs unverified. **[!]**

## 4. Test-time / inference-time compute

**OpenAI o1**, *Learning to reason with LLMs*, [openai.com/index/learning-to-reason-with-llms](https://openai.com/index/learning-to-reason-with-llms), 12 Sep 2024. Verbatim (note the exact wording): *"We have found that the performance of o1 consistently improves with more reinforcement learning (train-time compute) and with more time spent thinking (test-time compute)."* **[S]** ([Silicon Republic, 13 Sep 2024](https://www.siliconrepublic.com/machines/openai-o1-reasoning-ai-model-preview); openai.com is behind a Cloudflare 403, so this is a verbatim secondary quote).

**Noam Brown (OpenAI), 12 Sep 2024** ([The Decoder](https://the-decoder.com/openai-o1/)): *"The longer it thinks, the better it does on reasoning tasks."* / *"We're no longer bottlenecked by pretraining. We can now scale inference compute too."* **[S]** — the crispest named-person statement of the 2024 shift.

**o3 / ARC-AGI** — **[P]** primary, ARC Prize (François Chollet), 20 Dec 2024: [arcprize.org/blog/oai-o3-pub-breakthrough](https://arcprize.org/blog/oai-o3-pub-breakthrough): *"OpenAI's new o3 system … has scored a breakthrough 75.7% on the Semi-Private Evaluation set at our stated public leaderboard $10k compute limit. A high-compute (172x) o3 configuration scored 87.5%."* ARC Prize adds: *"The low-efficiency score of 87.5% is quite expensive, but still shows that performance on novel tasks does improve with increased compute (at least up to this level.)"* It states it presented these results in person with Sam Altman and Mark Chen during the final "12 Days of OpenAI" event. TechCrunch reports OpenAI "applied around 10x more computing to train o3 than its predecessor, o1." **Correction for slides: there is NO OpenAI blog post announcing o3 in Dec 2024** — OpenAI's own feed ([news/rss.xml](https://openai.com/news/rss.xml)) shows the earliest o3 items as *OpenAI o3-mini* (Fri 31 Jan 2025) and *Introducing OpenAI o3 and o4-mini* (Wed 16 Apr 2025); o3 was announced on the live stream. o3 FrontierMath 25.2% is **secondary only** **[!]**.

**Papers.** s1 [arXiv:2501.19393](https://arxiv.org/abs/2501.19393) (31 Jan 2025), Muennighoff et al., budget forcing; s1-32B beats o1-preview by up to 27% on MATH/AIME24. **[P]** Inference Scaling Laws [arXiv:2408.00724](https://arxiv.org/abs/2408.00724) (Wu, Sun, Li, Welleck, Yang; ICLR 2025): *"scaling inference compute with inference strategies can be more computationally efficient than scaling model parameters."* **[P]** Large Language Monkeys [arXiv:2407.21787](https://arxiv.org/abs/2407.21787) (31 Jul 2024): coverage scales over four orders of magnitude, *"suggesting the existence of inference-time scaling laws."* **[P]** Follow-up [arXiv:2502.17578](https://arxiv.org/abs/2502.17578) (24 Feb 2025): per-problem failure falls exponentially; a heavy-tailed success distribution turns the aggregate into a power law. **[P]**

**Plateau evidence — external, not OpenAI.** Epoch AI analysis, [TechCrunch 12 May 2025](https://techcrunch.com/2025/05/12/improvements-in-reasoning-ai-models-may-slow-down-soon-analysis-finds/): progress "could slow down… as soon as within a year," quoting Josh You (Epoch AI): *"If there's a persistent overhead cost required for research, reasoning models might not scale as far as expected."* **[S]**

**2026 points to selection, not sampling, as the bottleneck.** [arXiv:2609.13257](https://arxiv.org/abs/2609.13257) (6 Sep 2026): expanding the pool 4→16 raises *oracle* quality by +9.23 IQ, but *"none of twelve adaptive-depth policies outperforms uniform compute"* — sampling headroom ≠ selection gain. **[P]** [arXiv:2608.28496](https://arxiv.org/abs/2608.28496) (28 Aug 2026): sequential sampling "can degrade accuracy when inference budgets are large." **[P]**

## 5. 2026 papers and statements

- **Skaling: Chinchilla's Exponents Meet Kaplan's Coupling** [arXiv:2608.07222](https://arxiv.org/abs/2608.07222) (7 Aug 2026): *"standard formulations systematically under- and overestimate loss at data-scarce and overtraining extremes. This failure originates in the underlying assumption that model size and training data impact the loss independently."* **[P]**
- **Hyperparameter Scaling Laws Across MoE Sparsity** [arXiv:2609.08690](https://arxiv.org/abs/2609.08690) (8 Sep 2026): 1,800 runs, ~20T tokens, *"200,000 equivalent H800 GPU-hours."* **[P]**
- **OpenEuroLLM scaling laws** [arXiv:2608.28308](https://arxiv.org/abs/2608.28308) (28 Aug 2026) — models "both undertraining and overtraining regimes." **[P]**
- **Sam Altman**, at Stanford (via [The Decoder, 21 Jun 2026](https://the-decoder.com/sam-altman-says-a-whole-generation-of-researchers-held-ai-back-by-underestimating-what-scaling-could-do/)): *"Betting against LLMs scaling at this point feels quite misguided to me."* **[S]**
- **Yann LeCun**, 4 Jul 2025 ([36Kr EN](https://eu.36kr.com/en/p/3364112069871367), aggregation not first-person): *"The era of the 'Pre-trained Scaling Myth' is coming to an end."* **[S]**
- **Dario Amodei**, Dwarkesh Podcast, 13 Feb 2026 — *"Pretraining continues to yield improvements. Now, RL is showing similarly reliable scaling…"*; *"the lack of public recognition of how close we are to the end of the exponential."* **[!] third-party transcript mirrors only** (quicklets.ai / pod.wave.co); dwarkesh.com unreachable, so treat as unconfirmed.
- **Demis Hassabis**: a 20VC episode is titled "…Why LLMs Will Not Commoditise & We Have Not Hit Scaling Laws…" (Libsyn directory, release 04/07/2026), but **no verbatim quote retrievable** **[!]**.

No NeurIPS 2025 / ICLR 2026 / ICML 2026 keynote on scaling verified **[!]**.

## 6. Did any lab disclose training compute?

| Model | Disclosure | Status |
|---|---|---|
| **DeepSeek-V3** [arXiv:2412.19437](https://arxiv.org/abs/2412.19437) | *"requires only **2.788M H800 GPU hours** for its full training"*; 671B total / 37B activated; 14.8T tokens | **[P] full GPU-hour disclosure** (v1 27 Dec 2024, v2 18 Feb 2025) |
| **Llama 3 405B** [arXiv:2407.21783](https://arxiv.org/abs/2407.21783) | *"pre-trained using **3.8 × 10^25 FLOPs**, almost 50× more than the largest version of Llama 2"*; 405B params, 15.6T tokens | **[P] full FLOP disclosure** (31 Jul 2024 — just before the window; the key precedent) |
| **Kimi K2** [arXiv:2507.20534](https://arxiv.org/abs/2507.20534) | 32B activated / 1T total; 15.5T tokens; H800 cluster topology. **No total GPU-hours or FLOPs** — full v2 HTML searched | **[P] verified absence** (v1 28 Jul 2025, v2 3 Feb 2026) |
| **Qwen3** [arXiv:2505.09388](https://arxiv.org/abs/2505.09388) | No compute figure in abstract; adds a *"thinking budget mechanism"* for inference | **[P] verified absence** |
| **Llama 4** | **Not verified** — correct arXiv ID not located (2504.19413 is Mem0) | **[!]** |
| Any 2026 frontier model | **No compute disclosure found** | **[!]** |

---

## Unverified / low-confidence

1. **Dario Amodei "10% chance scaling could stagnate due to insufficient data"** — the citing preprint [arXiv:2508.05619](https://arxiv.org/abs/2508.05619) ref. [2] points to a Kevin Roose / Casey Newton podcast transcript, **July 2023** (NYT *Hard Fork*, episode dated 21 Jul 2023). No accessible transcript contains the sentence, and the preprint cites a generic NYT section URL rather than an episode permalink. **Do not present this as a 2025–2026 statement.** **[!]** (That preprint's acknowledgements also state: *"Manus and Perplexity were helpful for literature search and citation validation."*)
2. **Sutskever "two axes of scaling have plateaued"** — no source in any wording. **[!]**
3. **Amodei Feb 2026 / Hassabis 2026 quotes** — third-party transcript mirrors or partial directory listings only. **[!]**
4. **o1 blog post text** — openai.com serves HTTP 403 (Cloudflare) to non-browser clients; the quote above is a verbatim secondary reproduction. URL and date confirmed via OpenAI's own RSS feed. **[S]**
5. **o3 FrontierMath 25.2%** — secondary only; no Epoch AI primary page found. **[!]**
6. **LeCun July 2025 quote** — aggregation site, not first-person. **[S]**
7. **No RL compute scaling exponent** found anywhere. **[!]**
8. **GRPO successors** (DAPO, GSPO, Dr. GRPO) — arXiv IDs unverified. **[!]**
9. **Llama 4 compute**, and **any 2026 frontier-model compute disclosure** — nothing found. **[!]**
