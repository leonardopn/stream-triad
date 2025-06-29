# 📊 Benchmark STREAM Triad - Análise Comparativa

## 🎯 Objetivo

Comparação de performance entre diferentes linguagens e paradigmas de programação usando o benchmark STREAM Triad (`A = B + α * C`).

## 🔧 Configuração dos Testes

### Hardware/Software

-   **Vetor:** 100.000.000 elementos (double precision)
-   **Memória:** ~2.4 GB total de dados
-   **Constantes:** α = 2.0, B = 3.0, C = 1.0
-   **Data:** 29 de junho de 2025

### Implementações Testadas

1. **JavaScript (Node.js)** - Single-threaded, interpretado
2. **Chapel** - Compilado, com threads (4 e 8 threads)
3. **C/MPI** - Compilado, com processos (1 e 4 processos)

## 📈 Resultados Detalhados

### Tabela de Performance

| Implementação          | Tempo (s) | Bandwidth (GB/s) | Speedup vs JS |
| ---------------------- | --------- | ---------------- | ------------- |
| JavaScript (exec 1)    | 5.089     | 0.472            | 1.00x         |
| JavaScript (exec 2)    | 4.862     | 0.494            | 1.00x         |
| **JavaScript (média)** | **4.976** | **0.483**        | **1.00x**     |
| Chapel (4 threads)     | 2.800     | 0.857            | **1.78x**     |
| Chapel (8 threads)     | 2.092     | 1.147            | **2.38x**     |
| C/MPI (1 processo)     | 0.854     | 2.809            | **5.82x**     |
| C/MPI (4 processos)    | 0.802     | 2.992            | **6.20x**     |

## Análise de Escalabilidade

### Chapel (4 → 8 threads)

-   **Melhoria na Bandwidth:** 33.9% ⬆️
-   **Redução no Tempo:** 25.3% ⬇️
-   **Eficiência Teórica:** 66.9% (muito boa!)

### C/MPI (1 → 4 processos)

-   **Melhoria na Bandwidth:** 6.5% ⬆️
-   **Redução no Tempo:** 6.1% ⬇️
-   **Eficiência Teórica:** 26.6% (limitada por overhead)

## 🏆 Ranking de Performance

| Posição | Implementação      | Bandwidth (GB/s) | Diferença |
| ------- | ------------------ | ---------------- | --------- |
| 🥇      | C/MPI (4 proc)     | 2.992            | -         |
| 🥈      | C/MPI (1 proc)     | 2.809            | -6.1%     |
| 🥉      | Chapel (8 threads) | 1.147            | -61.7%    |
| 4º      | Chapel (4 threads) | 0.857            | -71.4%    |
| 5º      | JavaScript         | 0.483            | -83.9%    |

## 💡 Insights Principais

### ✅ Descobertas Positivas

-   **Chapel escala melhor que C/MPI** (33.9% vs 6.5% de melhoria)
-   **JavaScript V8 é surpreendentemente competitivo** para uma linguagem interpretada
-   **Chapel oferece excelente trade-off** entre produtividade e performance

### 🔍 Observações Técnicas

-   **C/MPI já é altamente otimizado** - adicionar processos gera pouco ganho
-   **Chapel tem boa escalabilidade intra-node** com threads
-   **Overhead de comunicação em MPI** limita ganhos de paralelização

## 📊 Comparações Diretas

### Chapel vs JavaScript

-   **4 threads:** 1.78x mais rápido
-   **8 threads:** 2.38x mais rápido
-   **Melhoria máxima:** 138% de performance superior

### C/MPI vs JavaScript

-   **1 processo:** 5.82x mais rápido
-   **4 processos:** 6.20x mais rápido
-   **Melhoria máxima:** 520% de performance superior

### C/MPI vs Chapel

-   **C (1 proc) vs Chapel (4 threads):** C é 3.28x mais rápido
-   **C (4 proc) vs Chapel (8 threads):** C é 2.61x mais rápido

## 🎯 Conclusões

### Justificativa para Chapel

1. **Performance competitiva** mesmo sendo de alto nível
2. **Melhor escalabilidade relativa** que C/MPI
3. **Produtividade superior** ao C tradicional
4. **Supera significativamente** linguagens interpretadas

### Recomendações de Uso

-   **JavaScript:** Prototipagem rápida, aplicações web
-   **Chapel:** Computação científica, produtividade + performance
-   **C/MPI:** Maximum performance, aplicações críticas

### Eficiência de Paralelização

| Linguagem | Speedup Teórico    | Speedup Real | Eficiência |
| --------- | ------------------ | ------------ | ---------- |
| Chapel    | 2.0x (4→8 threads) | 1.34x        | **66.9%**  |
| C/MPI     | 4.0x (1→4 proc)    | 1.06x        | **26.6%**  |

---

_Benchmark realizado em 29/06/2025 usando STREAM Triad com 100M elementos_
