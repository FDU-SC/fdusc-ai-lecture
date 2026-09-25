# Artificial Analysis model leaderboard — capture notes

Companion to `research/data/aa-models.json`.

## Capture summary

- **Date/time of capture:** 2026-09-19, 02:01–02:03 CST (UTC+8) = 2026-09-18T18:01–18:03Z.
- **Models captured:** **652** (complete leaderboard; one JSON object per model, `slug` unique).
- **Release-date range (all 652):** `2022-11-30` → `2026-09-11` (all 652 rows have a release date).
- **Field coverage across the 652 rows:**

  | field | non-null rows |
  |---|---|
  | `name`, `slug`, `org`, `release_date`, `open_weights`, `is_reasoning`, `context_window_tokens`, `deprecated` | 652 |
  | `intelligence_index` | 643 |
  | `price_input` / `price_output` / `blended_price` | 436 |
  | `intelligence_index` **and** a price (plottable) | 434 |
  | `cache_hit_price` | 247 |
  | `output_tokens_per_task` | 156 |
  | `cost_per_task` | 146 |
  | `openness` (AA Openness Index) | 322 |
  | `parameters_billions` / `license_name` | 383 / 367 |

- **Distinct labs (`org`):** 59.

### Important: the 161-model "ranked" subset

AA's own FAQ on the same page says *"…out of **161** models ranked"*, *"**80** open weights models out of 161"*, *"leads among **141** reasoning models"*.

The `intelligenceIndexIsEstimated` flag partitions the list exactly:

| subset | models |
|---|---|
| `intelligence_index` present, `intelligence_index_is_estimated == false` — the **current Intelligence Index v4.3 ranked set** | **161** |
| `intelligence_index` present but estimated (back-filled / legacy Index versions) | 482 |
| no intelligence index at all | 9 |

Of the 161 ranked models, **80** are open weights and **141** are reasoning — matching AA's FAQ numbers exactly, which is the main correctness check on this capture.

- **155 of the 161 ranked models have prices** → this is the cleanest set for a price-vs-intelligence curve.
- Ranked-subset release range: `2024-12-26` → `2026-09-11`.

> For an accurate price-vs-intelligence chart, filter on
> `intelligence_index_is_estimated === false` (161 rows, 155 with prices).
> The other 482 estimated scores are not on the same Index version and are not
> directly comparable. The full 652 rows are included so nothing is hidden.

## URL(s) and technique that produced the data

The documented API (`https://artificialanalysis.ai/api/v2/data/llms/models`) is
closed — it returns `{"error":"API key is required"}` (re-confirmed; see
`research/scratch/raw/aa_api.json`). The data was taken from the **React Server
Component (RSC) flight payload**, which is the authoritative first-party source.

Two fetches were used, and they agree exactly:

1. **Primary (richest):** `https://artificialanalysis.ai/models/gemini-3-5-flash-lite`
   with the header `RSC: 1` (plus a browser `User-Agent` and `--compressed`).
   Returning the flight payload directly instead of the full HTML shrinks the
   response from 3.6 MB to ~0.4 MB. This payload embeds the **entire 652-model
   leaderboard with the full 75-field per-model schema** — intelligence index,
   all price fields including the blended variants, release date, creator,
   open-weights/reasoning flags, per-task token counts and per-task costs.
   Saved as `research/scratch/aa/aa_model_page_gemini-3-5-flash-lite.rsc.txt`.
2. **Cross-check:** `https://artificialanalysis.ai/leaderboards/models` with
   `RSC: 1` (the URL named in the task). Saved as
   `research/scratch/aa/aa_leaderboards_models.rsc.txt`.

**Cross-validation result:** both payloads contain a 652-element `models` array;
the slug sets are identical and **0 field mismatches** were found across
`intelligenceIndex`, `price1mInputTokens`, `price1mOutputTokens`, `isReasoning`
and `isOpenWeights`.

Parsing: concatenate the `self.__next_f.push([1,"…"])` chunks (for HTML) or read the
flight body (for the `RSC: 1` response), locate `"models":[`, and bracket-match the
array. The model-page array contains 651 objects plus **one Next.js string
reference** (`$e:…:currentModel`); that reference is the page's own model
(`gemini-3-5-flash-lite`), recovered from the `"currentModel":{…}` object, giving
the full 652. Scripts: `research/scratch/aa/parse_rsc.py`,
`research/scratch/aa/build.py`.

A headless browser was **not** needed — the full table is in the server payload.

### Failed / inconclusive attempts (recorded as requested)

- `RSC: 1` against `/models/gemini-3-5-flash-lite` **without** `?_rsc=` first hung
  and timed out at 60 s once, then succeeded on retry with the same headers. No
  data loss — the successful response is what was used.
- `/data/<hash>.txt` manifests referenced by the page (e.g.
  `/data/f5cc7a899f267e0b.txt`) are **encrypted binary**, not JSON, and were not used.
- No `/api/...` route is referenced anywhere in the leaderboard payload.
- A stale CDN-cached copy of `/leaderboards/models` (plain HTML, no `RSC` header)
  listed four MBZUAI models under old slugs (`k2-1b-final`, `k2-4b-ph1`,
  `k2-7b-ph2`, `k2-mova-36b-mid5`) and the creator as "MBZUAI Institute of
  Foundation Models". The fresh `RSC: 1` leaderboard payload and the model page
  both use the current slugs (`k2-horizon-0-9b`, `k2-horizon-3-7b`, `k2-horizon-7b`,
  `k2-horizon-mova-36b-a4b`) and creator "Institute of Foundation Models". This is
  the same four models relabelled — net model count is unchanged at 652. The
  **fresh snapshot was used**; the stale variant was not mixed in.

## Field mapping (what AA calls each column)

| our field | AA field (in the `models` payload) | notes |
|---|---|---|
| `name` | `name` | AA leaderboard display name, e.g. `Claude Fable 5.1 (Adaptive Reasoning, Max Effort, Default Fallback)` |
| `slug` | `slug` | AA's model slug |
| `short_name` | `shortName` | shorter label AA uses in charts |
| `org` | `creator.name` | verbatim AA creator name (`creator.slug` / `creator.id` also kept) |
| `release_date` | `releaseDate` | ISO `YYYY-MM-DD` |
| `release_family` | `release.name` (`release.slug` → `release_slug`) | base model family behind an effort/reasoning variant |
| `effort` | `effort.label` | reasoning effort variant (`max`, `high`, …) where applicable |
| `intelligence_index` | `intelligenceIndex` | Artificial Analysis Intelligence Index (v4.3 for the 161 ranked rows) |
| `intelligence_index_is_estimated` | `intelligenceIndexIsEstimated` | **filter on `false` for the comparable ranked set** |
| `price_input` | `price1mInputTokens` | USD per 1M input tokens |
| `price_output` | `price1mOutputTokens` | USD per 1M output tokens |
| `blended_price` | `price1mBlended7To2To1` | see below |
| `cache_hit_price` / `cache_write_price` | `cacheHitPrice` / `cacheWritePrice` | USD per 1M tokens |
| `open_weights` | `isOpenWeights` | boolean |
| `is_reasoning` | `isReasoning` | boolean |
| `cost_per_task` | `intelligenceIndexCostPerTask.cost.total` | USD, weighted average per Intelligence Index task; full breakdown kept in `cost_per_task_breakdown` |
| `output_tokens_per_task` | `intelligenceIndexOutputTokensPerTask.output` | weighted-average output tokens per Index task (= `reasoning` + `answer`, both also kept) |
| `intelligence_index_time_per_task` | `intelligenceIndexTimePerTask` | seconds |
| `context_window_tokens` | `contextWindowTokens` | |
| `openness` | `openness` | AA Openness Index, 0–100 |
| `parameters_billions` / `active_parameters_billions` | `parameters` / `inferenceParametersActiveBillions` | open-weights models only |
| `license_name` | `licenseName` | |
| `deprecated` | `deprecated` | 381 of 652 rows are flagged deprecated |

### Which price blend AA displays

**AA's displayed "blended" price is a 7:2:1 cache-hit : input : output ratio** —
that is the field `price1mBlended7To2To1`, and it is what `blended_price` holds.

This is stated verbatim on AA's own model page:

> "Gemini 3.5 Flash-Lite costs $0.30 per 1M input tokens and $2.50 per 1M output
> tokens (based on Google's API). For a **blended rate (7:2:1 cache
> hit/input/output ratio)**, this is $0.33 per 1M tokens."
> — `https://artificialanalysis.ai/models/gemini-3-5-flash-lite`
> (saved in `research/scratch/aa/evidence_blend.txt`)

Verified numerically: `(7×0.03 + 2×0.30 + 1×2.50) / 10 = 0.331` = AA's own
`price1mBlended7To2To1` for that model. AA also publishes four other ratios, all
kept in the JSON for completeness:

| our field | AA field | ratio (cache:input:output) |
|---|---|---|
| `blended_price` | `price1mBlended7To2To1` | **7:2:1 — the one AA displays** |
| `blended_price_0_3_1` | `price1mBlended0To3To1` | 0:3:1 (classic 3:1 input:output, no cache) |
| `blended_price_1_1` | `price1mBlended0To1To1` | 0:1:1 |
| `blended_price_100_1_1` | `price1mBlended100To1To1` | 100:1:1 |
| `blended_price_0_100_1` | `price1mBlended0To100To1` | 0:100:1 |

`blended_price` is AA's own published value, **not** recomputed here.

**Cache-price fallback (verified):** for the 189 models that have input/output
prices but no `cacheHitPrice`, AA substitutes the **input price** for the cache-hit
term in the blend, i.e. `(7×input + 2×input + 1×output) / 10`. Spot-checked on
`quasar-438b`, `gpt-5-1-codex`, `qwen3-5-27b` and `grok-4` — all match exactly.
(For the 247 models that do have a cache-hit price, that price is used instead.)

## What could NOT be obtained, and rows dropped

**Nothing was dropped** — all 652 leaderboard rows are present. Nulls mark
genuinely unpublished values; nothing was guessed, interpolated or filled in.

Could not obtain:

- **`median_tokens_per_task`** — AA does not publish a *median* tokens-per-task
  figure. It publishes a **weighted-average** output tokens per Intelligence Index
  task, which is recorded as `output_tokens_per_task` (with `reasoning_tokens_per_task`
  and `answer_tokens_per_task`). `median_tokens_per_task` is therefore `null` on
  every row rather than being mislabelled. `cost_per_task` is available for 146 rows.
- **Prices for 216 of 652 models** — AA does not carry an API price for them
  (mostly deprecated, research, or self-host-only open-weights releases). These are
  left `null`.
- **Intelligence Index for 9 models** — `null`.
- **Per-task cost/token data** — limited to models AA has run the full Index
  evaluation on: 146 have `cost_per_task`, 156 have `output_tokens_per_task`
  (out of 161 ranked).
- **Index version per row** — the payload does not expose an explicit Index version
  string. The `intelligence_index_is_estimated` flag plus the 161/80/141 reconciliation
  against AA's FAQ is the available proxy; the 482 estimated rows mix older Index
  versions and should not be plotted on the same axis without care.
- **`org` is AA's creator name verbatim.** AA labels some labs differently from the
  names in the brief — e.g. xAI appears as **`SpaceXAI`**, Zhipu as **`Z AI`**,
  Moonshot as **`Kimi`**. These were **not** normalised, to avoid inventing a mapping.

## Provenance / scratch files

- `research/scratch/aa/aa_model_page_gemini-3-5-flash-lite.rsc.txt` — raw primary payload.
- `research/scratch/aa/aa_leaderboards_models.rsc.txt` — raw cross-check payload.
- `research/scratch/aa/models_full_652.json` — extracted 651-object array (pre-reference-resolution).
- `research/scratch/aa/current_model.json` — the 652nd model recovered from `currentModel`.
- `research/scratch/aa/evidence_blend.txt` — the 7:2:1 blend quote.
- `research/scratch/aa/aa_leaderboard_faq.json` — AA FAQ Q/A used as the reconciliation check.
- `research/scratch/aa/parse_rsc.py`, `research/scratch/aa/build.py` — extraction and build scripts.
