# ILSVRC trajectory — working notes (primary sources)

All figures below are from the OFFICIAL ImageNet results pages unless stated.
Metric note: the competition reported **top-5 classification error** ("flat cost" in 2010/2011),
measured on the **test set**. From ILSVRC2014 onward there was no standalone classification
task — classification error is a column inside the **Classification+Localization (CLS-LOC)** task.
ILSVRC2017 had no classification task at all; classification error appears in CLS-LOC.

## Official results pages
- 2010: https://image-net.org/challenges/LSVRC/2010/results.php
- 2011: https://image-net.org/challenges/LSVRC/2011/results.php
- 2012: https://image-net.org/challenges/LSVRC/2012/results
- 2013: https://image-net.org/challenges/LSVRC/2013/results.php
- 2014: https://image-net.org/challenges/LSVRC/2014/results.php
- 2015: https://image-net.org/challenges/LSVRC/2015/results.php
- 2016: https://image-net.org/challenges/LSVRC/2016/results.php
- 2017: https://image-net.org/challenges/LSVRC/2017/results.php

## Year-by-year (classification, top-5 error, test set)

- **2010** (taster; metric named "flat cost" = top-5 error)
  - 1. NEC-UIUC (NEC Labs America + UIUC + Rutgers) — flat cost **0.28191 (28.19%)**
    "using sift and lbp feature with two non-linear coding representations and stochastic SVM,
    optimized for top-5 hit rate". Team: Yuanqing Lin, Fengjun Lv, Shenghuo Zhu, Ming Yang,
    Timothee Cour, Kai Yu; UIUC: LiangLiang Cao, Zhen Li, Min-Hsuan Tsai, Xi Zhou, Thomas Huang;
    Rutgers: Tong Zhang.
  - 2. XRCE (Jorge Sanchez, Florent Perronnin, Thomas Mensink) — **0.33649 (33.65%)**,
    Fisher-kernel system (Perronnin, Sanchez & Mensink, ECCV 2010).
  - ILSVRC2010 was held as a "taster competition" with PASCAL VOC 2010.
  - ILSVRC2010 dataset: 1,261,406 train / 50,000 val / 150,000 test (Russakovsky et al. 2015, Table 2).

- **2011** (taster)
  - 1. XRCE (Florent Perronnin; Jorge Sanchez) — flat cost **0.25770 (25.77%)**. Hier cost 0.10980.
  - 2. University of Amsterdam & University of Trento (van de Sande, Uijlings, Smeulders,
    Gevers, Sebe, Snoek) — **0.31010 (31.01%)**, "selective search gorilla".
  - 3. UvA+Trento (plain) — 0.34560.
  - ILSVRC2011 added the single-object localization taster.

- **2012** (Task 1 classification, "Error (5 guesses)")
  - 1. **SuperVision** (Krizhevsky, Sutskever, Hinton, U. Toronto) — **0.15315 (15.315%)**
    "Using extra training data from ImageNet Fall 2011 release" (this is the 7-CNN ensemble:
    5 CNNs + 2 pre-trained on Fall 2011; the paper's 15.3%).
  - SuperVision, supplied data only — **0.16422 (16.422%)** (the 5-CNN ensemble).
  - 2. **ISI** (Univ. of Tokyo) — **0.26172 (26.172%)** "Weighted sum of scores from each
    classifier with SIFT+FV, LBP+FV, GIST+FV, and CSIFT+FV". This is the AlexNet paper's "26.2%".
  - 3. OXFORD_VGG — 0.26979; XRCE/INRIA 0.27058.
  - AlexNet paper (NIPS 2012) states: top-5 test error 15.3% vs 26.2% second best.
    Single CNN = 18.2% top-5 (validation); 5 CNNs = 16.4%. (from paper, carried in project factcheck)

- **2013** (Task 2 classification, "Error")
  - 1. **Clarifai** (Matthew Zeiler, Clarifai) — **0.11197 (11.197%)**
    "Multiple models trained on the original data plus an additional model trained on 5000 categories"
    (i.e. **outside data**). Best entry using original data only: Clarifai **0.11743 (11.743%)**.
  - 2. **NUS** — **0.12953 (12.953%)** (adaptive non-parametric rectification + refined
    PASCAL VOC12 solution, retrained on val).
  - Team **ZF** (Zeiler & Fergus, NYU) best entry: 0.13511 (13.511%) "5 models (4 different
    architectures)"; single model 0.14079. OverFeat-NYU best 0.14182 (7-CNN voting).
  - CAUTION: the "ZFNet won ILSVRC 2013" story vs the official table — the official table's
    top classification entry is Clarifai (Zeiler's company), 11.197%. The Zeiler & Fergus
    paper reports 11.7% (needs paper-body verification); that matches the Clarifai
    original-data entry (11.743%), not the outside-data entry.

- **2014** (no standalone classification task; CLS-LOC Task 2a; ordered by classification error)
  - 1. **GoogLeNet** (Szegedy et al., Google) — **0.06656 (6.656%)**
    entry note: "No localization. Top5 val score is 6.66% error."
  - 2. **VGG** (Simonyan & Zisserman, Oxford) — **0.07325–0.07407 (7.325–7.407%)**
    "a combination of multiple ConvNets". Single VGG ConvNet: **0.08434 (8.434%)**.
  - VGG abstract: "our team secured the first and the second places in the localisation and
    classification tracks respectively" — i.e. VGG won localization, was 2nd in classification.
  - GoogLeNet abstract: set new state of the art for classification and detection in ILSVRC 2014;
    "GoogLeNet, a 22 layers deep network".
  - Detection, Task 1a (provided data), by mAP: NUS 0.37212; MSRA (SPP-net, He et al.) 0.351103;
    single SPP-net 0.318403. With extra data: GoogLeNet ensemble 0.439329 (single 0.380277).

- **2015** (CLS-LOC Task 2a)
  - 1. **MSRA** (He, Zhang, Ren, Sun) — Ensemble A classification error **0.03567 (3.567%)**
    (ResNet; the paper's 3.57% is an ensemble of six residual nets, "only with two 152-layer
    ones at the time of submitting"; validation top-5 3.567%).
  - By classification error the runner-up was **ReCeption — 0.03581 (3.581%)** (method not
    disclosed on the page). MSRA also took localization (0.090178).
  - ResNet-152 single model: **4.49% top-5 validation error** (paper); top-1 19.38%.
  - Detection Task 1a winner: MSRA ensemble 0.620741 mAP (single model 0.588451).

- **2016** (CLS-LOC Task 2a, ordered by classification error)
  - 1. **Trimps-Soushen** (Third Research Institute, Ministry of Public Security, P.R. China) —
    Ensemble 2/3/4 classification error **0.02991 (2.991%)**; Ensembles also best at localization.
  - 2. **ResNeXt** — Ensemble C **0.03031 (3.031%)** (no bounding-box results).
  - 3. **CU-DeepLink** — 0.03042.
  - Detection Task 1a winner: CUImage ensemble 0.662751 mAP (single GBD-Net 0.633634).

- **2017** (no classification task; classification error inside CLS-LOC Task 2a)
  - 1. **WMW (Momenta)** — Ensemble C classification error **0.02251 (2.251%)**; the entry
    abstract (Jie Hu, Li Shen, Gang Sun) presents the Squeeze-and-Excitation block.
    SENet paper abstract: ILSVRC 2017 classification submission "won first place and reduced
    the top-5 error to 2.251%, surpassing the winning entry of 2016 by a relative improvement
    of ~25%". https://arxiv.org/abs/1709.01507
  - 2. **Trimps-Soushen** — 0.02481 (2.481%).
  - 3. NUS-Qihoo_DPNs (CLS-LOC) — 0.0274.
  - Detection Task 1a winner: BDAT sub3 0.732227 mAP. VID winner IC&USYD.

## Human baseline

- Primary source: Russakovsky et al., "ImageNet Large Scale Visual Recognition Challenge",
  IJCV 2015 / arXiv:1409.0575, Section 6.4 "Human accuracy on large-scale image classification".
  - §6.4 relies on "expert annotators who learned to recognize a large portion of the 1000
    ILSVRC classes. During training, the annotators labeled a few hundred validation images
    for practice and later switched to the test set images."
  - §6.4.1: "Annotator A1 evaluated a total of 1500 test set images. The GoogLeNet
    classification error on this sample was estimated to be 6.8% ... The human error was
    estimated to be 5.1%." (quoted via AI Impacts, which cites Russakovsky Table 9)
  - There were (at least) two human annotators; the 5.1% figure is the better one (A1).
  - URL: https://arxiv.org/abs/1409.0575 | AI Impacts summary (19 Oct 2020):
    https://aiimpacts.org/time-for-ai-to-cross-the-human-performance-range-in-imagenet-image-classification/
- Caveats: (1) expert, trained annotator — practiced on a few hundred validation images;
  (2) single annotator on a 1,500-image subsample, not the full 100,000-image test set;
  (3) the paper itself frames it as an estimate; (4) "5.0%" appears in secondary sources —
  no primary source found for 5.0%; the primary figure is 5.1%.
- Beginner (untrained) human: AI Impacts' own small trial (5 people, Karpathy's interface)
  got 74–89% top-5 accuracy (11–26% error), median 81% accuracy — explicitly not a random
  sample and untimed.

## First to beat the human baseline

- **He, Zhang, Ren & Sun, "Delving Deep into Rectifiers: Surpassing Human-Level Performance
  on ImageNet Classification", arXiv:1502.01852, submitted 6 Feb 2015.**
  - Single model (PReLU-net): **5.71% top-5** — "surpasses all existing multi-model results".
  - Multi-model: **4.94% top-5 test error**, "26% relative improvement over the ILSVRC 2014
    winner (GoogLeNet, 6.66%)".
  - Exact claim: "To our knowledge, our result is the first to surpass human-level performance
    (5.1%, Russakovsky et al.) on this visual recognition challenge." (abstract)
  - NOTE: the 4.94% headline is a **multi-model/ensemble** result. The single-model number is 5.71%,
    which does NOT beat 5.1%. This is an important lecture caveat.
- First **competition** entry under 5.1%: ILSVRC 2015, MSRA ResNet — 3.567% (6-model ensemble)
  top-5 test; single ResNet-152 4.49% top-5 validation.
- 2014 winner GoogLeNet 6.66% was still above human.

## End of ILSVRC

- ILSVRC 2017 was the final competition.
- ILSVRC2017 index page, News, Jul 26 2017: "We are passing the baton to Kaggle.
  From now on, all three challenges (LOC-CLS, DET, VID) will be hosted on Kaggle!"
  https://image-net.org/challenges/LSVRC/2017/index.php
  (Kaggle: https://www.kaggle.com/c/imagenet-object-localization-challenge)
- Workshop was renamed "Beyond ImageNet Large Scale Visual Recognition Challenge" (CVPR 2017,
  July 26 2017): "The workshop will mark the last of the ImageNet Challenge competitions, and
  focus on unanswered questions and directions for the future."
  https://image-net.org/challenges/beyond_ilsvrc.php
  - Fei-Fei Li & Jia Deng talk: "ImageNet: Where are we going? And where have we been?"
- ILSVRC2017 tasks were object localization (1000 cls), object detection (200 cls),
  object detection from video (30 cls) — no classification task.
- Reason given: last competition; challenge's goal achieved; moving to Kaggle hosting and
  to new/remaining questions. (The concise causal "because error saturated below human"
  framing is widely repeated but I have NOT found an official sentence stating that as the reason.)
