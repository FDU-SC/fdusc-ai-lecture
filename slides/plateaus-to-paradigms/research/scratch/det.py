import sys, json, urllib.parse, urllib.request, time
def rec(query, size=1, alen=1200):
    url='https://inspirehep.net/api/literature?'+urllib.parse.urlencode({'q':query,'size':size,'sort':'mostrecent','fields':'titles,abstracts,publication_info,arxiv_eprints,dois,earliest_date,preprint_date,report_numbers,collaborations,urls,imprints,document_type,number_of_pages'})
    req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
    for a in range(3):
        try: d=json.load(urllib.request.urlopen(req,timeout=60)); break
        except Exception as e: print('retry',e,file=sys.stderr); time.sleep(4)
    else: return
    if not d['hits']['hits']: print('NO HITS:',query); return
    for h in d['hits']['hits']:
        m=h['metadata']
        print('='*100)
        print('TITLE:', ' '.join(m.get('titles',[{}])[0].get('title','').split()))
        print('DATE:', m.get('earliest_date'), '| preprint:', m.get('preprint_date'))
        print('ARXIV:', (m.get('arxiv_eprints') or [{}])[0].get('value',''))
        print('DOI:', '; '.join(x.get('value','') for x in m.get('dois',[])))
        print('PUB:', json.dumps(m.get('publication_info',[]))[:400])
        print('REPORT:', ','.join(x.get('value','') for x in m.get('report_numbers',[])))
        print('COLLAB:', ','.join(x.get('value','') for x in m.get('collaborations',[])))
        ab=(m.get('abstracts') or [{}])[0].get('value','')
        print('ABSTRACT:', ' '.join(ab.split())[:alen])
if __name__=='__main__':
    for a in sys.argv[1:]:
        rec(a); time.sleep(1.5)
