# ImageNet-pretrained vision backbones transferred to satellite / remote sensing

Compiled 2026-09-19. Scope: concrete, dated, published results on transferring ImageNet-pretrained
vision backbones to remote-sensing (RS) / satellite scene-classification targets.

**Access constraints that shaped this file (important for judging confidence).** The egress network of
this session is heavily restricted (China-based IP; `arxiv.org`, `github.com`, `en.wikipedia.org`,
`openaccess.thecvf.com`, `huggingface.co`, `ieeexplore.ieee.org`, `web.archive.org` were all
unreachable, and the fetch tool refuses `application/pdf` outright). Working routes that WERE found and
used: `api.openalex.org` (returns full abstracts verbatim as inverted indexes), `api.crossref.org`,
`api.semanticscholar.org`, `ar5iv.labs.arxiv.org` (intermittent), `isprs-archives.copernicus.org`
(serves JATS XML front matter), and `hf-mirror.com` (a Chinese mirror of HuggingFace that serves
`/papers/<arxiv-id>.md` and the `huggingchat/papers-content` bucket of arXiv full text as markdown).
Every number below is labelled with how it was obtained: **abstract** (read verbatim from a metadata
API) vs **table** (read the actual results table in the full text).

---

## 1. Results table

Confidence codes: **A** = number read verbatim from the results table of the full text, primary source;
**B** = number read verbatim from the paper's own abstract, primary source at abstract level;
**C** = number read from a *different* peer-reviewed paper that explicitly attributes it to the cited
paper (secondary reproduction); **D** = not verified at primary level.

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | conf |
|---|---|---|---|---|---|---|---|---|
| Marmanis, Datcu, Esch, Stilla — "Deep Learning Earth Observation Classification Using ImageNet Pretrained Networks", IEEE GRSL 13(1):105–109 | 2016 (online 2015-12) | An ImageNet-challenge-pretrained CNN used to extract an initial representation, transferred into a supervised CNN classifier + a feature-fusion step (two-stage). *The specific backbone is NOT named in the abstract* | Not frozen — representations are transferred into a supervised CNN classifier trained with class labels (the abstract calls it "end-to-end") | UC Merced Land Use | **OA improved from 83.1% up to 92.4%** (their own prior-best baseline → their method) | "previously best stated results" = 83.1% OA (as stated in the abstract; the exact protocol behind 83.1% is not given in the abstract) | https://doi.org/10.1109/LGRS.2015.2499239 | B |
| Penatti, Nogueira, dos Santos — "Do deep features generalize from everyday objects to remote sensing and aerial scenes domains?", IEEE CVPRW 2015 (EARTHVISION), pp. 44–51 | 2015 | CaffeNet (Caffe, ImageNet/AlexNet-lineage) and OverFeat, used as **off-the-shelf feature extractors** + SVM | **Frozen / off-the-shelf** (no fine-tuning) | UC Merced Land Use; Brazilian Coffee Scenes | Abstract (verbatim): ConvNets "obtained the best results for **aerial** images, while for **remote sensing**, they performed well but were **outperformed by low-level color descriptors, such as BIC**"; fusing multiple ConvNets "obtains state-of-the-art results for … UCMerced". Numbers (secondary, see §2.2): UC Merced **93.42%** (pre-trained CaffeNet + SVM); Coffee Scenes **84.8%** (CaffeNet+SVM) and **81.2%** (OverFeat+SVM) vs **BIC 87.0%** and **BoVW 80.5%** | Classical: BIC color descriptor 87.0%, BoVW (dense SIFT) 80.5% on Coffee Scenes; VLAT 94.30% on UC Merced | https://doi.org/10.1109/CVPRW.2015.7301382 | B (abstract) / C (numbers) |
| Castelluccio, Poggi, Sansone, Verdoliva — "Land Use Classification in Remote Sensing Images by Convolutional Neural Networks", arXiv:1508.00092 | 2015 | **CaffeNet and GoogLeNet pretrained on ImageNet-1k (ILSVRC)**; three modalities compared: from scratch, fine-tuning, and penultimate-layer feature vector | **Both**: fine-tuning (20,000 iters) and off-the-shelf feature-vector + softmax | UC Merced Land Use; Brazilian Coffee Scenes | UC Merced: **GoogLeNet fine-tuned 97.10%**, **CaffeNet fine-tuned 95.48%**; text: "about 10% and 5% better, respectively, than the design from scratch"; at 5,000 iters 95.12% / 96.48%. Coffee Scenes: **CaffeNet fine-tuned 90.94%**, CaffeNet from scratch 90.17%, **GoogLeNet from scratch 91.83% (best)**, GoogLeNet fine-tuned 90.75%; feature-vector 85.02% / 84.02% | UC Merced best classical reference **VLAT 94.30%** (Fisher/tensor encodings of HOG+RGB); CaffeNet **off-the-shelf + SVM 93.42%** (this is Penatti et al.'s result); Coffee Scenes best classical **BIC 87.0%**, **BoVW 80.5%**, off-the-shelf CaffeNet+SVM 84.8%, OverFeat+SVM 81.2% | https://arxiv.org/abs/1508.00092 | A |
| Nogueira, Penatti, dos Santos — "Towards better exploiting convolutional neural networks for remote sensing scene classification", Pattern Recognition 61:539–556 | 2017 issue (online 2016-07-03) | **Six popular ImageNet-pretrained ConvNets** (incl. CaffeNet, GoogLeNet, VGG-lineage), tested under full training / fine-tuning / feature extraction | **All three compared** (from scratch, fine-tuned, frozen features + linear SVM) | UC Merced (2,100 imgs/21 classes); WHU-RS19 (1,005/19); Brazilian Coffee Scenes (2,876/2) | Abstract (verbatim): "Results point that **fine tuning tends to be the best performing strategy**. In fact, **using the features from the fine-tuned ConvNet with linear SVM obtains the best results**." **Exact per-dataset accuracy numbers NOT VERIFIED** (see §3) | Classical low-level descriptors (ACC, BIC, LCH, LAS, SASI, HOG, GIST) and BoVW | https://doi.org/10.1016/j.patcog.2016.07.001 | B (conclusion); D (numbers) |
| Xia, Hu, Hu, Shi, Bai, Zhong, Zhang, Lu — "AID: A Benchmark Data Set for Performance Evaluation of Aerial Scene Classification", IEEE TGRS 55(7):3965–3981 (arXiv:1608.05167) | 2017 | Deep CNNs (CaffeNet/GoogLeNet/OverFeat-lineage) used both as ImageNet-pretrained global feature extractors **and** fully trained/fine-tuned baselines on AID | **Both** are baselines in this paper | AID (Aerial Image Dataset) | Dataset verified: **10,000 images, 30 classes**, 600×600 px, 0.5–8 m, classes from 220 to 420 images. Verified verbatim: "using the existing aerial scene datasets … to fully train the networks such as CaffeNet or GoogLeNet **showed a drop in accuracies compared with using the networks as global feature extractors**". **Exact fine-tuned CNN OA values on AID NOT VERIFIED** (see §3) | Low-level (SIFT, LBP, color histogram, GIST), mid-level (BoVW and variants), and deep-CNN baselines | https://doi.org/10.1109/TGRS.2017.2685945 | A (dataset stats, quote); D (OA numbers) |
| Cheng, Han, Lu — "Remote Sensing Image Scene Classification: Benchmark and State of the Art", Proceedings of the IEEE 105(10):1865–1883 (arXiv:1703.00121) | 2017 | Reviews/benchmarks deep feature learning; introduces **NWPU-RESISC45**; evaluates representative deep methods including ImageNet-pretrained CNNs as baselines | Mixed (the paper reviews both; its own baselines include deep CNNs) | NWPU-RESISC45 | Dataset verified: **31,500 images, 45 classes, 700 images/class**. Verified verbatim: "the saturation of accuracy (e.g., **almost 100% classification accuracy on the most popular UC Merced dataset with deep ConvNets features**)". **Exact fine-tuned VGG-16/GoogLeNet OA on NWPU-RESISC45 NOT VERIFIED** (see §3) | Handcrafted features, unsupervised feature learning, deep feature learning | https://doi.org/10.1109/JPROC.2017.2675998 | A (dataset stats, quote); D (OA numbers) |
| Sumbul, Charfuelan, Demir, Markl — "BigEarthNet: A Large-Scale Benchmark Archive for Remote Sensing Image Understanding", IEEE IGARSS 2019, pp. 5901–5904 | 2019 | A **shallow CNN trained on BigEarthNet** compared against a **state-of-the-art CNN pre-trained on ImageNet** (i.e. the ImageNet-transfer baseline is the thing being beaten) | Shallow CNN trained in-domain on BigEarthNet; the ImageNet CNN is used pre-trained | BigEarthNet (Sentinel-2, 590,326 patches, multi-label, CORINE Land Cover 2018) | Abstract (verbatim): "a **shallow** CNN architecture **trained on BigEarthNet provides much higher accuracy compared to a state-of-the-art CNN model pre-trained on ImageNet**". **No numbers in the abstract; exact accuracies NOT VERIFIED** (see §3) | State-of-the-art CNN pre-trained on ImageNet | https://doi.org/10.1109/IGARSS.2019.8900532 | B (direction of result); D (numbers) |
| Risojević, Stojnić — "Do we still need ImageNet pre-training in remote sensing scene classification?", ISPRS Archives XLIII-B3-2022:1399–1406 (arXiv:2111.03690) | 2022 | **ResNet-50 pre-trained on ImageNet-1k, supervised** (Keras) and **self-supervised (SwAV)**; also HRRS in-domain pre-training and domain-adaptive pre-training | **All three compared** (from scratch / frozen features + softmax / fine-tuned) | MLRSNet, RESISC45, PatternNet, RSI-CB, AID, UCM | 80% train, scratch vs IN-1k FT: RESISC45 **95.11 → 97.04**; AID **93.92 → 97.30**; MLRSNet single **97.74 → 98.61**; PatternNet **99.49 → 99.84**; RSI-CB **99.39 → 99.55**; MLRSNet multi-label **91.83 → 92.41**. 20% train, scratch vs IN-1k FT: RESISC45 **85.44 → 93.85**, AID **79.14 → 94.40**, UCM **58.93 → 94.64**, PatternNet **98.04 → 99.51**, RSI-CB **97.29 → 99.15**. Frozen features (20% train): RESISC45 IN-1k **86.94** vs IN-1k-SwAV **89.21** vs MLRSNet-pretrained **93.21**; UCM IN-1k **92.86** vs SwAV **93.27** vs MLRSNet **93.45**. Domain-adaptive (ImageNet-SwAV → MLRSNet → FT): RESISC45 **95.89**, AID **96.09**, UCM **97.14** | Training from scratch; supervised vs self-supervised ImageNet pre-training; in-domain HRRS pre-training | https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-1399-2022 | A |
| He, Girshick, Dollár — "Rethinking ImageNet Pre-training", ICCV 2019, pp. 4917–4926 (arXiv:1811.08883) | 2019 | ResNet-50 / ResNet-101 / ResNeXt-152 backbones in Mask R-CNN (FPN + GN/SyncBN), ImageNet-pretrained vs random init | **Both** (fine-tuned from ImageNet vs trained from scratch) | **COCO** (object detection / instance segmentation / keypoints) — **NOT remote sensing** | 6× schedule, bbox AP: R50 random init **41.3** vs IN-pretrain **41.1**; R101 **42.7** vs **42.3**; X152 from scratch **50.9 bbox AP / 43.2 mask AP** vs **50.3 / 42.5** with ImageNet pre-training; COCO 2018 test-challenge **51.3 bbox AP / 43.6 mask AP** from scratch. Also: "ImageNet pre-training **speeds up** convergence … but does **not necessarily provide regularization or improve final target task accuracy**" | ImageNet pre-training ("the current de facto paradigm of 'pre-training and fine-tuning'") | https://doi.org/10.1109/ICCV.2019.00502 | A |

---

## 2. Prose per result (nuance, and how each number was verified)

### 2.1 Marmanis et al. 2016 — the canonical early RS transfer result (confidence B)

**Citation (verified via Crossref + OpenAlex):** Dimitrios Marmanis, Mihai Datcu, Thomas Esch, Uwe Stilla,
"Deep Learning Earth Observation Classification Using ImageNet Pretrained Networks",
*IEEE Geoscience and Remote Sensing Letters*, vol. 13, no. 1, pp. 105–109.
Crossref `published-print` = January 2016; OpenAlex `publication_date` = 2015-12-01 (online first).
DOI 10.1109/LGRS.2015.2499239. (Crossref counts ~575 citations; OpenAlex ~648 as of 2026-09.)

**What I verified and how.** The abstract was reconstructed verbatim from OpenAlex's
`abstract_inverted_index` (a lossless word-position encoding), via the OpenAlex API. The relevant sentence
is:

> "Comparative results over the UC Merced Land Use benchmark prove that our method significantly
> outperforms previously best stated results, **improving overall accuracy from 83.1% up to 92.4%**."

Also verbatim: "we propose a novel method by considering a pretrained CNN designed for tackling an
entirely different problem, namely, the ImageNet challenge, and exploit it to extract an initial set of
representations. The derived representations are then transferred into a supervised CNN classifier, along
with their class labels … Through this two-stage framework, we successfully deal with the limited-data
problem in an end-to-end processing scheme." And: the method "introduces a novel feature fusion algorithm
that … tackles dimensionality" (feature fusion of multiple backbone representations).

**Nuances the lecture must respect.**

1. **83.1% is not the historical SOTA on UC Merced.** By 2015–2016 several classical methods already
   exceeded 90% on UC Merced (Castelluccio's Table II lists 92.38–94.30% for HMFF, Dirichlet, FV, VLAT,
   etc.). So the "83.1% → 92.4%" pair must be read as *Marmanis's own baseline under their own protocol*,
   not as "the field's previous best ever". The abstract does not state the split/protocol, and I could
   **not** verify it (the paper is closed access, not on arXiv, and PDFs are unreadable in this
   environment). **Do not present 83.1% as a field-wide prior best.**
2. **The backbone is not named in the abstract.** Widely-repeated secondary claims that this paper used
   "VGG-16" or "OverFeat" could **not** be verified here (see §3).
3. It is genuinely a *fine-tuning/transfer* result (representations transferred into a supervised CNN
   classifier), not a frozen-feature SVM result.

### 2.2 Penatti, Nogueira & dos Santos 2015 — the important counter-example (confidence B, numbers C)

**Citation (verified via OpenAlex):** Otávio A. B. Penatti, Keiller Nogueira, Jefersson A. dos Santos,
"Do deep features generalize from everyday objects to remote sensing and aerial scenes domains?",
*2015 IEEE Conference on Computer Vision and Pattern Recognition Workshops (CVPRW)*, pp. 44–51.
DOI 10.1109/CVPRW.2015.7301382. (OpenAlex ~714 citations.)

**This paper is routinely mis-cited as "ImageNet features beat classical descriptors in remote sensing".**
Its own abstract says the opposite for one of the two targets. Verbatim (reconstructed from OpenAlex):

> "We experimentally evaluate ConvNets trained for recognizing everyday objects for the classification of
> aerial and remote sensing images. ConvNets obtained the best results for **aerial** images, while for
> **remote sensing**, they performed well but were **outperformed by low-level color descriptors, such as
> BIC**. We also present a correlation analysis, showing the potential for combining/fusing different
> ConvNets with other descriptors or even combining multiple ConvNets. A preliminary set of experiments
> fusing ConvNets obtains state-of-the-art results for the well-known UCMerced dataset."

So: the "remote sensing" target where ConvNets *lost* to a colour descriptor is the **Brazilian Coffee
Scenes** dataset (green/red/NIR SPOT imagery) — a spectral-domain shift from RGB ImageNet. This is a
first-class nuance for a lecture on "when does ImageNet transfer work".

**Numbers.** The penultimate-layer numbers themselves are **not** in the abstract and the CVPRW full text
was not reachable (CVF and the PDF are blocked here). The numbers reported in the table row are taken from
**Castelluccio et al. (2015)**, whose Table II lists "CNN [8] 2015 93.42 pre-trained ConvNet (CaffeNet)
with SVM classifier" (UC Merced; [8] = this Penatti paper) and whose Table IV is explicitly labelled
"**ALL REFERENCE DATA FROM [8]**" and lists BIC 87.0, BOVW 80.5, CNN-1 84.8 (pre-trained CaffeNet + SVM),
CNN-2 81.2 (pre-trained OverFeat + SVM) on Brazilian Coffee Scenes. Treat these as **secondary
reproduction** (confidence C), not as directly-read primary values.

### 2.3 Castelluccio et al. 2015 — the cleanest early fine-tuning-vs-scratch-vs-frozen comparison (confidence A)

**Citation:** Marco Castelluccio, Giovanni Poggi, Carlo Sansone, Luisa Verdoliva, "Land Use Classification
in Remote Sensing Images by Convolutional Neural Networks", arXiv:1508.00092 (submitted 1 Aug 2015).
Never published in a journal as far as I can verify (OpenAlex records only the arXiv DOI
10.48550/arXiv.1508.00092). **Cite it as an arXiv preprint, not as a peer-reviewed paper.**

**How verified:** I read the results tables in the full text (markdown rendering of the paper, obtained via
`hf-mirror.com/papers/1508.00092.md`, a mirror serving HuggingFace's ~55 kB markdown conversion of the
arXiv source; the `.../papers/1508.00092` route also worked). These are **table reads**, not abstract
claims.

**UC Merced Land Use** (5-fold cross-validation; both datasets are 5-fold):

- Fine-tuning: **CaffeNet 95.48%**, **GoogLeNet 97.10%**. Verbatim: "the fine-tuning approach, as expected,
  provides the best results with both CaffeNet and GoogLeNet, reaching an overall accuracy of 95.48% and
  97.10%, respectively. This is about 10% and 5% better, respectively, than the design from scratch,
  confirming the limited value of this latter option when training data are limited."
- Feature-vector (penultimate layer + softmax): "pretty good results … but clearly inferior to those of the
  fine-tuning approach, with a gap of 1–3%".
- Table II (SOTA comparison, best in bold): GoogLeNet fine-tuned **97.10** vs the best non-CNN reference
  **VLAT 94.30** (HOG+RGB, vectors of locally aggregated tensors, Negrel et al. 2014), FV 93.80, Dirichlet
  92.80, VLAD 92.50, HMFF 92.38, COPD/Partlets 91.33, Sparselets 91.46, UFL-SC 90.26, mCENTRIST 89.90, PSR
  89.10, MCMI 88.20, UFL 81.67 — and the **off-the-shelf CaffeNet + SVM** entry "CNN [8] 2015 **93.42**".
  Intro sentence: "we obtain a gain of almost 3% with respect to the best reference".

**Brazilian Coffee Scenes** (2 classes, green/red/NIR — i.e. NOT ImageNet-like):

- Table III: CaffeNet from scratch 90.17, **CaffeNet fine-tuned 90.94**, CaffeNet feature-vector 85.02;
  **GoogLeNet from scratch 91.83 (bold = best)**, GoogLeNet fine-tuned 90.75, GoogLeNet feature-vector 84.02.
- Table IV (all reference data from Penatti et al.): BIC 87.0, BoVW 80.5, pre-trained CaffeNet+SVM 84.8,
  pre-trained OverFeat+SVM 81.2, proposed 91.8.

**The nuance that matters most:** on the NIR-containing Coffee Scenes target the ordering *inverts* — a
GoogLeNet **trained from scratch** (91.83%) beats fine-tuning (90.75%) and crushes the off-the-shelf
feature path (84.02%), and both CNN paths lose to a simple colour descriptor (BIC, 87.0%) when used
off-the-shelf. The authors explain this as the domain distance from ImageNet: "The images are not optical
(green-red-infrared instead of red-green-blue), hence intrinsically different from the Imagenet samples
used for pre-training." On the RGB aerial UC Merced target, transfer wins decisively. **Same paper, same
backbones, opposite conclusions depending on how ImageNet-like the target is.**

### 2.4 Nogueira, Penatti & dos Santos 2017 — fine-tuning vs off-the-shelf, systematically (confidence B; numbers D)

**Citation (verified via Crossref/OpenAlex):** Keiller Nogueira, Otávio A. B. Penatti, Jefersson A. dos
Santos, "Towards better exploiting convolutional neural networks for remote sensing scene classification",
*Pattern Recognition*, vol. 61, pp. 539–556. DOI 10.1016/j.patcog.2016.07.001. OpenAlex
`publication_date` = 2016-07-03; the volume is the **January 2017** issue (so "2016 online / 2017 issue" —
both are defensible; say "Pattern Recognition 61 (2017), online July 2016"). arXiv version: 1602.01517.
OpenAlex ~922 citations.

**Verified verbatim (from the arXiv version's abstract and body, read via ar5iv):**

- Abstract: "We perform experiments with **six popular ConvNets using three remote sensing datasets** …
  Results point that **fine tuning tends to be the best performing strategy**. In fact, using the features
  from the fine-tuned ConvNet with linear SVM obtains the best results. We also achieved state-of-the-art
  results for the three datasets used."
- Body: three strategies are defined as (i) full training from scratch, (ii) fine-tuned ConvNets (either
  all layers, or only higher layers with early layers frozen), (iii) pre-trained ConvNets as fixed feature
  extractors (penultimate layer + linear classifier). Datasets: UCMerced (2,100 / 21 classes), WHU-RS19
  (1,005 / 19), Brazilian Coffee Scenes (2,876 / 2; green-red-NIR SPOT 2005). Classical baselines: ACC,
  BIC, LCH, LAS, SASI, HOG, GIST and BoVW.

**I could not read the results tables** (Section 6). Both routes (ar5iv HTML and the arXiv-derived
markdown) were cut off by the fetch tool's ~60 kB output cap before Section 5.3, and the results section is
later still. So the exact per-dataset accuracies (the paper's headline numbers) are **unverified** here.

### 2.5 Xia et al. 2017 (AID) — dataset + the "from scratch drops accuracy" statement (confidence A for what is stated; OA numbers D)

**Citation (verified via Crossref/OpenAlex/Semantic Scholar):** Gui-Song Xia, Jingwen Hu, Fan Hu, Baoguang
Shi, Xiang Bai, Yanfei Zhong, Liangpei Zhang, Xiaoqiang Lu, "AID: A Benchmark Data Set for Performance
Evaluation of Aerial Scene Classification", *IEEE TGRS* 55(7):3965–3981, 2017.
DOI 10.1109/TGRS.2017.2685945. arXiv:1608.05167. OpenAlex ~2,220 citations.

**Verified (dataset facts + one key quote), from the full text read via ar5iv and from the HF-mirror
markdown:** AID = **10,000 images in 30 classes**, 600×600 px, multi-resolution (~0.5 m to ~8 m), collected
from Google Earth, per-class counts 220–420 (Table 1 read in full). Key quote on transfer:

> "as reported in [41], using the existing aerial scene datasets (e.g. UC-Merced dataset [57] and the
> WHU-RS19 dataset [56]) to fully train the networks such as CaffeNet [80] or GoogLeNet [81] **showed a
> drop in accuracies compared with using the networks as global feature extractors**. This can be explained
> by the fact that the large scale networks usually contain millions of parameters to be trained,
> therefore, to train them using the aerial datasets with only a few hundreds or thousands images will
> easily stick in overfitting and local minimum."

Also verified: the paper's own framing that UC-Merced/WHU-RS19 "results on them are already saturated",
and that deep learning baselines were run under "different experimental settings" (training ratios).

**Not verified:** the actual headline numbers of the paper's own deep baselines — i.e. the fine-tuned
CaffeNet / GoogLeNet / VGG-16 overall accuracies on AID at the 20%/50%/80% training ratios (Table(s) in
Section 5). The fetch cap cut the document at Section 4.1, and the arXiv v1 markdown (Aug 2016) also cut
before Section 5. The published TGRS version is the one that contains the VGG-16 baseline. **Do not quote
AID fine-tuned CNN OA numbers without checking the TGRS PDF.** (Widely circulated values such as
"GoogLeNet ~86–89%" and "VGG-16 ~89–93% on AID" could **not** be traced to a primary source here — see §3.)

### 2.6 Cheng, Han & Lu 2017 (Proceedings of the IEEE / NWPU-RESISC45) — dataset + saturation quote (confidence A for what is stated; OA numbers D)

**Citation (verified via OpenAlex):** Gong Cheng, Junwei Han, Xiaoqiang Lu, "Remote Sensing Image Scene
Classification: Benchmark and State of the Art", *Proceedings of the IEEE* 105(10):1865–1883, 2017.
DOI 10.1109/JPROC.2017.2675998. arXiv:1703.00121. OpenAlex ~2,689 citations.

**Verified (full text read via the HF-mirror markdown):** NWPU-RESISC45 = **31,500 images, 45 classes, 700
images per class**, 256×256 px, 0.2–30 m. Verbatim from the introduction:

> "almost all existing datasets have a number of limitations, including the small scale of scene classes
> and the image numbers, the lack of image variations and diversity, and **the saturation of accuracy
> (e.g., almost 100% classification accuracy on the most popular UC Merced dataset [38] with deep ConvNets
> features [82])**."

The same paper also documents the review categories (handcrafted / unsupervised feature learning / deep
feature learning) and that "several representative methods are evaluated using the proposed dataset and
the results are reported as a useful baseline". **Not verified:** the specific fine-tuned ImageNet-pretrained
CNN accuracies (CaffeNet/GoogLeNet/VGG-16) reported in its benchmarking section — the fetch cap cut the
document in Section III.B, before Section V.

### 2.7 Sumbul et al. 2019 (BigEarthNet) — an explicit inversion of the ImageNet-transfer assumption (confidence B)

**Citation (verified via OpenAlex):** Gencer Sumbul, Marcela Charfuelan, Begüm Demir, Volker Markl,
"BigEarthNet: A Large-Scale Benchmark Archive for Remote Sensing Image Understanding", *IEEE IGARSS 2019*,
pp. 5901–5904. DOI 10.1109/IGARSS.2019.8900532. (OpenAlex ~549 citations.)

**Attribution correction (important):** the task brief calls this "Neumann et al. 2019". That is wrong for
this paper — the IGARSS 2019 BigEarthNet paper's first author is **Gencer Sumbul**. "Neumann et al. 2020"
is a *different*, related paper (transfer from ImageNet vs from remote-sensing datasets on BigEarthNet,
EuroSAT, So2Sat, RESISC45, UCM) that Risojević & Stojnić 2022 cite as `[Neumann et al., 2020]`.

**Verified verbatim (abstract):** BigEarthNet "consists of **590,326 Sentinel-2 image patches**, each of
which is a section of i) 120×120 pixels for 10 m bands; ii) 60×60 pixels for 20 m bands and iii) 20×20
pixels for 60 m bands", multi-label, annotated from **CORINE Land Cover 2018**. On the transfer question:

> "Experimental results obtained in the framework of RS image scene classification problems show that a
> **shallow** Convolutional Neural Network (CNN) architecture **trained on BigEarthNet provides much higher
> accuracy compared to a state-of-the-art CNN model pre-trained on ImageNet** (which is a very popular
> benchmark archive in computer vision)."

So yes — BigEarthNet **did** involve ImageNet pre-training, but as the **baseline to be beaten** by
in-domain pre-training, not as the proposed method. **No numbers appear in the abstract; I could not
verify the accuracies** (the IGARSS PDF is unreadable here and the arXiv version 1902.06148 is not present
in the accessible full-text bucket).

### 2.8 Risojević & Stojnić 2022 — "when did ImageNet transfer stop being obviously necessary?" (confidence A)

**Citation (two verified versions; the ISPRS one is preferred as peer-reviewed):**
Vladimir Risojević, Vladan Stojnić, "DO WE STILL NEED IMAGENET PRE-TRAINING IN REMOTE SENSING SCENE
CLASSIFICATION?", *Int. Arch. Photogramm. Remote Sens. Spatial Inf. Sci.*, XLIII-B3-2022, 1399–1406, 2022.
DOI 10.5194/isprs-archives-XLIII-B3-2022-1399-2022 (arXiv:2111.03690).
Note: the arXiv preprint is titled "**Do we still need ImageNet pre-training in remote sensing scene
classification?**" and the ISPRS Archives version is all-caps "DO WE STILL NEED IMAGENET PRE-TRAINING IN
REMOTE SENSING SCENE CLASSIFICATION?" — same paper, same authors, same numbers.

**How verified:** I read the JATS XML abstract from Copernicus, the ISPRS HTML landing page, **and** the
full text (Tables 1–9 plus Discussion) from the arXiv HTML via ar5iv. Numbers below are **table reads**.

**The "default assumption" evidence (verbatim, first sentence of the abstract):**

> "Due to the scarcity of labeled data, **using supervised models pre-trained on ImageNet is a de facto
> standard in remote sensing scene classification**."

and in the introduction: "A standard approach for applying transfer learning in high resolution remote
sensing (HRRS) scene classification has been to start with a supervised model trained on ImageNet and
either use it for feature extraction or fine-tune it to the target task (Hu et al., 2015; Nogueira et al.,
2017)." and "Models pre-trained on ImageNet have quickly gained popularity for remote sensing image
classification (Penatti et al., 2015; Hu et al., 2015; Marmanis et al., 2015; Liang et al., 2016;
Nogueira et al., 2017; Zhao et al., 2017; Tong et al., 2020). Although **pre-training on ImageNet is a de
facto standard**, several papers also reported experiments with pre-training on remote sensing image
datasets."

Caveat for the lecture: this is the *strongest* explicit "de facto standard" wording I found, but it is
dated **2022** — i.e. it describes the situation at the moment the field started questioning it. It is
evidence that ImageNet pre-training was the default *by 2022*, not a direct measurement of when it *became*
the default. The earlier papers in this file (Castelluccio 2015, Nogueira 2017, Xia 2017) show the practice
was already routine in 2015–2017 but do not contain an explicit "this is standard practice" sentence that I
could verify.

**Results — training from scratch vs fine-tuning on 80% of each source dataset (Table 2, accuracy/F1 %):**

| dataset | scratch | fine-tune (supervised IN-1k) | fine-tune (SwAV IN-1k) |
|---|---|---|---|
| MLRSNet (multi-label) | 91.83 | 92.41 | 92.58 |
| MLRSNet (single-label) | 97.74 | 98.61 | 98.85 |
| RESISC45 | 95.11 | 97.04 | 96.87 |
| PatternNet | 99.49 | 99.84 | 99.82 |
| RSI-CB | 99.39 | 99.55 | 99.64 |
| AID | 93.92 | 97.30 | 97.85 |

Verbatim reading: "fine-tuning both supervised and self-supervised models pre-trained on ImageNet
outperforms training from scratch in all the cases. However, for both variants of MLRSNet, as well as for
PatternNet and RSI-CB, the differences are very small, and for RESISC45 the difference is around 2%,
indicating that, **even for medium-sized datasets, ImageNet pre-training plays a diminishing role in HRRS
scene classification.**"

**Frozen features, 20% target training (Table 3, %):** supervised ImageNet-1k vs ImageNet-1k-SwAV vs
in-domain HRRS pre-training — RESISC45: **86.94 / 89.21 / 93.21**; MLRSNet single-label target: **91.69 /
93.22 / 91.96**; AID: **90.81 / 92.98 / 92.68**; UCM: **92.86 / 93.27 / 93.45**. Verbatim: "feature
extractors pre-trained on HRRS image datasets outperform supervised feature extractors pre-trained on both
ImageNet-100 and ImageNet-1k in all the cases. Interestingly, self-supervised pre-training considerably
outperforms supervised pre-training on ImageNet-1k … Moreover, self-supervised pre-training is comparable
to pre-training on remote sensing datasets."

**Fine-tuning, 20% target training (Table 5, %):** scratch vs ImageNet-1k vs ImageNet-1k-SwAV —
RESISC45 **85.44 / 93.85 / 94.48**; AID **79.14 / 94.40 / 95.37**; UCM **58.93 / 94.64 / 94.29**;
PatternNet **98.04 / 99.51 / 99.65**; RSI-CB **97.29 / 99.15 / 99.25**; MLRSNet single **93.87 / 96.62 /
97.27**. Verbatim: "both supervised and self-supervised pre-training on ImageNet-1k outperform training
from scratch and pre-training on HRRS datasets in all the cases … Nevertheless, it should be noted that the
differences are small **challenging again the role of ImageNet-1k as an ubiquitous pre-training
dataset.**"

**Domain-adaptive pre-training (Table 7, %):** ImageNet-1k(SwAV) → MLRSNet(single) then fine-tune:
RESISC45 **95.89**, AID **96.09**, UCM **97.14**.

**The paper's stated conclusion, verbatim from the Discussion (§5):**

> "our experimental results show that **training from scratch on most of the used HRRS image datasets
> results in only slightly lower performance than fine-tuning the ImageNet pre-trained models on the same
> datasets.** For example, the differences on both variants of MLRSNet, PatternNet and RSI-CB are less than
> 1%, with somewhat larger gaps on RESISC45 and AID. These results suggest that **for larger and some
> medium-sized HRRS image datasets we might avoid ImageNet pre-training and still achieve competitive
> results.**"

with the crucial qualification that ImageNet pre-training still buys something as a *starting point for
domain adaptation*, and that class overlap between the adaptation set and the target matters:

> "when pre-trained networks are end-to-end fine-tuned, supervised ImageNet pre-training slightly
> outperforms pre-training on HRRS image datasets, while self-supervised ImageNet models after fine-tuning
> outperform both supervised ImageNet and in-domain models."

**So the precise answer to "when did ImageNet transfer stop being obviously necessary" is:** not a clean
date. On small targets (UCM: 58.93% scratch vs 94.64% fine-tuned) ImageNet pre-training remained
essential; on larger/medium HRRS benchmarks (MLRSNet, PatternNet, RSI-CB) the gap closed to <1% by 2022,
and the authors explicitly say ImageNet pre-training's role is "diminishing" and can be "avoided" there.

### 2.9 He, Girshick & Dollár 2019 — the general-CV "rethinking" paper, and what it does NOT cover (confidence A)

**Citation (verified via OpenAlex):** Kaiming He, Ross Girshick, Piotr Dollár, "Rethinking ImageNet
Pre-Training", *ICCV 2019*, pp. 4917–4926. DOI 10.1109/ICCV.2019.00502. arXiv:1811.08883. OpenAlex ~1,029
citations.

**Verified by reading Tables 1–3 and §5 of the full text (ar5iv).** Numbers: with a 6× schedule, Mask
R-CNN + FPN + GroupNorm bbox AP on COCO val2017: R50 random init **41.3** vs ImageNet-pretrained **41.1**;
R101 **42.7** vs **42.3**. Best-schedule comparison (Table 2) shows from-scratch ahead on most metrics
(e.g. R50 AP75 45.6 vs 44.6). ResNeXt-152 from scratch: **50.9 bbox AP / 43.2 mask AP** val2017, and
**51.3 bbox AP / 43.6 mask AP** on the COCO 2018 test-challenge set — "without using any external data";
the same model *with* ImageNet pre-training got **50.3 / 42.5**.

**Remote-sensing coverage: NONE.** The entire abstract and all experiments concern COCO object detection,
instance segmentation and human-keypoint detection. There is no remote-sensing dataset anywhere in the
abstract, and the experimental sections I read (COCO only) contain none. **This paper is frequently cited
in remote-sensing talks as if it settled the question for RS — it did not; it is evidence from COCO.** The
only RS-relevant content is conceptual: the paper's own framing that ImageNet pre-training "is a historical
workaround … for when the community does not have enough target data or computational resources to make
training on the target task doable", and that pre-training "speeds up convergence early in training, but
does not necessarily provide regularization or improve final target task accuracy".

---

## 3. COULD NOT VERIFY

### 3.1 Numbers I could not confirm at primary-source level (do not quote as verified)

1. **Marmanis et al. 2016 — the actual backbone and the 83.1% baseline's protocol.** The abstract (read
   verbatim) names no architecture and no split. Widely repeated claims that they used "VGG-16" or
   "OverFeat" as the pretrained network, and that 83.1% was the field's prior SOTA on UC Merced, are
   **unverified**; the IEEE GRSL paper is closed access, absent from arXiv, and PDFs cannot be read in this
   environment. *Confidence in the 92.4%/83.1% pair from the abstract: high. Confidence in any specific
   backbone attribution: none.*
2. **Penatti et al. 2015 — the per-dataset accuracies printed in their own tables.** CVPRW 2015 full text
   unreachable (CVF blocked, PDF unsupported). Values reported here come from Castelluccio et al.'s
   reproduction (confidence C). The *qualitative* claim (ConvNets win on aerial/UC Merced, lose to BIC on
   the NIR "remote sensing" set) is verbatim from Penatti's own abstract (confidence high).
3. **Nogueira et al. 2017 — all per-dataset accuracy values on UC Merced / WHU-RS19 / Brazilian Coffee
   Scenes.** Only the qualitative conclusion ("fine tuning tends to be the best performing strategy … the
   features from the fine-tuned ConvNet with linear SVM obtains the best results") is verified, from the
   abstract. The results section could not be reached under the fetch output cap via either ar5iv or the
   arXiv-derived markdown.
4. **Xia et al. 2017 (AID) — the fine-tuned ImageNet-pretrained CNN overall accuracies on AID**
   (CaffeNet / GoogLeNet / VGG-16 at the 20%/50%/80% training ratios). The paper's deep-baseline table was
   not reachable. The dataset statistics (10,000 images / 30 classes / 600×600 px) and the
   scratch-vs-feature-extractor statement **are** verified.
5. **Cheng et al. 2017 (Proceedings of the IEEE) — the specific fine-tuned VGG-16 / GoogLeNet / CaffeNet
   accuracies on NWPU-RESISC45.** Not reachable (document cut before the benchmarking section). The dataset
   statistics (31,500 / 45 / 700-per-class) and the "almost 100% … on UC Merced" saturation quote **are**
   verified.
6. **BigEarthNet (Sumbul et al. 2019) — the actual accuracy numbers** behind "a shallow CNN trained on
   BigEarthNet provides much higher accuracy compared to a state-of-the-art CNN model pre-trained on
   ImageNet". Direction of the result is verbatim from the abstract; the magnitude is not.
7. **When exactly ImageNet pre-training became the *default assumption*.** I found exactly one explicit,
   peer-reviewed, verbatim "de facto standard" statement — Risojević & Stojnić (2022), quoted in §2.8. I
   did **not** find an earlier (2015–2019) peer-reviewed paper that says in so many words "ImageNet
   pre-training is standard practice in remote sensing". The 2015–2017 papers show the practice being
   routine and expected, which is weaker evidence than an explicit statement. Flag this if the lecture
   wants to date the transition precisely.
8. **"Neumann et al. 2019 BigEarthNet (IGARSS)"** — as given in the task brief, this attribution is
   **incorrect**. The IGARSS 2019 BigEarthNet paper is **Sumbul, Charfuelan, Demir, Markl**. A separate
   "Neumann et al. 2020" paper does exist and does compare ImageNet vs remote-sensing pre-training (it is
   cited as `[Neumann et al., 2020]` inside Risojević & Stojnić 2022, which summarises it as: experiments on
   BigEarthNet, EuroSAT, So2Sat, RESISC45 and UCM, with fine-tuning from RS-dataset pre-training beating
   fine-tuning from ImageNet, and medium-resolution source datasets generalising poorly to high-resolution
   targets). I did **not** independently verify Neumann et al. 2020's own citation or numbers.
9. **Related work surfaced but not used as primary evidence:** "Is Self-Supervised Pre-training on
   Satellite Imagery Better than ImageNet? A Systematic Study with Sentinel-2" (found only via a
   third-party summary page, `aimodels.fyi`); and a 2026 Springer article snippet reading "Transfer
   learning from ImageNet pretrained models has proven highly effective for remote sensing tasks, despite
   significant doma[in gap]" (`10.1007/s44352-026-00027-4`) — both were only seen as search-result
   fragments, not read. Excluded from the table for that reason.

### 3.2 Tool / access failures (recorded as required)

Confirmed unreachable (`TypeError: fetch failed` or equivalent), each retried 2–3 times:

- `arxiv.org/abs/*`, `arxiv.org/pdf/*`, `www.arxiv.org`, `cn.arxiv.org`, `export.arxiv.org` — all failed.
  arXiv is DNS/connection-blocked from this egress. (Workaround found: `ar5iv.labs.arxiv.org` — itself
  intermittently reachable — and `hf-mirror.com`.)
- `ar5iv.labs.arxiv.org` — failed on the first 3 attempts, succeeded on later attempts. Intermittent.
- `openaccess.thecvf.com` (and `www.cv-foundation.org` not tried) — failed, so Penatti CVPRW full text
  unreachable.
- `huggingface.co` (both `/papers/<id>` and `/buckets/...`) — failed. Reached instead via `hf-mirror.com`.
- `en.wikipedia.org` — rejected: "hostname resolves to a non-public IP address" (DNS-poisoned from this
  egress).
- `github.com`, `r.jina.ai`, `web.archive.org`, `synthical.com`, `paperswithcode.com`,
  `api.semanticscholar.org` (transient 429s when called in parallel bursts — it later worked when called
  singly), `www.connectedpapers.com`, `www.x-mol.com`, `www.scilit.net`/`www.scilit.com`,
  `www.researchgate.net`, `www.tandfonline.com`, `www.mdpi.com` (HTTP 403 Akamai),
  `www.cell.com` (HTTP 403 Cloudflare), `xueshu.baidu.com` (HTTP 403 anti-bot),
  `www.chinaarxiv.org` (`ENOTFOUND`), `xxx.itp.ac.cn` (`ENOTFOUND`).
- `doi.org/10.1109/LGRS.2015.2499239` resolved but redirected cross-origin to `ieeexplore.ieee.org`,
  which is unreachable — so the Marmanis full text was never obtainable.
- `www.themoonlight.io` — HTTP 429 "Vercel Security Checkpoint" on every attempt.
- **All PDFs are unusable**: the fetch tool returns `unsupported content type "application/pdf"`. This is
  why `isprs-archives...pdf`, `mdpi.com/.../pdf`, `elib.dlr.de/...pdf`, the ISPRS AID/Marmanis PDFs and
  every repository-hosted accepted manuscript were inaccessible.
- **The fetch tool truncates long documents at roughly 60 kB with no way to page**, and spill-to-file only
  sometimes captures the omitted tail. This is the single reason the AID, NWPU-RESISC45, Nogueira and
  Cheng results tables could not be read: each document was cut before its results section. Reading the
  spill file at `/tmp/dsh-spill-zFMGl3/session-e747c125d5bd/99b8ec2ee1d2-web_fetch.txt` confirmed the
  Nogueira fetch ended in §5.2.1 with nothing further retrievable.
- I did **not** bypass any of this with `curl`/`wget`, because the task rules restrict bash to inspecting
  files I created.

---

## 4. All URLs actually fetched / verified

Every URL below returned HTTP 200 (or a documented redirect) and was used as evidence above.

**Metadata + verbatim abstracts (primary bibliographic evidence):**

1. https://api.openalex.org/works?filter=title.search:Deep%20Learning%20Earth%20Observation%20Classification%20Using%20ImageNet%20Pretrained&per-page=3 — Marmanis abstract (83.1% → 92.4%), venue, volume/pages, citation count
2. https://api.crossref.org/works?query.bibliographic=Deep+Learning+Earth+Observation+Classification+Using+ImageNet+Pretrained+Networks&rows=2 — Marmanis Crossref record (GRSL 13(1):105–109, Jan 2016)
3. https://api.openalex.org/works?filter=title.search:Do%20deep%20features%20generalize%20from%20everyday%20objects%20to%20remote%20sensing%20and%20aerial%20scenes%20domains&per-page=2&select=doi,display_name,publication_year,publication_date,biblio,cited_by_count,abstract_inverted_index,authorships,primary_location — Penatti abstract (ConvNets beat by BIC on remote sensing)
4. https://api.openalex.org/works?filter=title.search:Land%20Use%20Classification%20in%20Remote%20Sensing%20Images%20by%20Convolutional%20Neural%20Networks&per-page=2&select=... — Castelluccio record (arXiv-only, DOI 10.48550/arxiv.1508.00092)
5. https://api.openalex.org/works?filter=title.search:Towards%20better%20exploiting%20convolutional%20neural%20networks%20for%20remote%20sensing%20scene%20classification&per-page=2&select=... — Nogueira record (Pattern Recognition 61:539–556)
6. https://api.openalex.org/works?filter=title.search:AID%20A%20Benchmark%20Data%20Set%20for%20Performance%20Evaluation%20of%20Aerial%20Scene%20Classification&per-page=2&select=... — Xia/AID record (TGRS 55(7):3965–3981)
7. https://api.openalex.org/works?filter=title.search:Remote%20Sensing%20Image%20Scene%20Classification%20Benchmark%20and%20State%20of%20the%20Art&per-page=1&select=... — Cheng record (Proc. IEEE 105(10):1865–1883)
8. https://api.openalex.org/works?filter=title.search:BigEarthNet%20large-scale%20benchmark%20archive%20remote%20sensing%20image%20understanding&per-page=1&select=... — Sumbul record (IGARSS 2019:5901–5904) + abstract
9. https://api.openalex.org/works?filter=title.search:Rethinking%20ImageNet%20Pre-training&per-page=1&select=... — He record (ICCV 2019:4917–4926) + abstract
10. https://api.openalex.org/works/https://doi.org/10.3390/rs9030225?select=... — Wang et al. 2017, *Remote Sensing* 9(3):225 (used only to identify an MDPI transfer table seen in a search fragment; no number taken from it)
11. https://api.semanticscholar.org/graph/v1/paper/arXiv:1508.00092?fields=title,abstract,openAccessPdf,tldr,venue,year,authors — Castelluccio cross-check (no OA PDF)
12. https://api.semanticscholar.org/graph/v1/paper/DOI:10.1109/TGRS.2017.2685945?fields=title,externalIds,year,venue — established AID arXiv ID = 1608.05167

**Full text read (results tables and/or conclusion sections):**

13. https://hf-mirror.com/papers/1508.00092.md — **Castelluccio et al. full text with Tables I–IV** (UC Merced 97.10/95.48/93.42/94.30; Coffee Scenes 90.94/91.83/87.0/84.8/81.2)
14. https://hf-mirror.com/buckets/huggingchat/papers-content/tree/1508/1508.00092.md — same paper, alternate route
15. https://hf-mirror.com/papers/1508.00092 — HF paper page (abstract + AI summary, cross-check)
16. https://hf-mirror.com/api/papers/1508.00092 — HF papers API JSON (abstract, AI keywords)
17. https://hf-mirror.com/api/buckets/huggingchat/papers-content/tree/1508/1508.00092.md — bucket file metadata (55,282 bytes, text/markdown)
18. https://ar5iv.labs.arxiv.org/html/1811.08883 — **He et al. 2019 full text, Tables 1–3** (COCO only, no RS)
19. https://ar5iv.labs.arxiv.org/html/2111.03690 — **Risojević & Stojnić full text, Tables 1–9 + Discussion** (the "de facto standard" quote and all accuracy tables)
20. https://ar5iv.labs.arxiv.org/html/1602.01517 — Nogueira et al. arXiv full text (abstract + §5.2; results section cut)
21. https://ar5iv.labs.arxiv.org/html/1608.05167 — Xia/AID full text (dataset tables + §2.3 quote; §5 cut)
22. https://hf-mirror.com/buckets/huggingchat/papers-content/tree/1703/1703.00121.md — **Cheng et al. full text part 1** (NWPU-RESISC45 stats, saturation quote; §V cut)
23. https://hf-mirror.com/buckets/huggingchat/papers-content/tree/1608/1608.05167.md — AID arXiv-derived markdown (dataset details; §5 cut)
24. https://isprs-archives.copernicus.org/articles/XLIII-B3-2022/1399/2022/isprs-archives-XLIII-B3-2022-1399-2022.xml — **JATS XML: Risojević & Stojnić abstract, authors, DOI, pages** (peer-reviewed version)
25. https://isprs-archives.copernicus.org/articles/XLIII-B3-2022/1399/2022/ — ISPRS landing page (title, date)
26. https://isprs-archives.copernicus.org/articles/XLII-3/657/2018/isprs-archives-XLII-3-657-2018.xml — Jiang et al. 2018 ISPRS Archives (control test: confirmed Copernicus XML carries front matter only, empty `<body/>`; not used as a source)
27. https://www.alphaxiv.org/abs/1508.00092 — Castelluccio abstract cross-check (third independent copy)

**Connectivity probes (no content used):** https://example.com (HTTP 200), https://www.alphaxiv.org/pdf/1508.00092 (JS-only), https://hf-mirror.com/ (HTTP 200), https://hf-mirror.com/papers/1602.01517 (HTTP 404 — not in HF's paper index), https://hf-mirror.com/papers/2111.03690 (HTTP 404), https://hf-mirror.com/api/buckets/huggingchat/papers-content/tree/1902/1902.06148.md (empty listing — BigEarthNet arXiv full text not mirrored), https://www.paperdigest.org/paper/?paper_id=arxiv-1508.00092 (HTTP 200, no content), https://www.emergentmind.com/papers/1508.00092 (abstract only).

**web_search queries that produced usable evidence** (the search index also carries full text of IEEE/Elsevier/arXiv PDFs and of the HuggingFace markdown, so a few table fragments were visible in result titles, e.g. `fine-tuning | 10,000 | 90.94` from `huggingface.co/buckets/huggingchat/papers-content/tree/1508/1508.00092.md`, later confirmed by reading the file itself): roughly 12 queries. The productive ones were the per-paper title lookups, and the query that returned a
HuggingFace bucket URL with the fragment `fine-tuning | 10,000 | 90.94` — that fragment is what revealed
the arXiv-full-text Markdown mirror route, whose contents were then confirmed by fetching the file itself.
