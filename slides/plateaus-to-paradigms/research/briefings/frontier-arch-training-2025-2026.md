# Frontier AI Architecture & Training Technique Trends, Jan 2025 – Sep 2026

All numbers below were extracted directly from primary sources (arXiv abstracts/full text, official model cards, lab repos). Secondary sources are labelled. Fetch tooling was unreliable, so most primary sources were pulled over `curl`; where a fact could not be confirmed it is listed at the end.

## 1. Mixture-of-Experts at scale

**DeepSeek-V3** ([arXiv:2412.19437](https://arxiv.org/abs/2412.19437), v1 27 Dec 2024, v2 18 Feb 2025): 671B total / 37B active; 61 layers, hidden 7168; each MoE layer = **1 shared + 256 routed experts, 8 activated**, expert intermediate dim 2048; all FFNs except the first three layers are MoE. Auxiliary-loss-free balancing (sigmoid affinity + per-expert bias term), multi-token prediction, FP8 mixed precision; 14.8T tokens, 2.788M H800 GPU-hours, no irrecoverable loss spikes. Context extended 4K→32K→128K via YaRN.

**Kimi K2** ([arXiv:2507.20534](https://arxiv.org/abs/2507.20534), v1 28 Jul 2025, v2 3 Feb 2026): **1.04T total / 32.6B active**, 61 layers, **384 experts (8 active + 1 shared)**, 64 attention heads (vs 128 in V3), 1 dense layer, no expert grouping — a chosen **sparsity of 48**. MuonClip (Muon + QK-clip) gave 15.5T-token pretraining with zero loss spikes.

**Qwen3** ([arXiv:2505.09388](https://arxiv.org/abs/2505.09388), 14 May 2025): Qwen3-235B-A22B = 235B/22B, **94 layers, 64 Q / 4 KV heads, 128 experts / 8 active**, **no shared experts**, global-batch load-balancing loss, 128K context; Qwen3-30B-A3B = 48 layers, 128/8.

**Llama 4** ([MODEL_CARD.md](https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md), release 5 Apr 2025): Scout = 109B total / 17B active, **16 experts**; Maverick = 400B total / 17B active, **128 experts**. ~40T and ~22T tokens; Maverick shipped with FP8 weights.

**gpt-oss** ([arXiv:2508.10925](https://arxiv.org/abs/2508.10925), 8 Aug 2025): gpt-oss-120b = 36 layers, **116.83B total / 5.13B active, 128 experts, top-4**; gpt-oss-20b = 24 layers, 20.91B / 3.61B, 32 experts. MoE weights in **MXFP4**; 2.1M H100-hours for 120b.

**GLM-4.5** ([arXiv:2508.06471](https://arxiv.org/abs/2508.06471), 8 Aug 2025): 355B total / 32B active, 23T tokens. **MiniMax-01** ([arXiv:2501.08313](https://arxiv.org/abs/2501.08313), 14 Jan 2025): 32 experts, 456B/45.9B. **MiniMax-M1** ([arXiv:2506.13585](https://arxiv.org/abs/2506.13585), 16 Jun 2025): same backbone, 1M native context, CISPO RL, full RL on 512 H800s in 3 weeks for $534,700.

**2026 MoE:** **Kimi K3** ([repo](https://github.com/MoonshotAI/Kimi-K3), Jul 2026, [tech report PDF](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf)): **2.8T total / 104B active, 93 layers, 896 experts with 16 active + 2 shared**, latent MoE dim 3584, "Stable LatentMoE". **GLM-5** ([arXiv:2602.15763](https://arxiv.org/abs/2602.15763), 17 Feb 2026): **744B / 40B active**, 28.5T tokens. **Qwen3.5-397B-A17B** (16 Feb 2026) and **Qwen3.8-2.4T-A95B** (12 Aug 2026) per [Qwen's official README](https://github.com/QwenLM/Qwen3-Next/blob/main/README.md). **MiniMax-M3** ([arXiv:2606.13392](https://arxiv.org/abs/2606.13392), 11 Jun 2026): ~428B / ~23B active.

## 2. Attention variants

**MLA** is the incumbent: DeepSeek-V2/V3, Kimi K2, and Kimi K3 (as *Gated MLA*). **DeepSeek Sparse Attention (DSA)** shipped in DeepSeek-V3.2-Exp ([repo created 29 Sep 2025](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp)) — a lightning indexer selects top-k tokens, reducing core attention from O(L²) to O(Lk) with benchmark parity to V3.1-Terminus. GLM-5 also integrates DSA.

2026 sparse-attention refinements: **IndexCache** ([arXiv:2603.12201](https://arxiv.org/abs/2603.12201), 12 Mar 2026) reuses indices across layers, removing 75% of indexer compute (1.82× prefill / 1.48× decode on a 30B DSA model); **MiniMax Sparse Attention** ([arXiv:2606.13392](https://arxiv.org/abs/2606.13392), 11 Jun 2026) does blockwise sparse attention on GQA, cutting per-token attention compute **28.4×** at 1M context with 14.2× prefill / 7.6× decode wall-clock on H800.

**Linear-attention hybrids:** MiniMax lightning attention (MiniMax-01); **Kimi Linear** ([arXiv:2510.26692](https://arxiv.org/abs/2510.26692), 30 Oct 2025) introduces **Kimi Delta Attention (KDA)** — Gated DeltaNet plus finer channel-wise gating — reporting it beats full MLA at 3B activated / 48B total with 75% less KV cache and 6× decode at 1M. Qwen's official README states **Qwen3-Next-80B-A3B** (11 Sep 2025) and Qwen3.5 use **Gated Delta Networks + sparse MoE**. Kimi K3 uses a **3:1 KDA : Gated MLA** layer pattern plus **Attention Residuals (AttnRes)** across depth. GLM-5.3-Flash adds sparse+linear hybrid attention and Manifold-Constrained Hyper-Connections ([GLM-5 repo](https://github.com/zai-org/GLM-5), 2026).

**SSM/Transformer hybrids:** Jamba ([arXiv:2403.19887](https://arxiv.org/abs/2403.19887), 28 Mar 2024), Nemotron-H ([arXiv:2504.03624](https://arxiv.org/abs/2504.03624), 4 Apr 2025), Falcon-H1 ([arXiv:2507.22448](https://arxiv.org/abs/2507.22448), 30 Jul 2025), Hunyuan-TurboS ([arXiv:2505.15431](https://arxiv.org/abs/2505.15431), 21 May 2025).

**Sliding-window/global:** gpt-oss alternates **banded (bandwidth 128) and fully dense** attention layers, GQA with 8 KV heads, YaRN-extended to 131,072 tokens.

## 3. Long context

Trajectory: 128K (DeepSeek-V3, Qwen3 native 32,768 → 4× via YaRN+DCA) → 1M (**MiniMax-01**, 14 Jan 2025, trained at 1M and **extrapolating to 4M**) → 10M (**Llama 4 Scout**, 5 Apr 2025; Maverick 1M). **Gemini 2.5** ([tech report](https://storage.googleapis.com/deepmind-media/gemini/gemini_v2_5_report.pdf)) is sparse MoE with 1M-token input; the same report notes **Gemini 2.0 Pro (Feb 2025) carried a 2M-token window**. **Gemini 3 Pro** ([model card](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-3-Pro-Model-Card.pdf), release Nov 2025) is a sparse MoE with **1M input / 64K output**.

2026: **Kimi K3 = 1,048,576 tokens**; GLM-5.2 claims a "solid 1M-token context"; MiniMax-M3 = 1M. **No verified 2026 frontier model exceeds 1M** in my sources.

Effective vs advertised: **RULER** ([arXiv:2404.06654](https://arxiv.org/abs/2404.06654), Apr 2024) and **NoLiMa** ([arXiv:2502.05167](https://arxiv.org/abs/2502.05167), 7 Feb 2025) both show large gaps between advertised windows and usable context; NoLiMa shows degradation as literal needle-question overlap drops, with several 128K models collapsing well before their limit. "Context Length Alone Hurts LLM Performance Despite Perfect Retrieval" (EMNLP 2025 Findings) reports the same effect. DeepSeek-V3 itself only validated NIAH to 128K.

## 4. Interpretability / SAEs

Anthropic **Scaling Monosemanticity** (21 May 2024, [transformer-circuits.pub](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html)); OpenAI **"Scaling and evaluating sparse autoencoders"** ([arXiv:2406.04093](https://arxiv.org/abs/2406.04093), 6 Jun 2024); Anthropic **circuit tracing / attribution graphs** using cross-layer transcoders (27 Mar 2025, [methods](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)), applied to Claude 3.5 Haiku. Anthropic **auditing for hidden objectives** (13 Mar 2025), **Petri** open-source auditing tool (6 Oct 2025, used in Claude 4 / Sonnet 4.5 system cards and by UK AISI), **introspection** (29 Oct 2025), and **"A global workspace in language models"** — the J-space, found via Jacobians (6 Jul 2026). All four Anthropic items verified from their own pages.

## 5. muP / hyperparameter transfer

Foundations: **µTransfer / Tensor Programs V** ([arXiv:2203.03466](https://arxiv.org/abs/2203.03466), 7 Mar 2022) and **Cerebras-GPT** ([arXiv:2304.03208](https://arxiv.org/abs/2304.03208), 6 Apr 2023). 2026 activity is academic, MoE-specific: [arXiv:2605.14200](https://arxiv.org/abs/2605.14200) (13 May 2026), **GQA-μP** [arXiv:2605.15290](https://arxiv.org/abs/2605.15290) (14 May 2026), and [arXiv:2608.20061](https://arxiv.org/abs/2608.20061) (20 Aug 2026).

## 6. Low-precision training

DeepSeek-V3 pioneered FP8 at scale (tile/block-wise quantization, FP8 activation dispatch, BF16 optimizer states, validated at ~1T tokens with <0.25% relative loss error). **"Scaling FP8 training to trillion-token LLMs"** is [arXiv:2409.12517](https://arxiv.org/abs/2409.12517) — **v1 19 Sep 2024, v2 10 Feb 2025** (the Feb 2025 date is the revision, not the original): Smooth-SwiGLU, FP8 Adam moments, 7B on 256 Gaudi2, ~34% throughput gain. **NVFP4** pretraining: [arXiv:2509.25149](https://arxiv.org/abs/2509.25149) (29 Sep 2025, v2 4 Mar 2026). 2026: **Kimi K3 quantizes MoE expert weights to MXFP4 with MXFP8 activations using quantization-aware training from the SFT stage onward** (K3 tech report, verified).

## 7. Post-Transformer in 2026

**No verified 2026 frontier model is non-Transformer.** Kimi K3, Qwen3.8-2.4T, GLM-5.x, MiniMax-M3 and Gemini 3.x are all MoE Transformers; the change is *hybridization inside* the Transformer (KDA/Gated-MLA interleaving, sparse attention, AttnRes). Beyond it: **Mamba-3** ([arXiv:2603.15569](https://arxiv.org/abs/2603.15569), 16 Mar 2026, ICLR 2026) — complex-valued state update + MIMO, evaluated at **1.5B**, not frontier. **RWKV-7 "Goose"** ([arXiv:2503.14456](https://arxiv.org/abs/2503.14456), 18 Mar 2025). **HRM** ([arXiv:2506.21734](https://arxiv.org/abs/2506.21734), 26 Jun 2025) and **HRM-Text** ([arXiv:2605.20613](https://arxiv.org/abs/2605.20613), 20 May 2026) — a 1B hierarchical-recurrent model trained on 40B tokens for ~$1,500. DeepSeek's **Engram** ([repo](https://github.com/deepseek-ai/Engram), 12 Jan 2026) adds conditional N-gram memory as a *complementary sparsity axis* to MoE, not a Transformer replacement.

## Unverified / low-confidence

- **Gemma Scope (Aug 2024)** — DeepMind blog unreachable; not verified.
- **MiniMax-M2 = 230B total / 10B active** — MiniMax's site is JS-rendered and HuggingFace is unreachable; could not verify.
- **Qwen3-Next expert count / total params** — only "80B-A3B" + "Gated Delta Networks + sparse MoE" verified from Qwen's README; expert count unverified.
- **Meta's Llama 4 iRoPE description** — ai.meta.com unreachable; the model card does not mention iRoPE. Chunked-attention details unverified.
- **GPT-5 context window** — the [GPT-5 System Card](https://cdn.openai.com/gpt-5-system-card.pdf) (13 Aug 2025) contains **no architecture, parameter, or context-window disclosure**; openai.com returns 403. Any GPT-5 context number is unverified here.
- **Diffusion LMs** — Mercury Coder (Feb 2025), Mercury 2, and Gemini Diffusion rest on secondary sources only; no primary confirmation obtained.
- **Chroma "context rot" report** — secondary; the underlying effect is corroborated by NoLiMa and the EMNLP 2025 Findings paper above.
- **muP at frontier scale** — no primary claim that any named 2026 frontier model used muP/µTransfer was found; treat such claims as unsupported.
- **Qwen3.8-2.4T-A95B / Qwen3.5-397B-A17B architecture** — parameter counts verified from Qwen's README; layer/expert counts and context window unverified.
