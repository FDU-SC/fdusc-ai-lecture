#!/usr/bin/env python3
import sys, glob, os, xml.etree.ElementTree as ET
NS = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
maxsum = int(os.environ.get('MAXSUM', '420'))
files = sys.argv[1:] or sorted(glob.glob('q/*.xml'))
for f in files:
    try:
        root = ET.parse(f).getroot()
    except Exception as e:
        print(f'## {f}: PARSE ERR {e}'); continue
    ents = root.findall('a:entry', NS)
    print(f'\n## {os.path.basename(f)}  n={len(ents)}')
    for e in ents:
        aid = e.find('a:id', NS).text.split('/abs/')[-1]
        ti = ' '.join(e.find('a:title', NS).text.split())
        pub = e.find('a:published', NS).text[:10]
        summ = ' '.join(e.find('a:summary', NS).text.split())
        jr = e.find('arxiv:journal_ref', NS)
        doi = e.find('arxiv:doi', NS)
        extra = ''
        if jr is not None: extra += f' | J:{jr.text}'
        if doi is not None: extra += f' | DOI:{doi.text}'
        print(f'{pub} {aid}{extra}\n  {ti}\n  {summ[:maxsum]}')
