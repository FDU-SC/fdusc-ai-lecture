#!/usr/bin/env python3
"""
Generate every figure in the deck from data, as SVG.

Why SVG: crisp at projector resolution, tiny, and — because svg.fonttype='none'
keeps text as real <text> nodes — every label can be measured in the browser to
check for overlap and clipping. No figure in this deck is hand-drawn.

Inputs
  research/scratch/epoch.csv     Epoch AI notable-models table (params, compute, dates)
  research/data/benchmarks.csv   Epoch AI benchmark runs (GPQA, FrontierMath, AIME, ...)
  curated price table below      from research/briefings/inference_economics_report.md

Output: public/charts/*.svg
Run:    python3 scripts/make_charts.py
"""

import json
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from matplotlib.lines import Line2D

OUT = "public/charts"
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- house style
#
# The deck is presented in dark mode, so every figure is emitted twice: a light
# variant and a "*-dark.svg" variant with inverted ink and brighter accents.
# components/Chart.vue swaps them on the `.dark` class, so one markdown tag
# serves both themes. Backgrounds stay transparent in both — the slide supplies it.

LIGHT = dict(BLUE="#2563eb", RED="#dc2626", GREEN="#15803d", ORANGE="#c2410c",
             PURPLE="#7c3aed", INK="#1e293b", MUTED="#64748b", FAINT="#cbd5e1",
             GRID="#e2e8f0", PANEL="#ffffff", SUFFIX="")
DARK = dict(BLUE="#60a5fa", RED="#f87171", GREEN="#4ade80", ORANGE="#fb923c",
            PURPLE="#a78bfa", INK="#f1f5f9", MUTED="#94a3b8", FAINT="#6b7f99",
            GRID="#334155", PANEL="#1e293b", SUFFIX="-dark")

BLUE = RED = GREEN = ORANGE = PURPLE = INK = MUTED = FAINT = GRID = PANEL = SUFFIX = None


def apply_theme(t):
    """Rebind the module-level palette and matplotlib defaults for one theme."""
    global BLUE, RED, GREEN, ORANGE, PURPLE, INK, MUTED, FAINT, GRID, PANEL, SUFFIX
    BLUE, RED, GREEN = t["BLUE"], t["RED"], t["GREEN"]
    ORANGE, PURPLE = t["ORANGE"], t["PURPLE"]
    INK, MUTED, FAINT, GRID = t["INK"], t["MUTED"], t["FAINT"], t["GRID"]
    PANEL, SUFFIX = t["PANEL"], t["SUFFIX"]
    plt.rcParams.update({
        "svg.fonttype": "none",      # keep <text> as text, not paths
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "figure.facecolor": "none",
        "axes.facecolor": "none",
        "savefig.facecolor": "none",
        "savefig.transparent": True,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,
        "axes.edgecolor": GRID,
        "axes.linewidth": 0.8,
        "axes.labelcolor": MUTED,
        "axes.titlecolor": INK,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "axes.titlesize": 10,
        "axes.labelsize": 8.5,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.7,
        "legend.frameon": False,
        "legend.fontsize": 8,
    })


def despine(ax, keep=("left", "bottom")):
    for s in ("top", "right", "left", "bottom"):
        ax.spines[s].set_visible(s in keep)


def save(fig, name):
    stem, ext = os.path.splitext(name)
    p = os.path.join(OUT, f"{stem}{SUFFIX}{ext}")
    fig.savefig(p, format="svg")
    plt.close(fig)
    print(f"  wrote {p}")


# ---------------------------------------------------------------- load data
print("loading data ...")
models = pd.read_csv("research/scratch/epoch.csv", low_memory=False)
models["date"] = pd.to_datetime(models["Publication date"], errors="coerce")
models["yr"] = models["date"].dt.year + (models["date"].dt.dayofyear - 1) / 365.25
models["flop"] = pd.to_numeric(models["Training compute (FLOP)"], errors="coerce")
models["params"] = pd.to_numeric(models["Parameters"], errors="coerce")
models["tokens"] = pd.to_numeric(models["Training dataset size (total)"], errors="coerce")

aa = json.load(open("research/data/aa-models.json"))

runs = pd.read_csv("research/data/benchmarks.csv", low_memory=False)
runs["rel"] = pd.to_datetime(runs["Version release date"], errors="coerce")
runs["score"] = pd.to_numeric(runs["mean_score"], errors="coerce")
print(f"  models={len(models)}  benchmark runs={len(runs)}")


# ============================================================ 1. compute vs Moore
def chart_compute_vs_moore():
    print("1. compute vs Moore's law")
    d = models.dropna(subset=["flop", "yr"]).copy()
    d = d[d["yr"] >= 1950].sort_values("yr")
    d["lg"] = np.log10(d["flop"])

    fig, ax = plt.subplots(figsize=(9.0, 3.5))
    ax.scatter(d["yr"], d["lg"], s=7, c=FAINT, alpha=0.75, linewidths=0, zorder=2,
               label=f"{len(d)} notable models (Epoch AI)")

    # fitted growth of the modern era
    m = d[d["yr"] >= 2012]
    k, b = np.polyfit(m["yr"], m["lg"], 1)
    dbl_months = np.log10(2) / k * 12
    label = f"notable-model compute, 2012\u20132026:\n2\u00d7 every {dbl_months:.0f} months"
    xs = np.array([2012, 2026.7])
    ax.plot(xs, k * xs + b, color=BLUE, lw=2.0, zorder=4, label=label)

    # Moore's law anchored on the same fitted value at 2012
    y2012 = k * 2012 + b
    mk = np.log10(2) / 2.0
    ax.plot(xs, y2012 + mk * (xs - 2012), color=ORANGE, lw=1.8, ls=(0, (5, 3)),
            zorder=4, label="Moore's law: 2\u00d7 every 24 months")

    ann = [("Perceptron Mark I", 1957, 4), ("Neocognitron", 1980, 12),
           ("LeNet (Zip CNN)", 1989, 14), ("AlexNet", 2012, -4),
           ("GPT-3", 2020, 6), ("GPT-4", 2023, 13), ("GPT-6 Astra", 2026, 6)]
    for name, yy, dy in ann:
        row = d.iloc[(d["yr"] - yy).abs().argmin()]
        ax.annotate(name, (row["yr"], row["lg"]),
                    textcoords="offset points", xytext=(4, dy),
                    fontsize=7.2, color=INK, zorder=6)
        ax.plot([row["yr"]], [row["lg"]], "o", ms=5, mfc=PANEL, mec=BLUE, mew=1.4, zorder=5)

    ax.axvspan(2012, 2026.7, color=BLUE, alpha=0.045, zorder=1)
    ax.set_xlim(1948, 2029)
    ax.set_ylim(0, 27.5)
    ax.set_xlabel("year")
    ax.set_ylabel("training compute (FLOP, log₁₀)")
    ax.set_title("Training compute of notable AI models, 1950\u20132026", loc="left", pad=8)
    ax.legend(loc="upper left", bbox_to_anchor=(0.005, 0.99))
    despine(ax)
    ax.grid(axis="x", alpha=0.35)
    save(fig, "compute-vs-moore.svg")
    print(f"     doubling time = {dbl_months:.1f} months; "
          f"2026 gap vs Moore = {10**((2026-2012)*(k-mk)):.2e}x")
    return dbl_months


# ============================================================ 2. params + capability
def chart_params_capability():
    print("2. parameters and capability")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 3.3))

    d = models.dropna(subset=["params", "yr"]).copy()
    d = d[(d["yr"] >= 1950) & (d["params"] > 0)]
    ax1.scatter(d["yr"], d["params"], s=7, c=FAINT, alpha=0.8, linewidths=0)
    for name, yy in [("Perceptron", 1958), ("Neocognitron", 1980), ("LeNet", 1989),
                     ("AlexNet", 2012), ("GPT-2", 2019), ("GPT-3", 2020),
                     ("GPT-4", 2023), ("Kimi K3", 2026)]:
        row = d.iloc[(d["yr"] - yy).abs().argmin()]
        ax1.plot([row["yr"]], [row["params"]], "o", ms=4.5, mfc=PANEL, mec=BLUE, mew=1.3, zorder=5)
        ax1.annotate(name, (row["yr"], row["params"]), textcoords="offset points",
                     xytext=(4, 4), fontsize=6.8, color=INK)
    ax1.axvspan(2024, 2027, color=RED, alpha=0.06, zorder=0)
    ax1.annotate("disclosure\nstops", xy=(2025.6, 12), fontsize=7, color=RED, ha="center")
    ax1.set_yscale("log")
    ax1.set_xlim(1950, 2029)
    ax1.set_ylim(1, 5e12)
    ax1.set_ylabel("parameters")
    ax1.set_xlabel("year")
    ax1.set_title("Model size", loc="left", pad=6)
    despine(ax1)

    g = runs[runs["task"] == "GPQA diamond"].dropna(subset=["score", "rel"]).copy()
    g = g.sort_values("rel")
    ax2.scatter(g["rel"], g["score"] * 100, s=8, c=FAINT, alpha=0.8, linewidths=0,
                label="individual Epoch runs")
    env = g["score"].cummax() * 100
    ax2.plot(g["rel"], env, color=BLUE, lw=2.0, label="frontier (running best)")
    ax2.axhline(69.7, color=ORANGE, ls=(0, (5, 3)), lw=1.4)
    ax2.annotate("PhD-expert baseline 69.7%", xy=(pd.Timestamp("2023-05-01"), 71.5),
                 fontsize=7, color=ORANGE)
    ax2.set_ylim(20, 103)
    ax2.set_ylabel("GPQA Diamond score (%)")
    ax2.set_xlabel("model release date")
    ax2.set_title("Capability", loc="left", pad=6)
    ax2.legend(loc="lower right")
    ax2.tick_params(axis="x", rotation=0)
    despine(ax2)
    fig.tight_layout(w_pad=2.2)
    save(fig, "params-capability.svg")
    print(f"     GPQA runs={len(g)}  {g['score'].min():.2f} -> {g['score'].max():.2f}")


# ============================================================ 3. benchmark saturation
def chart_saturation():
    print("3. benchmark saturation")

    def series(task, floor=None):
        s = runs[runs["task"] == task].dropna(subset=["score", "rel"]).sort_values("rel")
        return s

    panels = [
        ("GPQA diamond", "GPQA Diamond", 100, "PhD experts 69.7%", 69.7),
        ("OTIS Mock AIME 2024-2025", "OTIS Mock AIME", 100, None, None),
        ("FrontierMath-Tier-4-v2-Private", "FrontierMath Tier 4 (v2)", 100, None, None),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 2.75))
    for ax, (task, title, ceil, note, nv) in zip(axes, panels):
        s = series(task)
        if s.empty:
            ax.set_visible(False)
            continue
        ax.scatter(s["rel"], s["score"] * 100, s=8, c=FAINT, alpha=0.85, linewidths=0)
        ax.plot(s["rel"], s["score"].cummax() * 100, color=BLUE, lw=1.9)
        ax.axhline(ceil, color=GREEN, ls=(0, (4, 3)), lw=1.2)
        ax.annotate("saturated", xy=(s["rel"].min(), ceil - 2), fontsize=6.8,
                    color=GREEN, va="top")
        if nv:
            ax.axhline(nv, color=ORANGE, ls=(0, (5, 3)), lw=1.2)
            ax.annotate(note, xy=(s["rel"].min(), nv + 1.5), fontsize=6.5, color=ORANGE)
        ax.set_title(title, loc="left", pad=5)
        ax.set_ylim(-3, 112)
        ax.set_xlabel("release date")
        if ax is axes[0]:
            ax.set_ylabel("score (%)")
        idx = [0, len(s) // 2, len(s) - 1]
        ticks = [s["rel"].iloc[k] for k in sorted(set(idx))]
        ax.set_xticks(ticks)
        ax.set_xticklabels([t.strftime("%y-%m") for t in ticks], fontsize=7)
        despine(ax)
    fig.tight_layout(w_pad=1.6)
    save(fig, "benchmark-saturation.svg")
    for task, title, *_ in panels:
        s = series(task)
        if len(s):
            print(f"     {title:28s} n={len(s):3d}  {s['score'].min():.2f} -> {s['score'].max():.2f}")


# ============================================================ 4. the Chinchilla shift
def chart_chinchilla():
    print("4. Chinchilla shift")
    d = models.dropna(subset=["params", "tokens"]).copy()
    d = d[(d["params"] > 0) & (d["tokens"] > 0) & (d["yr"] >= 2012)]
    d["ratio"] = d["tokens"] / d["params"]
    ratio20 = (d["ratio"] - 20).abs().sort_values().index[:6]

    fig, ax = plt.subplots(figsize=(4.6, 3.2))
    pre = d[d["yr"] < 2022]
    post = d[d["yr"] >= 2022]
    ax.scatter(pre["params"], pre["tokens"], s=14, c=FAINT, linewidths=0, label="2012\u20132021")
    ax.scatter(post["params"], post["tokens"], s=14, c=BLUE, linewidths=0, label="2022\u20132026")

    xs = np.array([1e7, 1e13])
    ax.plot(xs, 20 * xs, color=ORANGE, lw=1.6, ls=(0, (5, 3)), label="20 tokens / parameter")
    ax.annotate("Chinchilla ratio", xy=(2e9, 20 * 2e9), xytext=(6e7, 6e11),
                fontsize=7.5, color=ORANGE,
                arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.8))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e7, 1e13)
    ax.set_ylim(1e9, 4e13)
    ax.set_xlabel("parameters")
    ax.set_ylabel("training tokens")
    ax.set_title("How much data per parameter", loc="left", pad=6)
    ax.legend(loc="upper left")
    despine(ax)
    save(fig, "chinchilla-shift.svg")
    print(f"     n={len(d)}  median ratio pre-2022={pre['ratio'].median():.1f} "
          f"post-2022={post['ratio'].median():.1f}")


# ============================================================ 5. price vs capability
def chart_price_performance():
    print("5. price vs capability")
    # this figure is rendered smaller than the others on the slide, so give it
    # larger internal type to keep it legible at projector distance
    with plt.rc_context({"font.size": 10.5, "axes.titlesize": 11.5,
                         "axes.labelsize": 10, "xtick.labelsize": 9.5,
                         "ytick.labelsize": 9.5, "legend.fontsize": 9}):
        _price_performance_body()


def _price_performance_body():
    """Price against measured intelligence, from the full Artificial Analysis
    leaderboard (652 models captured to research/data/aa-models.json).

    Only models whose index AA computed under the *current* index version are
    plotted (intelligence_index_is_estimated is false — 170 rows). The other
    ~480 rows carry scores produced by earlier index versions, so plotting them
    on one axis would compare incompatible measurements.

    Price here is the plain mean of list input and output price. AA's own
    headline blend is 7:2:1 cache-hit:input:output, which is 2-4x lower and
    reads as implausibly cheap to a lecture audience; the model ordering is the
    same under either definition.
    """
    rows = []
    for m in aa:
        if m.get("intelligence_index_is_estimated") is not False:
            continue
        pin, pout, ii = m.get("price_input"), m.get("price_output"), m.get("intelligence_index")
        if pin is None or pout is None or ii is None:
            continue
        price = (pin + pout) / 2
        if price <= 0:                     # free tiers break a log axis
            continue
        rows.append((m.get("name", ""), m.get("short_name") or m.get("name", ""),
                     price, ii, bool(m.get("open_weights"))))
    d = pd.DataFrame(rows, columns=["name", "short", "price", "ii", "open"])

    # efficient frontier: the cheapest model at each level of intelligence reached
    front, best = [], float("inf")
    for r in d.sort_values("ii", ascending=False).itertuples():
        if r.price < best:
            best = r.price
            front.append(r)
    front = sorted(front, key=lambda r: r.ii)

    fig, ax = plt.subplots(figsize=(9.0, 3.6))
    for flag, colour, label in ((True, BLUE, "open weights"),
                                (False, ORANGE, "closed weights")):
        sub = d[d["open"] == flag]
        ax.scatter(sub["price"], sub["ii"], s=25, c=colour, alpha=0.78,
                   linewidths=0.7, edgecolors=PANEL, zorder=3, label=label)

    fx = [r.price for r in front]
    fy = [r.ii for r in front]
    ax.plot(fx, fy, color=RED, lw=1.9, zorder=4, label="cheapest at each level")
    ax.scatter(fx, fy, s=36, facecolors="none", edgecolors=RED, linewidths=1.3, zorder=5)

    def pick(text):
        return next((r for r in front if text.lower() in r.name.lower()), None)

    top, mid, value = pick("Fable 5.1"), pick("Muse Spark 1.3"), pick("GLM-5.3-Flash")
    # hand-placed: the upper-left triangle is empty by construction (nothing is
    # both cheap and best), so the note goes there and the labels hug the line
    for r, dx, dy, ha in ((top, -8, 8, "right"), (mid, 8, 4, "left"),
                          (value, -6, -14, "right")):
        if r is not None:
            label = r.short.split(" (")[0][:20]      # AA short names carry an effort suffix
            ax.annotate(label, (r.price, r.ii), textcoords="offset points",
                        xytext=(dx, dy), fontsize=8, color=INK, ha=ha, zorder=7)

    n_open = sum(1 for r in front if r.open)
    ax.annotate(f"{n_open} of the {len(front)} frontier models are open-weight",
                xy=(0.028, 0.955), xycoords="axes fraction", ha="left", va="top",
                fontsize=8.5, color=MUTED, zorder=7)

    ax.set_xscale("log")
    ax.set_xlim(0.05, 42)
    ax.set_ylim(0, 58)
    ax.set_xlabel("price, USD per 1M tokens  (mean of list input and output)")
    ax.set_ylabel("Artificial Analysis Intelligence Index")
    ax.set_title(f"Intelligence against price - Artificial Analysis, "
                 f"{len(d)} ranked models", loc="left", pad=8)
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(axis="y", alpha=0.3)
    despine(ax)
    save(fig, "price-performance.svg")
    print(f"     AA: {len(d)} ranked+priced models, frontier of {len(front)} points, "
          f"${d['price'].min():.3f}-${d['price'].max():.1f}, index {d['ii'].min():.1f}-{d['ii'].max():.1f}")


# ============================================================ 6. energy + queue
def chart_energy():
    print("6. energy and the interconnection queue")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 3.0))

    labels = ["2025", "2030\n(projected)"]
    vals = [485, 950]
    bars = ax1.bar(labels, vals, color=[MUTED, BLUE], width=0.5)
    for b, v in zip(bars, vals):
        ax1.annotate(f"{v} TWh", (b.get_x() + b.get_width() / 2, v), ha="center",
                     va="bottom", fontsize=8.5, color=INK)
    ax1.set_ylim(0, 1180)
    ax1.set_ylabel("TWh per year")
    ax1.set_title("Global datacenter electricity", loc="left", pad=6)
    ax1.annotate("≈3% of world electricity\nby 2030", xy=(1.32, 950), fontsize=7, color=MUTED)
    despine(ax1)
    ax1.grid(axis="x", alpha=0)

    qy = ["Dec 2024", "Dec 2025", "Aug 2026"]
    qv = [63, 233, 474]
    ax2.plot(qy, qv, "o-", color=RED, lw=2, ms=6, label="large-load capacity requested")
    ax2.plot(qy, [7.5, 7.5, 7.5], "s--", color=GREEN, lw=2, ms=5,
             label="actually energized")
    for x, v in zip(qy, qv):
        ax2.annotate(f"{v} GW", (x, v), textcoords="offset points", xytext=(0, 7),
                     ha="center", fontsize=8, color=RED)
    ax2.annotate("7.5 GW", xy=(2, 7.5), textcoords="offset points", xytext=(-6, 7),
                 ha="right", fontsize=8, color=GREEN)
    ax2.set_ylim(0, 560)
    ax2.set_ylabel("GW")
    ax2.set_title("One grid's interconnection queue (ERCOT)", loc="left", pad=6)
    ax2.legend(loc="upper left")
    despine(ax2)
    ax2.grid(axis="x", alpha=0)
    fig.tight_layout(w_pad=2.4)
    save(fig, "energy-queue.svg")


# ============================================================ 7. claimed vs audited
def chart_claimed_vs_audited():
    print("7. claimed vs audited")
    # Deliberately NOT including ARC-AGI-3 here. ARC Prize publishes both its
    # Standard-harness result and the Provider Adapter result as verified scores
    # answering two different questions; neither is a claim that failed an audit.
    # That case is a harness-sensitivity story and has its own figure.
    rows = [
        ("A-Lab\nmaterials",            78, 5),
        ("SWE-bench Verified\nvs Pro",  77, 18),
        ("FeatureBench\nsame model",    74, 11),
    ]
    fig, ax = plt.subplots(figsize=(4.7, 3.2))
    x = np.arange(len(rows))
    w = 0.36
    claim = [r[1] for r in rows]
    audit = [r[2] for r in rows]
    b1 = ax.bar(x - w / 2, claim, w, color=FAINT, label="as announced")
    b2 = ax.bar(x + w / 2, audit, w, color=RED, label="under an independent test")
    for bars in (b1, b2):
        for b in bars:
            ax.annotate(f"{b.get_height():g}", (b.get_x() + b.get_width() / 2, b.get_height()),
                        ha="center", va="bottom", fontsize=7.5, color=INK)
    ax.set_xticks(x)
    ax.set_xticklabels([r[0] for r in rows], fontsize=7.2)
    ax.set_ylim(0, 132)
    ax.set_ylabel("percent")
    ax.set_title("Announced figure vs independent test", loc="left", pad=6)
    ax.legend(loc="upper left", fontsize=7.5)
    despine(ax)
    ax.grid(axis="x", alpha=0)
    save(fig, "claimed-vs-audited.svg")


# ============================================================ 7b. harness sensitivity
def chart_harness_effect():
    """ARC-AGI-3, GPT-6 Astra (Sep 2026).

    Both bars are ARC Prize *verified* scores, published side by side on the same
    results page. The point is not that one is fake: the benchmark organisation
    itself reports both, because they answer different questions — a neutral
    cross-provider interface versus the provider's own context management.
    Source: arcprize.org/results/openai-gpt-6-astra
    """
    print("7b. harness sensitivity (ARC-AGI-3)")
    fig, ax = plt.subplots(figsize=(4.7, 3.2))
    labels = ["Standard\nharness", "Provider Adapter\nharness"]
    vals = [62.71, 99.95]
    bars = ax.bar(labels, vals, color=[MUTED, BLUE], width=0.5)
    for b, v in zip(bars, vals):
        ax.annotate(f"{v:.1f}%", (b.get_x() + b.get_width() / 2, v), ha="center",
                    va="bottom", fontsize=10.5, color=INK)
    ax.annotate("", xy=(0.12, 68), xytext=(0.88, 96),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.6,
                                connectionstyle="arc3,rad=-0.25"))
    ax.annotate("37 points.\nSame model,\nsame week.", xy=(0.5, 76), ha="center",
                fontsize=8, color=RED, linespacing=1.3)
    ax.set_ylim(0, 122)
    ax.set_ylabel("ARC-AGI-3 Semi-Private (%)")
    ax.set_title("Two verified scores for one model", loc="left", pad=6)
    despine(ax)
    ax.grid(axis="x", alpha=0)
    save(fig, "harness-effect.svg")


# ============================================================ 8. paradigm timeline
def chart_paradigm_timeline():
    print("8. paradigm timeline")
    # (label, start, phase boundaries rise->rush->refine, end)
    P = [
        ("Prologue",      1943, 1943, 1956, 1966, 1969),
        ("Symbolic AI &\nExpert Systems", 1969, 1974, 1982, 1987, 1987),
        ("Backpropagation\n& Connectionism", 1986, 1989, 1992, 1995, 1995),
        ("Statistical\nLearning", 1995, 2000, 2006, 2012, 2012),
        ("Deep\nLearning", 2012, 2014, 2016, 2017, 2017),
        ("Transformers\n& Scale", 2017, 2020, 2023, 2026.7, 2026.7),
    ]
    fig, ax = plt.subplots(figsize=(9.0, 3.9))
    for i, (lab, s, a, b, c, e) in enumerate(P):
        y = len(P) - 1 - i
        ax.add_patch(Rectangle((s, y - 0.30), a - s, 0.60, color=BLUE, alpha=0.85, lw=0))
        ax.add_patch(Rectangle((a, y - 0.30), b - a, 0.60, color=BLUE, alpha=0.55, lw=0))
        ax.add_patch(Rectangle((b, y - 0.30), max(c, e) - b, 0.60, color=BLUE, alpha=0.26, lw=0))
        ax.text(s - 1.5, y, lab, ha="right", va="center", fontsize=7.6, color=INK, linespacing=1.15)

    ax.annotate("new idea", xy=(1980, 5.05), fontsize=7.5, color=BLUE, ha="center")
    ax.annotate("the rush", xy=(1990, 5.05), fontsize=7.5, color=BLUE, ha="center")
    ax.annotate("refinement", xy=(2004, 5.05), fontsize=7.5, color=MUTED, ha="center")

    for n, (yy, txt) in enumerate([(1969, "Perceptrons"), (1986, "backprop"), (1995, "SVM"),
                                    (2012, "AlexNet"), (2017, "Transformer"), (2022, "ChatGPT")]):
        ax.plot([yy], [-0.75], "|", ms=9, color=INK, mew=1.2)
        ax.annotate(txt, (yy, -0.95 if n % 2 == 0 else -1.42), rotation=0,
                    ha="center", va="top", fontsize=6.8, color=MUTED)

    ax.set_xlim(1928, 2030)
    ax.set_ylim(-1.9, 5.7)
    ax.axis("off")
    ax.annotate("Shading marks the three phases; where each phase starts is an interpretation, "
                "not a measurement",
                xy=(1928, 5.55), fontsize=7, color=MUTED)
    save(fig, "paradigm-timeline.svg")


def _lum(hexcol):
    h = hexcol.lstrip("#")
    ch = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    ch = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in ch]
    return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]


def report_contrast():
    """Guard the palette: the deck is presented dark, so every text colour must
    clear WCAG AA (4.5:1) against its own slide background. 'faint' is the
    recessive scatter colour — data marks, not text — so it only has to stay
    visible, not readable."""
    print("\ncontrast against slide background (WCAG AA text = 4.5:1)")
    for name, bg, keys in (("dark ", "#121212", ("INK", "MUTED", "FAINT", "GREEN", "ORANGE")),
                           ("light", "#ffffff", ("INK", "MUTED", "FAINT", "GREEN", "ORANGE"))):
        pal = DARK if name.strip() == "dark" else LIGHT
        row = []
        for k in keys:
            a, b = _lum(pal[k]), _lum(bg)
            r = (max(a, b) + 0.05) / (min(a, b) + 0.05)
            flag = "" if r >= 4.5 else ("  <- marks only" if k == "FAINT" else "  <- BELOW AA")
            row.append(f"{k.lower()} {r:.2f}{flag}")
        print(f"  {name}: " + " | ".join(row))


# ============================================================ 9. the paradigm cycle
def chart_paradigm_cycle():
    """A schematic, not a measurement.

    Makes the deck's spine visible: within one paradigm the structural returns
    fall off, and a new paradigm resets them. Deliberately drawn as an
    illustrative curve and labelled as such — there is no dataset behind the
    vertical axis, and pretending otherwise would be the exact sin the deck
    spends five slides warning about.
    """
    print("9. paradigm cycle (schematic)")
    P = [("Symbolic AI\n& Expert Systems", 1969, 5.5),
         ("Backpropagation\n& Connectionism", 1986, 4.0),
         ("Statistical\nLearning", 1995, 7.0),
         ("Deep\nLearning", 2012, 3.5),
         ("Transformers\n& Scale", 2017, 6.0)]

    fig, ax = plt.subplots(figsize=(9.0, 3.6))
    t = np.linspace(1940, 2032, 1400)
    env = np.zeros_like(t)
    for i, (label, start, tau) in enumerate(P):
        age = np.clip((t - start) / tau, 0, None)
        y = np.where(t >= start, age * np.exp(1 - age), 0.0)
        env = np.maximum(env, y)
        ax.plot(t, y, color=BLUE, lw=1.3, alpha=0.42 if i < len(P) - 1 else 0.85, zorder=3)
        ax.annotate(label, (start + tau, 1.0), textcoords="offset points",
                    xytext=(0, 7), ha="center", va="bottom", fontsize=7.2,
                    color=INK, linespacing=1.2, zorder=6)

    ax.plot(t, env, color=RED, lw=2.0, zorder=5)
    ax.annotate("structural progress per unit of effort", xy=(1943, 1.245),
                fontsize=8, color=MUTED)
    ax.annotate("each new paradigm resets it", xy=(1943, 1.135),
                fontsize=8, color=RED)
    ax.annotate("", xy=(2016.5, 1.02), xytext=(2004, 0.30),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.1,
                                connectionstyle="arc3,rad=0.22"), zorder=6)

    ax.set_xlim(1940, 2033)
    ax.set_ylim(0, 1.32)
    ax.set_yticks([])
    ax.set_xlabel("year")
    ax.set_title("One curve per paradigm: fast structural gains, then diminishing returns",
                 loc="left", pad=8)
    ax.grid(axis="y", alpha=0)
    despine(ax, keep=("bottom",))
    save(fig, "paradigm-cycle.svg")



# ============================================================ 10. ILSVRC trajectory
def chart_imagenet():
    """ILSVRC top-5 classification error, 2010-2017.

    Every figure below is the official competition TEST-set result from the
    image-net.org results pages, cross-checked against the winning papers. Two
    things the chart deliberately spells out because the usual retellings get
    them wrong: from 2012 onward the headline number is an ENSEMBLE, and the
    2016-2017 figures are the classification component of the LOC task (the
    standalone classification task had been folded in by then).
    """
    print("10. ImageNet trajectory")
    yrs = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
    err = [28.19, 25.77, 15.32, 11.74, 6.67, 3.57, 2.99, 2.25]
    who = ["NEC-UIUC", "XRCE", "AlexNet", "Clarifai", "GoogLeNet",
           "ResNet", "Trimps-Soushen", "WMW (SENet)"]

    fig, ax = plt.subplots(figsize=(9.0, 3.5))
    ax.axvspan(2009.6, 2012, color=MUTED, alpha=0.07, zorder=0)
    ax.annotate("hand-designed features", xy=(2010.8, 27.4), ha="center",
                fontsize=8, color=MUTED)
    ax.annotate("learned features", xy=(2014.9, 27.4), ha="center",
                fontsize=8, color=MUTED)

    ax.plot(yrs, err, "-", color=BLUE, lw=2.0, zorder=3)
    ax.scatter(yrs, err, s=44, c=BLUE, edgecolors=PANEL, linewidths=1.0, zorder=4)
    # 2012 sits right next to the 12% human line, so its label goes above the
    # point; everything else sits below
    for x, y, w in zip(yrs, err, who):
        dy = 10 if x == 2012 else -15
        ax.annotate(w, (x, y), textcoords="offset points", xytext=(0, dy),
                    ha="center", fontsize=8, color=INK, zorder=6)

    ax.axhline(5.1, color=GREEN, ls=(0, (5, 3)), lw=1.4, zorder=2)
    ax.annotate("trained human annotator, 5.1%", xy=(2010.1, 5.6), fontsize=7.6,
                color=GREEN, zorder=6)
    ax.axhline(12.0, color=GREEN, ls=(0, (2, 3)), lw=1.1, alpha=0.7, zorder=2)
    ax.annotate("less-trained annotator, 12.0%", xy=(2010.1, 12.5), fontsize=7.6,
                color=GREEN, zorder=6)

    ax.annotate("", xy=(2012.0, 16.4), xytext=(2014.5, 22.0),
                arrowprops=dict(arrowstyle="->", color=RED, lw=1.4,
                                connectionstyle="arc3,rad=0.25"), zorder=6)
    ax.annotate("the margin that started it", xy=(2014.6, 22.6), fontsize=8,
                color=RED, ha="center", zorder=6)

    ax.set_xlim(2009.6, 2017.7)
    ax.set_ylim(0, 30)
    ax.set_xticks(yrs)
    ax.set_ylabel("top-5 classification error (%)")
    ax.set_title("ILSVRC, official test-set results — ensembles from 2012 onward",
                 loc="left", pad=8)
    ax.grid(axis="x", alpha=0)
    despine(ax)
    save(fig, "imagenet-error.svg")
    print(f"     {yrs[0]}-{yrs[-1]}: {err[0]:.1f}% -> {err[-1]:.2f}%, "
          f"human expert {5.1}%")



# ============================================================ 11. XOR
def chart_xor():
    """XOR is not linearly separable, and one hidden layer fixes it.

    Nothing here is drawn by hand: panel A shows the best achievable linear
    boundary (which necessarily misclassifies one point), and panel B shows the
    actual decision regions of the two-hidden-unit solution
    h1 = OR, h2 = AND, out = h1 - 2*h2 - 0.5.
    """
    print("11. XOR")
    P = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([0, 1, 1, 0])

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.2))

    # --- panel A: the best a single hyperplane can do
    g = np.linspace(-0.45, 1.45, 260)
    X, Y = np.meshgrid(g, g)
    Z = X + Y - 1.0                     # the best linear separator for XOR
    a1.contourf(X, Y, Z, levels=[-9, 0, 9], colors=[BLUE, ORANGE], alpha=0.13)
    a1.contour(X, Y, Z, levels=[0], colors=[INK], linewidths=1.3, linestyles="--")
    for (px, py), lab in zip(P, y):
        col = BLUE if lab else ORANGE
        a1.scatter([px], [py], s=150, c=col, edgecolors=PANEL, linewidths=1.6, zorder=5)
        a1.annotate(str(lab), (px, py), ha="center", va="center", fontsize=9.5,
                    color=PANEL, zorder=6)
    a1.annotate("any straight line\ngets at least one wrong",
                xy=(0.5, 1.06), ha="center", fontsize=8, color=INK)
    a1.set_title("One hyperplane", loc="left", pad=6)

    # --- panel B: OR and AND, then their difference
    Z1 = (X + Y - 0.5 > 0).astype(float)
    Z2 = (X + Y - 1.5 > 0).astype(float)
    out = (Z1 - 2 * Z2 - 0.5 > 0).astype(float)
    a2.contourf(X, Y, out, levels=[-0.5, 0.5, 1.5], colors=[ORANGE, BLUE], alpha=0.13)
    a2.contour(X, Y, X + Y - 0.5, levels=[0], colors=[MUTED], linewidths=1.0)
    a2.contour(X, Y, X + Y - 1.5, levels=[0], colors=[MUTED], linewidths=1.0)
    for (px, py), lab in zip(P, y):
        col = BLUE if lab else ORANGE
        a2.scatter([px], [py], s=150, c=col, edgecolors=PANEL, linewidths=1.6, zorder=5)
        a2.annotate(str(lab), (px, py), ha="center", va="center", fontsize=9.5,
                    color=PANEL, zorder=6)
    a2.annotate("two hidden units carve\nthe right band",
                xy=(0.5, 1.06), ha="center", fontsize=8, color=INK)
    a2.set_title("Two hidden units, then a layer above them", loc="left", pad=6)

    for ax in (a1, a2):
        ax.set_xlim(-0.45, 1.45)
        ax.set_ylim(-0.45, 1.45)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_xlabel("input 1")
        despine(ax)
        ax.grid(alpha=0)
    a1.set_ylabel("input 2")
    fig.tight_layout(w_pad=2.0)
    save(fig, "xor.svg")


# ============================================================ 12. learning rate
def chart_learning_rate():
    """Real gradient descent on a non-convex 1-D loss, at three step sizes.

    The trajectories are computed, not sketched: too small crawls, the middle
    one settles into the nearer minimum, and the large one overshoots into the
    other basin and then diverges.
    """
    print("12. learning rate")

    def f(x):
        return 0.25 * x**4 - 0.5 * x**2 + 0.12 * x

    def df(x):
        return x**3 - x + 0.12

    rates = [(0.06, GREEN, "0.06  — too slow"),
             (0.35, BLUE, "0.35  — converges"),
             (1.05, RED, "1.05  — overshoots clear out")]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 3.2))
    xs = np.linspace(-1.9, 1.9, 600)
    a1.plot(xs, f(xs), color=MUTED, lw=1.4, zorder=2)

    for lr, col, label in rates:
        x, path = 1.72, [1.72]
        for _ in range(28):
            x = x - lr * df(x)
            path.append(x)
            if not np.isfinite(x) or abs(x) > 30:
                break
        p = np.array(path)
        inside = p[np.abs(p) <= 2.2]
        if len(inside) > 1:
            a1.plot(inside, f(inside), "o-", color=col, ms=3.6, lw=1.2,
                    alpha=0.9, zorder=4, label=label)
        if len(inside) < len(p):        # it left the frame — say so
            xe = inside[-1] if len(inside) else p[0]
            a1.annotate("leaves", (xe, f(xe)), textcoords="offset points",
                        xytext=(10, 6), fontsize=7.4, color=col,
                        arrowprops=dict(arrowstyle="->", color=col, lw=1.0), zorder=7)
        a2.semilogy(np.abs(np.array(path)) * 0 + np.maximum(np.abs(f(np.clip(p, -6, 6))), 1e-6),
                    "o-", color=col, ms=3.2, lw=1.2, zorder=4)

    a1.set_xlim(-2.2, 2.2)
    a1.set_xlabel("parameter value")
    a1.set_ylabel("loss")
    a1.set_title("Same loss, three step sizes", loc="left", pad=6)
    a1.legend(loc="lower right", fontsize=7.4)
    despine(a1)

    a2.set_xlabel("update step")
    a2.set_ylabel("loss (log)")
    a2.set_title("What the loss does", loc="left", pad=6)
    a2.set_ylim(1e-3, 1e5)
    despine(a2)
    fig.tight_layout(w_pad=2.2)
    save(fig, "learning-rate.svg")


# ============================================================ 13. bias-variance
def chart_bias_variance():
    """The classic U-curve, from an actual experiment.

    Fits polynomials of increasing degree to noisy samples of a fixed target
    function, repeated over many random draws, and plots the real training and
    test error. No hand-drawn curve.
    """
    print("13. bias-variance")
    rng = np.random.default_rng(7)

    def target(x):
        return np.sin(1.6 * np.pi * x)

    degrees = list(range(1, 13))
    n_train, trials = 20, 240
    train_err = np.zeros(len(degrees))
    test_err = np.zeros(len(degrees))
    xt = np.linspace(0.05, 0.95, 400)   # avoid the Runge edges dominating

    for i, deg in enumerate(degrees):
        tr, te = [], []
        for _ in range(trials):
            x = np.sort(rng.uniform(0, 1, n_train))
            y = target(x) + rng.normal(0, 0.30, n_train)
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")      # high-degree fits are ill-conditioned
                c = np.polyfit(x, y, deg)
            tr.append(np.mean((np.polyval(c, x) - y) ** 2))
            te.append(np.mean((np.polyval(c, xt) - target(xt)) ** 2))
        train_err[i] = np.median(tr)
        test_err[i] = np.median(te)

    fig, ax = plt.subplots(figsize=(6.2, 3.3))
    ax.plot(degrees, train_err, "o-", color=BLUE, ms=4, lw=1.6, label="training error")
    ax.plot(degrees, test_err, "o-", color=RED, ms=4, lw=1.6, label="test error")
    best = degrees[int(np.argmin(test_err))]
    ax.axvline(best, color=MUTED, ls=(0, (4, 3)), lw=1.1)
    ax.annotate(f"best generalisation\ndegree {best}", xy=(best + 0.35, max(test_err) * 0.82),
                fontsize=8, color=MUTED)
    ax.annotate("underfitting", xy=(1.4, max(test_err) * 0.93), fontsize=8.5, color=MUTED)
    ax.annotate("overfitting", xy=(12.2, max(test_err) * 0.93), fontsize=8.5,
                color=MUTED, ha="center")
    ax.set_xlabel("model flexibility (polynomial degree)")
    ax.set_ylabel("mean squared error")
    ax.set_ylim(0, max(test_err) * 1.08)
    ax.set_title(f"Fit {n_train} noisy points, {trials} draws — median error",
                 loc="left", pad=8)
    ax.legend(loc="upper center", fontsize=8.5)
    despine(ax)
    save(fig, "bias-variance.svg")
    print(f"     best degree {best}: train {train_err[best-1]:.3f} test {test_err[best-1]:.3f}; "
          f"deg {degrees[-1]}: train {train_err[-1]:.3f} test {test_err[-1]:.3f}")


# ============================================================ 14. scaling shapes
def chart_scaling_shapes():
    """The three scaling axes, drawn in their real functional forms.

    Not three copies of the same curve: pretraining is a power law in loss, RL
    post-training follows a sigmoid, and test-time accuracy saturates. The point
    of the figure is that only one of them is a straight line on a log axis.
    """
    print("14. scaling shapes")
    fig, axes = plt.subplots(1, 3, figsize=(9.0, 2.7))
    c = np.logspace(0, 4, 300)

    axes[0].loglog(c, 2.6 * c ** -0.34, color=BLUE, lw=2.0)
    axes[0].set_title("Pre-training", loc="left", pad=5)
    axes[0].set_xlabel("compute")
    axes[0].set_ylabel("loss")
    axes[0].annotate("power law:\na straight line here", xy=(30, 1.25), fontsize=7.6, color=MUTED)

    z = np.log10(c)
    sig = 1 / (1 + np.exp(-(z - 3.0) * 1.7))
    axes[1].semilogx(c, sig, color=GREEN, lw=2.0)
    axes[1].set_ylim(0, 1.12)
    axes[1].set_title("Post-training RL", loc="left", pad=5)
    axes[1].set_xlabel("compute")
    axes[1].set_ylabel("performance")
    axes[1].annotate("sigmoid:\nsaturates", xy=(1.4, 0.72), fontsize=7.6, color=MUTED)

    tt = 1 - np.exp(-c / 900)
    axes[2].semilogx(c, tt, color=ORANGE, lw=2.0)
    axes[2].set_ylim(0, 1.12)
    axes[2].set_title("Test-time compute", loc="left", pad=5)
    axes[2].set_xlabel("tokens spent thinking")
    axes[2].set_ylabel("accuracy")
    axes[2].annotate("a ceiling per problem", xy=(1.4, 0.30), fontsize=7.6, color=MUTED)

    for ax in axes:
        ax.grid(alpha=0.25)
        despine(ax)
    fig.tight_layout(w_pad=1.6)
    save(fig, "scaling-shapes.svg")


# ============================================================ 15. roofline
def chart_roofline():
    """The roofline for one H100, with the two operating points that matter.

    Numbers are the published H100 SXM figures: ~989 TFLOP/s dense BF16 and
    3.35 TB/s of HBM bandwidth, which puts the ridge at ~295 FLOP/byte.
    Arithmetic intensities are computed from the operation shapes, and the
    assumptions are printed by the script.
    """
    print("15. roofline")
    peak = 989e12          # FLOP/s, BF16 dense, H100 SXM
    bw = 3.35e12           # bytes/s, HBM3

    ai = np.logspace(-1, 4, 400)
    roof = np.minimum(peak, bw * ai)

    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    ax.loglog(ai, roof, color=INK, lw=2.0, zorder=3)
    ridge = peak / bw
    ax.axvline(ridge, color=MUTED, ls=(0, (4, 3)), lw=1.1)
    ax.annotate(f"ridge at {ridge:.0f} FLOP/byte", xy=(ridge * 1.08, 2e11),
                fontsize=8, color=MUTED)
    ax.axvspan(0.1, ridge, color=BLUE, alpha=0.07)
    ax.annotate("memory-bound — the hardware\nwaits on HBM, not on maths",
                xy=(0.12, 4.0e14), fontsize=8.5, color=BLUE)
    ax.annotate("compute-bound", xy=(ridge * 1.35, 2.2e12), fontsize=8.5, color=MUTED)

    def gemm(n, dtype_bytes=2):
        flops = 2 * n ** 3
        byts = 3 * n ** 2 * dtype_bytes
        return flops / byts

    def gemv(n, dtype_bytes=2):
        flops = 2 * n ** 2
        byts = n ** 2 * dtype_bytes + n * dtype_bytes
        return flops / byts

    pts = [(gemm(4096), "4096x4096 matmul", 0, 12),
           (60.0, "attention, long context", 0, -22),
           (gemv(4096), "one token, decoded", -4, -26)]
    for x, label, dx, dy in pts:
        y = min(peak, bw * x)
        ax.plot([x], [y], "o", ms=7, mfc=PANEL, mec=RED, mew=1.6, zorder=6)
        ax.annotate(f"{label}\n{x:.0f} FLOP/byte", (x, y), textcoords="offset points",
                    xytext=(dx, dy), ha="center", fontsize=7.6, color=RED, zorder=7)

    ax.set_xlim(0.1, 1e4)
    ax.set_ylim(1e11, 3e15)
    ax.set_xlabel("arithmetic intensity (FLOP per byte moved)")
    ax.set_ylabel("attainable FLOP/s")
    ax.set_title("Roofline for one H100 (dense BF16, 3.35 TB/s HBM)", loc="left", pad=8)
    despine(ax)
    save(fig, "roofline.svg")
    print(f"     ridge {ridge:.0f}; GEMM4096 {gemm(4096):.0f}; GEMV4096 {gemv(4096):.1f}")



# ============================================================ 16. Hopfield dynamics
def chart_hopfield():
    """A real Hopfield network, not a sketch of one.

    100 neurons, five stored patterns learned by the Hebbian rule, started from
    corrupted versions. Plotted per individual neuron update, because that is
    the granularity at which the energy guarantee actually holds: every single
    asynchronous update either lowers the energy or leaves it unchanged.
    """
    print("16. hopfield dynamics")
    rng = np.random.default_rng(11)
    N, P = 100, 5
    patterns = rng.choice([-1.0, 1.0], size=(P, N))
    W = patterns.T @ patterns / N
    np.fill_diagonal(W, 0.0)

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.2))
    for frac, col in ((0.10, GREEN), (0.25, BLUE), (0.40, ORANGE), (0.55, RED)):
        s = patterns[0].copy()
        s[rng.choice(N, size=int(frac * N), replace=False)] *= -1
        energies, overlaps = [], []
        for step in range(200):
            i = rng.integers(N)                         # one unit at a time
            h = W[i] @ s
            s[i] = 1.0 if h >= 0 else -1.0
            energies.append(-0.5 * s @ W @ s)
            overlaps.append(float(s @ patterns[0]) / N)
        a1.plot(energies, color=col, lw=1.5, label=f"{int(frac*100)}% corrupted")
        a2.plot(overlaps, color=col, lw=1.5)

    a1.set_xlabel("individual unit updates")
    a1.set_ylabel("energy")
    a1.set_title("Energy never goes up", loc="left", pad=6)
    a1.legend(loc="upper right", fontsize=7.6)
    despine(a1)

    a2.axhline(1.0, color=MUTED, ls=(0, (4, 3)), lw=1.0)
    a2.set_xlabel("individual unit updates")
    a2.set_ylabel("overlap with the stored pattern")
    a2.set_ylim(-0.15, 1.14)
    a2.set_title("The corrupted state falls into it", loc="left", pad=6)
    despine(a2)
    fig.tight_layout(w_pad=2.0)
    save(fig, "hopfield.svg")


# ============================================================ 17. attention paths
def chart_attention_paths():
    """Why path length matters. A schematic, and labelled as one.

    Left: in a recurrent net the signal between two distant positions travels
    through every position in between, so the gradient does too. Right: in
    self-attention every pair is one hop.
    """
    print("17. attention paths")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.6, 2.9))
    n = 9
    xs = np.arange(n)

    for ax in (a1, a2):
        ax.set_xlim(-0.8, n - 0.2)
        ax.set_ylim(-1.0, 2.4)
        ax.axis("off")

    for i in range(n):
        a1.plot([xs[i], xs[i] + 1], [0, 0], color=FAINT, lw=1.4, zorder=1) if i < n - 1 else None
    a1.scatter(xs, [0] * n, s=170, c=PANEL, edgecolors=MUTED, linewidths=1.4, zorder=3)
    for i in range(n - 1):
        a1.annotate("", xy=(xs[i + 1] - 0.22, 0), xytext=(xs[i] + 0.22, 0),
                    arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.2), zorder=2)
    a1.annotate("", xy=(xs[7], 0.42), xytext=(xs[1], 0.42),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.8,
                                connectionstyle="arc3,rad=-0.32"), zorder=4)
    a1.annotate("7 hops", xy=(4, 1.35), ha="center", fontsize=9, color=RED)
    a1.set_title("Recurrent: distance O(n)", loc="left", pad=4)

    a2.scatter(xs, [0] * n, s=170, c=PANEL, edgecolors=MUTED, linewidths=1.4, zorder=3)
    for i in range(n):
        for j in range(i + 1, n):
            hot = {i, j} == {1, 7}
            a2.plot([xs[i], xs[j]], [0, 0], color=RED if hot else FAINT,
                    lw=1.8 if hot else 0.7, zorder=2 if hot else 1)
    a2.annotate("1 hop, for every pair at once", xy=(4, 0.55), ha="center",
                fontsize=9, color=RED)
    a2.set_title("Self-attention: distance O(1)", loc="left", pad=4)

    fig.tight_layout(w_pad=1.6)
    save(fig, "attention-paths.svg")


# ============================================================ 18. education RCT
def chart_education_rct():
    """Bastani et al., PNAS 2025 — the same study, two tutor designs.

    Practice gains are large in both arms; the difference is what happens on the
    exam taken with no AI. Numbers are the paper's own effect sizes.
    """
    print("18. education RCT")
    labels = ["Plain\nGPT-4 tutor", "Guardrailed\ntutor (hints, not answers)"]
    practice = [48, 127]
    exam = [-17, 0]

    x = np.arange(len(labels))
    w = 0.36
    fig, ax = plt.subplots(figsize=(6.4, 3.3))
    b1 = ax.bar(x - w / 2, practice, w, color=BLUE, label="on practice problems")
    b2 = ax.bar(x + w / 2, exam, w, color=RED, label="on the exam, with no AI")
    for bars in (b1, b2):
        for b in bars:
            v = b.get_height()
            ax.annotate(f"{v:+d}%" if v else "0%", (b.get_x() + b.get_width() / 2, v),
                        ha="center", va="bottom" if v >= 0 else "top",
                        textcoords="offset points", xytext=(0, 4 if v >= 0 else -4),
                        fontsize=9, color=INK)
    ax.axhline(0, color=MUTED, lw=1.0)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.6)
    ax.set_ylim(-45, 155)
    ax.set_ylabel("effect on performance (%)")
    ax.set_title("Same model, two designs, opposite exam results", loc="left", pad=8)
    ax.legend(loc="upper left", fontsize=8.4)
    despine(ax)
    ax.grid(axis="x", alpha=0)
    save(fig, "education-rct.svg")


# ============================================================ 19. METR productivity
def chart_metr():
    """METR's 2025 randomised trial on experienced open-source developers.

    What they forecast, what the trial measured, and what they believed
    afterwards. All three figures are from the study.
    """
    print("19. METR productivity")
    labels = ["Forecast\nbefore starting", "Measured\nby the trial", "Believed\nafterwards"]
    vals = [24, -19, 20]
    cols = [MUTED, RED, MUTED]

    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    bars = ax.bar(labels, vals, color=cols, width=0.52)
    for b, v in zip(bars, vals):
        ax.annotate(f"{v:+d}%", (b.get_x() + b.get_width() / 2, v), ha="center",
                    va="bottom" if v >= 0 else "top", textcoords="offset points",
                    xytext=(0, 5 if v >= 0 else -5), fontsize=10.5, color=INK)
    ax.axhline(0, color=INK, lw=1.2)
    ax.set_ylim(-42, 42)
    ax.set_ylabel("change in completion time (%)")
    ax.set_title("Faster, or slower? METR's randomised trial", loc="left", pad=8)
    ax.annotate("slower, and they did not notice", xy=(1, -19),
                textcoords="offset points", xytext=(0, -38), ha="center",
                fontsize=8.4, color=RED)
    despine(ax)
    ax.grid(axis="x", alpha=0)
    save(fig, "metr-productivity.svg")



# ============================================================ 20. XCON rule growth
def chart_xcon():
    """How many rules an expert system needed, over time.

    Real figures from Bachant & McDermott, "R1 Revisited", AI Magazine 5(3),
    1984: the rule count tracked coverage almost linearly — which is the
    knowledge-acquisition bottleneck drawn as a curve. The dip in April 1980 is
    the rewrite onto OPS5, not a loss of coverage.
    """
    print("20. XCON rule growth")
    dates = ["Apr\n1979", "Oct\n1979", "Apr\n1980", "Dec\n1980", "Jul\n1982", "Nov\n1983"]
    rules = [250, 750, 500, 850, 2000, 3303]

    fig, ax = plt.subplots(figsize=(7.0, 3.2))
    x = np.arange(len(rules))
    ax.plot(x, rules, "-o", color=BLUE, lw=2.0, ms=6, mfc=PANEL,
            mec=BLUE, mew=1.6, zorder=4)
    ax.fill_between(x, rules, color=BLUE, alpha=0.10, zorder=2)
    for xi, yi in zip(x, rules):
        ax.annotate(f"{yi:,}", (xi, yi), textcoords="offset points",
                    xytext=(0, 9), ha="center", fontsize=8.2, color=INK)
    ax.annotate("rewritten onto OPS5;\ncoverage did not shrink",
                xy=(2, 560), xytext=(0.05, 2250), fontsize=7.6, color=MUTED,
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9,
                                connectionstyle="arc3,rad=-0.18"))
    ax.set_xticks(x)
    ax.set_xticklabels(dates, fontsize=8)
    ax.set_ylim(0, 3800)
    ax.set_ylabel("rules in the system")
    ax.set_title("XCON at DEC: rules had to grow with coverage", loc="left", pad=8)
    despine(ax)
    ax.grid(axis="x", alpha=0)
    save(fig, "xcon-rules.svg")





# ============================================================ 21. LeNet
def chart_lenet():
    """LeNet-5's pipeline, in the same visual language as the other figures.

    Shapes are from the 1998 paper. The boxes are outlined rather than filled
    so that colour carries meaning — convolutions, pooling, the classifier —
    without the diagram reading as a different kind of picture.
    """
    print("21. LeNet pipeline")
    layers = [
        ("input\n32x32", "one greyscale\ncheque digit", MUTED),
        ("C1: 6 maps\n28x28", "5x5 convolution\nedges", BLUE),
        ("S2: 6 maps\n14x14", "average pooling\ntolerance to shift", MUTED),
        ("C3: 16 maps\n10x10", "5x5 convolution\nstrokes, loops", BLUE),
        ("S4: 16 maps\n5x5", "average pooling", MUTED),
        ("C5: 120", "fully connected", BLUE),
        ("F6: 84", "fully connected", BLUE),
        ("output: 10", "one score per\ndigit 0-9", GREEN),
    ]
    fig, ax = plt.subplots(figsize=(9.0, 2.8))
    ax.set_xlim(-0.5, len(layers) - 0.5)
    ax.set_ylim(-0.30, 1.55)
    ax.axis("off")

    for i, (name, what, col) in enumerate(layers):
        ax.add_patch(Rectangle((i - 0.40, 0.62), 0.80, 0.44, facecolor=col,
                               alpha=0.10, edgecolor=col, linewidth=1.2, zorder=3))
        ax.text(i, 0.84, name, ha="center", va="center", fontsize=7.8,
                color=INK, zorder=4, linespacing=1.3)
        ax.text(i, 0.33, what, ha="center", va="center", fontsize=6.9,
                color=MUTED, zorder=4, linespacing=1.35)
        if i:
            ax.annotate("", xy=(i - 0.42, 0.84), xytext=(i - 0.58, 0.84),
                        arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9), zorder=2)

    ax.annotate("", xy=(3.0, -0.14), xytext=(1.0, -0.14),
                arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9))
    ax.text(2.0, -0.03, "each stage sees a slightly larger patch of the digit",
            ha="center", fontsize=7.4, color=MUTED)
    ax.text(-0.46, 1.42, "About 60,000 parameters in total. It read the courtesy "
            "amount field on cheques, in several US banks from 1996.",
            fontsize=7.8, color=MUTED)
    save(fig, "lenet.svg")



# ============================================================ 22. architecture trade-off
def chart_arch_params():
    """Parameters against error for the ILSVRC-era architectures.

    Replaces a six-column table with the one relationship worth seeing: VGG got
    a bit more accurate than GoogLeNet while using twenty times the parameters,
    and ResNet got much more accurate without getting bigger. All figures are
    the official ILSVRC test entries, which from 2012 on are ensembles.
    """
    print("22. architecture trade-off")
    # (model, year, params in millions, top-5 error, is_ensemble)
    A = [("AlexNet", 2012, 60, 15.32),
         ("VGG-19", 2014, 144, 7.32),
         ("GoogLeNet", 2014, 6.8, 6.66),
         ("ResNet-152", 2015, 60, 3.57)]

    fig, ax = plt.subplots(figsize=(7.4, 3.4))
    for name, yr, par, err in A:
        col = BLUE if name in ("GoogLeNet", "ResNet-152") else MUTED
        ax.scatter([par], [err], s=90, c=col, edgecolors=PANEL, linewidths=1.4, zorder=5)
        ax.annotate(f"{name}\n{yr}", (par, err), textcoords="offset points",
                    xytext=(0, -24), ha="center", fontsize=8, color=INK,
                    linespacing=1.3, zorder=6)

    ax.annotate("", xy=(6.8, 8.5), xytext=(144, 8.5),
                arrowprops=dict(arrowstyle="<->", color=RED, lw=1.3), zorder=4)
    ax.annotate("20x fewer parameters,\nslightly more accurate",
                xy=(31, 9.6), ha="center", fontsize=8, color=RED, linespacing=1.35, zorder=6)

    ax.set_xscale("log")
    ax.set_xlim(4, 260)
    ax.set_ylim(0, 19)
    ax.set_xticks([10, 30, 100])
    ax.set_xticklabels(["10M", "30M", "100M"])
    ax.set_xlabel("parameters")
    ax.set_ylabel("ImageNet top-5 error (%)")
    ax.set_title("Bigger was not the same as better", loc="left", pad=8)
    despine(ax)
    grid = ax.grid(axis="x", alpha=0)
    save(fig, "arch-params.svg")


# ============================================================ 23. training data growth
def chart_data_growth():
    """How much text the models were trained on, 2019 to 2024.

    The data thread of the deck, on its own. Six years, and the corpus grows by
    roughly three orders of magnitude — which is the other half of why the same
    architecture suddenly started working.
    """
    print("23. training data growth")
    D = [("GPT-2", 2019, 10e9, "WebText, ~40 GB"),
         ("GPT-3", 2020, 300e9, ""),
         ("Chinchilla", 2022, 1.4e12, ""),
         ("Llama 2", 2023, 2e12, ""),
         ("Llama 3", 2024, 15e12, "")]

    fig, ax = plt.subplots(figsize=(7.6, 3.3))
    yr = [d[1] for d in D]
    tk = [d[2] for d in D]
    ax.semilogy(yr, tk, "-o", color=GREEN, lw=2.0, ms=7, mfc=PANEL, mec=GREEN, mew=1.6, zorder=4)
    ax.fill_between(yr, tk, 1e9, color=GREEN, alpha=0.08, zorder=2)
    for name, y, t, note in D:
        lab = f"{name}\n{t/1e9:,.0f}B" + (f"\n{note}" if note else "")
        ax.annotate(lab, (y, t), textcoords="offset points",
                    xytext=(0, 12 if name != "Llama 2" else -34), ha="center",
                    fontsize=7.8, color=INK, linespacing=1.3, zorder=6)
    ax.set_xticks(yr)
    ax.set_ylim(2e9, 2e14)
    ax.set_ylabel("training tokens")
    ax.set_title("Training text grew about a thousandfold in five years", loc="left", pad=8)
    despine(ax)
    ax.grid(axis="x", alpha=0)
    save(fig, "data-growth.svg")



CHARTS = [
    chart_compute_vs_moore,
    chart_params_capability,
    chart_saturation,
    chart_chinchilla,
    chart_price_performance,
    chart_energy,
    chart_claimed_vs_audited,
    chart_harness_effect,
    chart_paradigm_timeline,
    chart_paradigm_cycle,
    chart_imagenet,
    chart_xor,
    chart_learning_rate,
    chart_bias_variance,
    chart_scaling_shapes,
    chart_roofline,
    chart_hopfield,
    chart_attention_paths,
    chart_education_rct,
    chart_metr,
    chart_xcon,
    chart_lenet,
    chart_arch_params,
    chart_data_growth,
]

if __name__ == "__main__":
    for theme in (LIGHT, DARK):
        name = "dark" if theme["SUFFIX"] else "light"
        print(f"generating charts ({name} theme) ...")
        apply_theme(theme)
        for fn in CHARTS:
            fn()
    report_contrast()
    print("done.")
