import json, sys, datetime
sys.path.insert(0,'/home/zecyel/slides/ch1/research/scratch/aa')
from parse_rsc import find_arrays

S='/home/zecyel/slides/ch1/research/scratch/aa/'
# 1) rich per-model detail from the model page RSC (652 models, 75+ fields incl. blends)
fl_model=open('/tmp/m_rsc3.txt',encoding='utf-8',errors='replace').read()
arr=[a for p,a in find_arrays(fl_model,'models') if a and len(a)==652 and isinstance(a[0],dict) and len(a[0])>20][0]
detail={}
for m in arr:
    if isinstance(m,dict): detail[m['slug']]=m
cm=json.load(open(S+'current_model.json'))
detail[cm['slug']]=cm
print("detail models:", len(detail))

# 2) fresh leaderboard RSC (652) for cross-validation
fl_lb=open('/tmp/lb_rsc.txt',encoding='utf-8',errors='replace').read()
lbar=[a for p,a in find_arrays(fl_lb,'models') if a and len(a)==652 and isinstance(a[0],dict) and len(a[0])>20][0]
lb={m['slug']:m for m in lbar}
print("leaderboard models:", len(lb))

# cross-check shared slugs
shared=set(detail)&set(lb)
print("shared slugs:", len(shared))
mism=0
for s in shared:
    a,b=detail[s],lb[s]
    for f in ['intelligenceIndex','price1mInputTokens','price1mOutputTokens','isReasoning','isOpenWeights']:
        if a.get(f)!=b.get(f):
            mism+=1
            if mism<=5: print("  MISMATCH", s, f, a.get(f), b.get(f))
print("field mismatches:", mism)
print("detail-only:", sorted(set(detail)-set(lb)))
print("lb-only:", sorted(set(lb)-set(detail)))

def g(m,k): return m.get(k)

def cost_total(m):
    c=m.get('intelligenceIndexCostPerTask')
    if isinstance(c,dict) and isinstance(c.get('cost'),dict): return c['cost'].get('total')
    return None
def cost_parts(m):
    c=m.get('intelligenceIndexCostPerTask')
    if isinstance(c,dict) and isinstance(c.get('cost'),dict):
        return {f: c['cost'].get(f) for f in ['total','input','nonCacheInput','cacheRead','cacheWrite','output','reasoning','answer']}
    return None
def tok(m):
    t=m.get('intelligenceIndexOutputTokensPerTask')
    if isinstance(t,dict): return t
    return None

rows=[]
for s in sorted(detail):
    m=detail[s]; cr=m.get('creator') or {}
    t=tok(m) or {}
    rows.append({
        "name": m.get('name'),
        "slug": m.get('slug'),
        "short_name": m.get('shortName'),
        "org": cr.get('name'),
        "creator_slug": cr.get('slug'),
        "creator_id": cr.get('id'),
        "release_date": m.get('releaseDate'),
        "release_family": (m.get('release') or {}).get('name') if isinstance(m.get('release'),dict) else None,
        "effort": (m.get('effort') or {}).get('label') if isinstance(m.get('effort'),dict) else None,
        "intelligence_index": m.get('intelligenceIndex'),
        "intelligence_index_is_estimated": m.get('intelligenceIndexIsEstimated'),
        "price_input": m.get('price1mInputTokens'),
        "price_output": m.get('price1mOutputTokens'),
        "blended_price": m.get('price1mBlended7To2To1'),
        "blended_price_0_3_1": m.get('price1mBlended0To3To1'),
        "blended_price_1_1": m.get('price1mBlended0To1To1'),
        "blended_price_100_1_1": m.get('price1mBlended100To1To1'),
        "blended_price_0_100_1": m.get('price1mBlended0To100To1'),
        "cache_hit_price": m.get('cacheHitPrice'),
        "cache_write_price": m.get('cacheWritePrice'),
        "open_weights": m.get('isOpenWeights'),
        "is_reasoning": m.get('isReasoning'),
        "median_tokens_per_task": None,
        "output_tokens_per_task": t.get('output'),
        "reasoning_tokens_per_task": t.get('reasoning'),
        "answer_tokens_per_task": t.get('answer'),
        "cost_per_task": cost_total(m),
        "cost_per_task_breakdown": cost_parts(m),
        "intelligence_index_time_per_task": m.get('intelligenceIndexTimePerTask'),
        "context_window_tokens": m.get('contextWindowTokens'),
        "parameters_billions": m.get('parameters'),
        "active_parameters_billions": m.get('inferenceParametersActiveBillions'),
        "license_name": m.get('licenseName'),
        "openness": m.get('openness'),
        "deprecated": m.get('deprecated'),
        "release_slug": (m.get('release') or {}).get('slug') if isinstance(m.get('release'),dict) else None,
    })

rows.sort(key=lambda r: (r['intelligence_index'] is None, -(r['intelligence_index'] or 0), r['name'] or ''))
json.dump(rows, open('/home/zecyel/slides/ch1/research/data/aa-models.json','w'), indent=1)
print("WROTE rows:", len(rows))
