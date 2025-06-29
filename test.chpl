use BlockDist;
use Time;

config const n: int = 100_000_000;
config const alpha: real = 2.0;

proc main() {
    const B_val: real = 3.0;
    const C_val: real = 1.0;
    const expected_A_val = B_val + alpha * C_val;

    var t: stopwatch;

    writeln("Iniciando STREAM Triad em ", numLocales, " locales...");
    writeln("Tamanho do Vetor: ", n);

    const ProblemSpace = {1..n} dmapped new blockDist(boundingBox={1..n});
    var A, B, C: [ProblemSpace] real;

    B = B_val;
    C = C_val;
    
    t.start();
    A = B + alpha * C;
    t.stop();

    const isCorrect = && reduce (A == expected_A_val);

    writeln("------------------------------------");
    if isCorrect {
        writeln("VERIFICAÇÃO: SUCESSO! O resultado está correto.");
    } else {
        writeln("VERIFICAÇÃO: FALHA! O resultado está incorreto.");
    }

    writeln("Tempo de execução (cálculo principal): ", t.elapsed(), " segundos.");

    const totalBytes = 3 * n * 8; // 8 bytes por real (64 bits)
    const bandwidth = totalBytes / t.elapsed() / 1.0e9; 
    writeln("Largura de banda: ", bandwidth, " GB/s");
}