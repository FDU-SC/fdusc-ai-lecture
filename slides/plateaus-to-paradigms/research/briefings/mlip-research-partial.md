# MLIP / AI-for-materials research notes (verified 2026-09-16)

## (a) Results table

| Date | Result | Venue tier | What was actually verified |
|---|---|---|---|
| 2022-02-05 (arXiv) | M3GNet, arXiv:2202.02450, DOI 10.1038/s43588-022-00349-3 | Peer-reviewed (Nat. Comput. Sci. 2022) | Title, authors (Chen & Ong), DOI, abstract; trained on MP relaxation trajectories; screened 31M hypothetical structures, ~1.8M potentially stable |
| 2023-02-28 | CHGNet, arXiv:2302.14231 | Preprint (API record) | Abstract: pretrained on MPtrj = "~1.5 million inorganic structures" incl. magnetic moments; 413k params (leaderboard) |
| 2023-08-28 (v3 2024-12-10) | Matbench Discovery, arXiv:2308.14920; **Nat. Mach. Intell. 7(6):836–847, online 2025-06-23, DOI 10.1038/s42256-025-01055-1** | Peer-reviewed | Journal/volume/pages/date/authors read from Nature citation metadata |
| 2023-12-29 (v3 2025-09-04) | MACE-MP-0, arXiv:2401.00096 | Preprint | Full abstract; MACE-MPA-0 = same architecture retrained on MPtrj + sAlex |
| 2024-05-08 | MatterSim v1, arXiv:2405.04967 | Preprint | Abstract: 0–5000 K, ≤1000 GPa, "up to ten-fold enhancement in precision", 15 meV/atom vs experiment ≤1000 K |
| 2024-05-11 | "Overcoming systematic softening in universal MLIPs by fine-tuning", arXiv:2405.07105 | Preprint | Source of MACE-MPA-0; documents systematic softening failure mode |
| 2024-10-16 | OMat24, arXiv:2410.12771 | Preprint (Meta tech report) | ~118M structures, "400M+ core hours" (via subagent full-text read) |
| 2024-10-29 | Orb-v2, arXiv:2410.22570 | Preprint | Title/date/authors via API |
| 2025-02-17 | eSEN, arXiv:2502.12147 | Preprint | Abstract: energy-conservation test; SoTA on stability/thermal-conductivity/phonons |
| 2025-04-08 | Orb-v3, arXiv:2504.06231 | Preprint | Abstract: ">10× reduction in latency and >8× reduction in memory" |
| 2025-06-30 (v2 2026-03-04) | UMA, arXiv:2506.23971 | Preprint (Meta FAIR) | Abstract: "half a billion unique 3D atomic structures"; UMA-medium 1.4B params, ~50M active |
| 2025-08-25 | GRACE foundation models, arXiv:2508.17936 | Preprint | Foundational GACE paper |
| 2026-04-10 | EquiformerV3, arXiv:2604.09130 | Preprint | 1.75× speedup over EquiformerV2 |
| 2026-07-12 | TECE (edge cluster expansion + radial rotary attention), arXiv:2607.10664 | Preprint | #2 on leaderboard |
| 2026-09-13 | Prophet-OAME-MBD enters Matbench Discovery at **CPS 0.912, rank 1** | Preprint (vendor PDF) | Leaderboard row + RSS metrics |

## Matbench Discovery — what it actually measures

It does **not** use a metric called "corrected predicted stability". As of the 2026-09-16 fetch the site ranks by **CPS** ("Combined Performance Score"), defined on the site as: "CPS combines discovery F1 (50%), geometry RMSD (10%), and phonons κ_SRME (40%). MD and diatomics are excluded. CPS uses unique-prototype discovery scores." (https://matbench-discovery.materialsproject.org/). The underlying paper metric is **F1** for predicting which unrelaxed WBM structures fall on/below the MP convex hull, plus **DAF** (discovery acceleration factor vs random), MAE/R²/RMSE on formation energy, and geometry RMSD. Test sets: WBM 256,963 structures / 85 elements; PhononDB PBE 103 structures / 34 elements; DynaMat v1.0 17 systems (https://matbench-discovery.materialsproject.org/benchmarks).

**Leaderboard (unique-prototype view, 43 of 53 eligible models, fetched 2026-09-16):**

| # | Model | CPS | F1 | DAF | MAE (eV/atom) | κ_SRME | RMSD (Å) | Params | Date added | Training set |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Prophet-OAME-MBD | 0.912 | 0.928 | 6.065 | 0.018 | 0.065 | 0.059 | 62.3M | 2026-09-13 | 16.4M(324M) MPtrj+OMat24+sAlex+ELEMENTA |
| 2 | TECE-OAM-RRA-1.0 | 0.908 | 0.929 | 6.073 | 0.017 | 0.093 | 0.058 | 222M | 2026-07-05 | 6.6M(113M) MPtrj+OMat24+sAlex |
| 3 | EquFlashV2 | 0.907 | 0.929 | 6.069 | 0.018 | 0.094 | 0.058 | 44.9M | 2026-06-11 | 6.6M(113M) |
| 4 | EquiformerV3+DeNS-OAM | 0.902 | **0.931** | 6.074 | 0.018 | 0.118 | 0.059 | 30.3M | 2026-04-07 | 6.6M(113M) |
| 5 | GRACE-3L-OAM-L | 0.900 | 0.925 | 6.041 | 0.018 | 0.121 | 0.058 | 42.1M | 2026-07-02 | 6.6M(113M) |
| 8 | eSEN-30M-OAM | 0.888 | 0.925 | 6.069 | 0.018 | 0.170 | 0.061 | 30.2M | 2025-03-17 | 6.6M(113M) |
| 12 | SevenNet-Omni-i12 | 0.873 | 0.906 | 5.954 | 0.021 | 0.192 | 0.062 | 54.9M | 2026-01-12 | COSMOSDataset |
| 15 | **ORB v3** | 0.860 | 0.905 | 5.912 | 0.024 | 0.210 | 0.075 | 25.5M | 2025-04-05 | 6.47M(133M) MPtrj+Alex+OMat24 |
| 17 | Allegro-OAM-L | 0.840 | 0.895 | 5.674 | 0.022 | 0.319 | 0.065 | 9.7M | 2025-09-08 | 6.6M(113M) |
| 22 | **MACE-MPA-0** | 0.795 | 0.852 | 5.582 | 0.028 | 0.412 | 0.073 | 9.06M | 2024-12-09 | 3.37M(12M) MPtrj+sAlex |
| 25 | MatterSim v1 5M | 0.767 | 0.862 | 5.852 | 0.024 | 0.575 | 0.073 | 4.55M | 2024-12-16 | MatterSim (own) |
| 35 | **MACE-MP-0** | 0.637 | 0.669 | 3.777 | 0.057 | 0.697 | 0.091 | 4.69M | 2023-07-14 | 146k(1.58M) MPtrj |
| 41 | M3GNet | 0.428 | 0.569 | 2.882 | 0.075 | 0.593 | 0.112 | 228k | 2022-09-20 | 62.8k(188k) MPF |
| 42 | CHGNet | 0.400 | 0.613 | 3.361 | 0.063 | 0.689 | 0.095 | 413k | 2023-03-03 | 146k(1.58M) MPtrj |
| 43 | NequIP-GNoME | n/a | 0.829 | 5.523 | 0.035 | n/a | n/a | 16.2M | 2024-02-03 | 6M(89M) GNoME |

Full-test-set F1 values differ slightly (e.g. eSEN-30M-OAM 0.902, ORB v3 0.887, MACE-MP-0 0.668, GRACE-3L-OAM-L 0.905) — from https://matbench-discovery.materialsproject.org/rss.xml.

**UMA is NOT on the Matbench Discovery leaderboard** (scanned all 66 RSS entries; /models/uma-s-1p1 returns HTTP 404).

## Compute cost (verified by subagent full-text reads)

- MACE-MP-0: original MP-0a "200 epochs with 40–80 NVIDIA A100 GPUs across 10–20 nodes on Perlmutter"; updated MP-0b3 "99 epochs with 32 NVIDIA H100 GPUs across 8 nodes on the Jean Zay cluster"; "Training the medium-sized model took approx. 2,600 GPU hours" (https://arxiv.org/html/2401.00096v3). MACE-MPA-0 has **no** separate figure.
- UMA training (Table 8, https://arxiv.org/html/2506.23971v1): UMA-S 46,080 H200 GPU-h; UMA-M 129,024 H200 GPU-h; UMA-L 95,232 H100 GPU-h.
- eSEN-30M-MP: 335 A100 GPU-days, as cited by DPA4 (https://arxiv.org/html/2606.02419v3).
- GNoME: the widely repeated "~5 million GPU-hours" figure is **not** in Nature 624:80–85; the paper says only "Training was performed on four TPU v3 chips" plus hundreds of millions of first-principles calculations (https://www.nature.com/articles/s41586-023-06735-9).
- Inference, single H100 80 GB (UMA Table 3): UMA-S 44/16/1.6 steps/s at 100/1k/10k atoms; Orb-v3-conservative-inf-omat 77/30/3.7; MACE-MPA-0 38/24/2.9; eSEN-30M-OAM 8/1.7/OOM. "UMA-S can simulate 1000 atoms at 16 steps per second (1.4 ns-per-day)."
- **"10⁶× faster than DFT" is not supported by any primary source found.** The verifiable tier is ~10⁴–10⁵ on like-for-like relaxations: M3GNet "about 22 seconds on a single CPU core … while the corresponding DFT relaxation took 15 hours on 32 cores" (~7.9×10⁴ core-seconds). The M3GNet phonon "four orders of magnitude" claim is explicitly apples-to-oranges (frozen-phonon vs DFPT, different supercells). A 23-model 2026 benchmark states the scaling caveat: DFT cost ≈ cubic in atom count vs near-linear for fixed-cutoff MLFFs (https://arxiv.org/pdf/2607.07647).

## What "DFT accuracy" actually means

- Reference data are predominantly **PBE / PBE+U** (MPtrj, MPF, OMat24). r2SCAN alternatives exist (MP-ALOE, arXiv:2507.05559) and functional-mixing is an active problem (arXiv:2607.24327).
- Documented failure modes with sources: **systematic softening** of universal potentials (arXiv:2405.07105); **Hubbard-U mismatch** ("Better without U", arXiv:2601.21056); **heterogeneous catalysis** (arXiv:2512.16702, J. Chem. Phys. 164, 194119 (2026)); **surfaces/cleavage** (arXiv:2508.21663, AI Sci. 1, 025002 (2025); arXiv:2509.25807); **phonons/anharmonicity** (arXiv:2509.03401, Adv. Intell. Discov. 2025; arXiv:2402.18891); **migration/reaction barriers** (arXiv:2512.03642, DOI 10.1039/D5DD00534E); **DFT reference uncertainty itself** (arXiv:2510.19774).
- **Magnetism**: only 3 of the leaderboard's models predict magnetic moments; MACE-MP-0 has no explicit spin degrees of freedom. **Long range**: 6 Å cutoffs (UMA, Orb-v3) mean adsorbates >7 Å apart are treated as non-interacting; MACE-MP-0 has no explicit long-range electrostatics.

## Dataset sizes as of 2026 (subagent, URLs fetched 2026-09-16)

| dataset | count | functional | date | URL |
|---|---|---|---|---|
| Materials Project | **154,387** structures; 35,388 with E_hull ≤ 0 (PBE/GGA+U) | PBE/PBE+U; r2SCAN recompute ~26 % done | DB v2026.04.13, live 2026-06-08 | https://optimade.materialsproject.org/v1/structures?page_limit=1 |
| OQMD | 568,000 entries *as included in LeMat-Bulk* (post-exclusion) — **not** OQMD's own total | PBE(+U) | 2025-11 | https://arxiv.org/abs/2511.05178 |
| Alexandria | **5.8M** structures, 175k on the convex hull | PBE/PBEsol/SCAN | v1 2025-12-09, v2 2026-05-01 | https://arxiv.org/abs/2512.09169 |
| sAlex / sAlex25 | sAlex 10M train + 0.5M val; sAlex25 14M | PBE | 2026 | https://arxiv.org/abs/2512.09169 |
| OMat24 | **111M** structures (train split 100,824,585) | PBE and PBE+U | v1 2024-10-16, v2 2026-05-20 | https://arxiv.org/html/2410.12771v2 |
| OMol25 | **>140M** DFT single-point calculations, ~83M unique systems, 83 elements | ωB97M-V/def2-TZVPD | v1 2025-05-13, v2 2026-03-04 | https://arxiv.org/html/2505.08762v2 |
| MatPES | ~400,000 structures | PBE + r2SCAN | 2025-03-06 | https://arxiv.org/abs/2503.04070 |
| MPtrj | ~1.5M structures | PBE/PBE+U | 2023 | https://arxiv.org/abs/2302.14231 |

Verbatim quotes: MP metadata `data_available: 154387`; LeMat-Bulk "Materials Project (146,000 entries), OQMD (568,000 entries), and Alexandria (4.62 million entries)"; Alexandria "now contains 5.8 million structures with 175 thousand compounds on the convex hull"; OMat24 "a total of 111 million structures". Licences: OMat24 CC 4.0 (https://huggingface.co/datasets/fairchem/OMAT24), OMol25 CC BY 4.0 (https://huggingface.co/facebook/OMol25).

## Could NOT verify

1. OQMD's own current total (oqmd.org DNS fails) — 568k is a LeMat-Bulk post-exclusion figure only. OMat24 unique-composition count. "sAlex ≈ 6M" (contradicted: sAlex is 10M/10.5M). NanoMagnet, CarboNet, TM23, DPA/OpenLAM, MatText, JARVIS-DFT.
2. Journal venues for OMat24 and OMol25 — arXiv/technical report only, no peer-reviewed venue found.
4. Any independent replication of Prophet-OAME-MBD's #1 CPS (vendor PDF only, no arXiv).
5. MatterGen's generated space group / the claim that TiCr2O6 was validated — **false** per subagent full-text search.
6. Excited-state behaviour of MLIPs — no benchmark found.
7. A-Lab H2O/CO2 contamination argument — absent from the PRX Energy critique full text.
