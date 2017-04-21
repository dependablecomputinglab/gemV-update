bench_home="/home/sohwisoo/miBench"

case "$2" in
hello )
  bench="helloWorld/hello_$3"
  options=""
  ;;
matmul )
  bench="matrixmul/matmul_$3"
  options=""
  ;;
qsort )
  bench="automotive/qsort/qsort_small_$3"
  options="$bench_home/automotive/qsort/input_small.dat"
  ;;
stringsearch )
  bench="office/stringsearch/search_small_$3"
  options=""
  ;;
gsm )
  bench="telecomm/gsm/bin/toast_$3"
  options="-fps -c $bench_home/telecomm/gsm/data/small.au"
  ;;
bitcount )
  bench="automotive/bitcount/bitcnts_$3"
  options=75000
  ;;
jpeg )
  bench="consumer/jpeg/jpeg-6a/cjpeg_$3"
  options="-dct int -progressive -opt -outfile output_small_encode.jpeg $bench_home/consumer/jpeg/input_small.ppm"
  ;;
fft )
  bench="telecomm/FFT/fft_$3"
  options="4 4096"
  ;;
dijkstra )
  bench="network/dijkstra/dijkstra_small_$3"
  options="$bench_home/network/dijkstra/input.dat"
  ;;
basicmath ) 
  bench="automotive/basicmath/basicmath_small_$3"
  options=""
  ;;
typese )
  bench="/consumer/typeset/lout-3.24/lout_$3"
  options=" -I $bench_home/consumer/typeset/lout-3.24/include -D $bench_home/consumer/typeset/lout-3.24/data -F $bench_home/consumer/typeset/lout-3.24/font -C $bench_home/consumer/typeset/lout-3.24/maps -H $bench_home/consumer/typeset/lout-3.24/hyph $bench_home/consumer/typeset/small.lout"
  ;;
crc )
  bench="telecomm/CRC32/crc_$3"
  options="$bench_home/telecomm/adpcm/data/small.pcm"
  ;;
patricia )
  bench="network/patricia/patricia_$3"
  options="$bench_home/network/patricia/small.udp"
  ;;
sha )
  bench="security/sha/sha_$3"
  options="$bench_home/security/sha/input_small.asc"
  ;;
ispell )
  bench="office/ispell/ispell_$3"
  options="$bench_home/office/ispell/tests/americanmed+ < $bench_home/office/ispell/tests/small.txt"
  ;;
susan )
  bench="automotive/susan/susan_$3"
  options="$bench_home/automotive/susan/input_small.pgm m5out/susan_result -e"
  ;;
esac

protection=no_protection								# Protection scheme to be used
vul_analysis=no								# Enable/Disable vulnerability analysis
cpu_type=arm_detailed								# CPU Type
num_procs=1									# Number of processors
gemv_exec_path=./build/$1/gem5.fast		# Path to gemv executable
config_path=./configs/example/se.py		# Path to config file

$gemv_exec_path -d $2 -re --stdout-file=simout_$3 --stderr-file=simerr_$3 --stats-file=stats_$3 $config_path --cpu-type=$cpu_type --caches -n $num_procs -c "$bench_home/$bench" -o "$options" --cpu-type=$cpu_type --caches --vul_analysis=yes --vul_params=params.in --output=$2/result