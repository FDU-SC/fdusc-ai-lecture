import sys, urllib.parse, urllib.request, xml.etree.ElementTree as ET, datetime, json

NS={'a':'http://www.w3.org/2005/Atom','arxiv':'http://arxiv.org/schemas/atom'}
def q(search, n=40, sort='submittedDate'):
    url='https://export.arxiv.org/api/query?search_query='+urllib.parse.quote(search,safe='')+f'&max_results={n}&sortBy={sort}&sortOrder=descending'
    for attempt in range(4):
        try:
            req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 (research; contact: local)'})
            d=urllib.request.urlopen(req, timeout=60).read()
            break
        except Exception as e:
            import time
            print('retry', attempt, e, file=sys.stderr); time.sleep(6*(attempt+1))
            if attempt==3: raise
    r=ET.fromstring(d)
    out=[]
    tot=r.find('opensearch:totalResults',{'opensearch':'http://a9.com/-/spec/opensearch/1.1/'})
    for e in r.findall('a:entry',NS):
        pub=e.find('a:published',NS).text[:10]
        t=' '.join(e.find('a:title',NS).text.split())
        idu=e.find('a:id',NS).text
        jr=e.find('arxiv:journal_ref',NS)
        doi=e.find('arxiv:doi',NS)
        out.append((pub,t,idu,jr.text if jr is not None else '',doi.text if doi is not None else ''))
    return (tot.text if tot is not None else '?'), out

if __name__=='__main__':
    search=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 40
    tot,rows=q(search,n)
    print(f"### {search}  (total={tot})")
    for pub,t,idu,jr,doi in rows:
        print(f"{pub} | {t} | {idu} | {jr} | {doi}")
