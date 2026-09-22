#!/bin/bash
# usage: ./fetch.sh URL OUTFILE
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
for i in 1 2 3 4 5; do
  code=$(curl -sL -m 45 -A "$UA" -H 'Accept-Language: en-US,en;q=0.9' -o "$2" -w "%{http_code}" "$1" 2>/dev/null)
  sz=$(stat -c%s "$2" 2>/dev/null || echo 0)
  if [ "$code" = "200" ] && [ "$sz" -gt 500 ]; then echo "OK HTTP:$code SIZE:$sz TRY:$i $1"; exit 0; fi
  sleep 3
done
echo "FAIL HTTP:$code SIZE:$sz $1"; exit 1
