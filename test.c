#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char *argv[])
{
    // ---- CONFIGURAÇÃO ----
    const int N = 100000000; // Deve ser o mesmo valor do código Chapel
    const double alpha = 2.0;
    const double B_val = 3.0;
    const double C_val = 1.0;

    int rank, num_procs;
    double start_time, end_time, elapsed_time;

    // ---- INICIALIZAÇÃO MPI ----
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &num_procs);

    // Cada processo calcula o tamanho de seu "pedaço" local
    int local_n = N / num_procs;

    // Validação para garantir que a divisão é exata
    if (N % num_procs != 0)
    {
        if (rank == 0)
        {
            fprintf(stderr, "Erro: O tamanho do vetor (N) deve ser divisível pelo número de processos.\n");
        }
        MPI_Finalize();
        return 1;
    }

    // Alocação de memória para os vetores locais em CADA processo
    double *local_a = (double *)malloc(local_n * sizeof(double));
    double *local_b = (double *)malloc(local_n * sizeof(double));
    double *local_c = (double *)malloc(local_n * sizeof(double));

    // O processo 'root' (rank 0) cria e inicializa os vetores completos
    double *global_a = NULL;
    if (rank == 0)
    {
        double *global_b = (double *)malloc(N * sizeof(double));
        double *global_c = (double *)malloc(N * sizeof(double));
        global_a = (double *)malloc(N * sizeof(double)); // Usado para receber o resultado final

        for (int i = 0; i < N; i++)
        {
            global_b[i] = B_val;
            global_c[i] = C_val;
        }

        printf("Iniciando STREAM Triad com %d processo(s) MPI...\n", num_procs);
        printf("Tamanho do Vetor: %d\n", N);

        // ---- MEDIÇÃO DE TEMPO ----
        MPI_Barrier(MPI_COMM_WORLD); // Sincroniza todos os processos antes de começar
        start_time = MPI_Wtime();

        // Distribui os dados do processo root para todos os outros
        MPI_Scatter(global_b, local_n, MPI_DOUBLE, local_b, local_n, MPI_DOUBLE, 0, MPI_COMM_WORLD);
        MPI_Scatter(global_c, local_n, MPI_DOUBLE, local_c, local_n, MPI_DOUBLE, 0, MPI_COMM_WORLD);

        free(global_b);
        free(global_c);
    }
    else
    {
        // Todos os outros processos (não-root) se preparam para receber os dados
        MPI_Barrier(MPI_COMM_WORLD);
        MPI_Scatter(NULL, local_n, MPI_DOUBLE, local_b, local_n, MPI_DOUBLE, 0, MPI_COMM_WORLD);
        MPI_Scatter(NULL, local_n, MPI_DOUBLE, local_c, local_n, MPI_DOUBLE, 0, MPI_COMM_WORLD);
    }

    // ---- CÁLCULO PRINCIPAL ----
    // Cada processo (incluindo o de rank 0) executa o cálculo em sua porção local dos dados.
    for (int i = 0; i < local_n; i++)
    {
        local_a[i] = local_b[i] + alpha * local_c[i];
    }

    // ---- AGREGAÇÃO DOS DADOS ----
    // Junta os resultados 'local_a' de todos os processos de volta no 'global_a' do processo root.
    MPI_Gather(local_a, local_n, MPI_DOUBLE, global_a, local_n, MPI_DOUBLE, 0, MPI_COMM_WORLD);

    // Sincroniza novamente e para o cronômetro
    MPI_Barrier(MPI_COMM_WORLD);
    if (rank == 0)
    {
        end_time = MPI_Wtime();
        elapsed_time = end_time - start_time;

        // ---- VERIFICAÇÃO E RESULTADOS ----
        const double expected_A_val = B_val + alpha * C_val;
        int isCorrect = 1;
        for (int i = 0; i < N; i++)
        {
            if (global_a[i] != expected_A_val)
            {
                isCorrect = 0;
                break;
            }
        }

        printf("------------------------------------\n");
        if (isCorrect)
        {
            printf("VERIFICAÇÃO: SUCESSO! O resultado está correto.\n");
        }
        else
        {
            printf("VERIFICAÇÃO: FALHA! O resultado está incorreto.\n");
        }
        printf("Tempo de execução (distribuição, cálculo, agregação): %.6f segundos.\n", elapsed_time);

        const double numBytes = 3.0 * N * sizeof(double);
        const double bandwidth = numBytes / elapsed_time / 1.0e9; // Converte para GB/s
        printf("Largura de banda: %.6f GB/s\n", bandwidth);

        free(global_a);
    }

    // Libera a memória local em todos os processos e finaliza
    free(local_a);
    free(local_b);
    free(local_c);
    MPI_Finalize();
    return 0;
}