#!/usr/bin/env bash
# Fetch many arXiv queries with rate limiting, save to files.
set -u
cd "$(dirname "$0")"
mkdir -p q
fetch() {
  name="$1"; q="$2"; mr="${3:-40}"
  url="https://export.arxiv.org/api/query?search_query=${q}&start=0&max_results=${mr}&sortBy=submittedDate&sortOrder=descending"
  for attempt in 1 2 3 4 5; do
    code=$(curl -sS --http1.1 -m 90 -o "q/${name}.xml" -w "%{http_code}" "$url")
    if [ "$code" = "200" ] && [ -s "q/${name}.xml" ]; then
      echo "OK  $name ($(wc -c < q/${name}.xml) bytes)"; return 0
    fi
    echo "retry $name http=$code attempt=$attempt"; sleep $((attempt*6))
  done
  echo "FAIL $name"
}

fetch nqs_hubbard      'abs:%22neural+quantum+states%22+AND+abs:%22Hubbard%22' 40
sleep 4
fetch nqs_dmrg         'abs:%22neural+quantum+states%22+AND+abs:%22DMRG%22' 40
sleep 4
fetch nqs_transformer  'abs:%22transformer%22+AND+abs:%22neural+quantum+states%22' 40
sleep 4
fetch nqs_lgt          'abs:%22neural+quantum+states%22+AND+abs:%22gauge%22' 40
sleep 4
fetch nqs_frustrated   'abs:%22neural+quantum+states%22+AND+abs:%22frustrated%22' 40
sleep 4
fetch nqs_j1j2         'abs:%22J1-J2%22+AND+abs:%22neural%22' 40
sleep 4
fetch flow_lattice     'abs:%22normalizing+flows%22+AND+abs:%22lattice%22' 40
sleep 4
fetch lqcd_ml          'abs:%22lattice+QCD%22+AND+abs:%22machine+learning%22' 40
sleep 4
fetch flow_gauge       'abs:%22flow-based+sampling%22' 40
sleep 4
fetch topo_freezing    'abs:%22topological+freezing%22' 40
sleep 4
fetch diff_gauge       'abs:%22diffusion+model%22+AND+abs:%22gauge%22' 40
sleep 4
fetch mace             'abs:%22MACE%22+AND+abs:%22interatomic%22' 40
sleep 4
fetch mlip_phonon      'abs:%22machine+learning%22+AND+abs:%22interatomic+potential%22+AND+abs:%22phonon%22' 40
sleep 4
fetch macemp0          'abs:%22MACE-MP-0%22' 40
sleep 4
fetch mattersim        'abs:%22MatterSim%22' 40
sleep 4
fetch foundmodel_phon  'abs:%22foundation+model%22+AND+abs:%22phonon%22' 40
sleep 4
fetch chgnet           'abs:%22CHGNet%22' 40
sleep 4
fetch sc_ml            'abs:%22superconductor%22+AND+abs:%22machine+learning%22' 60
sleep 4
fetch sc_tc            'abs:%22superconducting%22+AND+abs:%22critical+temperature%22+AND+abs:%22machine+learning%22' 40
sleep 4
fetch hydride_ml       'abs:%22hydride%22+AND+abs:%22superconduct%22+AND+abs:%22machine+learning%22' 40
sleep 4
fetch ai_discovery     'abs:%22autonomous+laboratory%22+AND+abs:%22materials%22' 30
sleep 4
fetch gnome             'all:%22GNoME%22' 30
echo DONE
