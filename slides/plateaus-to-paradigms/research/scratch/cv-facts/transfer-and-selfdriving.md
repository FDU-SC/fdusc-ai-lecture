# ImageNet transfer across domains, and self-driving perception's switch to deep learning (2012–2016)

Compiled 2026-09-19. Working dir `/home/zecyel/slides/ch1`.

**Sourcing rules used here.** Every non-obvious number has a URL that was actually fetched unless it is explicitly
flagged. "Read the table" = the rendered full text was retrieved and the numeric table read; "abstract says" = only
the abstract was available. Company blogs and press releases are labelled **COMPANY BLOG** / **PRESS RELEASE, not
peer-reviewed**. A `COULD NOT VERIFY` section at the end lists every claim seen repeated in the wild that could not
be traced to a primary source, plus the tool failures that caused the gaps.

**Tooling reality for this session (affects how much is verified):** `web_fetch` could not read PDFs, truncated long
HTML pages, and failed intermittently on `arxiv.org` (roughly 8 consecutive failures before succeeding). Permanently
unreachable from this environment: `nature.com`, `ieeexplore.ieee.org`, `pubmed.ncbi.nlm.nih.gov`, `api.crossref.org`,
`api.semanticscholar.org`, `link.springer.com`, `openreview.net`, `zenodo.org`, `www.sciencedirect.com`,
`www.darpa.mil` (DNS `EAI_AGAIN`), `waymo.com/blog` (all attempts). `en.wikipedia.org` and `www.google.com` resolved
to non-public IPs and were refused by policy. `web_search` worked but returned mostly title+URL lists, so it was used
for *discovery*; numbers below come from `web_fetch`ed primary sources. `developer.nvidia.com`,
`arxiv.org`, `export.arxiv.org` (API), `ar5iv.labs.arxiv.org`, `papers.nips.cc`, `www.cvlibs.net`,
`mlanthology.org`, `press.bmwgroup.com`, `globenewswire.com`, `pmc.ncbi.nlm.nih.gov` and
`careers.withwaymo.com` were reachable.

---

## TASK B — Self-driving perception's switch to deep learning, ~2012–2016

### B.0 Timeline (dated milestones, all fetched unless flagged)

| date | milestone | source type | URL |
| --- | --- | --- | --- |
| 1989 | ALVINN (Pomerleau) — fully-connected net steers a car on public roads | CMU tech report (cited as ref [6] of the 2016 NVIDIA paper) | http://repository.cmu.edu/cgi/viewcontent.cgi?article=2874&context=compsci |
| ~2004 (July 2004 final report) | **DAVE** — DARPA seedling project, sub-scale RC car through a junk-filled alley; mean distance between crashes ~20 m | Net-Scale Technologies final technical report (cited as ref [5] of the NVIDIA paper) | http://net-scale.com/doc/net-scale-dave-report.pdf |
| 20 Mar 2012 | KITTI Vision Benchmark Suite goes online (stereo, flow, odometry) | Dataset changelog (primary) | https://www.cvlibs.net/datasets/kitti/ |
| 16–21 Jun 2012 | Geiger, Lenz, Urtasun, *Are we ready for autonomous driving? The KITTI vision benchmark suite*, CVPR 2012, pp. 3354–3361 | Peer-reviewed | https://doi.org/10.1109/CVPR.2012.6248074 · abstract: https://mlanthology.org/cvpr/2012/geiger2012cvpr-we/ |
| 12 Nov 2012 | KITTI adds "pre-trained **LSVM** baseline models for download" — the 2012 baseline is a latent SVM, i.e. classical | Dataset changelog (primary) | https://www.cvlibs.net/datasets/kitti/ |
| Dec 2013 | NIPS 2013: Szegedy, Toshev, Erhan (Google), *Deep Neural Networks for Object Detection* — "state-of-the-art performance on Pascal 2007 VOC" | Peer-reviewed | https://papers.nips.cc/paper_files/paper/2013/hash/f7cade80b7cc92b991cf4d2806d6bd78-Abstract.html |
| ~Jul 2015 | NVIDIA starts the DAVE-2 effort ("Nine months ago, a new effort was started at NVIDIA", written Apr 2016) | Peer-reviewed (self-reported) | https://arxiv.org/html/1604.07316v1 |
| 6 Apr 2016 | Cordts et al., *Cityscapes* dataset — 5,000 finely annotated + 20,000 coarsely annotated street images from 50 cities; "Object detection has benefited enormously from large-scale datasets, especially in the context of deep learning" | arXiv preprint (CVPR 2016) | https://arxiv.org/abs/1604.01685 |
| 25 Apr 2016 | **Bojarski et al., *End to End Learning for Self-Driving Cars*, arXiv:1604.07316v1** (v1 only — no v2) | arXiv preprint | https://arxiv.org/abs/1604.07316 |
| 17 May 2016 | Mobileye + STMicroelectronics announce EyeQ5; accelerators "optimized for … machine-learning tasks, including deep neural networks"; FAD vehicles "starting in 2020" | **PRESS RELEASE, not peer-reviewed** | https://www.globenewswire.com/news-release/2016/05/17/1586183/0/en/… |
| 24 May 2016 | Tadmor, Wexler, Rosenwein, Shalev-Shwartz, Shashua (Mobileye) — deep CNN face recognition, 98.2% LFW, 30 ms on one ARM Cortex A9 | arXiv preprint | https://arxiv.org/abs/1605.07270 |
| 1 Jul 2016 | BMW Group + Intel + Mobileye announce L3–L5 platform for 2021; Mobileye sensing "will be deployed on Mobileye's latest system-on-chip, the EyeQ®5" | **PRESS RELEASE, not peer-reviewed** | https://www.press.bmwgroup.com/usa/article/detail/T0261732EN_US/ |
| 17 Aug 2016 | NVIDIA blog "End-to-End Deep Learning for Self-Driving Cars" (same authors as the paper) — repeats 98% autonomy, 10 miles Garden State Parkway, 72 h data | **COMPANY BLOG, not peer-reviewed** | https://developer.nvidia.com/blog/deep-learning-self-driving-cars/ |
| 22 Dec 2016 | Teichmann, Weber, Zöllner, Cipolla, Urtasun, *MultiNet*, arXiv:1612.07695 — ImageNet-pretrained VGG-16/ResNet encoders fine-tuned on KITTI; 1st place KITTI road at submission | arXiv preprint | https://arxiv.org/abs/1612.07695 |
| 21 Aug 2017 | Shalev-Shwartz, Shammah, Shashua (Mobileye), *On a Formal Model of Safe and Scalable Self-driving Cars* (RSS) — safety formalization, **not** a deep-learning paper | arXiv preprint | https://arxiv.org/abs/1708.06374 |
| 26 Jul 2017 | KITTI adds 3D object detection benchmark (3D + bird's-eye-view evaluation) | Dataset changelog (primary) | https://www.cvlibs.net/datasets/kitti/ |
| 7 Dec 2018 | Bansal, Krizhevsky, Ogale (Waymo), *ChauffeurNet*, arXiv:1812.03079 | arXiv preprint | https://arxiv.org/abs/1812.03079 |
| 9 Dec 2018 | Waymo blog "Learning to Drive: Beyond Pure Imitation" | **COMPANY BLOG, not peer-reviewed** | https://waymo.com/blog/2018/12/learning-to-drive-beyond-pure-imitation_26/ (text reached via https://careers.withwaymo.com/blogs/89e712be-5d4a-48b3-a945-b60090823408/learning-to-drive-beyond-pure-imitation) |
| 29 Aug 2019 | Ngiam et al. (Waymo), *StarNet*, arXiv:1908.11069 | arXiv preprint | https://arxiv.org/abs/1908.11069 |
| 10 Dec 2019 | Sun et al. (Waymo), *Waymo Open Dataset*, arXiv:1912.04838 (CVPR 2020) | arXiv preprint / peer-reviewed | https://arxiv.org/abs/1912.04838 |

### B.1 NVIDIA DAVE-2 / "End to End Learning for Self-Driving Cars" (2016) — verified numbers

Primary: **arXiv:1604.07316v1, submitted Mon 25 Apr 2016 16:03:56 UTC; there is no v2.** Full text read at
https://arxiv.org/html/1604.07316v1 (abstract page: https://arxiv.org/abs/1604.07316).

Verified from the full text (HIGH confidence — read the prose and the evaluation section):

- **Architecture:** "9 layers, including a normalization layer, 5 convolutional layers and 3 fully connected layers";
  input image split into YUV planes; output = inverse turning radius `1/r`. Figure 4 caption: "about **27 million
  connections** and **250 thousand parameters**."
- **Training data:** "As of **March 28, 2016**, about **72 hours** of driving data was collected", sampled at 10 FPS.
  Vehicles: a 2016 Lincoln MKZ (drive-by-wire) and a 2013 Ford Focus.
- **Simulation eval:** an ensemble of pre-recorded test routes "correspond to about a total of **three hours and 100
  miles** of driving in Monmouth County, NJ." Autonomy metric explicitly defined: an intervention is triggered when
  the simulated car departs the lane centre by more than 1 m, and each intervention is charged a 6-second human
  recovery penalty; `autonomy = (1 − n·6s / elapsed) · 100`.
- **On-road headline (the number to quote):** "For a typical drive in Monmouth County NJ from our office in Holmdel to
  Atlantic Highlands, we are **autonomous approximately 98% of the time**." Also: "We also drove **10 miles** on the
  Garden State Parkway (a multi-lane divided highway with on and off ramps) with **zero intercepts**."
- **Speed:** "The system operates at **30 frames per second** (FPS)". Hardware: NVIDIA DevBox + Torch 7 for training,
  NVIDIA DRIVE™ PX running Torch 7 in the car.
- **Trained from scratch.** No ImageNet pretraining or transfer is used or mentioned anywhere in the paper. This is the
  clean counterexample to Task A's transfer-everywhere narrative: the canonical 2016 end-to-end driving result is a
  from-scratch CNN driven purely by steering-angle supervision.
- **DAVE lineage, verbatim:** "The groundwork for this project was done over 10 years ago in a DARPA seedling project
  known as DARPA Autonomous Vehicle (DARPA) in which a sub-scale radio control (RC) car drove through a junk-filled
  alley way." — **note:** the paper prints "(DARPA)" where the project is DAVE (the NVIDIA blog version of the same
  text prints "DARPA Autonomous Vehicle (DAVE)"). Treat "(DARPA)" as a typo in the arXiv v1 text.
  DAVE "was used to justify starting the DARPA **Learning Applied to Ground Robots (LAGR)** program"; "**DAVE's mean
  distance between crashes was about 20 meters** in complex environments."
- **Timing:** "Nine months ago, a new effort was started at NVIDIA" → the DAVE-2 effort began around **July 2015**.
- Authors are all NVIDIA Corporation (Holmdel, NJ).

**Company blog (mark as such):** NVIDIA's "End-to-End Deep Learning for Self-Driving Cars", dated **Aug 17, 2016**,
by the same seven-plus authors, https://developer.nvidia.com/blog/deep-learning-self-driving-cars/ — a company blog,
**not peer-reviewed**. It restates 98% autonomy, the 10 miles / zero intercepts, 72 h of data, 27 M connections,
30 FPS, and adds a video. **Inconsistency to be aware of:** the blog says "**About a year ago** we started a new
effort", while the paper says "**Nine months ago**" — do not treat the blog as the precise start date.

### B.2 KITTI (2012) and when deep learning took it over

- **The 2012 benchmark paper.** Geiger, Lenz, Urtasun, *Are We Ready for Autonomous Driving? The KITTI Vision
  Benchmark Suite*, CVPR 2012, pp. 3354–3361, DOI 10.1109/CVPR.2012.6248074. Abstract verified at
  https://mlanthology.org/cvpr/2012/geiger2012cvpr-we/ : the benchmarks "comprise **389 stereo and optical flow image
  pairs**, stereo visual odometry sequences of **39.2 km** length, and more than **200k 3D object annotations**
  captured in cluttered scenarios (up to 15 cars and 30 pedestrians are visible per image)." The paper's framing is
  explicitly pre-deep-learning: "visual recognition systems are still rarely employed in robotics applications …
  the lack of demanding benchmarks", and its finding is that "methods ranking high on established datasets such as
  **Middlebury** perform below average when being moved outside the laboratory to the real world."
- **The 2012 baselines were classical.** The KITTI changelog (https://www.cvlibs.net/datasets/kitti/) records:
  benchmark online **20.03.2012** (stereo, flow, odometry); "**19.08.2012**: The object detection and orientation
  estimation evaluation goes online!"; and "**12.11.2012**: Added pre-trained **LSVM** baseline models for download"
  — i.e. the shipped object-detection baseline was a latent SVM, not a neural network.
- **By the end of 2016 the road benchmark was deep-learning-only.** MultiNet (Dec 2016, see B.3) lists **all six**
  non-anonymous KITTI *road* leaderboard entries in its Table 1 as deep models: FTP 91.61% MaxF1, DDN 93.43%,
  Up_Conv_Poly 93.83%, DEEP-DIG 93.83%, LoDNN 94.07%, MultiNet 94.88%. There is no classical method left in that
  table. (Source: https://arxiv.org/html/1612.07695v2, Table 1.) *Precision caveat:* this is evidence for the **road**
  task only, as of Dec 2016; I did not obtain a dated leaderboard snapshot for KITTI 2D/3D **object detection**, so I
  cannot give a precise date for object detection specifically.
- **Late deep-learning-era additions** (changelog): 3D object detection with 3D + bird's-eye-view evaluation added
  **26.07.2017**; semantic segmentation and instance segmentation added **18.03.2018**; depth completion and
  single-image depth prediction added **11.12.2017**. The benchmark was extended *because* deep models could now
  attempt harder tasks.

### B.3 MultiNet (Dec 2016) — ImageNet transfer meeting self-driving, and a correction

**Correction to the brief:** MultiNet is **not** a Mobileye paper. *MultiNet: Real-time Joint Semantic Reasoning for
Autonomous Driving*, arXiv:1612.07695, submitted **22 Dec 2016** (v2 8 May 2018), is by **Marvin Teichmann, Michael
Weber, Marius Zöllner, Roberto Cipolla, Raquel Urtasun** — affiliations **University of Toronto, FZI Research Center
for Information Technology Karlsruhe, University of Cambridge**, with v2 adding **Uber Advanced Technologies Group**
for Urtasun. Full text: https://arxiv.org/html/1612.07695v2.

This is the single best bridge between Task A and Task B, because it is a dated 2016 self-driving perception paper
that **does** use ImageNet transfer:

- Encoder weights are "initialized using the weights pre-trained on **ImageNet Classification Data**"; encoders are
  **VGG16** (pool5 and fc7 variants) and **ResNet-50 / ResNet-101**. "In a second step, the final fully connected
  layers are removed and replaced by our decoders. Then the network is trained end-to-end using **KITTI** data. Thus
  MultiNet training follows a classic **fine-tuning pipeline**." (Direct quotation from the "MultiNet Training
  Strategy" section.)
- **KITTI road result:** submitted result **MaxF1 94.88%**, **AP 93.71%**, "**1st**" on the public KITTI Road
  Detection Leaderboard at submission time — beating FTP 91.61%, DDN 93.43%, Up_Conv_Poly 93.83%, DEEP-DIG 93.83%,
  LoDNN 94.07% (Table 1). The paper notes "Recently my approach was overtaken by newer submissions."
- **Segmentation decoder (held-out validation), MaxF1:** ResNet101 96.29%, VGG-fc7 95.94%, ResNet50 95.89%,
  VGG-pool5 95.80% (Table 2).
- **Detection decoder, AP moderate / easy / hard:** ResNet101 89.79 / 96.13 / 77.65; ResNet50 86.63 / 95.55 / 74.61;
  VGG-pool5 84.76 / 92.18 / 68.23; Faster-RCNN 78.42 / 91.62 / 66.85; "VGG no RIO pool" 77.00 / 86.45 / 60.82
  (Table 3). I.e. the ImageNet-pretrained ResNet-101 fine-tune beats Faster R-CNN by ~11 AP-moderate.
- **Speed:** v2 says inference "in less than 45 ms for all tasks" (>23 FPS); the v1 abstract said "less than 100 ms".
- **Its own account of the deep-learning takeover:** "This is mostly due to the **deep learning revolution which begun
  with the introduction of AlexNet in 2012**. Since then, the accuracy of new approaches has been increasing at a
  vertiginous rate."

### B.4 Mobileye — what is actually documented

I found **no Mobileye-authored peer-reviewed paper on deep learning for driving perception.** An arXiv API full-text
search for `all:Mobileye` (https://export.arxiv.org/api/query?search_query=all:Mobileye&max_results=40) returns only
**8** items and none is a Mobileye perception paper (they are third-party papers *about* Mobileye or citing it). An
arXiv API search `au:"Shashua" AND cat:cs.CV` returns only **2** items. What *is* verified:

- **Mobileye + STMicroelectronics, EyeQ5 — 17 May 2016, press release** (GlobeNewswire / STMicroelectronics).
  https://www.globenewswire.com/news-release/2016/05/17/1586183/0/en/… **PRESS RELEASE, not peer-reviewed.**
  Verified text: EyeQ5 is the "5th-generation System-on-Chip, scheduled to sample in H1 2018"; it "will feature eight
  multithreaded CPU cores coupled with **eighteen cores of Mobileye's next-generation … vision processors**"; "**8x**
  times over the current 4th generation EyeQ4"; "**more than 12 Tera operations per second**, while keeping power
  consumption **below 5W**"; 10 nm-or-below FinFET; "central computer performing sensor fusion for Fully Autonomous
  Driving (FAD) vehicles **starting in 2020**". The deep-learning relevance is explicit: "EyeQ5's proprietary
  accelerator cores are **optimized for a wide variety of computer-vision, signal-processing, and machine-learning
  tasks, including deep neural networks**", and "The SDK may also be used for prototyping and deployment of **Neural
  Networks**, and for access to **Mobileye pre-trained network layers**." Shashua: "The EyeQ5 continues the legacy
  Mobileye began in **2004** with **EyeQ1**."
- **BMW Group + Intel + Mobileye — 1 July 2016, BMW Group press release, Munich.**
  https://www.press.bmwgroup.com/usa/article/detail/T0261732EN_US/ **PRESS RELEASE, not peer-reviewed.** Verified:
  "bring solutions for highly and fully automated driving into series production by **2021**"; the platform "will
  address **level 3 to level 5** automated driving"; Shashua: "Mobileye is proud to contribute our expertise in
  sensing, localization, and driver policy … The processing of sensing, like our capabilities to understand the
  driving scene through a single camera already, **will be deployed on Mobileye's latest system-on-chip, the EyeQ®5**";
  and the release describes Mobileye as "the global leader in the development of computer vision and **machine
  learning**". It also states they were "present at the BMW Group Headquarters in Munich on **July 1, 2016**".
- **Mobileye-affiliated peer-reviewed machine-learning work that I could verify:** Tadmor, Wexler, Rosenwein,
  Shalev-Shwartz, Shashua, *Learning a Metric Embedding for Face Recognition using the Multibatch Method*,
  arXiv:1605.07270, submitted **24 May 2016**. https://arxiv.org/abs/1605.07270 — "train a deep convolutional neural
  network that achieves an accuracy of **98.2% on the LFW benchmark**, while its prediction runtime takes only
  **30 msec on a single ARM Cortex A9 core**"; "the entire training process took only **12 hours on a single Titan X
  GPU**." Subject is **face recognition on an embedded system**, not driving. (arXiv preprint; I did not verify a
  peer-reviewed venue.)
- **Mobileye-affiliated driving paper, but not a deep-learning one:** Shalev-Shwartz, Shammah, Shashua, *On a Formal
  Model of Safe and Scalable Self-driving Cars*, arXiv:1708.06374, submitted **21 Aug 2017**.
  https://arxiv.org/abs/1708.06374 — proposes Responsibility-Sensitive Safety (RSS), "a white-box, interpretable,
  mathematical model for safety assurance". It is about safety formalization and scalability, **not** about CNN
  perception. Do not cite it as evidence of Mobileye's deep-learning switch.

### B.5 Google / Waymo — what is actually documented

**I could not find a dated, authoritative, published statement of the date Google's or Waymo's perception stack
switched to deep learning.** Neither the papers nor the blog posts I reached say "we moved to deep learning in year X".
What can be documented with dates:

- **Google was doing peer-reviewed deep learning for detection by Dec 2013:** Christian Szegedy, Alexander Toshev,
  Dumitru Erhan, *Deep Neural Networks for Object Detection*, NIPS 2013 (Advances in Neural Information Processing
  Systems 26). https://papers.nips.cc/paper_files/paper/2013/hash/f7cade80b7cc92b991cf4d2806d6bd78-Abstract.html —
  "The approach achieves **state-of-the-art performance on Pascal 2007 VOC**." **Flag:** the NeurIPS abstract page does
  not print author affiliations, and I could not read the PDF header, so the Google affiliation is well-established
  common knowledge but **not verified by me from this document**. Treat the affiliation as unconfirmed.
- **Waymo's own peer-reviewed/preprint deep-learning work (dates verified):**
  - *ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst* — Mayank Bansal, Alex
    Krizhevsky, Abhijit Ogale, arXiv:1812.03079, submitted **7 Dec 2018**. https://arxiv.org/abs/1812.03079. The
    comments field links the video site `sites.google.com/view/waymo-learn-to-drive`, which is what ties it to Waymo.
    Verified quote: "standard behavior cloning is insufficient for handling complex driving scenarios … **30 million
    examples are still not enough**." They add synthesized perturbations and extra losses, and "demonstrate the model
    driving a car in the real world."
  - *StarNet: Targeted Computation for Object Detection in Point Clouds* — Ngiam, Caine, Han, Yang, Chai, Sun, Zhou,
    Yi, Alsharif, Nguyen, Chen, Shlens, Vasudevan, arXiv:1908.11069, submitted **29 Aug 2019**.
    https://arxiv.org/abs/1908.11069. Evaluated "on the large **Waymo Open Dataset** and the **KITTI** detection
    dataset"; "our detector can outperform a competitive baseline on **Pedestrian detection on the Waymo Open Dataset
    by more than 7 absolute mAP** while being more computationally efficient."
  - *Scalability in Perception for Autonomous Driving: Waymo Open Dataset* — Pei Sun et al., arXiv:1912.04838,
    submitted **10 Dec 2019**, **CVPR 2020**. https://arxiv.org/abs/1912.04838. "**1150 scenes** that each span
    **20 seconds**", LiDAR + camera, "15x more diverse than the largest camera+LiDAR dataset available".
- **Waymo company blog (mark as such):** "Learning to Drive: Beyond Pure Imitation", **dated Dec 9 2018**,
  https://waymo.com/blog/2018/12/learning-to-drive-beyond-pure-imitation_26/ — **COMPANY BLOG, not peer-reviewed.**
  `waymo.com/blog` failed to fetch on every attempt; I obtained the text via Waymo's own careers-site mirror of the
  same post, https://careers.withwaymo.com/blogs/89e712be-5d4a-48b3-a945-b60090823408/learning-to-drive-beyond-pure-imitation
  (a Waymo-operated domain, but still a company blog). Verified verbatim: "simple imitation of a large number of
  expert demonstrations is not enough to create a capable and reliable self-driving technology. Instead, we've found
  it valuable to **bootstrap from good perception and control** to simplify the learning task, to inform the model
  with additional losses, and to **simulate the bad rather than just imitate the good**." It says the post is "based
  on research we've just published" — i.e. ChauffeurNet.
- **COMPANY BLOG, URL only, NOT read:** "Google I/O Recap: Turning self-driving cars from science fiction into reality
  with the help of AI", https://waymo.com/blog/2018/05/google-io-recap-turning-self-driving-cars-from-scifi-to-reality-with-ai/
  (May 2018). Both `waymo.com` and the `waymo-blog.blogspot.com` mirror failed to fetch. **I have only the title and
  URL from search results and cannot quote or date-verify its contents. Do not cite it.**

### B.6 The DARPA context — a correction to the brief

**Correction:** the brief asks for "the 2012–2013 DARPA/autonomous-vehicle context". DARPA's autonomous *ground
vehicle* challenges were **2004, 2005 (Grand Challenge) and 2007 (Urban Challenge)** — not 2012–2013. The 2012–2013
DARPA milestone is the **DARPA Robotics Challenge** (humanoid disaster-response robots; announced 2012, Trials in
December 2013), which is not a self-driving programme.

**Confidence flag:** `www.darpa.mil` was **unreachable from this environment on every attempt** (`getaddrinfo
EAI_AGAIN`), so I could **not** read any DARPA primary document. The following URLs were surfaced by search but
**not fetched** — cite them only after someone verifies them:
- DARPA Urban Challenge fact sheet (2007): http://www.darpa.mil/grandchallenge/docs/FACT_SHEETS_Media0807.pdf
- DARPA news, "DRC Trials 2013 Countdown: A Look at the Competition Course" (2013):
  https://www.darpa.mil/news/2013/drc-trials-countdown-course

What *is* verified about the DARPA lineage comes from the NVIDIA paper's own text (arXiv:1604.07316v1), which
documents DAVE as a DARPA seedling project, its use to justify the DARPA **LAGR** programme, and DAVE's ~20 m mean
distance between crashes. That is a peer-reviewed-era arXiv preprint's account, not a DARPA document.

### B.7 Regulatory context (NHTSA)

**COULD NOT VERIFY from a primary source.** I did not fetch any NHTSA document in this session. The commonly cited
NHTSA **2013 "Preliminary Statement of Policy Concerning Automated Vehicles"** (which defined automation levels 0–4)
appeared only in secondary/tertiary sources in my searches, never from `nhtsa.gov` directly. Do not put the NHTSA
2013 levels taxonomy on a slide from this research without fetching the NHTSA PDF first.

---

## TASK A — ImageNet-pretrained backbones transferred to other domains

### A.0 When did ImageNet transfer become the default assumption? (dated, quoted)

This is the clearest, best-sourced part of Task A. The method existed and was shown to work in 2014; it was *not* yet
standard in medicine as late as 2016–2017; by 2018–2019 it was being called the de-facto paradigm, and the first
serious "do we still need it?" papers appear at the same moment.

| date | claim (verbatim) | source | URL |
| --- | --- | --- | --- |
| 23 Mar 2014 | "The results strongly suggest that features obtained from deep learning with convolutional nets should be the **primary candidate in most visual recognition tasks**." (OverFeat/ILSVRC13 features + linear SVM, beating hand-tuned SOTA across many datasets) | Razavian, Azizpour, Sullivan, Carlsson, *CNN Features off-the-shelf: an Astounding Baseline for Recognition*, arXiv:1403.6382 | https://arxiv.org/abs/1403.6382 |
| 6 Nov 2014 | Layer-by-layer quantification of transfer; "initializing a network with transferred features from almost any number of layers can produce a boost to generalization that lingers even after fine-tuning to the target dataset" | Yosinski, Clune, Bengio, Lipson, *How transferable are features in deep neural networks?*, NIPS 2014, arXiv:1411.1792 | https://arxiv.org/abs/1411.1792 |
| Feb 2016 | "**the fine-tuning of an ImageNet pre-trained CNN model on medical image datasets has not yet been exploited.**" | Shin, Roth, Gao, Lu, Xu, Nogues, Yao, Mollura, Summers, IEEE TMI 35(5):1285–1298 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4890616/ |
| Jul 2017 | Of ImageNet-pretrained CNNs: "**However, this situation does not apply to the medical image diagnosis domain.**" | Wang, Peng, Lu, Lu, Bagheri, Summers, *ChestX-ray8*, CVPR 2017 | https://ar5iv.labs.arxiv.org/html/1705.02315 |
| 21 Nov 2018 | "…we expect these discoveries will encourage people to rethink the current **de facto paradigm of `pre-training and fine-tuning' in computer vision**." | He, Girshick, Dollár, *Rethinking ImageNet Pre-training*, arXiv:1811.08883 | https://arxiv.org/abs/1811.08883 |
| 14 Feb 2019 | "Transfer learning from natural image datasets, particularly ImageNet, using standard large models and corresponding pretrained weights **has become a de-facto method** for deep learning applications to medical imaging." / "**the present standard** is to take an existing architecture designed for natural image datasets such as ImageNet … and then fine-tune the model on the medical imaging data." | Raghu, Zhang, Kleinberg, Bengio, *Transfusion*, NeurIPS 2019, arXiv:1902.07208 | https://arxiv.org/abs/1902.07208 |
| 2021 | v1: "Transfer learning (TL) from pretrained deep models is **a standard practice** in modern medical image classification". v2: "Transfer learning (TL) has become **the norm** for medical image classification". | Peng et al., arXiv:2106.05152 | https://arxiv.org/abs/2106.05152 |

**So:** the *capability* was demonstrated in 2014 (Razavian; Yosinski); in medical imaging it was explicitly **not yet
standard in early 2016** and still not assumed in mid-2017; it was called the **de-facto paradigm by late 2018 / 2019**;
and the first influential "pretraining is not necessary" counter-papers (He et al. 2018; Raghu et al. 2019) land at
exactly the moment it became universal. Per-domain "when did it become default" evidence is in the domain sections
below.

### A.1 Results by domain

Each subsection gives a condensed table; the linked `parts/*.md` file holds the per-result prose, all URLs, and
that domain's own failure log.

Full detail, per-result prose, all URLs and every tool failure for each domain are in the corresponding
`parts/` file; the tables below are the condensed, quotable form. **Confidence codes:** **A** = number read
verbatim from the results table of the primary full text; **B** = verbatim from the paper's own abstract;
**C** = reproduced from a different peer-reviewed paper that attributes it; **D** = not verified at primary level.

#### A.1 Medical imaging → `research/scratch/cv-facts/parts/medical.md`

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | conf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CheXNet — Rajpurkar et al., *Radiologist-Level Pneumonia Detection on Chest X-Rays* (arXiv only; **no peer-reviewed venue found**) | 2017 (v1 14 Nov 2017) | DenseNet-121, "initialized with weights from a model pretrained on ImageNet" | **fine-tuned end-to-end** (Adam, lr 0.001, ImageNet mean/std) | NIH ChestX-ray14 (112,120 images) | pneumonia AUROC **0.7680**; radiologist-comparison F1 **0.435** (95% CI 0.387–0.481) | Wang et al. 2017 AUROC **0.633**; Yao et al. **0.713**; radiologist avg F1 **0.387** | https://arxiv.org/abs/1711.05225 | A |
| Wang et al., *ChestX-ray8* (CVPR 2017, DOI 10.1109/CVPR.2017.369) | 2017 | AlexNet / GoogLeNet / VGGNet-16 / **ResNet-50**, all ImageNet ("network surgery") | fine-tuned | NIH ChestX-ray8 (108,948 images) | pneumonia AUROC: ResNet-50 **0.6333**, GoogLeNet 0.5990, AlexNet 0.5493, VGGNet-16 0.5100 | **NO from-scratch arm exists** — all four rows are ImageNet-initialized | https://arxiv.org/abs/1705.02315 | A |
| Tajbakhsh et al., IEEE TMI 35(5):1299–1312, DOI 10.1109/TMI.2016.2535302 | 2016 | AlexNet (Caffe ImageNet), **layer-wise** fine-tuning | fine-tuned vs from-scratch | 4 apps / 3 modalities: colonoscopy polyps, frame quality, CT pulmonary embolism, carotid ultrasound | **conclusion verbatim:** pretrained + adequate fine-tuning "**outperformed or, in the worst case, performed as well as**" from-scratch; fine-tuned nets **more robust to training-set size**; at 25% data the from-scratch net "showed dramatic performance degradation" | from-scratch AlexNet on same data; handcrafted CAD | https://arxiv.org/abs/1706.00712 | A (conclusion) / D (point numbers — results are FROC curves) |
| Shin et al., IEEE TMI 35(5):1285–1298, DOI 10.1109/TMI.2016.2528162 | 2016 | AlexNet + GoogLeNet ImageNet, 2.5D CT | **three arms compared: from scratch (RI), fine-tuned (TL), frozen off-the-shelf (ImNet)** | mediastinal/abdominal lymph-node detection in CT; ILD slice classification | mediastinal LN: **86% sensitivity @ 3 FP/patient** vs prior SOTA **78%** (stacked shallow) and **70%** (CNN); "CNNs trained from scratch **or** fine-tuned from ImageNet models consistently outperform CNNs that merely use off-the-shelf CNN features" | prior SOTA 78% / 70%; internal RI + off-the-shelf arms | https://pmc.ncbi.nlm.nih.gov/articles/PMC4890616/ | A (quote) / C (86% attribution to a specific config unverified) |
| Raghu, Zhang, Kleinberg, Bengio, *Transfusion* (NeurIPS 2019, arXiv:1902.07208) | 2019 | ResNet-50 + Inception-v3 ImageNet (also small CBR nets) | fine-tuned vs **random init** | Retina (~250k fundus, referable-DR AUC); CheXpert (~223k X-ray, 5 pathologies) | Retina AUC ResNet-50 **96.4%±0.05 (random) → 96.7%±0.04 (transfer)**; CheXpert **mixed**: atelectasis 79.52→79.76, edema 88.34→88.89. **Small-data (5k) ResNet50 92.2% → 94.6%**; CBR-LargeT 93.6→93.9 | from-scratch (random init), same architectures/data | https://arxiv.org/abs/1902.07208 | A |
| Stawiaski, *A Pretrained DenseNet Encoder for Brain Tumor Segmentation* (BraTS 2018, arXiv:1811.07542) | 2018 | DenseNet-121 ImageNet — "**an extreme case of transfer learning where we fix the weights** of the pretrained DenseNet encoder" | **FROZEN encoder** | BraTS 2018 (285 train patients) | Dice (val, fixed encoder): ET **0.792**, WT **0.899**, TC **0.847**; test 0.776 / 0.878 / 0.786 | **none reported** (only "competitive" on the leaderboard) | https://arxiv.org/abs/1811.07542 | A (numbers) / no delta available |
| Esteva et al., *Dermatologist-level classification of skin cancer*, Nature 542:115–118, DOI 10.1038/nature21056 | 2017 | "GoogleNet Inception v3 CNN architecture that was pretrained on approximately **1.28 million images (1,000 object categories)**" from ILSVRC 2014 (93.33% top-5); final layer removed | **fine-tuned, all layers** | 129,450 clinical images, 757 training classes, 2,032 diseases; 1,942 biopsy-labelled test images | 3-class accuracy **72.1 ± 0.9%** vs dermatologists **65.56%** / **66.0%**; 9-class **55.4 ± 1.7%** vs 53.3% / 55.0%; biopsy-proven tasks "AUC for each case is **over 91%**" | 21+ board-certified dermatologists; **no from-scratch CNN** | https://pmc.ncbi.nlm.nih.gov/articles/PMC8382232/ | A (72.1 / 55.4) / B (AUC ">91%" only; exact values are in Fig. 3) |

**Nuances that change how these should be presented.**
- **The three most-cited medical transfer results all lack a from-scratch control.** Wang et al. 2017, CheXNet
  and Esteva et al. 2017 each fine-tune ImageNet weights and compare only against *other methods* or clinicians.
  They are evidence that transfer *works*, not that it *beats scratch*.
- **The papers that actually ran the comparison disagree with the folk wisdom.** Shin et al. 2016: from-scratch
  and fine-tuned **both** beat frozen off-the-shelf features, and fine-tuning only clearly wins when labelled
  data are very scarce and the task is multi-class. Tajbakhsh et al. 2016: fine-tuning wins or ties, and is more
  data-efficient. **Raghu et al. 2019 (Transfusion) is the important negative result:** on large medical sets
  transfer is within noise (Retina 96.4→96.7; CheXpert mixed), the clear gain is confined to the small-data
  regime (5k images: 92.2→94.6%), and they attribute it mostly to **over-parameterization / weight scaling, not
  sophisticated feature reuse** — useful feature reuse is limited to the lowest 1–2 layers.
- **CheXNet is a preprint.** No CVPR/MICCAI/ISBI venue found. And the widely repeated pneumonia AUROC
  "0.7681" is **not** in the paper — Table 2 says **0.7680**.

#### A.2 Satellite / remote sensing → `research/scratch/cv-facts/parts/remote-sensing.md`

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | conf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Marmanis, Datcu, Esch, Stilla, IEEE GRSL 13(1):105–109, DOI 10.1109/LGRS.2015.2499239 | 2016 (online Dec 2015) | ImageNet-pretrained CNN → representations transferred into a supervised CNN classifier ("two-stage"); **backbone not named in the abstract** | not frozen | UC Merced Land Use | **OA 83.1% → 92.4%** | "previously best stated results" = 83.1% (their own protocol baseline) | https://doi.org/10.1109/LGRS.2015.2499239 | B |
| Penatti, Nogueira, dos Santos, CVPRW 2015:44–51, DOI 10.1109/CVPRW.2015.7301382 | 2015 | CaffeNet + OverFeat as **off-the-shelf** features + SVM | **FROZEN** | UC Merced; Brazilian Coffee Scenes | verbatim: ConvNets "obtained the best results for **aerial** images, while for **remote sensing**, they performed well but were **outperformed by low-level color descriptors, such as BIC**". UC Merced **93.42%**; Coffee Scenes CaffeNet+SVM **84.8%**, OverFeat+SVM 81.2% | Coffee Scenes: **BIC 87.0%**, BoVW 80.5%; UC Merced: VLAT **94.30%** | https://doi.org/10.1109/CVPRW.2015.7301382 | B (abstract) / C (numbers) |
| Castelluccio, Poggi, Sansone, Verdoliva, arXiv:1508.00092 (**preprint only**) | 2015 | **CaffeNet + GoogLeNet pretrained on ImageNet-1k (ILSVRC)** | **BOTH** — from scratch vs fine-tuning vs feature-vector | UC Merced; Coffee Scenes | UC Merced: **GoogLeNet FT 97.10%**, CaffeNet FT 95.48%, "**about 10% and 5% better, respectively, than the design from scratch**". Coffee Scenes: CaffeNet FT 90.94%, **GoogLeNet from scratch 91.83% (best)**, GoogLeNet FT 90.75%, feature-vector 85.02% / 84.02% | UC Merced VLAT **94.30%**; off-the-shelf CaffeNet+SVM 93.42%; Coffee Scenes BIC 87.0%, BoVW 80.5% | https://arxiv.org/abs/1508.00092 | A |
| Nogueira, Penatti, dos Santos, *Pattern Recognition* 61:539–556, DOI 10.1016/j.patcog.2016.07.001 | 2017 issue (online 3 Jul 2016) | six ImageNet-pretrained ConvNets | **ALL THREE compared** (scratch / fine-tuned / frozen + linear SVM) | UC Merced, WHU-RS19, Brazilian Coffee Scenes | verbatim: "**fine tuning tends to be the best performing strategy**. In fact, **using the features from the fine-tuned ConvNet with linear SVM obtains the best results**" | classical low-level descriptors + BoVW | https://doi.org/10.1016/j.patcog.2016.07.001 | B (conclusion) / D (per-dataset numbers) |
| Xia et al., *AID*, IEEE TGRS 55(7):3965–3981, DOI 10.1109/TGRS.2017.2685945 | 2017 | CaffeNet / GoogLeNet ImageNet, used both as global feature extractors and fully trained | BOTH | AID (10,000 images, 30 classes, 600×600, 0.5–8 m) | verbatim: fully training CaffeNet/GoogLeNet "**showed a drop in accuracies compared with using the networks as global feature extractors**" | low-level (SIFT/LBP/color/GIST), mid-level (BoVW), deep | https://doi.org/10.1109/TGRS.2017.2685945 | A (dataset stats + quote) / D (OA numbers) |
| Cheng, Han, Lu, *Proc. IEEE* 105(10):1865–1883, DOI 10.1109/JPROC.2017.2675998 | 2017 | NWPU-RESISC45 benchmark; ImageNet CNNs among baselines | mixed | NWPU-RESISC45 (31,500 images, 45 classes, 700/class) | verbatim: "the **saturation of accuracy** (e.g., **almost 100% classification accuracy on the most popular UC Merced dataset with deep ConvNets features**)" | handcrafted / unsupervised / deep | https://doi.org/10.1109/JPROC.2017.2675998 | A (dataset stats + quote) / D (OA numbers) |
| Risojević & Stojnić, *Do we still need ImageNet pre-training in remote sensing scene classification?*, ISPRS Archives XLIII-B3-2022:1399–1406 (arXiv:2111.03690) | 2022 | **ResNet-50 ImageNet-1k supervised** and **self-supervised (SwAV)**; also in-domain HRRS and domain-adaptive pre-training | **ALL compared** (scratch / frozen / fine-tuned) | MLRSNet, RESISC45, PatternNet, RSI-CB, AID, UCM | **20% train, scratch → ImageNet FT:** UCM **58.93 → 94.64**, AID **79.14 → 94.40**, RESISC45 **85.44 → 93.85**, PatternNet 98.04 → 99.51, RSI-CB 97.29 → 99.15. **80% train:** AID 93.92 → 97.30, RESISC45 95.11 → 97.04, RSI-CB 99.39 → 99.55. Frozen (20%): UCM ImageNet 92.86 / SwAV 93.27 / MLRSNet-pretrained 93.45 | scratch; supervised vs SSL ImageNet; in-domain HRRS pre-training | https://doi.org/10.5194/isprs-archives-XLIII-B3-2022-1399-2022 | A |
| Sumbul, Charfuelan, Demir, Markl, *BigEarthNet*, IGARSS 2019:5901–5904, DOI 10.1109/IGARSS.2019.8900532 | 2019 | a **shallow CNN trained in-domain on BigEarthNet** vs a state-of-the-art **ImageNet-pretrained** CNN | in-domain trained | BigEarthNet (Sentinel-2, 590,326 patches) | verbatim: "a **shallow** CNN architecture **trained on BigEarthNet provides much higher accuracy compared to a state-of-the-art CNN model pre-trained on ImageNet**" | ImageNet-pretrained CNN | https://doi.org/10.1109/IGARSS.2019.8900532 | B (direction) / D (magnitude) |

**Nuances.**
- **Penatti et al. 2015 is routinely mis-cited.** Its own abstract says off-the-shelf ImageNet ConvNet features
  were **beaten by a low-level colour descriptor (BIC, 87.0%)** on the NIR "remote sensing" set, and only won on
  RGB *aerial* imagery and after multi-network fusion.
- **Castelluccio et al. 2015 contains the inversion on its own tables:** on NIR Coffee Scenes, GoogLeNet
  **from scratch (91.83%)** beat both fine-tuning (90.75%) and off-the-shelf features (84.02%) — same backbones,
  same paper, opposite verdict depending on how ImageNet-like the target domain is.
- **Marmanis's "83.1%" is not the field's UC Merced SOTA** — several classical methods already exceeded 92–94%
  there. Present it as *their own* baseline, not a field-wide best.
- **The best "default assumption" quotation for this domain** (peer-reviewed, verbatim, Risojević & Stojnić 2022
  abstract): "Due to the scarcity of labeled data, using supervised models **pre-trained on ImageNet is a de facto
  standard** in remote sensing scene classification." Their own conclusion is size-dependent: "for larger and some
  medium-sized HRRS image datasets we might avoid ImageNet pre-training and still achieve competitive results" —
  differences <1% on MLRSNet/PatternNet/RSI-CB, but on UCM scratch collapses to 58.93% vs 94.64% fine-tuned.
- **Attribution correction:** the IGARSS 2019 BigEarthNet paper is **Sumbul, Charfuelan, Demir, Markl**, not
  "Neumann et al. 2019". A separate Neumann et al. 2020 does compare ImageNet vs RS pre-training but was not
  independently verified here.
- **He et al. 2019 (*Rethinking ImageNet Pre-training*) covers COCO only — zero remote sensing.** It is often
  cited in remote-sensing talks as if it settled the RS question; it did not.

#### A.3 Microscopy / histopathology → `research/scratch/cv-facts/parts/microscopy.md`

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | conf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Xu et al., *Large scale tissue histopathology image classification, segmentation, and visualization via deep convolutional activation features*, BMC Bioinformatics 18:281, DOI 10.1186/s12859-017-1685-x | 2017 | ImageNet AlexNet (LSVRC-2013 CognitiveVision model) **fc2 4096-d features** | **FROZEN** + linear SVM (plus a fine-tuned variant) | MICCAI 2014 Brain Tumor challenge (GBM vs LGG); colon cancer (Zhejiang) | brain classification **97.8%** vs handcrafted 77.8% and whole-image CNN 62.2%; colon binary **98.0%** vs 90.1%; colon multiclass 87.2% vs 75.5%. Segmentation: brain 84.0% frozen / 84.4% fine-tuned vs 64.0% handcrafted; colon 93.2% / 94.8% vs 77.0% | handcrafted SIFT+LBP+L\*a\*b (186-d); whole-image CNN | https://doi.org/10.1186/s12859-017-1685-x | A (Tables 4 & 6) |
| Caicedo et al., *Nucleus segmentation across imaging experiments: the 2018 Data Science Bowl*, Nature Methods 16:1247–1253, DOI 10.1038/s41592-019-0612-7 | 2019 | **all three DSB-2018 winners used natural-image pretraining**: 1st ImageNet-pretrained encoders, 2nd ImageNet+COCO FPN, 3rd COCO Mask R-CNN | **fine-tuned** | Kaggle Data Science Bowl 2018 / BBBC038 (15 unseen experiments) | 1st: score **0.6316**, mean **F1 0.7120**, recall@IoU0.7 **77.62%**; 2nd 0.6147 / 0.6987; 3rd 0.6141 / 0.7008 | classical **CellProfiler 0.5281 / 0.6280 / 59.35%** | https://doi.org/10.1038/s41592-019-0612-7 | A (Table 1) |
| Ciga, Xu & Martel, *Self supervised contrastive learning for digital histopathology*, arXiv:2011.13971 | 2020/21 | ImageNet-supervised vs **in-domain SimCLR self-supervised** on 57 unlabeled histopathology datasets (ResNet-18/34/50/101) | **frozen linear probe and fine-tuned** | BACH, Lymph, BreakHis, NCT-CRC-HE-100K, Gleason2019 + segmentation/regression | frozen macro-F1: **ImageNet 41.1 → SimCLR SSL 69.3** (+28.2 pts, ResNet-18); fine-tuned 66.7 → 77.0; random init 35.5 frozen / 55.7 fine-tuned. Segmentation: ImageNet **wins** for ResNet-50 (69.7 vs 66.7) | random init; in-domain self-supervision | https://arxiv.org/abs/2011.13971 | A (Tables 1 & 2) |
| **counterexample —** Ronneberger, Fischer, Brox, *U-Net*, MICCAI 2015, arXiv:1505.04597 | 2015 | **none — trained from scratch** (Caffe, Gaussian init std √(2/N)) | — | ISBI 2012 EM segmentation; ISBI Cell Tracking Challenge 2015 | warping error **0.000353** vs Cireşan 0.000420; IOU PhC-U373 **0.9203** vs 0.83, DIC-HeLa **0.7756** vs 0.46 | prior best (2nd place in ISBI CTC) | https://arxiv.org/abs/1505.04597 | A |
| **counterexample —** Litjens et al., *Deep learning as a tool for increased accuracy and efficiency of histopathological diagnosis*, Sci Rep 6:26286, DOI 10.1038/srep26286 | 2016 | **none — trained from scratch** (Theano 0.7 / pylearn2 0.1 + boosting) | — | 225 prostate slides; 271 sentinel nodes | prostate **AUC 0.99** (0.95–1.0) median, 0.98 90th-pct; lymph node AUC 0.90 test / 0.88 consecutive; FROC 0.90@1FP, 0.93@2FP | pathologist workflow | https://doi.org/10.1038/srep26286 | A (numbers) |

**Nuances.**
- **Correction to a very common mis-attribution:** Litjens et al. 2016 (Sci Rep) is **NOT** an ImageNet-pretrained
  CNN. A full-text grep for ImageNet/pretrain/pretrained/initialize/weights finds "ImageNet" only in the reference
  list (Krizhevsky). It is a **from-scratch** result — which makes it a better "before" data point, not a transfer
  result. Do not present its AUC 0.99 as ImageNet transfer.
- **U-Net (2015) was trained from scratch** and still beat the field on ISBI 2012/2015 — a clean counterexample to
  "transfer is necessary" in microscopy.
- **The DSB-2018 result is the event-level marker of the shift:** in a challenge whose explicit goal was one
  configuration-free model across 15 unseen microscopy experiments, **all three winning teams** used natural-image
  pretraining, fine-tuned. Caveat: the paper attributes the win also to pre/post-processing and augmentation, and
  its from-scratch U-Net control is **not** a matched-architecture ablation.
- **The most interesting 2020 result is the opposite direction:** Ciga et al. show in-domain self-supervised
  pretraining beats ImageNet transfer substantially for **classification** (frozen: 41.1 → 69.3 macro-F1) while
  ImageNet still wins for **segmentation** — i.e. the natural-image advantage is task-dependent.

#### A.4 Agriculture → `research/scratch/cv-facts/parts/agriculture.md`

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | conf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mohanty, Hughes, Salathé, *Using Deep Learning for Image-Based Plant Disease Detection*, Front. Plant Sci. 7:1419, DOI 10.3389/fpls.2016.01419 | 2016 (22 Sep 2016) | **AlexNet and GoogLeNet, ImageNet-pretrained**; only `fc8` (AlexNet) / loss-{1,2,3}+classifier (GoogLeNet) re-initialized | **FINE-TUNED** — "we do not limit the learning of any of the layers" | PlantVillage: 54,306 images, 38 classes (14 species × 26 diseases + healthy); colour / grayscale / segmented; 80-20 … 20-80 splits | 80-20 colour split: **GoogLeNet transfer mean F1 0.9934, overall accuracy 99.35%**; AlexNet TL F1 0.9927 (99.28%) | **from-scratch, same architectures:** GoogLeNet 0.9836 (98.37%), AlexNet 0.9782 (97.82%) on the same split; random = 2.63% | https://public-pages-files-2025.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2016.01419/xml/nlm (full-text NLM XML) | A (Table 1) |
| Mohanty et al. — **field-condition test** (same paper) | 2016 | same fine-tuned models | fine-tuned | 121 and 119 real-world web images "taken under conditions different from the images used for training" | **31.40% accuracy on 121 images; 31.69% on 119**; top-5 correct 52.89% / 65.61% | random over 38 classes = 2.63% | same XML; also in the arXiv v2 abstract https://www.alphaxiv.org/abs/1604.03169 | A |
| Olsen et al., *DeepWeeds: A Multiclass Weed Species Image Dataset for Deep Learning*, Sci. Rep. 9:2058, DOI 10.1038/s41598-018-38343-3, arXiv:1810.05726 | 2019 (14 Feb 2019) | **ResNet-50 + Inception-v3 with ImageNet weights** — confirmed in the authors' own code (`ResNet50(weights='imagenet', include_top=False)`) | **FINE-TUNED**, 5-fold CV | DeepWeeds: 17,509 images, 8 weed species + negative = 9 classes, 8 sites in northern Australia | **ResNet-50 mean accuracy 95.7%; Inception-v3 95.1%**; ResNet-50 inference **53.4 ms/image** | the other ImageNet-pretrained architecture; both positioned as new baselines vs earlier smaller weed datasets | https://doi.org/10.1038/s41598-018-38343-3 · code: https://raw.githubusercontent.com/AlexOlsen/DeepWeeds/master/deepweeds.py | A (paper + author code) |
| Sa et al., *DeepFruits: A Fruit Detection System Using Deep Neural Networks*, Sensors 16(8):1222, DOI 10.3390/s16081222 | 2016 | Faster R-CNN adapted "through transfer learning" (RGB + NIR); backbone widely reported as VGG-16/ImageNet but **methods not readable here** | fine-tuned (transfer stated in abstract; layer policy unverified) | own sweet-pepper (+7 other fruit) image datasets, RGB + NIR | **F1 0.838** for sweet-pepper detection; retraining on a new fruit takes "four hours to annotate and train" | **F1 0.807** — the authors' prior pipeline ("improving from 0.807 to 0.838") | https://doi.org/10.3390/s16081222 | B (abstract); backbone D |
| Bargoti & Underwood, *Deep Fruit Detection in Orchards*, arXiv:1610.03677 | 2016/17 | Faster R-CNN "**initialising the Deep Convolutional Neural Network directly from ImageNet features**" | fine-tuned from ImageNet init | orchard imagery: mangoes, almonds, apples | **F1 > 0.9 for apples and mangoes** ("best yet detection performance for these orchards") | cross-orchard transfer gave "**negligible performance gain**" over plain ImageNet init; augmentation cut required training images >2× | https://arxiv.org/abs/1610.03677 | B |
| **counterexample —** Dyrmann, Karstoft, Midtiby, *Plant species classification using deep convolutional neural network*, Biosystems Engineering 151:72–80, DOI 10.1016/j.biosystemseng.2016.08.024 | 2016 | **nothing — "The network is built from scratch"** (deliberate) | from scratch | 10,413 images, 22 weed and crop species at early growth stages, 6 source datasets | classification accuracy **86.2%** | no pretrained comparison reported | https://doi.org/10.1016/j.biosystemseng.2016.08.024 | B |
| Pound et al., plant phenotyping (bioRxiv 053033 full text; GigaScience version `gix083`) | 2016/17 | pretraining status **NOT verified** | unverified | root-tip and shoot phenotyping (wheat/barley) | **root-tip 98.4%, shoot 97.3%; localisation 99.8% / 99.1%**; baseline "80–90% have been typical" | prior classical pipelines | https://www.biorxiv.org/content/10.1101/053033 | A (preprint numbers) / D (pretraining + published-version match) |

**Nuances.**
- **The famous PlantVillage "99.35%" is the *GoogLeNet fine-tuned-from-ImageNet* number, not a from-scratch
  number** — and this paper is one of the few in this whole deliverable that reports a **matched from-scratch
  control**, which transfer beats in every configuration (GoogLeNet 98.37% → 99.35%; AlexNet 97.82% → 99.28%).
- **But the same paper's field-condition test is the essential caveat:** on 121 / 119 real-world web images the same
  fine-tuned models collapse to **31.40% / 31.69%**. PlantVillage is lab-condition imagery; the 99.35% does not
  transfer to the field. That sentence is in the arXiv v2 abstract but **not** in the published Frontiers abstract.
- **Bargoti & Underwood is the cleanest agriculture evidence for the "ImageNet init is the default" claim** — and it
  also shows the domain-specific pre-training that people assume will help (cross-orchard transfer) gave
  "negligible performance gain" over plain ImageNet initialization.
- **Corrections:** "WeedNet 2016" is wrong — Sa et al., IEEE RA-L, DOI 10.1109/LRA.2017.2774979, arXiv:1709.03329
  (SegNet fine-tuned, multispectral MAV, "~0.8 F1 and 0.78 AUC"). "Lee et al. DeepWeeds" is a conflation;
  DeepWeeds is **Olsen et al.** Grinblat et al. 2016's correct DOI is **10.1016/j.compag.2016.07.003**
  (not `…07.005`, which is a cattle paper).
- **No accuracy number could be verified for Ferreira et al. 2017 or Grinblat et al. 2016** — do not print one.
- **Could not obtain any exact quotation from Kamilaris & Prenafeta-Boldú 2018** ("Deep learning in agriculture:
  A survey") on every route tried, so **do not attribute a "standard practice" quote to it.** The quotations that
  *were* directly read and do support the default-assumption claim are from Mohanty, Sa, and Bargoti & Underwood
  (above).


#### A.5 Industrial inspection / defect detection → `research/scratch/cv-facts/parts/industrial.md`

Note the structural difference from the other domains: industrial anomaly detection is dominated by methods that use
an ImageNet-pretrained backbone as a **fixed feature extractor**, often with **no training on the target dataset at
all**. That makes ImageNet transfer load-bearing in a way it is not elsewhere.

| paper | year | what transferred | frozen or fine-tuned | dataset | result + number | baseline | URL | conf |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PatchCore — Roth, Pemula, Zepeda, Schölkopf, Brox, Gehler, CVPR 2022:14318–14328, arXiv:2106.08265 | 2022 | **WideResNet-50 ImageNet**, layer2+layer3 | **FROZEN — no training on the target dataset at all** ("without requiring training on the dataset at hand") | MVTec AD | **image AUROC 99.1%** (PatchCore-25%), 99.0% (10% / 1% coreset) | SPADE 85.5, PatchSVDD 92.1, DifferNet 94.9, **PaDiM 95.3**, PaDiM\* 97.9, Mahalanobis-AD 95.8 | https://arxiv.org/abs/2106.08265 | A |
| PaDiM — Defard, Setkov, Loesch, Audigier, ICPR 2020 Workshops (2021):475–489, arXiv:2011.08785, DOI 10.1007/978-3-030-68799-1_35 | 2020 | ResNet-18 / WideResNet-50-2 / EfficientNet-B5, "**all pretrained on ImageNet**" | **FROZEN** ("avoid ponderous neural network optimization by only using a pretrained CNN") | MVTec AD | localisation AUROC **97.1%**, PRO **90.8%** (PaDiM-R18, all classes); texture classes PaDiM-WR50-Rd550 **96.9 / 93.2** vs SPADE 92.9 / 88.4, AE-SSIM 78 / 56.7, VAE 61.2 / 49.9 | AE / VAE / SPADE / classical | https://arxiv.org/abs/2011.08785 | A (localisation) / C (detection 95.3 / 97.9 from PatchCore's table) |
| Bergmann, Fauser, Sattlegger, Steger, *Uninformed Students*, CVPR 2020:4183–4192, arXiv:1911.02357 | 2020 | **teacher network distilled over ImageNet patches** ("Here, we use ImageNet"); teacher frozen, students trained on the target | teacher **frozen**, students trained | MVTec AD | per-class AUROC read directly: Bottle **.918**, Cable .865, Capsule .916, Hazelnut .937, Metal nut .895, Pill .935, Screw .928, Carpet .695, Grid .819, Leather .819, Tile .912, Wood .725 | 1-NN, OC-SVM, K-Means, ℓ2-AE, VAE, SSIM-AE, AnoGAN, CNN feature dictionary | https://arxiv.org/abs/1911.02357 | A (per-class) / **mean NOT verified; metric label of that column unconfirmed** |
| Bergmann et al., *MVTec AD — A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection*, CVPR 2019:9592–9600 | 2019 | official baselines include "**feature descriptors using pre-trained convolutional neural networks**", alongside classical CV and from-scratch AEs/GANs | frozen descriptors | MVTec AD | **mean AUROC table NOT verified** — paper is PDF-only, no arXiv/OA HTML copy (OpenAlex confirms) | classical CV + from-scratch AE/GAN | https://openaccess.thecvf.com/content_CVPR_2019/html/Bergmann_MVTec_AD_--_A_Comprehensive_Real-World_Dataset_for_Unsupervised_Anomaly_CVPR_2019_paper.html | B (presence of pretrained-CNN baselines only) |
| Gharbage, Teulière, Bouges, Chateau (UCA/CNRS + Michelin), *Rethinking Transfer Learning for Industrial Inspection: DINOv3 vs. ImageNet Pretraining Across RGB and X-ray Tasks*, **arXiv:2605.23472 — PREPRINT, not peer-reviewed** | 2026 | ConvNeXt-T ImageNet-1k vs DINOv3; ResNet-50 ImageNet baseline | both frozen and full fine-tune | Severstal steel, Rubber Rings, RarePlanes, **GDXray X-ray** | ResNet-50 ImageNet full-FT: 63.28 / 73.87 / 78.39 mIoU, 24.42 box mAP@50. ConvNeXt-T ImageNet frozen 21.32 vs **DINOv3 frozen 7.88 on X-ray**; full-FT 29.74 vs 27.84 → **ImageNet still wins under X-ray modality shift** | DINOv3 self-supervised; from-scratch | https://arxiv.org/abs/2605.23472 | A (numbers) — but **preprint** |
| Ibrahim & Tapamo, *JAIT* 5:242–252, DOI 10.37965/jait.2025.0683; Torabipour & Gandomi, *ABMIR* 3(2):73–88, DOI 10.22034/abmir.2025.23563.1162 | 2025 | ensemble of 3 pre-trained CNNs (fine-tuned); VGG16 + transfer learning + attention | fine-tuned | NEU / X-SDD; NEU-CLS / NEU-DET | **100% NEU**, 99.27% X-SDD; **99.98% NEU-CLS, 99.92% NEU-DET**, "at least 4% over baseline VGG16" | baseline VGG16 (its ImageNet pretraining **not** stated) | https://doi.org/10.37965/jait.2025.0683 | B (abstract level; the 100% is suspicious) |

**Nuances.**
- **PatchCore is the strongest single number in the whole deliverable:** image AUROC **99.1%** on MVTec AD using a
  **frozen ImageNet WideResNet-50** with **no target-dataset training** — beat PaDiM 95.3 and SPADE 85.5. Note the
  abstract's "**up to 99.6%**" is the *ensemble*; the single-model claim is 99.1%. The repo README's WR50 baseline
  gives 99.2% image / 98.1% segmentation AUROC.
- **Correction:** Natarajan et al. is **2017** (IEEE ICIT, pp. 986–991, DOI 10.1109/ICIT.2017.7915495), not 2020.
  Its contents were not verified (not open access).
- **Correction:** PaDiM's DOI is **10.1007/978-3-030-68799-1_35**, not `…68763-2_3`.
- **What is missing:** no *peer-reviewed* industrial paper was found that runs the explicit controlled
  "ImageNet fine-tune vs random-init, same protocol" comparison on a defect dataset (NEU-DET / DAGM 2007 /
  KolektorSDD / Magnetic Tile / BTAD). The 2026 preprint states the default-assumption claim explicitly —
  "the dominant transfer-learning paradigm … has relied on supervised ImageNet pretraining, which has served as
  **the standard initialization strategy** … In industrial inspection, this approach **remains widely used** because
  it offers a practical solution when task-specific annotations are scarce" — but it is a **preprint**, so label it
  as such on a slide. The peer-reviewed candidate (Cheng et al., *J. Manufacturing Systems* 84:152–172, 2026,
  DOI 10.1016/j.jmsy.2025.11.022) could not be fetched.

#### A.6 Cross-cutting conclusion on Task A

The honest shape of the evidence is **not** "ImageNet pretraining always wins". It is:

1. **It transfers broadly, and dramatically so in small-data regimes.** Risojević & Stojnić 2022 is the cleanest
   demonstration: at 20% training data, UCM goes **58.93% → 94.64%**, AID **79.14% → 94.40%**, RESISC45
   **85.44% → 93.85%**. Shin et al. 2016 and Tajbakhsh et al. 2016 reach the same conclusion for medical imaging,
   and Transfusion 2019 confirms the gain concentrates in the small-data regime (5k: 92.2% → 94.6%).
2. **At large data scale the advantage shrinks to noise or vanishes.** Transfusion: Retina 96.4 → 96.7 AUC,
   CheXpert mixed, and the residual benefit is over-parameterization/weight scaling rather than feature reuse.
   He et al. 2019: Mask R-CNN on COCO, random init 41.3 AP vs ImageNet-pretrained 41.1 (R50); ResNeXt-152 from
   scratch 50.9 AP vs 50.3 pretrained. The 2022 remote-sensing paper says the same for large HRRS datasets (<1%).
3. **Domain distance matters, and sometimes it flips the answer.** Castelluccio 2015: on NIR Coffee Scenes,
   GoogLeNet **from scratch (91.83%)** beat fine-tuned ImageNet (90.75%). Ciga et al. 2020: in-domain
   self-supervision beats ImageNet transfer for histopathology **classification** (frozen 41.1 → 69.3 macro-F1)
   while ImageNet still wins for **segmentation**. Penatti 2015: off-the-shelf ImageNet features **lose to a
   colour descriptor** on NIR remote sensing.
4. **In industrial anomaly detection it is load-bearing**, because the dominant methods (PatchCore, PaDiM,
   Uninformed Students) use the ImageNet backbone **frozen and untrained on the target data** and still hit
   99.1% image AUROC on MVTec AD.
5. **Sometimes the celebrated result does not involve transfer at all.** NVIDIA DAVE-2 (self-driving) and U-Net
   (microscopy) were trained from scratch; Litjens et al. 2016 (SciPy-reported prostate AUC 0.99) is commonly
   described as ImageNet-pretrained and is **not**.


---

## COULD NOT VERIFY (consolidated)

### Task B
1. **A dated, published statement of when Google/Waymo switched perception to deep learning — NOT FOUND.** Waymo's
   peer-reviewed papers (ChauffeurNet 2018, StarNet 2019, Waymo Open Dataset 2019) prove deep learning was in use by
   2018–2019, but none states a switch date. The Waymo blog posts that might (May 2018 I/O recap, Dec 2018
   ChauffeurNet post) are company blogs; `waymo.com/blog` was unfetchable and the May 2018 post could not be read at all.
2. **Google's affiliation on Szegedy/Toshev/Erhan, NIPS 2013** — the NeurIPS abstract page shows no affiliations and
   the PDF was unreadable. The Google affiliation is very widely known but unverified here.
3. **StarNet as "the 2017 Waymo paper"** — the brief's guess is wrong on the date. StarNet is **2019**
   (arXiv:1908.11069, 29 Aug 2019). arXiv:1704.05519, submitted 18 Apr 2017, is a *different* paper: Janai, Güney,
   Behl, Geiger, *Computer Vision for Autonomous Vehicles: Problems, Datasets and State of the Art* — the survey, not
   StarNet. Do not merge these two.
4. **"Mobileye's 2016 MultiNet / deep multi-task learning work" — MIS-ATTRIBUTED.** arXiv:1612.07695 *MultiNet* is
   Teichmann, Weber, Zöllner, Cipolla, Urtasun (Toronto / FZI Karlsruhe / Cambridge / Uber ATG), **not Mobileye**. I
   found no Mobileye-authored deep-learning-for-driving paper at all (arXiv full-text search for "Mobileye" returns 8
   items, none of them it). Correct the lecture material.
5. **"DARPA 2012–2013 autonomous-vehicle context" — wrong decade.** DARPA's driving challenges were 2004/2005/2007;
   2012–2013 is the DARPA *Robotics* Challenge (humanoids). `www.darpa.mil` was unreachable, so no DARPA document was
   read; the two DARPA URLs above are search-surfaced only.
6. **Any NHTSA primary document (e.g. the 2013 "Preliminary Statement of Policy Concerning Automated Vehicles").**
   Not fetched; seen only in secondary sources.
7. **The precise date KITTI *object detection* (as opposed to road segmentation) became deep-learning-dominated.**
   I have a Dec 2016 all-deep snapshot for the road leaderboard only (MultiNet Table 1), plus the changelog dates for
   when the 3D detection benchmark was added (26.07.2017).
8. **Mobileye's EyeQ4 deep-learning specifics.** EyeQ4 is referenced only comparatively in the EyeQ5 press release
   ("8x times over the current 4th generation EyeQ4"); I found no primary EyeQ4 deep-learning document.
9. **Waymo blog May 2018 "Google I/O Recap …"** — URL known, contents never retrieved (waymo.com and the blogspot
   mirror both failed).
10. **ALVINN's and DAVE's own documents** (CMU tech report 1989; Net-Scale July 2004 final report) — cited by the
    NVIDIA paper as refs [6] and [5], URLs recorded above, but **not fetched** by me (PDF content type unsupported).

### Cross-cutting
11. **`Rethinking ImageNet Pre-training` vs the transfer results.** He et al. 2019 (arXiv:1811.08883) is verified: with
    enough data, from-random-init Mask R-CNN matches ImageNet pretraining on COCO in *final* accuracy (50.9 AP on COCO
    detection without external data), with pretraining mainly accelerating early convergence. Note this is
    **detection/instance segmentation on COCO**, not any of the five domains below; do not generalise it to them.
12. **`Do we still need ImageNet pre-training in remote sensing scene classification?` (arXiv:2111.03690)** is the
    domain-specific analogue; see the remote-sensing section for what was verified from it.
13. **Litjens et al. 2017 (Medical Image Analysis) direct quotation** that ImageNet pretraining was standard practice —
    **NOT CONFIRMED**. The arXiv full text truncates before the Discussion and ScienceDirect is blocked; the abstract
    and introduction contain no such claim. Do not quote Litjens from this research.
14. **"CheXNet pneumonia AUROC 0.7681"** — the widely repeated value; the paper's own table says **0.7680**. See the
    medical section.
15. **ISIC 2018 results attributed to ImageNet transfer** — the ISIC 2018 challenge paper explicitly did not record
    out-of-domain pretraining ("Use of out-of-domain data (non-dermoscopic), such as ImageNet, was expected to be
    mentioned in manuscripts, but not required to be disclosed in a separate meta-data field"), so its headline
    numbers (best balanced accuracy 0.885; top melanoma AUC 0.949) **cannot** be labelled ImageNet-transfer results.

### Per-domain gaps (do NOT put these on slides)
16. **Medical:** the **Litjens et al. 2017** "standard practice" quotation (item 13); CheXNet's peer-reviewed venue
    (none found); a from-scratch control in Wang et al. 2017 (none exists); which Shin et al. 2016 configuration
    produced the 86%@3FP figure; a BraTS transfer-vs-scratch delta (no from-scratch control in Stawiaski 2018);
    Esteva et al.'s per-task AUC values (figure only).
17. **Remote sensing:** fine-tuned AID overall accuracies (Xia et al.); fine-tuned VGG-16/GoogLeNet accuracies on
    NWPU-RESISC45 (Cheng et al.); Nogueira et al. 2017's per-dataset accuracies; Penatti et al. 2015's own printed
    table values; Marmanis et al. 2016's backbone and split protocol (closed-access IEEE GRSL, not on arXiv);
    BigEarthNet's accuracy magnitudes. **Also: "Neumann et al. 2019 BigEarthNet" is a wrong attribution** — the
    IGARSS 2019 paper is Sumbul, Charfuelan, Demir, Markl; Neumann et al. 2020 is a different paper, not verified.
    **No pre-2019 explicit "ImageNet pretraining is standard practice" sentence was findable for this domain** — the
    best is Risojević & Stojnić 2022 ("a de facto standard").
18. **Microscopy:** Spanhol et al. IJCNN 2016 / SMC 2017 BreakHis numbers (IEEE paywalled, author PDFs unreachable);
    Cireşan et al. 2013's numeric F1 (the widely quoted ~0.78 — paywalled, absent from the abstract); Veta et al.
    2015 per-team F1s; whether Falk et al. 2019 and Pound et al. used ImageNet initialization; Tellez et al. 2019's
    ImageNet setting (fetch truncated). **Correction: Litjens et al. 2016 (Sci Rep 6:26286) is NOT an
    ImageNet-pretrained CNN** — a full-text grep finds "ImageNet" only in its reference list; it is a from-scratch
    result. Do not present its prostate AUC 0.99 as transfer. Also note the brief's DSB-2018 phrasing: the three
    winners' pretraining was ImageNet / ImageNet+COCO / COCO, not uniformly ImageNet.
19. **Agriculture:** Ferreira et al. 2017 accuracy (publisher elided the abstract — **no number verified**);
    Grinblat et al. 2016 accuracy (none verified; correct DOI 10.1016/j.compag.2016.07.003); whether Pound et al.
    used ImageNet pretraining, and whether the bioRxiv preprint numbers match the published GigaScience version;
    DeepFruits' VGG-16 backbone; any PlantCLEF accuracy; per-class metrics for DeepWeeds. **No exact quotation from
    Kamilaris & Prenafeta-Boldú 2018 could be obtained on any route** — do not attribute a "standard practice" quote
    to that survey. Also: "WeedNet 2016" is wrong (Sa et al., IEEE RA-L, DOI 10.1109/LRA.2017.2774979,
    arXiv:1709.03329) and "Lee et al. DeepWeeds" is a conflation (it is Olsen et al.).
20. **Industrial:** MVTec AD (CVPR 2019) baseline **mean** AUROC values; Uninformed Students' **mean** MVTec AUROC
    (and even the metric label of the per-class column read, since the caption was unreachable); any peer-reviewed
    industrial paper running a controlled "ImageNet fine-tune vs random-init, same protocol" comparison on NEU-DET /
    DAGM 2007 / KolektorSDD / Magnetic Tile / BTAD; Natarajan et al.'s contents (citation corrected to **2017**,
    IEEE ICIT pp. 986–991, DOI 10.1109/ICIT.2017.7915495); "He et al. 2020 FDM thermal" and "Ren et al. 2017
    surface-defect survey" (no records retrieved); no MTD / MVTec LOCO / BTAD numbers; PaDiM's own image-level
    detection table (the 95.3 / 97.9 figures come from **PatchCore's** Table 1, a third party's transcription).
    **Correction: PaDiM's DOI is 10.1007/978-3-030-68799-1_35**, not `…68763-2_3`.
21. **The industrial "default assumption" claim rests on a preprint.** The explicit quotation ("the dominant
    transfer-learning paradigm … has relied on supervised ImageNet pretraining, which has served as the standard
    initialization strategy … In industrial inspection, this approach remains widely used") comes from
    Gharbage et al., arXiv:2605.23472, a 2026 **preprint — not peer-reviewed**. Label it as such. The peer-reviewed
    candidate (Cheng et al., *J. Manufacturing Systems* 84:152–172, DOI 10.1016/j.jmsy.2025.11.022) was unreachable.


### Tool / access failures (for the record)
- `web_fetch` cannot read PDFs (`unsupported content type "application/pdf"`) and truncates long HTML pages — this
  caused several of the gaps above (Litjens §5 Discussion; Shin et al. §IV tables; KITTI PDFs).
- `arxiv.org` returned `TypeError: fetch failed` on roughly 8 consecutive attempts early in the session, then began
  working; URLs with an explicit `vN` suffix (`/abs/XXXX.NNNNNv1`) were noticeably more reliable than bare ones.
- Permanently blocked / unreachable: `www.darpa.mil` (DNS `EAI_AGAIN`), `waymo.com/blog`, `waymo-blog.blogspot.com`,
  `web.archive.org`, `en.wikipedia.org` and `www.google.com` (resolved to non-public IPs; refused by policy),
  `nature.com`, `ieeexplore.ieee.org`, `pubmed.ncbi.nlm.nih.gov`, `api.crossref.org`, `api.semanticscholar.org`,
  `link.springer.com`, `openreview.net`, `zenodo.org`, `huggingface.co`, `r.jina.ai`.
- `europepmc.org` and `academic.oup.com` returned HTTP 403. `pmc.ncbi.nlm.nih.gov` article pages worked, but its
  per-table URLs hit an NCBI reCAPTCHA.
- `web_search` failed with `TypeError: fetch failed` on the DeepSeek search endpoint 3 times, then recovered.
- Cross-origin redirects were not followed by `web_fetch` (hit for `doi.org`, `export.arxiv.org` over `http`).

### Workarounds that DID work (worth reusing on this host)
- **`api.openalex.org/works/doi:<DOI>`** returns a complete record including `abstract_inverted_index` — a lossless
  word-position encoding of the abstract. This was the single most reliable route to verbatim numbers here, and it
  is how Mohanty et al. 2016 and Olsen et al. 2019 were verified when the publisher sites were blocked.
- **`export.arxiv.org/api/query?search_query=...`** works and supports author/category/full-text queries — used to
  prove that no Mobileye-authored deep-learning paper exists on arXiv.
- **`arxiv.org/abs/<id>vN` and `arxiv.org/html/<id>vN`** succeeded where the bare `/abs/<id>` failed; adding an
  explicit `vN` suffix noticeably improved reliability.
- **`public-pages-files-2025.frontiersin.org/journals/<journal>/articles/<doi>/xml/nlm`** serves the full NLM XML of
  Frontiers papers even when `frontiersin.org` is blocked — this is how Mohanty et al.'s actual results table
  (rather than just its abstract) was read.
- **`raw.githubusercontent.com`** exposes authors' training code, which is how DeepWeeds' ImageNet initialization was
  confirmed at code level (`ResNet50(weights='imagenet', include_top=False)`).
- **`api.openalex.org`**, `api.crossref.org`, `api.semanticscholar.org`, `www.ebi.ac.uk/europepmc/webservices/rest/`,
  `data.mendeley.com/public-api`, `api.biorxiv.org`, `agris.fao.org`, `papers.nips.cc`, `www.cvlibs.net`,
  `mlanthology.org`, `press.bmwgroup.com`, `globenewswire.com`, `pmc.ncbi.nlm.nih.gov` (article pages only),
  `openaccess.thecvf.com` (HTML abstract pages only), and `careers.withwaymo.com` all worked at least intermittently.

