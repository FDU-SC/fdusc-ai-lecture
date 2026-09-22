import sys, json, urllib.parse, urllib.request, time
def q(query, size=25, sort='mostrecent', fields='titles,publication_info,arxiv_eprints,dois,earliest_date,preprint_date,report_numbers,collaborations'):
    url='https://inspirehep.net/api/literature?'+urllib.parse.urlencode({'q':query,'size':size,'sort':sort,'fields':fields})
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    for a in range(3):
        try:
            d=json.load(urllib.request.urlopen(req,timeout=60)); break
        except Exception as e:
            print('retry',e,file=sys.stderr); time.sleep(4)
    else: raise SystemExit(1)
    print(f"### {query}  (hits={d['hits']['total']})")
    for h in d['hits']['hits']:
        m=h['metadata']
        ti=' '.join(m.get('titles',[{}])[0].get('title','').split())
        dt=(m.get('earliest_date') or m.get('preprint_date') or '?')
        ep=m.get('arxiv_eprints',[{}])[0].get('value','')
        doi=m.get('dois',[{}])[0].get('value','') if m.get('dois') else ''
        pi=m.get('publication_info',[{}])[0]
        jr=' '.join(str(pi.get(k,'')) for k in ('journal_title','journal_volume','artid','page_start','year')).strip()
        rn=','.join(r.get('value','') for r in m.get('report_numbers',[]))
        coll=','.join(c.get('value','') for c in m.get('collaborations',[]))
        print(f"{dt} | {ti} | arXiv:{ep} | DOI:{doi} | {jr} | {rn} | {coll}")
if __name__=='__main__':
    q(sys.argv[1], int(sys.argv[2]) if len(sys.argv)>2 else 25)
