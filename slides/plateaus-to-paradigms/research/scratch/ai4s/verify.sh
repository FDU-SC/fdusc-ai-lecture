#!/usr/bin/env bash
# verify URLs resolve
while read -r u; do
  [ -z "$u" ] && continue
  printf "%-72s " "$u"
  curl -sS -m 25 -o /dev/null -w "%{http_code} -> %{url_effective}\n" -L -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36" "$u" || echo FAIL
done
