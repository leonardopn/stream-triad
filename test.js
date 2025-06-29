// STREAM Triad em JavaScript (sem paralelismo)
// Equivalente aos códigos Chapel e C para comparação de performance

const N = 100_000_000; // Mesmo tamanho dos outros códigos
const alpha = 2.0;
const B_val = 3.0;
const C_val = 1.0;

function main() {
	console.log("Iniciando STREAM Triad em JavaScript (single-threaded)...");
	console.log(`Tamanho do Vetor: ${N}`);

	// Alocação e inicialização dos arrays
	const A = new Array(N);
	const B = new Array(N);
	const C = new Array(N);

	// Inicialização dos arrays B e C
	for (let i = 0; i < N; i++) {
		B[i] = B_val;
		C[i] = C_val;
	}

	// Medição de tempo do cálculo principal
	const startTime = performance.now();

	// Cálculo STREAM Triad: A = B + alpha * C
	for (let i = 0; i < N; i++) {
		A[i] = B[i] + alpha * C[i];
	}

	const endTime = performance.now();
	const elapsedTime = (endTime - startTime) / 1000; // Converter para segundos

	// Verificação da correção
	const expected_A_val = B_val + alpha * C_val;
	let isCorrect = true;
	for (let i = 0; i < N; i++) {
		if (Math.abs(A[i] - expected_A_val) > 1e-10) {
			isCorrect = false;
			break;
		}
	}

	console.log("------------------------------------");
	if (isCorrect) {
		console.log("VERIFICAÇÃO: SUCESSO! O resultado está correto.");
	} else {
		console.log("VERIFICAÇÃO: FALHA! O resultado está incorreto.");
	}

	console.log(`Tempo de execução (cálculo principal): ${elapsedTime.toFixed(6)} segundos.`);

	// Cálculo da largura de banda
	const totalBytes = 3 * N * 8; // 8 bytes por double (64 bits)
	const bandwidth = totalBytes / elapsedTime / 1.0e9;
	console.log(`Largura de banda: ${bandwidth.toFixed(6)} GB/s`);
}

// Executar o programa
main();
