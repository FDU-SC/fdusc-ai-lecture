#!/usr/bin/env bash
set -u
cd "$(dirname "$0")"
mkdir -p q
fetch() {
  name="$1"; q="$2"; mr="${3:-40}"
  url="https://export.arxiv.org/api/query?search_query=${q}&start=0&max_results=${mr}&sortBy=submittedDate&sortOrder=descending"
  for attempt in 1 2 3 4 5 6; do
    code=$(curl -sS --http1.1 -m 90 -o "q/${name}.xml" -w "%{http_code}" "$url")
    if [ "$code" = "200" ] && [ -s "q/${name}.xml" ]; then
      echo "OK  $name ($(wc -c < q/${name}.xml) bytes)"; return 0
    fi
    echo "retry $name http=$code attempt=$attempt"; sleep $((attempt*8))
  done
  echo "FAIL $name"
}

fetch nqs_hubbard    'abs:%22neural+quantum+states%22+AND+abs:%22Hubbard%22' 40
sleep 5
fetch nqs_dmrg       'abs:%22neural+quantum+states%22+AND+abs:%22DMRG%22' 40
sleep 5
fetch nqs_trf        'abs:%22transformer%22+AND+abs:%22variational+Monte+Carlo%22' 40
sleep 5
fetch nqs_hub2       'ti:%22Hubbard%22+AND+abs:%22neural+network%22' 40
sleep 5
fetch mace_found     'ti:%22foundation+model+for+atomistic+materials+chemistry%22' 10
sleep 5
fetch mattersim_orig 'ti:%22MatterSim%22' 10
sleep 5
fetch chgnet_orig    'ti:%22CHGNet%22' 10
sleep 5
fetch nequip_orig    'ti:%22NequIP%22' 15
sleep 5
fetch mattergen      'ti:%22MatterGen%22' 15
sleep 5
fetch gnome_paper    'ti:%22Scaling+deep+learning+for+materials+discovery%22' 10
sleep 5
fetch alab_paper     'ti:%22autonomous+laboratory+for+the+accelerated+synthesis%22' 10
sleep 5
fetch nqs_2dhub25    'abs:%22two-dimensional+Hubbard%22+AND+abs:%22neural%22' 40
sleep 5
fetch mlip_review    'abs:%22machine+learning+interatomic+potentials%22+AND+abs:%22review%22' 30
sleep 5
fetch phonon_mlip25  'abs:%22phonon%22+AND+abs:%22universal+machine+learning+potential%22' 30
sleep 5
fetch sc_ai_disc     'abs:%22superconductors%22+AND+abs:%22artificial+intelligence%22' 40
sleep 5
fetch hydride_pred   'abs:%22superconducting%22+AND+abs:%22high-pressure%22+AND+abs:%22machine+learning%22' 30
sleep 5
fetch lqcd_flow25    'abs:%22flow%22+AND+abs:%22lattice+QCD%22+AND+abs:%22sampling%22' 40
sleep 5
fetch dmrg_nqs_2026  'abs:%22tensor+network%22+AND+abs:%22neural+quantum+states%22' 40
echo DONE
