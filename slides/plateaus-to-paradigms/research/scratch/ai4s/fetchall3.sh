#!/usr/bin/env bash
set -u
cd "$(dirname "$0")"
mkdir -p q
fetch() {
  name="$1"; q="$2"; mr="${3:-40}"
  url="https://export.arxiv.org/api/query?search_query=${q}&start=0&max_results=${mr}&sortBy=submittedDate&sortOrder=descending"
  for attempt in 1 2 3 4 5 6 7; do
    code=$(curl -sS --http1.1 -m 90 -o "q/${name}.xml" -w "%{http_code}" "$url")
    if [ "$code" = "200" ] && [ -s "q/${name}.xml" ]; then
      echo "OK  $name ($(wc -c < q/${name}.xml) bytes)"; return 0
    fi
    echo "retry $name http=$code attempt=$attempt"; sleep $((attempt*10))
  done
  echo "FAIL $name"
}
fetch flow4d_su3   'abs:%22trivializing%22+AND+abs:%22flow%22' 40
sleep 6
fetch flow_su3_dyn 'abs:%22SU(3)%22+AND+abs:%22normalizing+flow%22' 40
sleep 6
fetch flow_fermion 'abs:%22flow-based+sampling%22+AND+abs:%22fermion%22' 30
sleep 6
fetch lgt_diffusion 'abs:%22diffusion%22+AND+abs:%22lattice+field+theory%22' 40
sleep 6
fetch albergo      'au:%22Albergo%22+AND+abs:%22flow%22' 40
sleep 6
fetch mlip_phonon_bench 'abs:%22phonon%22+AND+abs:%22benchmark%22+AND+abs:%22machine+learning+potential%22' 30
sleep 6
fetch umlip_forces 'abs:%22universal+machine+learning+interatomic+potentials%22+AND+abs:%22forces%22' 30
sleep 6
fetch fd_phonon    'abs:%22force+field%22+AND+abs:%22phonon%22+AND+abs:%22accuracy%22' 20
sleep 6
fetch sc_exp_verify 'abs:%22machine+learning%22+AND+abs:%22superconductivity%22+AND+abs:%22experiment%22' 40
sleep 6
fetch ai_retract   'abs:%22retraction%22+AND+abs:%22machine+learning%22' 20
sleep 6
fetch ai_sci_disc  'abs:%22AI%22+AND+abs:%22scientific+discovery%22+AND+abs:%22materials%22' 30
sleep 6
fetch lqe2        'abs:%22lattice+QCD%22+AND+abs:%22generative%22' 30
echo DONE
