# 📊 Benchmark STREAM Triad - Relatório Técnico

*Gerado automaticamente em 29/06/2025 às 16:42:03*

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
| JavaScript | 1ª | 5.089 | 0.472 |
| JavaScript | 2ª | 4.862 | 0.494 |
| **JavaScript** | **Média** | **4.976** | **0.483** |
| Chapel | 4 threads | 2.800 | 0.857 |
| Chapel | 8 threads | 2.092 | 1.147 |
| C/MPI | 1 processo | 0.854 | 2.809 |
| C/MPI | 4 processos | 0.802 | 2.992 |

## 🚀 Análise de Speedup

### Speedup Relativo ao JavaScript (Baseline)

| Implementação | Speedup | Melhoria |
|---------------|---------|----------|
| Chapel (4 threads) | 1.78x | 77.7% |
| Chapel (8 threads) | 2.38x | 137.9% |
| C/MPI (1 processo) | 5.82x | 482.5% |
| C/MPI (4 processos) | 6.20x | 520.3% |

## 📈 Escalabilidade Intra-Linguagem

### Chapel: Escalabilidade com Threads
- **4 → 8 threads**
  - Melhoria na bandwidth: 33.9%
  - Redução no tempo: 25.3%
  - Eficiência: 66.9% (teórico: 2x)

### C/MPI: Escalabilidade com Processos  
- **1 → 4 processos**
  - Melhoria na bandwidth: 6.5%
  - Redução no tempo: 6.1%
  - Eficiência: 26.6% (teórico: 4x)

## 🥊 Comparação Direta: Chapel vs C/MPI

| Cenário | C/MPI é mais rápido por |
|---------|-------------------------|
| C (1 proc) vs Chapel (4 threads) | 3.28x |
| C (4 proc) vs Chapel (8 threads) | 2.61x |

## 🏆 Ranking Final

| 🏅 | Implementação | Bandwidth (GB/s) | Gap para 1º |
|----|---------------|------------------|-------------|
| 🥇 | C/MPI (4 processos) | 2.992 | - |
| 🥈 | C/MPI (1 processo) | 2.809 | 6.1% |
| 🥉 | Chapel (8 threads) | 1.147 | 61.7% |
| 4º | Chapel (4 threads) | 0.857 | 71.4% |
| 5º | JavaScript | 0.483 | 83.9% |

## 💡 Insights e Descobertas

### ✅ Pontos Fortes do Chapel
- **Melhor escalabilidade relativa** que C/MPI (33.9% vs 6.5%)
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
