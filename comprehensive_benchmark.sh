#!/bin/bash

echo "=========================================="
echo "BENCHMARK STREAM TRIAD - Análise Completa"
echo "Data: $(date)"
echo "=========================================="

# Função para extrair tempo e largura de banda
extract_metrics() {
    local output="$1"
    local time=$(echo "$output" | grep "Tempo de execução" | grep -oE '[0-9]+\.[0-9]+')
    local bandwidth=$(echo "$output" | grep "Largura de banda" | grep -oE '[0-9]+\.[0-9]+')
    echo "$time $bandwidth"
}

# Arrays para armazenar resultados
declare -a js_times=()
declare -a js_bandwidths=()
declare -a chapel_times=()
declare -a chapel_bandwidths=()
declare -a c_times=()
declare -a c_bandwidths=()

echo ""
echo "=== TESTE 1: JavaScript (Single-thread) - Execução 1 ==="
js_output1=$(node test.js)
echo "$js_output1"
js_metrics1=$(extract_metrics "$js_output1")
js_times+=($(echo $js_metrics1 | cut -d' ' -f1))
js_bandwidths+=($(echo $js_metrics1 | cut -d' ' -f2))

echo ""
echo "=== TESTE 2: JavaScript (Single-thread) - Execução 2 ==="
js_output2=$(node test.js)
echo "$js_output2"
js_metrics2=$(extract_metrics "$js_output2")
js_times+=($(echo $js_metrics2 | cut -d' ' -f1))
js_bandwidths+=($(echo $js_metrics2 | cut -d' ' -f2))

echo ""
echo "=== TESTE 3: Chapel (4 threads) ==="
chapel_output1=$(CHPL_RT_NUM_THREADS_PER_LOCALE=4 ./test-chapel)
echo "$chapel_output1"
chapel_metrics1=$(extract_metrics "$chapel_output1")
chapel_times+=($(echo $chapel_metrics1 | cut -d' ' -f1))
chapel_bandwidths+=($(echo $chapel_metrics1 | cut -d' ' -f2))

echo ""
echo "=== TESTE 4: Chapel (8 threads) ==="
chapel_output2=$(CHPL_RT_NUM_THREADS_PER_LOCALE=8 ./test-chapel)
echo "$chapel_output2"
chapel_metrics2=$(extract_metrics "$chapel_output2")
chapel_times+=($(echo $chapel_metrics2 | cut -d' ' -f1))
chapel_bandwidths+=($(echo $chapel_metrics2 | cut -d' ' -f2))

echo ""
echo "=== TESTE 5: C/MPI (1 processo) ==="
c_output1=$(mpirun -np 1 ./test-c)
echo "$c_output1"
c_metrics1=$(extract_metrics "$c_output1")
c_times+=($(echo $c_metrics1 | cut -d' ' -f1))
c_bandwidths+=($(echo $c_metrics1 | cut -d' ' -f2))

echo ""
echo "=== TESTE 6: C/MPI (4 processos) ==="
c_output2=$(mpirun -np 4 ./test-c)
echo "$c_output2"
c_metrics2=$(extract_metrics "$c_output2")
c_times+=($(echo $c_metrics2 | cut -d' ' -f1))
c_bandwidths+=($(echo $c_metrics2 | cut -d' ' -f2))

echo ""
echo "=========================================="
echo "RESUMO DOS RESULTADOS"
echo "=========================================="

printf "%-25s %-15s %-15s\n" "Teste" "Tempo (s)" "Bandwidth (GB/s)"
echo "--------------------------------------------------------"
printf "%-25s %-15s %-15s\n" "JavaScript (exec 1)" "${js_times[0]}" "${js_bandwidths[0]}"
printf "%-25s %-15s %-15s\n" "JavaScript (exec 2)" "${js_times[1]}" "${js_bandwidths[1]}"
printf "%-25s %-15s %-15s\n" "Chapel (4 threads)" "${chapel_times[0]}" "${chapel_bandwidths[0]}"
printf "%-25s %-15s %-15s\n" "Chapel (8 threads)" "${chapel_times[1]}" "${chapel_bandwidths[1]}"
printf "%-25s %-15s %-15s\n" "C/MPI (1 processo)" "${c_times[0]}" "${c_bandwidths[0]}"
printf "%-25s %-15s %-15s\n" "C/MPI (4 processos)" "${c_times[1]}" "${c_bandwidths[1]}"

echo ""
echo "=========================================="
echo "ANÁLISE DE PERFORMANCE"
echo "=========================================="

# Salvar resultados em arquivo para análise posterior
echo "js_times=(${js_times[@]})" >benchmark_results.txt
echo "js_bandwidths=(${js_bandwidths[@]})" >>benchmark_results.txt
echo "chapel_times=(${chapel_times[@]})" >>benchmark_results.txt
echo "chapel_bandwidths=(${chapel_bandwidths[@]})" >>benchmark_results.txt
echo "c_times=(${c_times[@]})" >>benchmark_results.txt
echo "c_bandwidths=(${c_bandwidths[@]})" >>benchmark_results.txt

echo "Resultados salvos em benchmark_results.txt para análise detalhada."
