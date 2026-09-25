# AI for Science & STEM, 2024 – Sep 2026 — lecture cut

1,400-word slide-ready brief. Tier: **[PR]** peer-reviewed · **[PP]** preprint · **[OFF]** official · **[JOUR]** journalism. Full evidence base with 79 URLs: `ai-for-science-briefing.md`.

## Headline results

| Date | Result | Tier | Verified |
|---|---|---|---|
| 2024-05-08 | AlphaFold 3: protein + DNA/RNA/ligand co-folding | **[PR]** | No code/weights/data; 10 predictions/day server cap |
| 2024-07 | AlphaProof + AlphaGeometry: 4/6 IMO 2024, silver | **[OFF]**→**[PR]** | Lean-checked; 3-day runtime |
| 2024-12-04 | GenCast beats ECMWF ENS on 97.2% of 1,320 targets | **[PR]** | Retrospective 2019 ERA5 |
| 2025-03-01 | A-Lab synthesis audit | **[PR]** PRX Energy 3, 011002 | 78% claim → **3/58 = 5%** |
| 2025-07-01 | ECMWF AIFS ENS operational | **[OFF]** | 31 km, >10× faster, ~1000× less energy |
| 2025-08-14 | Generative de novo antibiotics | **[PR]** Cell 188(21):5962 | 24 synthesised, 7 active, 2 bactericidal in vivo |
| 2025-11-12 | AlphaProof in Nature (651:607–613) | **[PR]** | RL inside Lean; 80M auto-formalized statements |
| 2026-01-19 | Nature corrects the A-Lab paper | **[PR]** | Narrowed to 36 of 57 |
| 2026-03-02 | AICON operational at DWD | **[PP]** | 13 km, 3-hourly |
| 2026-04-04 | AI resolves open GDA last-iterate rate question | **[PP]** | "Discovered autonomously by an AI system" |
| 2026-05-21 | AlphaProof Nexus: 9/353 open Erdős problems | **[PP]** | Lean-verified; few hundred USD each |
| 2026-05-22 | OpenAI refutes Erdős 1946 unit-distance conjecture | **[JOUR]** | 9 mathematicians incl. Gowers; no paper |
| 2026-07-15/16 | IMO 2026: dots-note 3.0 scores 42/42 | IMO graders | First perfect AI score; gold cutoff 29 |
| 2026-09-04 | Anthropic formalises Fermat's Last Theorem | **[OFF]** | 30,300 theorems, 13M lines Lean |
| 2026-09-07 | Rentosertib reverses biological age (Phase IIa) | **[PR]** | 42 patients, 6 aging clocks |
| 2026-09-09 | GENESIS-IPF-3: first Phase III AI-drug trial | **[OFF]** | NCT07687459; first patient dosed |
| 2026-09-14 | CMS L1 trigger: distilled normalising flow | **[PP]** | 40 MHz; FPGA latency **27–52 ns** |

## Mathematics

**AlphaProof** (Hubert/Mehta/Sartran *et al.*, Nature **651:607–613**, 12 Nov 2025, [10.1038/s41586-025-09833-y](https://doi.org/10.1038/s41586-025-09833-y)): RL inside Lean after **80M auto-formalized statements**; AlphaProof + AlphaGeometry took **4/6 IMO 2024** = silver (28/42). Authors flag limits on other problem classes. **AlphaGeometry2** ([2502.03544](https://arxiv.org/abs/2502.03544)): **84%** on IMO geometry 2000–2024 vs 54% — historical problems.

**IMO evaluation is the real story.** 2025: OpenAI announced **18 Jul** (35/42, graded by three IMO gold medallists, having declined official involvement); DeepMind announced **21 Jul** (also 35/42) but **graded by IMO judges** and certified by IMO President Gregor Dolinar. DeepMind's Thang Luong noted the IMO uses a **non-public scoring guide** without which a medal claim is unverifiable. **72 humans won gold, 5 scored a perfect 42** — AI did not beat the top humans ([eu.36kr.com](https://eu.36kr.com/en/p/3389556081328263)).

2026 (Shanghai, 15–16 Jul) had a **formal AI track**: problems released to models only after each day's human session, **all human intervention prohibited**. Xiaohongshu's **dots-note 3.0** scored **42/42 from IMO graders** — first perfect AI score in IMO history, 13 points above the 29-point gold cut ([China Daily](https://cn.chinadaily.com.cn/a/202607/22/WS6a607452a310d709c2fbf0ec.html)). Anthropic's "Claude Opus 5 42/42" is **model-panel self-grading**, not IMO grading — do not present them as equivalent.

**AlphaProof Nexus** ([2605.22763](https://arxiv.org/abs/2605.22763)): **9 of 353 open Erdős problems** autonomously resolved, **44/492 OEIS conjectures**, a few hundred USD each; two problems were **open 56 years**. Caveat: a *basic* LLM+Lean-compiler loop reproduced the successes. 9/353 ≈ 2.5%, matching **Tao's** ~1–2% estimate. Cleanest machine-checked case: [2604.03782](https://arxiv.org/abs/2604.03782) — "discovered autonomously by an AI system capable of writing formal proofs in Lean". **mathlib 2026-09-16: 136,850 definitions, 288,518 theorems, 772 contributors.** Tao co-authored [2607.07779](https://arxiv.org/abs/2607.07779), arguing systems remain "fundamentally limited" at frontier research mathematics. **Warning:** a Lean `native_decide` unsoundness (9 Sep 2026) allows a forged "proof".

## Biology, medicine, chemistry

**AlphaFold 3** shipped no code, weights or data — a 10/day server, restricted ligands, pseudocode. Reviewer Dunbrack was denied code "despite repeated requests" ([Retraction Watch](https://retractionwatch.com/2024/05/14/nature-earns-ire-over-lack-of-code-availability-for-google-deepmind-protein-folding-paper/)); code/weights came in Nov 2024 under a **non-commercial licence** that demonstrably blocked at least one published benchmark.

**Do not claim AF3 is worse than AF2.** On **110 unseen antibody–antigen complexes** AF3 **beats** AF2, Boltz-1 and Chai-1 ([bioRxiv](https://www.biorxiv.org/content/10.1101/2025.07.11.662141v2.full)). The real failure is **ranking**: best-model DockQ rises <0.3→>0.5 across 200 samples, top-ranked only reaches 0.37. FoldBench: antibody–antigen fails >60% for most models, AF3 best at 47.9%.

**Best 2026 co-folding result is negative** ([2603.05532](https://arxiv.org/abs/2603.05532)): Boltz-2 on **16,780 + 21,702 compounds** shows multiple poses, weak affinity correlation, **no significant correlation in the top 100** — "lacks the energetic resolution required for lead identification."

**Antibiotics (strongest wet-lab result here):** Cell **188(21):5962–5979.e22**, 14 Aug 2025 — 24 synthesised, 7 selectively antibacterial, **2 bactericidal against MDR isolates, efficacious in mice**.

**Clinic:** rentosertib (AI molecule + AI-found TNIK target) — Phase IIa biological-age reversal across six independent clocks; **first Phase III trial of a generative-AI drug** dosed **9 Sep 2026** (NCT07687459). Isomorphic Labs had **not** started trials. **AAV design: unverified.** **ESM3** (Science, 21 Feb 2025) produced esmGFP; **no evidence of an "ESM4."**

## Physics, weather, climate

**Shipped, but has not replaced physics.** ECMWF AIFS Single operational **25 Feb 2025**, AIFS ENS (51 members) **1 Jul 2025** — 31 km vs 9 km, up to **20%** surface-temperature gains, **>10× faster**, **~1000× less energy**. DWD **AICON** operational since **2 Mar 2026**. **But** on operational AIFS-vs-IFS 10 m wind over >9,000 stations, **raw IFS was substantially superior at all lead times** ([2606.02508](https://arxiv.org/abs/2606.02508)). GenCast's 97.2% win was against **retrospective ERA5**. Against station observations, AI weather errors run **15–45% larger** than against reanalysis ([2509.01879](https://arxiv.org/abs/2509.01879)). **No agency has retired physics NWP.**

**CERN gives the hardest production numbers:** CMS L1/Global Trigger, **40 MHz** in a **50 ns** budget, autoencoder live on Run 3 data; 2026 flow distillation at **27–52 ns** FPGA latency, ~325× compression, 8-bit.

**Correct two common mis-citations:** the 2024 RL tearing-mode paper (Nature 626:746–751) was **DIII-D, not KSTAR**; and "Samsung uses AlphaChip" is a misreading. **2025–26 fusion RL: nothing solid — treat as unresolved.**

## Materials

**Matbench Discovery** (*Nat. Mach. Intell.* 7(6):836–847, 2025) — **CPS = discovery F1 (50%) + geometry RMSD (10%) + phonon κ_SRME (40%)**, not throughput. Live leaderboard 2026-09-16: **Prophet-OAME-MBD 0.912** > TECE-OAM-RRA 0.908 > EquFlashV2 0.907 > EquiformerV3+DeNS 0.902 > GRACE-3L 0.900 > eSEN-30M 0.888 > ORB v3 0.860 > MACE-MPA-0 0.795 > MatterSim 0.767 > **MACE-MP-0 0.637** > M3GNet 0.428 > CHGNet 0.400. The paper's 2024 ordering is **out of date**. **UMA is not on this leaderboard.**

**Compute:** UMA-medium **129,024 H200 GPU-hours**; MACE-MP-0 medium **~2,600 GPU-hours**; but **data generation dwarfs training** — OMat24 (**111M structures**) 400M+ core-hours, OMol25 (**>140M calculations**) 6.6B CPU core-hours. **No primary source claims "millions of times faster than DFT"** — the best like-for-like figure is ~7.9×10⁴, and the heaviest MLIPs are **under 2×** DFT on a 192-atom benchmark ([2607.07647](https://arxiv.org/pdf/2607.07647)). "DFT accuracy" = **PBE-level** matching only; **only 3 leaderboard models emit magnetic moments** and MACE-MP-0 has no spin at all.

**MatterGen** (*Nature* 2025) now has a peer-reviewed correction: "**MatterGen predicts compounds from the training dataset**" (*Mater. Horiz.* `d6mh00268d`).

## Formal verification and chip design

**AlphaChip dispute is unresolved.** Nature 2021 → Correction 2022 → **Editor's Note 2023-09-20** → Note removed and **Addendum** 2024-09-26, renamed AlphaChip. Critiques ([2302.11014](https://arxiv.org/abs/2302.11014)): a stronger simulated-annealing baseline gets **26% better proxy cost at equal runtime with a quarter of the resources**; commercial placer beats it by **34% routed wirelength**. Markov ([2306.09633](https://arxiv.org/abs/2306.09633)): not top-5 in the 2023 MLCAD contest. Google's rebuttal ([2411.10053](https://arxiv.org/abs/2411.10053)): the critique didn't run the method as described. **Production evidence is exclusively Google's own.**

**LLM RTL is weaker than leaderboards suggest:** GateTruth ([2608.12635](https://arxiv.org/abs/2608.12635)) finds **72% of 46 RTLLM v2.0 designs below a 95% mutant-kill floor; three at 0%**. **No verified production deployment of LLM-generated RTL.** **Autoformalization, not proving, is the AI-prover bottleneck:** miniF2F end-to-end is **~36%** vs the 97%/69% reported when scored separately ([2511.03108](https://arxiv.org/abs/2511.03108)). Industrial anchors are thin but real: **Arm Morello-Cerise** (PLDI 2025), **AWS Cedar-in-Lean**.

## Critiques: what actually failed

**A-Lab is the strongest documented failure, not AlphaFold 3.** Claimed 43/58 (78%); Leeman *et al.* (PRX Energy 3, 011002) found "significant issues with 42", only three correctly synthesised — **all previously reported**. Real rate **3/58 = 5%**; Nature's **19 Jan 2026 correction** narrowed it to 36 of 57, "new to the laboratory."

**GNoME's 380,000 "stable" materials** drew "scant evidence" for novelty, credibility and utility in the first 250 entries (Chem. Mater. `10.1021/acs.chemmater.4c00643`); GNoME **never mentions compositional disorder**, and 0 K convex-hull stability is not synthesizability.

**Wet-lab validation fraction: no reliable estimate exists.** No systematic study covers AI-for-science. The closest figure (12/283 = 4.2%) is unusable — in vivo validation was an *inclusion criterion*. **No documented replication failure exists for halicin or Wong *et al.* 2023** — asserting one would be fabrication.

**AI drug success rates are disputed:** Phase I 80–90% / Phase II ~40% on just **67 molecules**, of which only 3–9 targets were genuinely novel (Jayatunga *et al.*, all BCG affiliates). Industry norm is **40–60%**.

**Three claims worth the lecture's weight:** (a) AI now produces *machine-checked, genuinely new* mathematics; (b) AI-driven science has shipped in operational infrastructure — ECMWF AIFS ENS, DWD AICON, CMS L1 at 27–52 ns — while **not** beating physics-based NWP where measured operationally; (c) the most instructive episode is the **A-Lab correction**: 78% audited down to 5%, then formally narrowed by Nature.
