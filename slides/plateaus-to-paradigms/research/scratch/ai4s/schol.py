#!/usr/bin/env python3
"""Search OpenAlex and Crossref, print compact results."""
import sys, json, subprocess, urllib.parse

def curl(url):
    r = subprocess.run(['curl','-sS','--http1.1','-m','45','-L',url], capture_output=True, text=True)
    return r.stdout

def oa(q, per=15, filt=None, sort=None):
    url = f'https://api.openalex.org/works?search={urllib.parse.quote(q)}&per-page={per}&mailto=research@example.org'
    if filt: url += f'&filter={filt}'
    if sort: url += f'&sort={sort}'
    try:
        d = json.loads(curl(url))
    except Exception as e:
        print('ERR', e); return
    print(f'### OpenAlex "{q}" count={d.get("meta",{}).get("count")}')
    for w in d.get('results', []):
        date = w.get('publication_date','?')
        ti = w.get('title','?')
        doi = (w.get('doi') or '').replace('https://doi.org/','')
        host = ((w.get('primary_location') or {}).get('source') or {}).get('display_name') or '?'
        cid = w.get('cited_by_count', 0)
        print(f'{date} | {host} | DOI:{doi} | cites={cid}\n    {ti}')

def cr(q, rows=15, extra=''):
    url = f'https://api.crossref.org/works?query.bibliographic={urllib.parse.quote(q)}&rows={rows}&select=DOI,title,container-title,issued,is-referenced-by-count,type&mailto=research@example.org'
    if extra: url += extra
    try:
        d = json.loads(curl(url))
    except Exception as e:
        print('ERR', e); return
    print(f'### Crossref "{q}" total={d["message"]["total-results"]}')
    for it in d['message']['items']:
        dt = it.get('issued',{}).get('date-parts',[['?']])[0]
        dt = '-'.join(str(x) for x in dt)
        ti = (it.get('title') or ['?'])[0]
        ct = (it.get('container-title') or ['?'])[0]
        print(f'{dt} | {ct} | DOI:{it["DOI"]} | cites={it.get("is-referenced-by-count",0)}\n    {ti}')

if __name__ == '__main__':
    mode = sys.argv[1]; q = sys.argv[2]
    n = int(sys.argv[3]) if len(sys.argv)>3 else 15
    if mode == 'oa': oa(q, n)
    elif mode == 'cr': cr(q, n)
