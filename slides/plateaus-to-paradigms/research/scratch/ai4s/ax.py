#!/usr/bin/env python3
"""Fetch arXiv API query, print compact records."""
import sys, urllib.parse, subprocess, re, xml.etree.ElementTree as ET

NS = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}

def fetch(query, max_results=30, start=0, date=None):
    q = query
    if date:
        q = f'({query})+AND+submittedDate:%5B{date}+TO+202609170000%5D'
    url = (f'https://export.arxiv.org/api/query?search_query={q}'
           f'&start={start}&max_results={max_results}'
           f'&sortBy=submittedDate&sortOrder=descending')
    out = subprocess.run(['curl', '-sS', '--http1.1', '-m', '60', url],
                         capture_output=True, text=True)
    return out.stdout, url

def show(xml, full=False, maxsum=900):
    try:
        root = ET.fromstring(xml)
    except Exception as e:
        print('PARSE ERR', e, xml[:300]); return 0
    tot = root.find('opensearch:totalResults', {'opensearch': 'http://a9.com/-/spec/opensearch/1.1/'})
    print(f'### totalResults={tot.text if tot is not None else "?"}')
    n = 0
    for e in root.findall('a:entry', NS):
        n += 1
        aid = e.find('a:id', NS).text
        ti = ' '.join(e.find('a:title', NS).text.split())
        pub = e.find('a:published', NS).text[:10]
        upd = e.find('a:updated', NS).text[:10]
        summ = ' '.join(e.find('a:summary', NS).text.split())
        jr = e.find('arxiv:journal_ref', NS)
        doi = e.find('arxiv:doi', NS)
        com = e.find('arxiv:comment', NS)
        print(f'[{n}] {pub} (upd {upd}) {aid}')
        print(f'    T: {ti}')
        if jr is not None: print(f'    J: {jr.text}')
        if doi is not None: print(f'    DOI: {doi.text}')
        if com is not None: print(f'    C: {" ".join(com.text.split())[:200]}')
        print(f'    S: {summ[:maxsum]}')
    return n

if __name__ == '__main__':
    q = sys.argv[1]
    mr = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    date = sys.argv[3] if len(sys.argv) > 3 else None
    full = len(sys.argv) > 4
    xml, url = fetch(q, mr, date=date)
    print('URL:', url)
    show(xml, full=full)
