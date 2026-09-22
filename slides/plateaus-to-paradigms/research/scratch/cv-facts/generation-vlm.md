# Generative Vision Models & Vision-Language Models — Verified Facts

Compiled 2026-09-19. Working dir `/home/zecyel/slides/ch1`. All facts below were read from **primary sources** (the papers' own LaTeX/PDF, official proceedings, official model cards). FID/IS numbers are quoted **with their exact variant, sample count, and reference split**, because these are the most-often-misquoted items in this area.

**How sources were obtained (transparency):** direct `arxiv.org` downloads were network-blocked from this machine, so the full arXiv text was read through the **ar5iv** rendering of the official arXiv LaTeX source (`ar5iv.labs.arxiv.org/html/<id>`), and venue-specific numbers were cross-checked against the **official** CVF Open Access PDFs, NeurIPS proceedings PDFs, and PMLR PDF. See "Retrieval failures" at the end.

---

## A) GENERATION

### A1. Identification: year, venue, first author, key idea

| Model | Year + venue | First author | Key idea (1–2 sentences) |
|---|---|---|---|
| **GAN** | 2014, NIPS (NeurIPS) 2014 | Ian J. Goodfellow | Two MLPs trained in a minimax two-player game: generator `G` maps noise to samples, discriminator `D` estimates P(sample came from data rather than `G`); `G` is trained to maximise `D`'s error. At the optimum `G` recovers the data distribution and `D` = 1/2 everywhere; trainable by backprop with no Markov chains or approximate inference. |
| **DCGAN** | arXiv Nov 2015; **ICLR 2016** | Alec Radford | A class of convolutional GANs with architectural constraints that make training stable: all-convolutional G/D, strided convolutions instead of pooling, batch normalisation, and no fully-connected hidden layers. The learned discriminator features transfer as general-purpose image representations. |
| **pix2pix** | arXiv Nov 2016; **CVPR 2017** | Phillip Isola | A generic **conditional** GAN for image-to-image translation: U-Net generator + a 70×70 **PatchGAN** discriminator, with loss = L1 + cGAN. It learns the loss (a structured loss over output patches) rather than using a hand-designed per-pixel loss. |
| **CycleGAN** | arXiv Mar 2017; **ICCV 2017** | Jun-Yan Zhu | Unpaired image-to-image translation with two mappings `G:X→Y`, `F:Y→X`, adversarial losses on both, plus a **cycle-consistency** loss `F(G(x))≈x`, `G(F(y))≈y`. This removes the need for paired training examples. |
| **StyleGAN** | arXiv Dec 2018; **CVPR 2019** | Tero Karras | A **style-based generator**: a mapping network turns `z` into an intermediate `w`, and `w` is injected at every resolution through adaptive instance normalisation (AdaIN), with independent per-layer noise. This gives scale-specific style control and a more disentangled latent space; the paper also releases the FFHQ dataset. |
| **StyleGAN2** | arXiv Dec 2019; **CVPR 2020** | Tero Karras | Removes StyleGAN's characteristic artifacts by **weight demodulation** (replacing AdaIN), **lazy regularization**, and **removing progressive growing** (skip connections in G, residual D); adds path-length regularization. |
| **DDPM** | arXiv Jun 2020; **NeurIPS 2020** | Jonathan Ho | Learns to reverse a gradual Gaussian noising process; the objective is a (re-weighted) variational bound, and a novel connection to denoising score matching yields the best results. Sampling is iterative denoising with a learned Gaussian reverse process. |
| **LDM / Stable Diffusion** | arXiv Dec 2021; **CVPR 2022** (weights released 2022) | Robin Rombach | Run diffusion in the **compressed latent space** of a pretrained autoencoder ("perceptual compression") instead of pixel space, keeping a U-Net with cross-attention for text/layout conditioning. This cuts training and inference cost dramatically versus pixel-space diffusion. |
| **DiT** | arXiv Dec 2022; **ICCV 2023** | William Peebles | Replaces the U-Net backbone of latent diffusion with a plain **Vision Transformer operating on latent patches**, injecting timestep/class via adaLN-Zero. Shows diffusion quality scales predictably with transformer Gflops. |

### A2. One concrete quality metric each — exact number, exact benchmark/variant

> ⚠️ **Read the "variant" column.** FID on CIFAR-10 ≠ FID-50K on ImageNet-256², and FID against the *training set* ≠ FID against the *validation set*. GAN/DCGAN predate IS and FID entirely.

| Model | Metric + number | Dataset / benchmark | Exact variant & protocol | URL (primary) |
|---|---|---|---|---|
| **GAN (2014)** | Gaussian **Parzen-window log-likelihood**: **MNIST 225 ± 2**; **TFD 2057 ± 26** | MNIST (real-valued) and Toronto Face Database (TFD) | Parzen window fitted to generated samples, σ cross-validated on the validation set; mean log-likelihood on test set. Comparators: DBN 138 ± 2 / 1909 ± 66; Stacked CAE 121 ± 1.6 / 2110 ± 50; Deep GSN 214 ± 1.1 / 1890 ± 29. **No Inception Score and no FID in this paper** (IS was introduced by Salimans et al. 2016). | [arXiv:1406.2661](https://arxiv.org/abs/1406.2661), [NeurIPS 2014](https://proceedings.neurips.cc/paper_files/paper/2014/hash/f033ed80deb0234979a61f95710dbe25-Abstract.html) |
| **GAN (2014) — CIFAR-10** | **No quantitative number reported.** The paper reports only qualitative CIFAR-10 samples (fully-connected model, and conv-D/deconv-G) | CIFAR-10 | Fig. 2 of the paper shows CIFAR-10 samples only. There is **no** CIFAR-10 IS/FID/Parzen figure to quote from the original paper. | [arXiv:1406.2661](https://arxiv.org/abs/1406.2661) |
| **DCGAN** | **CIFAR-10 classification accuracy 82.8%** | CIFAR-10 (features), DCGAN trained on ImageNet-1k | Discriminator conv features from all layers (max-pooled to 4×4, 28 672-dim) + L2-SVM. Baselines quoted in-paper: K-means 80.6%, multi-layer K-means 82.0%. Second result: SVHN with only 1000 labels → **22.48% test error**. No FID/IS (both metrics postdate DCGAN). | [arXiv:1511.06434](https://arxiv.org/abs/1511.06434) |
| **pix2pix** | **FCN-score (per-pixel accuracy) 0.66** | Cityscapes labels↔photos | U-Net + L1+cGAN: per-pixel acc. **0.66**, per-class acc. 0.23, class IOU 0.17. Ground truth: 0.80 / 0.26 / 0.21. (FCN-score = accuracy of an FCN-8s semantic segmenter trained on Cityscapes, applied to synthesised photos.) AMT "real vs fake": **18.9% ± 2.5%** of Turkers labelled generated aerial photos as real (L1 baseline 0.8% ± 0.3%); colorization **22.5% ± 1.6%**. | [CVPR 2017 (CVF)](https://openaccess.thecvf.com/content_cvpr_2017/html/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.html), [arXiv:1611.07004](https://arxiv.org/abs/1611.07004) |
| **CycleGAN** | **AMT "real vs fake": 26.8% ± 2.8%** (map→photo) / **23.2% ± 3.4%** (photo→map) of Turkers labelled results real | Google Maps ↔ aerial photos | Unpaired setting. FCN-scores (Cityscapes): labels→photos **0.52** per-pixel / 0.17 / 0.11 (pix2pix on paired data: 0.71 / 0.25 / 0.18); photo→labels **0.58** / 0.22 / 0.16 (pix2pix: 0.85 / 0.40 / 0.32). | [ICCV 2017 (CVF PDF)](https://openaccess.thecvf.com/content_ICCV_2017/papers/Zhu_Unpaired_Image-To-Image_Translation_ICCV_2017_paper.pdf), [arXiv:1703.10593](https://arxiv.org/abs/1703.10593) |
| **StyleGAN** | **FID = 4.40** | FFHQ, 1024² | Config **f** (style-based + mixing regularization). CelebA-HQ 1024² = **5.17**; baseline progressive GAN (config a) = 8.04 (FFHQ) / 7.79 (CelebA-HQ). ⚠️ **Variant:** "we calculate the FIDs using **50,000 images drawn randomly from the training set**, and report the **lowest distance encountered over the course of training**." Reference = training set, not validation set. LSUN Bedroom 256² FID 2.65, LSUN Car 512×384 FID 3.27 (50k images). | [CVPR 2019 (CVF PDF)](https://openaccess.thecvf.com/content_CVPR_2019/papers/Karras_A_Style-Based_Generator_Architecture_for_Generative_Adversarial_Networks_CVPR_2019_paper.pdf), [arXiv:1812.04948](https://arxiv.org/abs/1812.04948) |
| **StyleGAN2** | **FID = 2.84** | FFHQ, 1024² | Config **f** (StyleGAN2). StyleGAN baseline (config a) = **4.40** in the same table. LSUN Car 512×384: **2.32** (StyleGAN 3.27). ⚠️ **Variant:** "For each training run, we selected the training snapshot with the **lowest FID**. We computed each metric **10 times with different random seeds** and report their average." StyleGAN2's main text does **not** restate the reference split; it inherits StyleGAN's training-set/50k protocol for FFHQ (flagged below). | [CVPR 2020 (CVF PDF)](https://openaccess.thecvf.com/content_CVPR_2020/papers/Karras_Analyzing_and_Improving_the_Image_Quality_of_StyleGAN_CVPR_2020_paper.pdf), [arXiv:1912.04958](https://arxiv.org/abs/1912.04958) |
| **DDPM** | **FID = 3.17**, **Inception Score = 9.46 ± 0.11** | CIFAR-10, **unconditional** | Model `L_simple`. ⚠️ **Variant:** "Our FID score is computed **with respect to the training set**, as is standard practice; when we compute it with respect to the **test set, the score is 5.24**." 256×256 LSUN: sample quality similar to ProgressiveGAN (Table 3: LSUN Bedroom 6.36 with `L_simple`, 4.90 with the large model). | [NeurIPS 2020 proceedings PDF](https://proceedings.neurips.cc/paper_files/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf), [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) |
| **LDM / Stable Diffusion** | **FID = 3.60**, **IS = 247.67** | ImageNet **256×256**, class-conditional | `LDM-4-G`, 250 DDIM steps, classifier-free guidance scale **1.5**. No-guidance `LDM-4` = 10.56. Comparators in the same table: ADM-G 4.59 / 186.7; ADM 10.94; BigGAN-deep 6.95. Text-to-image (MS-COCO 256²): `LDM-KL-8-G` **FID 12.63 / IS 30.29** with **1.45B** params (GLIDE 6B = 12.24; Make-A-Scene 4B = 11.84; CogView 4B = 27.10). Unconditional CelebA-HQ 256² **FID 5.11**. ⚠️ **Variant:** FID/P&R computed from **50k samples vs the entire training set** of each dataset, using `torch-fidelity`; the authors note results shift slightly (e.g. 7.76 vs 7.77 ImageNet) depending on the pipeline. Text-to-image FID compares against **30 000 MS-COCO validation samples**. | [CVPR 2022 (CVF PDF)](https://openaccess.thecvf.com/content/CVPR2022/papers/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.pdf), [arXiv:2112.10752](https://arxiv.org/abs/2112.10752) |
| **DiT** | **FID-50K = 2.27**, sFID 4.60, **IS = 278.24** | ImageNet **256×256**, class-conditional | `DiT-XL/2-G`, classifier-free guidance **cfg = 1.5**. No guidance: 9.62. ImageNet **512×512**: **FID 3.04**. ⚠️ **Variant:** "we report **FID-50K using 250 DDPM sampling steps**… all values … are obtained by exporting samples and using **ADM's TensorFlow evaluation suite**" (i.e. ImageNet **validation**-set reference), 675M params, 118.64 Gflops at 256². The paper states it lowers "the previous best FID-50K of **3.60** achieved by LDM to 2.27". | [ICCV 2023 (CVF PDF)](https://openaccess.thecvf.com/content/ICCV2023/papers/Peebles_Scalable_Diffusion_Models_with_Transformers_ICCV_2023_paper.pdf), [arXiv:2212.09748](https://arxiv.org/abs/2212.09748) |

**Extra compute datapoints (generation), all quoted verbatim from the papers:**

- **StyleGAN2**: Table 5 — training a **single FFHQ config f network took ≈ 0.23 V100 GPU-years and 0.68 MWh**; the **entire project** consumed **51.05 V100 GPU-years / 131.61 MWh** (≈ "51 years … using a single GPU").
- **DiT**: Table 4 — `DiT-XL/2` at 256² was trained for **7 000K steps, batch 256, 118.64 Gflops, 675M params** (VAE excluded; VAE has 84M params).
- **CLIP's ViT-L/14**: 12 days on 256 V100 GPUs (see B).

---

## B) VISION-LANGUAGE

| Model | Year + venue | First author | Key idea | Metric + number | Dataset / benchmark | URL |
|---|---|---|---|---|---|---|
| **CLIP** | arXiv Feb 2021; **ICML 2021** (PMLR v139) | Alec Radford (OpenAI) | Learn image representations from raw text by **contrastive** pre-training: predict **which text as a whole is paired with which image** (not the exact words). At test time the class names are embedded by the text encoder to synthesise a zero-shot linear classifier. | **Zero-shot ImageNet top-1 = 76.2%** (top-5 95%), best model `ViT-L/14@336px`. Table 1: CLIP vs Visual N-Grams — ImageNet **11.5% → 76.2%**, aYahoo 72.4 → **98.4**, SUN 23.0 → **58.5**. | ImageNet (zero-shot; **no** ImageNet training examples used) | [PMLR v139](https://proceedings.mlr.press/v139/radford21a/radford21a.pdf), [arXiv:2103.00020](https://arxiv.org/abs/2103.00020) |
| **ViT** | arXiv Oct 2020; **ICLR 2021** | Alexey Dosovitskiy (Google Research, Brain Team) | Split an image into fixed-size **patches** (16×16), linearly embed them + position embeddings, and feed the sequence to a **standard Transformer encoder — no convolutions at all**. Works only when pre-trained at scale (ImageNet-21k / JFT-300M) then fine-tuned. | **ViT-H/14 (JFT-300M): ImageNet top-1 = 88.55%**, ImageNet-ReaL 90.72%, CIFAR-100 94.55%, VTAB (19 tasks) 77.63%. ViT-L/16 (JFT): 87.76%. ViT-L/16 (ImageNet-21k): **85.30%**. | ImageNet (fine-tuned; 518px for ViT-H/14, 512px for ViT-L/16), ImageNet-ReaL, CIFAR-100, VTAB | [arXiv:2010.11929](https://arxiv.org/abs/2010.11929), [OpenReview (ICLR 2021)](https://openreview.net/forum?id=YicbFdNTTy) |

### CLIP — requested details

- **Training data size:** **400 million (image, text) pairs**, collected from publicly available internet sources using a set of **500,000 queries** (base query list = all words occurring ≥100 times in English Wikipedia, augmented with high-PMI bi-grams, Wikipedia article names, and all WordNet synsets; up to 20,000 pairs per query, approximately class-balanced). The dataset is called **WIT (WebImageText)**; the paper says its total word count is similar to GPT-2's WebText. It is **not** released. — [arXiv:2103.00020](https://arxiv.org/abs/2103.00020)
- **Zero-shot ImageNet top-1:** **76.2%** (top-5 95%). The paper frames this as "improves accuracy on ImageNet from a proof of concept 11.5% to 76.2% and matches the performance of the original ResNet-50 despite using none of the 1.28 million crowd-labeled training examples".
- **Compute / architecture:** trained **32 epochs**, batch size **32 768**, mixed precision, gradient checkpointing; **eight** models total — five ResNets (RN50, RN101, RN50x4/×16/×64) and three **ViTs (ViT-B/32, ViT-B/16, ViT-L/14)**. The largest ResNet (RN50x64) took **18 days on 592 V100 GPUs**; the largest Vision Transformer (ViT-L/14) took **12 days on 256 V100 GPUs**. `ViT-L/14` was then pre-trained one extra epoch at **336px** (`ViT-L/14@336px`), which is the model behind the headline results.
- **Why it mattered:** (i) **zero-shot transfer** — no dataset-specific training, natural language specifies the concepts, so no fixed label set; (ii) the **contrastive objective** ("which caption goes with which image") proved a far more efficient proxy task than predicting exact words; (iii) zero-shot CLIP was markedly **more robust to distribution shift** than equally accurate supervised ImageNet models; (iv) it is competitive with fully supervised baselines on many tasks (matches original ResNet-50 on ImageNet). Text verbatim: "the simple pre-training task of predicting which caption goes with which image is an efficient and scalable way to learn SOTA image representations from scratch".

### ViT — requested details

- **What was new:** the paper's own claim is that "this reliance on CNNs is not necessary and a **pure transformer applied directly to sequences of image patches** can perform very well on image classification tasks." Earlier vision-attention work either combined attention with CNNs or replaced components while keeping the CNN structure; ViT keeps no convolutional structure.
- **ImageNet numbers:** ViT-H/14 pre-trained on **JFT-300M** reaches **88.55%** top-1 on ImageNet (fine-tuned), 90.72% on ImageNet-ReaL, 94.55% on CIFAR-100, 77.63% on VTAB; the smaller **ViT-L/16** reaches 87.76%. With only the public **ImageNet-21k** pre-training, ViT-L/16 reaches **85.30%**. Baselines in the same table: BiT-L (ResNet152x4, JFT) 87.54%; Noisy Student (EfficientNet-L2) 88.4/88.5.
- **Compute:** Table 2 reports pre-training cost in **TPUv3-core-days**: ViT-H/14 (JFT) **2.5k**, ViT-L/16 (JFT) **0.68k**, ViT-L/16 (ImageNet-21k) **0.23k** — versus BiT-L **9.9k** and Noisy Student **12.3k**. The paper notes ViT-L/16 on ImageNet-21k "could be trained using a standard cloud TPUv3 with 8 cores in approximately **30 days**".
- **Scale of data:** ImageNet-21k = 21k classes / 14M images; **JFT-300M = 18k classes / 303M high-resolution images** (in-house, not public).
- **Why it mattered:** it demonstrated that large-scale pre-training, not convolution, is what drives image-recognition performance — ViT "attains excellent results compared to state-of-the-art convolutional networks while requiring substantially fewer computational resources to train" once pre-trained at scale. The paper is explicit that **on ImageNet alone ViT underperforms comparable ResNets** (Figure 4 / Table 5): scale is the enabling factor.

### CLIP ↔ ViT relationship (confirmed)

CLIP used **two** image-encoder families. Verbatim: "For the second architecture, we experiment with the recently introduced **Vision Transformer (ViT)** (Dosovitskiy et al. 2020). We closely follow their implementation with only the minor modification of adding an additional layer normalization to the combined patch and position embeddings…". CLIP's largest ViT (**ViT-L/14**) is the backbone of the best CLIP model, and CLIP "vision transformers are about 3x more compute efficient than CLIP ResNets". ViT is cited by CLIP as arXiv 2010.11929 (the ICLR 2021 camera-ready version).

---

## SPECIAL VERIFICATION: Stable Diffusion training compute

### Verdict

> **The "~150,000 GPU-hours / 256 A100s" figure is NOT in the LDM paper.** It is the officially published compute for the **released Stable Diffusion v1.x checkpoints**, documented in the Stability/CompVis/runwayml **Hugging Face model cards**. The lecturer should attribute it to the release, not to Rombach et al.

### 1. What the LDM paper (Rombach et al.) actually says

Venue: arXiv Dec 2021 (**arXiv:2112.10752**), published at **CVPR 2022**. Both the arXiv and CVPR PDF texts were checked.

- **The only "150" in the paper is about *prior* work, not LDM.** Exact quote:
  > "As an example, training the most powerful DMs often takes hundreds of GPU days (e.g. **150 - 1000 V100 days** in [15]) and repeated evaluations on a noisy version of the input space render also inference expensive, so that producing 50k samples takes approximately 5 days [15] on a single A100 GPU."
  Reference [15] is Dhariwal & Nichol's **ADM** ("Diffusion Models Beat GANs on Image Synthesis"). So "150–1000 V100 days" characterises **ADM-scale prior diffusion models**.
- **LDM's own training setup is a single A100**, not 256. Exact quotes:
  > Sec. 4.1: "To obtain a comparable test-field, we **fix the computational resources to a single NVIDIA A100** for all experiments in this section and train all models for the same number of steps and with the same number of parameters."
  > Appendix (Table 18 discussion): "As they report their used compute in V100 days and **we train all our models on a single NVIDIA A100 GPU**, we convert the A100 days to V100 days by assuming a **×2.2 speedup** of A100 vs V100."
- **Where the paper does give a compute comparison:** **Table 18** ("Comparing compute requirements during training and inference throughput with state-of-the-art generative models. **Compute during training in V100-days**"). Key rows for **class-conditional ImageNet 256²**:
  | Model | Generator compute (V100-days) | FID |
  |---|---|---|
  | ADM (250 steps) | 916 | 10.94 |
  | ADM-G (250 steps) | 916 | 4.59 |
  | **LDM-4 (250 DDIM steps, 178K, bs 1200)** | **271** | 10.56 |
  | **LDM-4-G (…, cfg 1.5)** | **271** | **3.60** |
  So the paper's headline compute claim is **271 V100-days vs 916 V100-days for ADM** on ImageNet-256² generator training — **not** 150,000 anything. (At the paper's own ×2.2 factor, 271 V100-days ≈ 123.2 A100-days ≈ **≈ 2,956 A100-hours** — this is my arithmetic from the paper's own stated conversion factor, not a number stated in the paper. Note this is 2 orders of magnitude below the "150,000 hours" claim.)
- **Training data / model in the paper:** the text-conditional model is a **1.45B-parameter** KL-regularised LDM trained on **LAION-400M**. Quote: "For text-to-image image modeling, we train a **1.45B parameter KL-regularized LDM** conditioned on language prompts on **LAION-400M**."

### 2. What the released Stable Diffusion v1.x actually says (the source of the claim)

**SD v1.5 model card** — canonical URL `https://huggingface.co/stable-diffusion-v1-5/stable-diffusion-v1-5` (also mirrored at the older `runwayml/stable-diffusion-v1-5`). Under **"## Environmental Impact" → "**Stable Diffusion v1** **Estimated Emissions**"**, verbatim:

> "Based on that information, we estimate the following CO2 emissions using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in Lacoste et al. (2019)."
> - **Hardware Type:** A100 PCIe 40GB
> - **Hours used:** 150000
> - **Cloud Provider:** AWS
> - **Compute Region:** US-east
> - **Carbon Emitted (Power consumption x Time x Carbon produced based on location of power grid):** 11250 kg CO2 eq.

And in the same card's training section:
> - **Hardware:** 32 x 8 x A100 GPUs
> - **Optimizer:** AdamW
> - **Gradient Accumulations:** 2
> - **Batch:** 32 x 8 x 2 x 4 = 2048
> - **Learning rate:** warmup to 0.0001 for 10,000 steps and then kept constant

**SD v1.4 model card** — canonical URL `https://huggingface.co/CompVis/stable-diffusion-v1-4` — carries the **identical** emissions block (`Hardware: 32 x 8 x A100 GPUs`, `Hours used: 150000`, `Carbon Emitted: 11250 kg CO2 eq.`).

**So:** `32 × 8 = 256` A100 (PCIe 40GB) GPUs, and **150,000 hours**. The lecturer's "~150,000 GPU-hours / 256 A100s" matches **these model cards**. The primary source URLs are the two Hugging Face model cards above (retrieved through the `hf-mirror.com` mirror because `huggingface.co` was unreachable from this machine — see Retrieval failures).

### 3. Flags — the paper's LDM ≠ the released SD 1.x

1. **Different artifact, different budget.** The paper's LDM models are single-A100 research models; the 150,000-hour figure describes the released SD v1 Lineage. Do not present the two as the same run.
2. **Different dataset.** The paper's text-to-image LDM used **LAION-400M**. The SD v1.x release was "trained on **subsets of LAION-2B(en)**" (specifically `laion-aesthetics v2 5+`; the v1.1/v1.2 lineage also used `laion2B-en`, `laion-high-resolution` (170M examples ≥1024×1024), and `laion-improved-aesthetics`). LAION-5B itself is **5.85B CLIP-filtered image-text pairs** (2.3B English, 2.2B other languages), per the [LAION-5B announcement](https://laion.ai/blog/laion-5b/).
3. **"150,000" is not a from-scratch cost for v1.5.** The v1.5 card states the checkpoint "was initialized with the weights of the **Stable-Diffusion-v1-2** checkpoint and subsequently **fine-tuned on 595k steps** at 512×512"; v1.4 was likewise resumed from v1.2 for **225,000 steps**. The identical `Hours used: 150000` appears in both the v1.4 and v1.5 cards, so it reads as a **project-level ("Stable Diffusion v1") estimate**, not a per-checkpoint measurement. If the lecturer wants to be precise, say "the SD v1 model family is reported at ~150,000 GPU-hours on 256 A100s", not "SD 1.5 was trained for 150,000 hours".
4. **Ambiguity in "Hours used".** The cards do not define whether `Hours used` is per-GPU or total. The card's own carbon figure (11,250 kg CO2e) is consistent only with 150,000 being **total** GPU-hours across the 256 GPUs, not 150,000 wall-clock hours × 256 GPUs (the latter would be ~38M GPU-hours and orders of magnitude more carbon). **I did not find a primary definition of the field**, so treat this as a flagged ambiguity rather than a verified fact.

### 4. Safe phrasing for the lecture

> "The **LDM paper** (Rombach et al., CVPR 2022) trained each model on a **single A100** and compared compute in V100-days — its headline was **271 V100-days vs ADM's 916** on ImageNet-256². The popular *'150,000 GPU-hours on 256 A100s'* figure is not from the paper: it is what the **released Stable Diffusion v1 model cards** report for the SD v1 family (`32 × 8 × A100`, `Hours used: 150000`, `11,250 kg CO2e`), trained on subsets of **LAION-2B(en)** rather than the paper's **LAION-400M**."

---

## COULD NOT VERIFY

1. **Any "150,000 GPU-hours" statement in the LDM paper — confirmed ABSENT.** Both the arXiv v2 text and the CVPR 2022 PDF were searched exhaustively for `GPU`, `A100`, `V100`, `hours`, `150`: the only "150" is "150 - 1000 V100 days", describing **prior work (ADM)**. The paper's compute table uses **V100-days** (LDM-4 ImageNet-256 = 271). This is likely the origin of the confusion.
2. **The original GAN paper's "CIFAR-10 numbers" — there are none.** Goodfellow et al. 2014 report Parzen-window log-likelihood on **MNIST** (225 ± 2) and **TFD** (2057 ± 26) only; CIFAR-10 appears as **qualitative samples only**. There is **no Inception Score and no FID** in that paper (IS originates in Salimans et al., "Improved Techniques for Training GANs", 2016; FID in Heusel et al., 2017). Any slide claiming e.g. "the original GAN got IS x on CIFAR-10" is a misattribution.
3. **DCGAN and pix2pix/CycleGAN have no FID/IS in their original papers** — DCGAN (2015/16) predates both metrics; pix2pix and CycleGAN deliberately use **FCN-score** and **AMT** instead. This is not a gap in my search; it is the state of the papers.
4. **Exact public release dates of SD v1.4 / v1.5 (commonly given as Aug 2022 / Oct 2022).** I could not verify these from a primary source: the model cards do not carry release dates in the sections retrieved, and `huggingface.co` was unreachable. Secondary press exists but is not primary. Treat "2022 release" as the verifiable statement.
5. **StyleGAN2's FID reference split.** The StyleGAN2 main text specifies the snapshot-selection rule and 10-seed averaging, but does **not** explicitly restate that FID uses 50k training-set images (StyleGAN does state this explicitly). It presumably inherits StyleGAN's protocol, but I did not find it restated in the text I extracted — flag if a slide needs the reference split for StyleGAN2 specifically.
6. **The exact wording/semantics of "Hours used" in the ML CO2 Impact calculator** (per-GPU vs total) — the SD model cards link to the calculator but do not define the field; see flag 4 above.
7. **OpenReview's ICLR 2021 PDF for ViT** returned HTTP 403 and the forum page served a browser-verification challenge; ViT's ICLR 2021 venue was instead confirmed from the arXiv v2 comments field ("ICLR camera-ready version") and the paper's own header.
8. **No primary source found for a "GAN CIFAR-10 FID 7.3"-type number** or similar widely repeated GAN CIFAR-10 scores tied to the 2014 paper. If such a number is needed, it must be sourced to a specific later paper, not to Goodfellow et al.

---

## Retrieval failures / workarounds (recorded as requested)

| Target | Failure | Workaround used |
|---|---|---|
| `arxiv.org` (abs + `/pdf/`, incl. `export.arxiv.org`) via direct HTTP client | Connection timeouts, HTTP `000`, repeatedly | Read full text via **ar5iv** (`ar5iv.labs.arxiv.org/html/<id>`), which renders the official arXiv LaTeX source; metadata cross-checked via the `arxiv.org/abs` pages through the fetch tool (which worked) |
| `web_fetch` on arXiv **PDF** URLs | `unsupported content type "application/pdf"`; one `TypeError: fetch failed` | Used ar5iv HTML / official CVF & NeurIPS PDFs instead |
| `huggingface.co` | DNS resolves to `108.160.166.9`; all connections time out; `web_fetch` also failed | Retrieved the same model-card README content from the `hf-mirror.com` mirror of the identical repo paths; canonical HF URLs cited in the text |
| `openreview.net/pdf?id=YicbFdNTTy` | HTTP 403; forum page served a Cloudflare-style "Verifying your browser" page | Venue confirmed from the arXiv v2 comments field |
| `web_search` (DeepSeek endpoint) | One hard failure: `TypeError: fetch failed` on `api.deepseek.com/anthropic/v1/messages` | Retried; subsequent queries succeeded |
| `proceedings.neurips.cc` | First probe timed out (`000`); later probes succeeded | Retried; GAN 2014 and DDPM 2020 PDFs downloaded successfully |
| Guessed CVF filenames for StyleGAN (2019) / pix2pix (2017) / DiT | HTTP 404 (case- and word-order-sensitive paths) | Resolved via search/index: pix2pix = `content_cvpr_2017/html/Isola_Image-To-Image_…`, StyleGAN = `content_CVPR_2019/…` (upper-case), DiT = `content/ICCV2023/…` |

## Local copies of primary sources (for re-checking)

- `research/scratch/cv-facts/src/` — raw HTML (ar5iv renderings) and PDFs
- `research/scratch/cv-facts/txt/` — extracted text of each paper
- `research/scratch/cv-facts/cards/` — SD v1.4 / v1.5 model-card markdown
- `research/scratch/cv-facts/tabs.py` — HTML `<table>` extractor used for exact table values
