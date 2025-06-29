#!/usr/bin/env python3

print("=" * 50)
print("ANÁLISE DETALHADA DOS RESULTADOS - STREAM TRIAD")
print("=" * 50)

# Resultados dos testes
js_times = [5.089305, 4.861903]
js_bandwidths = [0.471577, 0.493634]

chapel_times = [2.80024, 2.09167]  # 4 threads, 8 threads
chapel_bandwidths = [0.857069, 1.14741]

c_times = [0.854252, 0.802117]  # 1 processo, 4 processos
c_bandwidths = [2.809476, 2.992082]

# Médias JavaScript
js_time_avg = sum(js_times) / len(js_times)
js_bandwidth_avg = sum(js_bandwidths) / len(js_bandwidths)

print(f"\n1. COMPARAÇÃO DE BASELINE (JavaScript vs outros):")
print("=" * 50)
print(f"JavaScript (média): {js_time_avg:.3f}s, {js_bandwidth_avg:.3f} GB/s")
print()

# Speedups sobre JavaScript
chapel_4_speedup = js_time_avg / chapel_times[0]
chapel_8_speedup = js_time_avg / chapel_times[1]
c_1_speedup = js_time_avg / c_times[0]
c_4_speedup = js_time_avg / c_times[1]

print(f"Chapel (4 threads): {chapel_4_speedup:.2f}x mais rápido que JavaScript")
print(f"Chapel (8 threads): {chapel_8_speedup:.2f}x mais rápido que JavaScript")
print(f"C/MPI (1 processo): {c_1_speedup:.2f}x mais rápido que JavaScript")
print(f"C/MPI (4 processos): {c_4_speedup:.2f}x mais rápido que JavaScript")

print(f"\n2. ESCALABILIDADE POR LINGUAGEM:")
print("=" * 35)

# Escalabilidade Chapel (4→8 threads)
chapel_bandwidth_scaling = chapel_bandwidths[1] / chapel_bandwidths[0]
chapel_time_improvement = (chapel_times[0] - chapel_times[1]) / chapel_times[0] * 100

print(f"Chapel (4→8 threads):")
print(f"  - Bandwidth: {chapel_bandwidth_scaling:.2f}x melhoria")
print(f"  - Tempo: {chapel_time_improvement:.1f}% de redução")

# Escalabilidade C/MPI (1→4 processos)
c_bandwidth_scaling = c_bandwidths[1] / c_bandwidths[0]
c_time_improvement = (c_times[0] - c_times[1]) / c_times[0] * 100

print(f"\nC/MPI (1→4 processos):")
print(f"  - Bandwidth: {c_bandwidth_scaling:.2f}x melhoria")
print(f"  - Tempo: {c_time_improvement:.1f}% de redução")

print(f"\n3. COMPARAÇÃO DIRETA CHAPEL vs C/MPI:")
print("=" * 40)

# Chapel vs C comparações
chapel_vs_c_similar = c_bandwidths[0] / chapel_bandwidths[0]  # C(1) vs Chapel(4)
chapel_vs_c_max = c_bandwidths[1] / chapel_bandwidths[1]      # C(4) vs Chapel(8)

print(f"C (1 processo) vs Chapel (4 threads): C é {chapel_vs_c_similar:.2f}x mais rápido")
print(f"C (4 processos) vs Chapel (8 threads): C é {chapel_vs_c_max:.2f}x mais rápido")

print(f"\n4. EFICIÊNCIA DE PARALELIZAÇÃO:")
print("=" * 35)

# Eficiência teórica vs real
chapel_theoretical_speedup = 2  # de 4 para 8 threads
chapel_efficiency = (chapel_bandwidth_scaling / chapel_theoretical_speedup) * 100

c_theoretical_speedup = 4  # de 1 para 4 processos
c_efficiency = (c_bandwidth_scaling / c_theoretical_speedup) * 100

print(f"Chapel:")
print(f"  - Teórico: {chapel_theoretical_speedup}x speedup (4→8 threads)")
print(f"  - Real: {chapel_bandwidth_scaling:.2f}x speedup")
print(f"  - Eficiência: {chapel_efficiency:.1f}%")

print(f"\nC/MPI:")
print(f"  - Teórico: {c_theoretical_speedup}x speedup (1→4 processos)")
print(f"  - Real: {c_bandwidth_scaling:.2f}x speedup")
print(f"  - Eficiência: {c_efficiency:.1f}%")

print(f"\n5. MELHORIAS PERCENTUAIS:")
print("=" * 30)

print(f"Chapel:")
print(f"  - 4→8 threads: {((chapel_bandwidths[1]/chapel_bandwidths[0]) - 1) * 100:.1f}% melhoria na bandwidth")
print(f"  - 4→8 threads: {chapel_time_improvement:.1f}% redução no tempo")

print(f"\nC/MPI:")
print(f"  - 1→4 processos: {((c_bandwidths[1]/c_bandwidths[0]) - 1) * 100:.1f}% melhoria na bandwidth")
print(f"  - 1→4 processos: {c_time_improvement:.1f}% redução no tempo")

print(f"\n6. INSIGHTS PRINCIPAIS:")
print("=" * 25)
print("✓ JavaScript (V8) serve como baseline confiável")
print("✓ Chapel oferece 33.9% de melhoria ao dobrar threads (4→8)")
print("✓ C/MPI oferece 6.5% de melhoria ao quadruplicar processos (1→4)")
print("✓ Chapel tem melhor escalabilidade relativa que C/MPI")
print("✓ C/MPI mantém superioridade absoluta em performance")
print("✓ Chapel oferece produtividade superior mantendo performance competitiva")

print(f"\n7. RANKING DE PERFORMANCE:")
print("=" * 30)
results = [
    ("C/MPI (4 proc)", c_bandwidths[1]),
    ("C/MPI (1 proc)", c_bandwidths[0]),
    ("Chapel (8 thr)", chapel_bandwidths[1]),
    ("Chapel (4 thr)", chapel_bandwidths[0]),
    ("JavaScript", js_bandwidth_avg)
]

for i, (name, bandwidth) in enumerate(results, 1):
    print(f"{i}º: {name} - {bandwidth:.3f} GB/s")

print(f"\n8. CONCLUSÕES TÉCNICAS:")
print("=" * 28)
print(f"• Chapel vs JavaScript: até {chapel_8_speedup:.1f}x mais rápido")
print(f"• C/MPI vs JavaScript: até {c_4_speedup:.1f}x mais rápido") 
print(f"• C/MPI vs Chapel: {chapel_vs_c_max:.1f}x mais rápido no melhor caso")
print(f"• Chapel tem boa escalabilidade intra-node (threads)")
print(f"• C/MPI tem menor overhead de paralelização mas menor ganho relativo")
