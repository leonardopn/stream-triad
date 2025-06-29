#!/usr/bin/env python3

import datetime

def generate_markdown_report():
    # Dados dos resultados
    js_times = [5.089305, 4.861903]
    js_bandwidths = [0.471577, 0.493634]
    
    chapel_times = [2.80024, 2.09167]
    chapel_bandwidths = [0.857069, 1.14741]
    
    c_times = [0.854252, 0.802117]
    c_bandwidths = [2.809476, 2.992082]
    
    # Cálculos
    js_time_avg = sum(js_times) / len(js_times)
    js_bandwidth_avg = sum(js_bandwidths) / len(js_bandwidths)
    
    chapel_4_speedup = js_time_avg / chapel_times[0]
    chapel_8_speedup = js_time_avg / chapel_times[1]
    c_1_speedup = js_time_avg / c_times[0]
    c_4_speedup = js_time_avg / c_times[1]
    
    chapel_bandwidth_scaling = chapel_bandwidths[1] / chapel_bandwidths[0]
    chapel_time_improvement = (chapel_times[0] - chapel_times[1]) / chapel_times[0] * 100
    
    c_bandwidth_scaling = c_bandwidths[1] / c_bandwidths[0]
    c_time_improvement = (c_times[0] - c_times[1]) / c_times[0] * 100
    
    chapel_vs_c_1 = c_bandwidths[0] / chapel_bandwidths[0]
    chapel_vs_c_4 = c_bandwidths[1] / chapel_bandwidths[1]
    
    # Gerar Markdown
    markdown = f"""# 📊 Benchmark STREAM Triad - Relatório Técnico

*Gerado automaticamente em {datetime.datetime.now().strftime('%d/%m/%Y às %H:%M:%S')}*

## 🎯 Resumo Executivo

Este benchmark compara três implementações do algoritmo STREAM Triad (`A = B + α * C`) para avaliar performance de diferentes linguagens e paradigmas de programação.

## 📋 Especificações do Teste

- **Tamanho do vetor:** 100.000.000 elementos (double precision)
- **Memória total:** ~2.4 GB de dados
- **Parâmetros:** α = 2.0, B = 3.0, C = 1.0
- **Métrica principal:** Largura de banda (GB/s)

## 📊 Resultados Completos

### Tabela de Performance Bruta

| Implementação | Execução | Tempo (s) | Bandwidth (GB/s) |
|---------------|----------|-----------|------------------|
| JavaScript | 1ª | {js_times[0]:.3f} | {js_bandwidths[0]:.3f} |
| JavaScript | 2ª | {js_times[1]:.3f} | {js_bandwidths[1]:.3f} |
| **JavaScript** | **Média** | **{js_time_avg:.3f}** | **{js_bandwidth_avg:.3f}** |
| Chapel | 4 threads | {chapel_times[0]:.3f} | {chapel_bandwidths[0]:.3f} |
| Chapel | 8 threads | {chapel_times[1]:.3f} | {chapel_bandwidths[1]:.3f} |
| C/MPI | 1 processo | {c_times[0]:.3f} | {c_bandwidths[0]:.3f} |
| C/MPI | 4 processos | {c_times[1]:.3f} | {c_bandwidths[1]:.3f} |

## 🚀 Análise de Speedup

### Speedup Relativo ao JavaScript (Baseline)

| Implementação | Speedup | Melhoria |
|---------------|---------|----------|
| Chapel (4 threads) | {chapel_4_speedup:.2f}x | {((chapel_4_speedup - 1) * 100):.1f}% |
| Chapel (8 threads) | {chapel_8_speedup:.2f}x | {((chapel_8_speedup - 1) * 100):.1f}% |
| C/MPI (1 processo) | {c_1_speedup:.2f}x | {((c_1_speedup - 1) * 100):.1f}% |
| C/MPI (4 processos) | {c_4_speedup:.2f}x | {((c_4_speedup - 1) * 100):.1f}% |

## 📈 Escalabilidade Intra-Linguagem

### Chapel: Escalabilidade com Threads
- **4 → 8 threads**
  - Melhoria na bandwidth: {((chapel_bandwidth_scaling - 1) * 100):.1f}%
  - Redução no tempo: {chapel_time_improvement:.1f}%
  - Eficiência: {(chapel_bandwidth_scaling / 2 * 100):.1f}% (teórico: 2x)

### C/MPI: Escalabilidade com Processos  
- **1 → 4 processos**
  - Melhoria na bandwidth: {((c_bandwidth_scaling - 1) * 100):.1f}%
  - Redução no tempo: {c_time_improvement:.1f}%
  - Eficiência: {(c_bandwidth_scaling / 4 * 100):.1f}% (teórico: 4x)

## 🥊 Comparação Direta: Chapel vs C/MPI

| Cenário | C/MPI é mais rápido por |
|---------|-------------------------|
| C (1 proc) vs Chapel (4 threads) | {chapel_vs_c_1:.2f}x |
| C (4 proc) vs Chapel (8 threads) | {chapel_vs_c_4:.2f}x |

## 🏆 Ranking Final

| 🏅 | Implementação | Bandwidth (GB/s) | Gap para 1º |
|----|---------------|------------------|-------------|
| 🥇 | C/MPI (4 processos) | {c_bandwidths[1]:.3f} | - |
| 🥈 | C/MPI (1 processo) | {c_bandwidths[0]:.3f} | {((c_bandwidths[1] - c_bandwidths[0]) / c_bandwidths[1] * 100):.1f}% |
| 🥉 | Chapel (8 threads) | {chapel_bandwidths[1]:.3f} | {((c_bandwidths[1] - chapel_bandwidths[1]) / c_bandwidths[1] * 100):.1f}% |
| 4º | Chapel (4 threads) | {chapel_bandwidths[0]:.3f} | {((c_bandwidths[1] - chapel_bandwidths[0]) / c_bandwidths[1] * 100):.1f}% |
| 5º | JavaScript | {js_bandwidth_avg:.3f} | {((c_bandwidths[1] - js_bandwidth_avg) / c_bandwidths[1] * 100):.1f}% |

## 💡 Insights e Descobertas

### ✅ Pontos Fortes do Chapel
- **Melhor escalabilidade relativa** que C/MPI ({((chapel_bandwidth_scaling - 1) * 100):.1f}% vs {((c_bandwidth_scaling - 1) * 100):.1f}%)
- **Eficiência de threads superior** (66.9% vs 26.6%)
- **Sintaxe de alto nível** mantendo performance competitiva

### ✅ Pontos Fortes do C/MPI
- **Performance absoluta superior** em todos os cenários
- **Maturidade e otimização** de décadas de desenvolvimento
- **Controle de baixo nível** sobre hardware

### ✅ JavaScript como Baseline
- **Performance surpreendente** para linguagem interpretada
- **V8 JIT otimizations** mostraram eficácia
- **Referência válida** para linguagens de alto nível

## 🎯 Recomendações de Uso

### Quando usar Chapel
- Desenvolvimento científico com foco em produtividade
- Prototipagem rápida de algoritmos paralelos
- Projetos que precisam de boa performance sem complexidade

### Quando usar C/MPI
- Performance crítica é prioridade absoluta
- Recursos computacionais limitados
- Controle fino sobre otimizações

### Quando usar JavaScript
- Prototipagem e validação de algoritmos
- Integração com ecosistemas web
- Desenvolvimento rápido sem requisitos de performance

## 📝 Metodologia

1. **Compilação:**
   - Chapel: `chpl test.chpl -o test-chapel`
   - C/MPI: `mpicc test.c -o test-c`

2. **Execução:**
   - Chapel: `CHPL_RT_NUM_THREADS_PER_LOCALE=N ./test-chapel`
   - C/MPI: `mpirun -np N ./test-c`
   - JavaScript: `node test.js`

3. **Validação:** Todos os testes verificaram corretude dos resultados

---

*Este relatório demonstra que Chapel oferece um excelente trade-off entre produtividade de desenvolvimento e performance computacional, justificando sua adoção em cenários de computação científica.*
"""

    with open('detailed_report.md', 'w', encoding='utf-8') as f:
        f.write(markdown)
    
    print("Relatório detalhado gerado em 'detailed_report.md'")
    print(f"Arquivo contém {len(markdown.splitlines())} linhas")

if __name__ == "__main__":
    generate_markdown_report()
