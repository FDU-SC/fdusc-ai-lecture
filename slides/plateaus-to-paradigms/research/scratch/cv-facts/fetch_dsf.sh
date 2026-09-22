#!/bin/bash
# usage: ./fetch_dsf.sh URL OUTFILE   -- retries, logs failures
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
LOG="/home/zecyel/slides/ch1/research/scratch/cv-facts/fetch_dsf.log"
for i in 1 2 3 4 5 6; do
  code=$(curl -sL -m 50 -A "$UA" -H 'Accept-Language: en-US,en;q=0.9' -o "$2" -w "%{http_code}" "$1" 2>/dev/null)
  sz=$(stat -c%s "$2" 2>/dev/null || echo 0)
  if [ "$code" = "200" ] && [ "$sz" -gt 800 ]; then echo "OK HTTP:$code SIZE:$sz TRY:$i $1" | tee -a "$LOG"; exit 0; fi
  sleep 2
done
echo "FAIL HTTP:$code SIZE:$sz $1" | tee -a "$LOG"; exit 1
