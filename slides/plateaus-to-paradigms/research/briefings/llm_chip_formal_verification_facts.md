# LLM chip design + formal verification facts (2026-09-16)

All URLs fetched. Labels: **[PR]** peer-reviewed, **[AX]** arXiv preprint, **[CB]** company blog, **[VPR]** vendor press/trade.

## Stream A — LLMs for RTL / chip design

1. **VerilogEval** [PR, ICCAD 2023 invited]: arXiv 2309.07544 (v1 2023-09-14, v2 2023-12-10). 156 HDLBits problems, simulation-checked; SFT on synthetic problem/code pairs improves pass rates. https://arxiv.org/abs/2309.07544
2. **VerilogEval v2 / "Revisiting VerilogEval"** [AX]: arXiv 2408.11053 (v1 2024-08-20, v2 2025-02-03). Adds spec-to-RTL tasks, failure classification, in-context learning. GPT-4o 63% pass on spec-to-RTL; Llama3.1-405B 58%; RTL-Coder-6.7B 34%; prompt engineering "remains crucial." https://arxiv.org/abs/2408.11053
3. **RTLLM** [PR, ASP-DAC 2024]: arXiv 2308.05345 (v1 2023-08-10, v3 2023-11-11). Three goals (syntax/function/design quality); "self-planning" prompting boosts GPT-3.5 significantly. https://arxiv.org/abs/2308.05345
4. **OpenLLM-RTL** [AX, ICCAD'24; posted 2025-03-19]: arXiv 2503.15112. RTLLM 2.0 = 50 hand-crafted designs; AssertEval = 18 assertion-generation designs; RTLCoder-Data 80K samples plus 7K verification-filtered samples. https://arxiv.org/abs/2503.15112
5. **ChipNeMo** (NVIDIA) [AX]: arXiv 2311.00176 (v1 2023-10-31, v5 2024-04-04). Chatbot, EDA-script generation, bug summarization; ChipNeMo-70B beats GPT-4 on two of three. NVIDIA's blog (2023-10-30) says it was built "for internal use," but describes prototypes, not a quantified production deployment. https://arxiv.org/abs/2311.00176 · https://blogs.nvidia.com/blog/llm-semiconductors-chip-nemo/
6. **Chip-Chat** [PR, MLCAD 2023]: arXiv 2305.13243. Engineer co-designed an 8-bit accumulator-based microprocessor with GPT-4; taped out on SkyWater 130nm; authors claim "world's first wholly-AI-written HDL for tapeout." DOI 10.1109/MLCAD58807.2023.10299874. https://arxiv.org/abs/2305.13243
7. **AlphaChip** (Google DeepMind 2024-09-26 update) [VPR]: used in the last three TPU generations — TPU v5e: 10 blocks, 3.2% wirelength reduction vs human experts; Trillium (6th gen): 25 blocks, 6.2% reduction. MediaTek "expanded AlphaChip" for Dimensity flagship 5G chips used in Samsung phones. Open-sourced with a checkpoint trained on 20 TPU blocks. https://the-decoder.com/google-deepmind-opens-up-alphachip-letting-researchers-train-ai-on-custom-chip-designs/
8. **Honest / negative results**:
   - RTL-Repo [PR, IEEE LAD'24]: arXiv 2405.17378 (2024-05-27). 4,000+ Verilog samples with full repository context; repo-scale generation remains hard. https://arxiv.org/abs/2405.17378
   - GateTruth [AX]: arXiv 2608.12635 (2026-08-12). Mutation-testing audit: of 46 auditable RTLLM v2.0 designs, 72% have testbenches killing <95% of injected mutants, three kill 0%; NVIDIA CVDP is unauditable because reference solutions are withheld; an unnoticed 4096-token cap truncated 3 of 7 models. https://arxiv.org/abs/2608.12635
   - PerfReasoning [AX]: arXiv 2609.04476 (2026-09-03). Best closed models >90% on performance-reasoning Q&A, but performance-model construction averages <15% for all but one configuration. https://arxiv.org/abs/2609.04476

## Stream B — industrial formal verification and AI-assisted formal methods

1. **Arm** [PR]: Morello-Cerise, PLDI 2025 (Seoul, 16–20 June 2025), pp. 1961–1983, DOI 10.1145/3729329 — mechanised proof of strong secure encapsulation for the Arm Morello ISA at full-scale specification; funded in part by Arm. https://eprints.gla.ac.uk/354740/
2. **NVIDIA** (benchmark, not deployment) [AX]: FVEval, arXiv 2410.23299 (2024-10-15), NVIDIA + UC Berkeley — first benchmark for LLM formal-verification tasks (assertion generation from NL, assertion suggestion). https://arxiv.org/abs/2410.23299
3. **AWS** [CB]: "Formally verified AES-XTS: The first AES algorithm to join s2n-bignum" (2026) and "A decade of mathematical certainty: Reflections on the Automated Reasoning Group." Pages resolve; bodies were not extractable. https://www.amazon.science/blog/formally-verified-aes-xts-the-first-aes-algorithm-to-join-s2n-bignum · https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group
4. **Synopsys** [VPR, 2025-09-04]: Synopsys.ai Copilot expansion — 30% faster ramp for junior engineers; 10X–20X faster script generation with PrimeTime; an unnamed "leading AI infrastructure solutions provider" reported 35% productivity improvement in formal-verification workflows via automated formal testbench creation. Unnamed customer, no independent verification. https://embeddedcomputing.com/technology/ai-machine-learning/ai-logic-devices-worload-acceleration/synopsys-expands-synopsysai-copilot-with-new-genai-capabilities-to-accelerate-semiconductor-design
5. **Synopsys DSO.ai** product page resolves, marketing only, no numbers: https://www.synopsys.com/ai/ai-powered-eda/dso-ai.html
6. **AI-for-proof, limits** [AX]: "Agentic Proof Automation: A Case Study," arXiv 2601.03768 (2026-01-07), Xu & Odersky. Lean 4 mechanisation of System Capless, >14,000 LOC; agents completed 189 proof-engineering tasks at 87% success, 16% needing human intervention; authors state agents "fall short in creative reasoning." Academic case study, not industrial production. https://arxiv.org/abs/2601.03768

## Claims I could NOT verify
- **Intel**: TACAS 2025 Intel TDX formal-methods chapter redirects to a paywall (https://link.springer.com/chapter/10.1007/978-3-032-22749-2_3); ARITH 2025 divide/square-root RTL proof PDF timed out. Neither read.
- **AlphaChip primary sources**: deepmind.google blog and Nature addendum timed out; TPU/MediaTek/Samsung numbers are trade-press only.
- **AMD, Apple, NVIDIA production**: no 2024–2026 primary source quantifying formal-verification scale verified.
- **Microsoft**: no verified production AI-formal deployment (arXiv 2310.04353 seen only in search results).
- **Google hardware/TPU formal methods** beyond AlphaChip placement; **AWS quantified results** (blocks, policies, engineer-hours): not verified/extracted.
- **Cadence JasperGold/Verisium AI quantified results**: unverified; only a Renesas "6x" claim via a non-primary aggregator.
- **Official VerilogEval v2 leaderboard**: none verified; "ChipAgents SOTA on VerilogEval" is an unfetchable PR-wire release.
