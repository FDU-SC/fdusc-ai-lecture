# ImageNet-pretrained vision backbones transferred to medical imaging — verified, sourced facts

Compiled 2026-09-19. Every non-obvious number below is backed by a URL that I actually fetched, except where
explicitly flagged. "Read the table" means I retrieved the paper's rendered full text (arXiv HTML / ar5iv /
PMC) and read the numeric table; "abstract says" means I only have the abstract.

Status legend for the **confidence** column:
- **HIGH** = I read the paper's full text / numeric table from the primary source.
- **MEDIUM** = primary source read, but the number is quoted in prose and the underlying table/figure was not retrievable.
- **LOW** = secondary summary or preprint only, or attribution uncertain.

---

## 1. Table

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | confidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rajpurkar, Irvin, Zhu, Yang, Mehta, Duan, Ding, Bagul, Langlotz, Shpanskaya, Lungren, Ng — *CheXNet: Radiologist-Level Pneumonia Detection on Chest X-Rays with Deep Learning* (arXiv preprint, no peer-reviewed venue found) | 2017 (v1 Nov 14 2017; v3 Dec 25 2017) | DenseNet-121, "initialized with weights from a model pretrained on ImageNet" | fine-tuned end-to-end (Adam, lr 0.001, ImageNet-mean/std normalization) | NIH ChestX-ray14 (112,120 frontal images; train 98,637 / val 6,351 / test 420) | pneumonia AUROC **0.7680**; radiologist comparison F1 **0.435** (95% CI 0.387–0.481) | Wang et al. 2017 AUROC **0.633** and Yao et al. 2017 AUROC **0.713** (Table 2); radiologist average F1 **0.387** (95% CI 0.330–0.442) (Table 1) | https://arxiv.org/abs/1711.05225 · full text https://arxiv.org/html/1711.05225v3 | HIGH (read Tables 1 and 2 in arXiv HTML v3) |
| Wang, Peng, Lu, Lu, Bagheri, Summers — *ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases* (CVPR 2017, DOI 10.1109/CVPR.2017.369) | 2017 | four ImageNet-pretrained backbones: AlexNet, GoogLeNet, VGGNet-16, ResNet-50 ("network surgery" on pre-trained models) | fine-tuned (SGD; train 70 / val 10 / test 20 split) | NIH ChestX-ray8 (108,948 frontal images, 32,717 patients) | pneumonia AUROC by backbone: ResNet-50 **0.6333**, GoogLeNet **0.5990**, AlexNet **0.5493**, VGGNet-16 **0.5100** (Table 3); best overall = ResNet-50, also 0.8141 cardiomegaly, 0.7891 pneumothorax | **No from-scratch baseline is reported in Table 3** — every row is ImageNet-initialized. Do not cite this paper as evidence that pretraining beats scratch. | https://arxiv.org/abs/1705.02315 · full text https://ar5iv.labs.arxiv.org/html/1705.02315 | HIGH for Table 3; caveat noted |
| Raghu, Zhang, Kleinberg, Bengio — *Transfusion: Understanding Transfer Learning for Medical Imaging* (NeurIPS 2019; arXiv 1902.07208) | 2019 | ResNet-50 and Inception-v3 with ImageNet pretrained weights (also a CBR family: CBR-LargeT/W, CBR-Small, CBR-Tiny) | fine-tuned (transfer) vs random init | **Retina** retinal fundus photographs (~250k imgs, referable-DR AUC) and **CheXpert** chest X-ray (~223k imgs, 5 pathologies, AUC) | Retina AUC: ResNet-50 random **96.4%±0.05** vs transfer **96.7%±0.04**; Inception-v3 **96.6%±0.13** vs **96.7%±0.05**; CBR-LargeT **96.2%±0.04** vs **96.2%±0.04** (Table 1). CheXpert AUC: ResNet-50 random vs transfer = atelectasis **79.52 vs 79.76**, cardiomegaly **75.23 vs 74.93**, consolidation **85.49 vs 84.42**, edema **88.34 vs 88.89**, pleural effusion **88.70 vs 88.07** (Table 2). Very-small-data (5,000 Retina pts, Table 3): ResNet50 **92.2% → 94.6%**, CBR-LargeT **93.6% → 93.9%**, CBR-LargeW **93.6% → 93.7%** | from-scratch (random init) training on the same data and architectures | https://arxiv.org/abs/1902.07208 · full text https://ar5iv.labs.arxiv.org/html/1902.07208 | HIGH (read Tables 1, 2, 3) |
| Tajbakhsh, Shin, Gurudu, Hurst, Kendall, Gotway, Liang — *Convolutional Neural Networks for Medical Image Analysis: Full Training or Fine Tuning?* (IEEE TMI 35(5):1299–1312, 2016; DOI 10.1109/TMI.2016.2535302) | 2016 (arXiv v1 2017) | AlexNet (the Caffe ImageNet model, 1.2M images / 1000 classes, snapshot at 360,000 iterations), fine-tuned in a **layer-wise** manner (only fc8 → fc7-fc8 → … → conv1-fc8) | fine-tuned (layer-wise), compared against AlexNet trained fully from scratch | 4 applications / 3 modalities: polyp detection in colonoscopy video, colonoscopy frame quality, pulmonary embolism detection in CT, carotid intima-media segmentation in ultrasound | **Qualitative but explicit conclusion:** "(1) the use of a pre-trained CNN with adequate fine-tuning outperformed or, in the worst case, performed as well as a CNN trained from scratch; (2) fine-tuned CNNs were more robust to the size of training sets than CNNs trained from scratch; (3) neither shallow tuning nor deep tuning was the optimal choice". Concrete data-size finding: at 25% of training data "the fully trained CNN showed dramatic performance degradation, but the deeply fine-tuned CNN still exhibited relatively high performance" | from-scratch AlexNet on the same medical data; also a handcrafted approach (for polyps and PE) | https://arxiv.org/abs/1706.00712 · full text https://ar5iv.labs.arxiv.org/html/1706.00712 · DOI https://doi.org/10.1109/TMI.2016.2535302 | HIGH for the conclusion (verbatim abstract); **LOW for point numbers** — the paper's quantitative results are FROC/ROC curves (Figs. 2, 4) and supplementary tables, not a single headline number |
| Shin, Roth, Gao, Lu, Xu, Nogues, Yao, Mollura, Summers — *Deep Convolutional Neural Networks for Computer-Aided Detection: CNN Architectures, Dataset Characteristics and Transfer Learning* (IEEE TMI 35(5):1285–1298, 2016; DOI 10.1109/TMI.2016.2528162) | 2016 | AlexNet and GoogLeNet pre-trained on ImageNet (1.2M images / 1000 classes), 2.5D CT views encoded as RGB | three arms compared: **from scratch (RI)**, **fine-tuned (TL)**, and **off-the-shelf frozen features (ImNet)** — TL = all layers except the last fine-tuned at 1/10 LR, last FC re-initialized | thoraco-abdominal **lymph node (LN) detection** in CT (388 mediastinal LNs / 90 patients; 595 abdominal LNs / 86 patients) and **interstitial lung disease (ILD)** slice classification (905 slices, 120 patients, 6 classes) | mediastinal LN detection: **86% sensitivity at 3 FP/patient** vs prior state of the art **78%** (stacked shallow learning) and **70%** (CNN); abstract: "CNNs trained from scratch or fine-tuned from ImageNet models consistently outperform CNNs that merely use off-the-shelf CNN features"; "Fine-tuning ImageNet-trained models for ILD classification is clearly advantageous … when the amount of labeled training data is highly insufficient and multi-class categorization is used" | prior SOTA 78% (stacked shallow) and 70% (CNN) for mediastinal LN; prior best abdominal LN 83% recall at 3 FP (Roth et al.); RI and off-the-shelf arms are internal baselines | https://pmc.ncbi.nlm.nih.gov/articles/PMC4890616/ · DOI https://doi.org/10.1109/TMI.2016.2528162 | HIGH for the quoted sentences; **attribution caveat**: the abstract attributes 86% to the paper overall — Section IV (which exact configuration produced it) was not retrievable |
| Stawiaski — *A Pretrained DenseNet Encoder for Brain Tumor Segmentation* (arXiv 1811.07542; BraTS 2018 challenge entry, team "Stryker") | 2018 | DenseNet-121 encoder pretrained on ImageNet; "an extreme case of transfer learning where we fix the weights of the pretrained DenseNet encoder" — only the precoder + decoder are learned | **FROZEN encoder** (pretrained DenseNet-121 weights stay fixed) | BraTS 2018 (285 training patients: 210 HGG / 75 LGG; 66 validation; 191 test) | BraTS 2018 validation Dice (M2 = fixed pretrained encoder): ET **0.792**, WT **0.899**, TC **0.847**; M1 variant: ET **0.768**, WT **0.892**, TC **0.815**. Testing set (M2): ET **0.776**, WT **0.878**, TC **0.786** | **None — the paper reports no from-scratch / randomly-initialized baseline.** It only claims the frozen ImageNet encoder is "competitive" on the BraTS leaderboard | https://arxiv.org/abs/1811.07542 · full text https://ar5iv.labs.arxiv.org/html/1811.07542 | HIGH for the numbers (read Tables 1–2); **no transfer-vs-scratch delta available** |
| Esteva, Kuprel, Novoa, Ko, Swetter, Blau, Thrun — *Dermatologist-level classification of skin cancer with deep neural networks* (Nature 542(7639):115–118, 2017; DOI 10.1038/nature21056) | 2017 | "GoogleNet Inception v3 CNN architecture that was pretrained on approximately 1.28 million images (1,000 object categories) from the 2014 ImageNet Large Scale Visual Recognition Challenge" (stated as 93.33% top-5); final classification layer removed | **fine-tuned — all layers**: "retrain it with our dataset, fine-tuning the parameters across all layers"; described by the authors as transfer learning | proprietary + public skin lesion images: 129,450 clinical images, 757 training classes, 2,032-disease taxonomy; 1,942 biopsy-labelled test images | 3-class validation accuracy **72.1 ± 0.9%** vs two dermatologists **65.56%** and **66.0%**; 9-class validation accuracy **55.4 ± 1.7%** vs **53.3%** and **55.0%**; biopsy-proven malignant-vs-benign: "The area under the curve (AUC) for each case is over 91%" (exact per-task AUC values are only in Fig. 3) | 21+ board-certified dermatologists (n = 25 / 22 / 21 per task); **no from-scratch CNN baseline** | https://pmc.ncbi.nlm.nih.gov/articles/PMC8382232/ (author manuscript) · DOI https://doi.org/10.1038/nature21056 | HIGH for pretraining description and 72.1/55.4 numbers; **MEDIUM for the AUC** — only ">91%" in text, numeric AUCs in a figure |
| *(extra, weakest row)* Matas, Serrano, Nogales, Moreno, Ferrándiz, Ojeda, Acha — *Mitigating Overfitting in Medical Imaging: Self-Supervised Pretraining vs. ImageNet Transfer Learning for Dermatological Diagnosis* (**arXiv preprint 2505.16773, not peer-reviewed as far as I could verify**) | 2025 | ConvNeXt-Tiny with ImageNet pretrained weights; **frozen feature extractor** + identical 2-layer classifier — compared against a ConvNeXt-Tiny VAE trained from scratch (self-supervised) on dermatology data | **frozen** (both backbones frozen; only the classifier trained) | proprietary teledermatology dataset (Hospital Universitario Virgen Macarena, ~200k images, dermatoscopic subset) merged with ISIC classes; 3-class priority triage | ImageNet-pretrained: train acc **87%** (+50.00%) but validation acc **75%** (+19.05%), overfitting gap **+0.060**; self-supervised from-scratch: train 65%, validation 65%, gap ≈ 0.000 | self-supervised VAE encoder trained from scratch (random init) — a from-scratch baseline | https://arxiv.org/abs/2505.16773 · full text https://ar5iv.labs.arxiv.org/html/2505.16773 | LOW–MEDIUM (preprint; small evaluation; author-reported) |

---

## 2. Prose notes per result

### 2.1 CheXNet (Rajpurkar et al. 2017) — the canonical "ImageNet DenseNet fine-tuned on chest X-ray" result
- Exact pretraining sentence: "The weights of the network are initialized with weights from a model pretrained on ImageNet" (Sec. 2.2). Model = 121-layer DenseNet; fine-tuned end-to-end, Adam, minibatch 16, initial LR 0.001 decayed by 10 on plateau; images downscaled to 224×224 and **normalized with ImageNet training-set mean/std**, plus random horizontal flips.
- The 14-pathology AUROC table (Table 2) is the most quoted: pneumonia **0.7680**, mass 0.8676, nodule 0.7802, emphysema 0.9371, cardiomegaly 0.9248, atelectasis 0.8094. CheXNet beats both comparison columns on all 14 classes.
- Human comparison (Table 1): only **four** radiologists, on **420** images, using F1 against the other radiologists' labels; CheXNet F1 = 0.435 vs radiologist average 0.387, difference 0.051 (95% CI 0.005–0.084).
- **Caveats worth stating on a slide:** (a) it is an arXiv preprint (v3, Dec 2017), not a peer-reviewed paper as far as I can find; (b) the "exceeds radiologists" claim rests on F1 computed against other radiologists as pseudo-ground-truth, a different metric from the AUROC used versus other algorithms; (c) the 0.768**1** value often quoted is not in the paper — the table says **0.7680**.

### 2.2 Wang et al. 2017 (ChestX-ray8) — the dataset/benchmark paper
- The benchmark deliberately compares four ImageNet-pretrained backbones after "network surgery" (drop the FC/classification layers, insert transition + global pooling + prediction + loss), i.e. all four are fine-tuned from ImageNet. Pneumonia AUROC: ResNet-50 0.6333 > GoogLeNet 0.5990 > AlexNet 0.5493 > VGGNet-16 0.5100.
- This is the source of the "0.633" pneumonia baseline that CheXNet beats.
- **Do not over-claim:** the paper contains no from-scratch training arm, so it cannot support "ImageNet pretraining beat scratch on ChestX-ray14". It does, however, explicitly state the *opposite of "pretraining is the norm"* — see §3.

### 2.3 Raghu et al. 2019 (Transfusion) — the important negative result
- Setup: ResNet-50 and Inception-v3 with ImageNet weights (fine-tuned) vs the same architectures from random init; plus the small "CBR" family. Two large datasets: Retina (~250k fundus images) and CheXpert (~223k chest X-rays).
- Headline: on Retina, transfer gained ≤0.3 AUC points (96.4→96.7 for ResNet-50) and **nothing** for the small CBR models; on CheXpert the effect was **mixed** — transfer *helped* edema (88.34→88.89) and pleural effusion (88.70→88.07, i.e. hurt on the max of 3 seeds) but *hurt* atelectasis (79.52→79.76), cardiomegaly and consolidation depending on seed spread. The paper's wording: "transfer learning does not help significantly" and "For Atelectasis, Cardiomegaly and Consolidation, transfer learning performs slightly worse, but helps with Edema and Pleural Effusion."
- Small-data regime (5,000 Retina examples, Table 3) is the *only* place transfer clearly helps: ResNet50 92.2% → 94.6%, while CBR-LargeT 93.6% → 93.9%. Their interpretation: the gain is a **model-size / over-parameterization effect**, not sophisticated feature reuse; meaningful feature reuse is confined to the lowest 1–2 layers, and a large part of the benefit is just weight *scaling* (their "Mean Var Init" control).
- So the correct nuance is: **transfer helped most on small datasets and for large over-parameterized models; on large medical datasets the benefit was within noise.**

### 2.4 Tajbakhsh et al. 2016/2017 — the systematic transfer-vs-scratch study
- Design: 4 medical applications in 3 specialties (radiology, cardiology, gastroenterology) covering classification, detection and segmentation, with AlexNet ImageNet weights fine-tuned in a **layer-wise** schedule, versus the same AlexNet trained from scratch and versus handcrafted CAD systems.
- Verified conclusion (verbatim from the abstract, reproduced identically in IEEE TMI and arXiv): pre-trained + adequate fine-tuning **"outperformed or, in the worst case, performed as well as"** from-scratch; fine-tuned nets were **more robust to training-set size**; the best tuning depth was application-dependent.
- The strongest concrete illustration in the text: when training data were cut to 25%, the from-scratch CNN degraded dramatically while the deeply fine-tuned CNN stayed strong (polyp detection, Fig. 2b). I could not read a single numeric FROC value from the primary source because the results are plotted as curves.

### 2.5 Shin et al. 2016 — the earliest of the three TMI studies, with a useful timestamp
- The paper compares **three** regimes explicitly: CNN from scratch (RI), off-the-shelf ImageNet features (ImNet), and ImageNet fine-tuning (TL). TL = all layers except the last at 1/10 learning rate, last FC randomly re-initialized and trained at 0.01.
- Headline verified numbers: mediastinal LN detection **86% sensitivity @ 3 FP/patient**, versus prior state of the art 78% (stacked shallow learning) and 70% (CNN). Prior abdominal LN best was 83% recall @ 3 FP.
- Verified qualitative findings: from-scratch and ImageNet-fine-tuned CNNs **both** beat purely off-the-shelf fixed features; fine-tuning is "clearly advantageous" specifically when labelled data are very scarce and the task is multi-class (ILD).
- **Uncertainty I am flagging:** I could not read Section IV's result tables, so I cannot say whether the 86% came from AlexNet-TL, GoogLeNet-TL, or the combined model. Do not attribute it to a specific architecture without checking.

### 2.6 BraTS / brain tumor segmentation (Stawiaski 2018)
- This is the cleanest "ImageNet-pretrained encoder → 3D MRI segmentation" example I could verify, and it is an **extreme** form: the pretrained DenseNet-121 encoder is **frozen** and only the decoder (plus a 3D "precoder") is trained — the authors explicitly call it "an extreme case of transfer learning where we fix the weights of the pretrained DenseNet encoder".
- BraTS 2018 validation Dice with the fixed pretrained encoder (M2): ET 0.792, WT 0.899, TC 0.847 (test set: 0.776 / 0.878 / 0.786). The paper argues frozen ImageNet features are "an interesting alternative to a relative small task specific 3D neural network".
- **Critical caveat:** there is **no from-scratch baseline** in this paper, so it cannot quantify the transfer gain. It also does not use standard 3D encoders (it feeds 2D slices along three anatomical orientations).

### 2.7 Esteva et al. 2017 (Nature) — dermatology
- Verified verbatim: "We utilize a GoogleNet Inception v3 CNN architecture that was pretrained on approximately 1.28 million images (1,000 object categories) from the 2014 ImageNet Large Scale Visual Recognition Challenge, and train it on our dataset using transfer learning." Methods: "We use Google's Inception v3 CNN architecture pretrained to 93.33% top-five accuracy on the 1,000 object classes (1.28 million images) of the 2014 ImageNet Challenge… We then remove the final classification layer from the network and retrain it with our dataset, **fine-tuning the parameters across all layers**."
- Verified numbers: 129,450 clinical images / 2,032 diseases / 757 training classes; 3-class validation overall accuracy **72.1 ± 0.9%** vs dermatologists 65.56% and 66.0%; 9-class **55.4 ± 1.7%** vs 53.3% and 55.0%; biopsy-proven binary tasks compared against ≥21 board-certified dermatologists with "AUC for each case is over 91%".
- **Caveats:** (a) the exact per-task AUCs (epidermal, melanocytic, dermoscopic) are in Fig. 3, not in the text — so any slide quoting e.g. "0.96 AUC" is quoting the figure or a secondary source; (b) this is **not** an ISIC 2018 result (ISIC 2018 came later); (c) a formal correction was published: Nature 2017 Jun 28;546(7660):686; (d) there is no from-scratch baseline.

### 2.8 On ISIC 2018 specifically
The ISIC 2018 challenge paper (Codella et al., arXiv 1902.03368) is the largest skin-image benchmark, but it **deliberately does not record pretraining strategy**: "Use of out-of-domain data (non-dermoscopic), such as ImageNet, was expected to be mentioned in manuscripts, but not required to be disclosed in a separate meta-data field." Its results (best balanced accuracy 0.885; per-class melanoma AUC 0.949 for the top submission, from Supplementary Table 2) therefore **cannot be attributed** to ImageNet transfer. I list it in COULD NOT VERIFY rather than in the table.

---

## 3. When did ImageNet transfer become the DEFAULT assumption? (dated, quoted evidence)

I could not verify a Litjens quotation (see COULD NOT VERIFY), but I found a clean dated arc across four primary sources:

1. **Feb 2016 — not yet standard (Shin et al., IEEE TMI).** Verbatim: *"Recently, ImageNet pre-trained CNNs have been used for chest pathology identification and detection in X-ray and CT modalities. They have yielded the best performance results by integrating low-level image features (e.g., GIST, bag of visual words (BoVW) and bag-of-frequency). However, **the fine-tuning of an ImageNet pre-trained CNN model on medical image datasets has not yet been exploited.**"*
   URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC4890616/
2. **Jul 2017 — still not standard in medical diagnosis (Wang et al., CVPR 2017).** Verbatim: *"So far, all image captioning and VQA techniques in computer vision strongly depend on the ImageNet pre-trained deep CNN models which already perform very well in a large number of object classes and serves a good baseline for further model fine-tuning. **However, this situation does not apply to the medical image diagnosis domain.**"*
   URL: https://ar5iv.labs.arxiv.org/html/1705.02315
3. **2019 — now called the de-facto standard (Raghu et al., NeurIPS 2019).** Abstract, verbatim: *"Transfer learning from natural image datasets, particularly ImageNet, using standard large models and corresponding pretrained weights **has become a de-facto method** for deep learning applications to medical imaging."* Introduction, verbatim: *"transfer learning has become integral to many applications — especially in medical imaging, where **the present standard** is to take an existing architecture designed for natural image datasets such as ImageNet, together with corresponding pretrained weights (e.g. ResNet, Inception), and then fine-tune the model on the medical imaging data. This basic formula has seen almost universal adoption across many different medical specialties."*
   URL: https://ar5iv.labs.arxiv.org/html/1902.07208
4. **2021 — "standard practice / the norm" (Peng et al., arXiv 2106.05152).** v1 abstract, verbatim: *"Transfer learning (TL) from pretrained deep models is **a standard practice** in modern medical image classification (MIC)."* v2 (published form of the same preprint), verbatim: *"Transfer learning (TL) has become **the norm** for medical image classification (MIC) and segmentation using deep learning… they are often adopted and fine-tuned as backbone models for the target tasks."*
   URLs: https://ar5iv.labs.arxiv.org/html/2106.05152 (v1) · https://arxiv.org/html/2106.05152v2 (v2)

**Summary of the arc:** the *method* (ImageNet fine-tuning) was pioneered in medical imaging in 2015–2016; as of early 2016 Shin et al. could still write that it "has not yet been exploited"; by 2019 Raghu et al. called it "a de-facto method" and "the present standard"; by 2021 it was "the norm". The 2016–2017 TMI studies by Shin et al. and Tajbakhsh et al. are the papers usually credited with establishing it.

---

## 4. COULD NOT VERIFY

1. **Litjens et al. 2017 exact quotation that "ImageNet pretraining is standard practice" — NOT CONFIRMED.** I retrieved both the arXiv PDF-rendered HTML (v1/v2, https://arxiv.org/html/1702.05747 and https://ar5iv.labs.arxiv.org/html/1702.05747) and the abstract, but the fetch tool truncates long pages at a fixed length, and the relevant material is in Section 5 "Discussion" (pp. 23–26) / Section 3.1.1 (p. 8), which I could not reach. The abstract and introduction that I *did* read contain no such claim. ScienceDirect/DOI access was blocked. A secondary reading-guide page (spatialread.com) summarises "Pre-trained Models: Understand the two main transfer learning strategies… This is a common starting point for new projects", but that is a **BLOG/secondary summary, not peer-reviewed**, and I do not treat it as a quotation. **Recommendation: do not put a Litjens quote on a slide without re-checking the PDF.**
2. **CheXNet's peer-reviewed status.** I found only the arXiv record (v1 Nov 2017, v3 Dec 2017); I found no CVPR/MICCAI/ISBI publication. Treat as a preprint.
3. **"CheXNet pneumonia AUROC 0.7681" (widely repeated) — could not confirm; the primary table says 0.7680.** See https://arxiv.org/html/1711.05225v3, Table 2.
4. **Wang et al. 2017 transfer-vs-scratch:** the paper has no from-scratch arm; the commonly implied comparison does not exist there.
5. **Shin et al. 2016 attribution of the 86%@3FP figure to a named model configuration.** The PMC article page is truncated before Section IV's tables, and the per-table PMC URLs (e.g. /table/T4/, /table/T6/) returned an NCBI reCAPTCHA interstitial on 2 attempts. Only the aggregate claim is verified.
6. **ISIC 2018 → ImageNet transfer attribution.** Codella et al. 2019 explicitly did not record out-of-domain (e.g. ImageNet) pretraining, so the top balanced accuracy 0.885 and melanoma AUC 0.949 cannot be labelled as ImageNet-transfer results. I also could not verify a dedicated ISIC 2018 "ImageNet vs from-scratch" comparison from a primary source.
7. **BraTS transfer-vs-scratch delta.** Stawiaski 2018 reports no randomly-initialized baseline. I did not find a peer-reviewed BraTS paper that isolates the ImageNet-pretrained-encoder effect with a matched from-scratch control.
8. **Esteva et al. exact per-task AUC values.** Only "over 91%" appears in the text; the values are plotted in Fig. 3. Do not quote a specific AUC for this paper without reading the figure.
9. **BLOG POST, not peer-reviewed** (seen but not used as evidence): "Understanding Transfer Learning for Medical Imaging", Google Research blog, https://research.google/blog/understanding-transfer-learning-for-medical-imaging/ — companion post for the Transfusion paper. I did not fetch it; all Transfusion numbers above come from the paper itself.
10. **The one 2025 dermatology row is an arXiv preprint** (2505.16773); I could not verify a peer-reviewed venue, and its comparison is a frozen-feature 3-class triage task. Use only with the "preprint" label.

### Tool / access failures encountered (for the record)
- `web_fetch` on **arxiv.org failed with `TypeError: fetch failed` on ~8 consecutive attempts** across abs, html, and pdf URLs early in the session, then succeeded later — the failures were intermittent, not permanent.
- Permanently unreachable / blocked during this session: nature.com, ieeexplore.ieee.org, pubmed.ncbi.nlm.nih.gov, api.crossref.org, api.semanticscholar.org, link.springer.com, openreview.net, zenodo.org, huggingface.co (cross-origin redirect), r.jina.ai, www.sciencestack.ai (DNS EAI_AGAIN). en.wikipedia.org and www.google.com resolved to **non-public IP addresses** (blocked).
- europepmc.org returned HTTP 403 (Cloudflare) and academic.oup.com returned HTTP 403.
- pmc.ncbi.nlm.nih.gov **worked** for full-text articles (PMC4890616, PMC8382232) but PMC per-table URLs hit a reCAPTCHA page.
- `web_fetch` cannot read PDFs (`unsupported content type "application/pdf"`), and it truncates long HTML pages, which is why several later sections/tables (Litjens §5, Shin §IV, Tajbakhsh supplementary) were unreachable.
- `web_search` worked throughout but returned mostly title+URL lists rather than snippet text, so it was used for discovery, not as a source of numbers.

---

## 5. URLs actually fetched and used

Primary sources (paper full text / abstract pages):
- https://arxiv.org/abs/1711.05225 — CheXNet abstract page
- https://arxiv.org/html/1711.05225v3 — CheXNet full text (Tables 1, 2)
- https://arxiv.org/abs/1705.02315 — ChestX-ray8 abstract page
- https://ar5iv.labs.arxiv.org/html/1705.02315 — ChestX-ray8 full text (Table 3, intro quotation)
- https://arxiv.org/abs/1902.07208 (via https://www.alphaxiv.org/abs/1902.07208 mirror) — Transfusion abstract
- https://ar5iv.labs.arxiv.org/html/1902.07208 — Transfusion full text (Tables 1, 2, 3; intro quotation)
- https://proceedings.neurips.cc/paper/2019/file/eb1e78328c46506b46a4ac4a1e378b91-Paper.pdf — NeurIPS camera-ready URL for Transfusion (link only; PDF not fetchable by the tool)
- https://arxiv.org/abs/1706.00712 — Tajbakhsh abstract page
- https://ar5iv.labs.arxiv.org/html/1706.00712 — Tajbakhsh full text (abstract conclusion, Table I, §VI-A)
- https://api.openalex.org/works/doi:10.1109/TMI.2016.2535302 — Tajbakhsh metadata (venue, volume 35(5):1299–1312, date 2016-03-07)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4890616/ — Shin et al. 2016 full text (abstract, intro, §III-C)
- https://api.openalex.org/works/doi:10.1109/TMI.2016.2528162 — Shin et al. metadata + OA location
- https://arxiv.org/abs/1811.07542 — BraTS DenseNet encoder abstract page
- https://ar5iv.labs.arxiv.org/html/1811.07542 — BraTS DenseNet encoder full text (Tables 1, 2)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8382232/ — Esteva et al. 2017 author manuscript full text
- https://api.openalex.org/works/doi:10.1038/nature21056 — Esteva metadata + OA location (PMC8382232)
- https://arxiv.org/abs/1702.05747 — Litjens survey abstract page
- https://arxiv.org/html/1702.05747 and https://ar5iv.labs.arxiv.org/html/1702.05747 — Litjens survey full text (intro only; Discussion unreachable)
- https://api.openalex.org/works/doi:10.1016/j.media.2017.07.005 — Litjens metadata
- https://ar5iv.labs.arxiv.org/html/2106.05152 (v1) and https://arxiv.org/html/2106.05152v2 — "Rethinking Transfer Learning for Medical Image Classification" abstracts + full text (standard-practice quotations, BIMCV table)
- https://arxiv.org/abs/1902.03368 and https://arxiv.org/html/1902.03368v2 — ISIC 2018 challenge (Supplementary Tables 1–2; disclosure caveat)
- https://ar5iv.labs.arxiv.org/html/2505.16773 — dermatology self-supervised vs ImageNet preprint (Table II)

Supporting / metadata / context:
- https://www.alphaxiv.org/abs/1711.05225 — CheXNet mirror (used before arxiv.org became reachable)
- https://www.alphaxiv.org/abs/1706.00712 — Tajbakhsh mirror
- https://www.alphaxiv.org/abs/1705.02315 — ChestX-ray8 mirror
- https://www.alphaxiv.org/abs/1902.07208 — Transfusion mirror
- https://europepmc.org/article/MED/26978662 — returned HTTP 403 (no content)
- https://example.com — connectivity probe (HTTP 200)

Failed and NOT used as sources: nature.com, ieeexplore.ieee.org, pubmed.ncbi.nlm.nih.gov, api.crossref.org,
api.semanticscholar.org, link.springer.com, openreview.net, zenodo.org, huggingface.co, r.jina.ai,
www.sciencestack.ai, en.wikipedia.org, www.google.com, academic.oup.com, pmc.ncbi.nlm.nih.gov/articles/PMC4890616/table/T4/,
pmc.ncbi.nlm.nih.gov/articles/PMC4890616/table/T6/.
