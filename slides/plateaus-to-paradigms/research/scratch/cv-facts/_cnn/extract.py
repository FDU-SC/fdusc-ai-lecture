import re, sys, html
p = sys.argv[1]
h = open(p, encoding='utf-8', errors='replace').read()
h = re.sub(r'(?is)<(script|style|svg|head)[^>]*>.*?</\1>', ' ', h)
h = re.sub(r'(?i)<br\s*/?>', '\n', h)
h = re.sub(r'(?i)</(p|div|tr|li|h[1-6]|table|caption|figcaption)>', '\n', h)
h = re.sub(r'(?i)</t[dh]>', ' | ', h)
h = re.sub(r'<[^>]+>', '', h)
h = html.unescape(h)
h = re.sub(r'[ \t\xa0]+', ' ', h)
h = re.sub(r'\n\s*\n+', '\n', h)
print(h.strip())
