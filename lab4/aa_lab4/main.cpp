#include <iostream>
#include <ctime>
#include <algorithm>
#include <chrono>
#include <thread>

#define SUCCESS 0
#define FAIL -1

int create_mtrx(int*** mtrx, int n, int m)
{
    (*mtrx) = new int* [n];
    if (!(*mtrx))
        return FAIL;

    int f = 0;
    int i = 0;
    for (; i < n && !f; i++)
    {
        (*mtrx)[i] = new int[m];
        if (!(*mtrx)[i])
            f = 1;
    }

    if (f)
    {
        for (int j = 0; j < i; j++)
            delete[](*mtrx)[i];
        delete[](*mtrx);
    }

    return SUCCESS;
}

void delete_mtrx(int** mtrx, int n)
{
    for (int i = 0; i < n; i++)
        delete[] mtrx[i];
    delete[] mtrx;
}

void input_mtrx(int** mtrx, int n, int m)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            std::cin >> mtrx[i][j];
}

void output_mtrx(int** mtrx, int n, int m)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            std::cout << mtrx[i][j] << " ";
        std::cout << std::endl;
    }
}

void fill_mtrx(int** mtrx, int n, int m)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            mtrx[i][j] = (i + j + 17) * (i + j - 13) - 13;
}

void run_mult(int (*alg)(int**, int**, int**, int, int, int, int))
{
    int n_a, m_a, n_b, m_b;

    std::cout << "Input sizes of first matrix, space separated: ";
    std::cin >> n_a >> m_a;

    std::cout << "Input sizes of second matrix, space separated: ";
    std::cin >> n_b >> m_b;

    if (m_a <= 0 || n_a <= 0 || m_b <= 0 || n_b <= 0)
    {
        std::cout << "Incorrect sizes of matricies: " << "(" << n_a \
			<< ", " << m_a << ") and (" << n_b << ", " << m_b << ")" << std::endl;
    }
    else if (m_a != n_b)
    {
        std::cout << "Can't multiply matricies with such sizes: " << "(" << n_a \
			<< ", " << m_a << ") and (" << n_b << ", " << m_b << ")" << std::endl;
    }
    else
    {
        int** A = nullptr;
        int** B = nullptr;
        int** result = nullptr;
        if (create_mtrx(&A, n_a, m_a) == SUCCESS)
        {
            if (create_mtrx(&B, n_b, m_b) == SUCCESS)
            {
                if (create_mtrx(&result, n_a, m_b) == SUCCESS)
                {
                    std::cout << "\nInput first matrix: " << std::endl;
                    input_mtrx(A, n_a, m_a);

                    std::cout << "\nInput second matrix: " << std::endl;
                    input_mtrx(B, n_b, m_b);

                    int t_count = 2;
                    if (alg(A, B, result, n_a, m_a, m_b, t_count) == SUCCESS)
                    {
                        std::cout << "\nResult of multiplication:" << std::endl;
                        output_mtrx(result, n_a, m_b);
                    }
                    else
                    {
                        std::cout << "\nMultiplication failed" << std::endl;
                    }

                    delete_mtrx(A, n_a);
                    delete_mtrx(B, n_b);
                    delete_mtrx(result, n_a);

                }
                else
                {
                    delete_mtrx(A, n_a);
                    delete_mtrx(B, n_b);
                    std::cout << "Memory error" << std::endl;
                }
            }
            else
            {
                delete_mtrx(A, n_a);
                std::cout << "Memory error" << std::endl;
            }
        }
        else
        {
            std::cout << "Memory error" << std::endl;
        }
    }
}

int vng_mult(int** A, int** B, int** result, int N_a, int M_a, int M_b, int fl)
{
    int* mulH = new int[N_a];
    int* mulV = new int[M_b];

    // PART 1
    int buf;
    for (int i = 0; i < N_a; i++)
    {
        buf = 0;
        for (int k = 1; k < M_a; k += 2)
            buf -= A[i][k - 1] * A[i][k];
        mulH[i] = buf;
    }

    // PART 2
    for (int j = 0; j < M_b; j++)
    {
        buf = 0;
        for (int k = 1; k < M_a; k += 2)
            buf -= B[k - 1][j] * B[k][j];
        mulV[j] = buf;
    }

    // PART 3 + 4
    for (int i = 0; i < N_a; i++)
        for (int j = 0; j < M_b; j++)
        {
            buf = mulH[i] + mulV[j];
            for (int k = 1; k < M_a; k += 2)
                buf += (A[i][k - 1] + B[k][j]) * (A[i][k] + B[k - 1][j]);

            if (M_a % 2)
                buf += A[i][M_a - 1] * B[M_a - 1][j];

            result[i][j] = buf;
        }


    return SUCCESS;
}

void scheme1_part1(int** A, int N_a, int M_a, int* mulH, int start, int end)
{
    int buf;
    for (int i = start; i < end; i++)
    {
        buf = 0;
        for (int k = 1; k < M_a; k += 2)
            buf -= A[i][k - 1] * A[i][k];
        mulH[i] = buf;
    }
}

void sheme1_part2(int** B, int M_a, int M_b, int* mulV, int start, int end)
{
    int buf;
    for (int j = start; j < end; j++)
    {
        buf = 0;
        for (int k = 1; k < M_a; k += 2)
            buf -= B[k - 1][j] * B[k][j];
        mulV[j] = buf;
    }
}

void scheme_2(int** A, int** B, int** result, int N_a, int M_a, int M_b, int* mulH, int* mulV, int start_row, int end_row)
{
    int buf;
    for (int i = start_row; i < end_row; i++)
        for (int j = 0; j < M_b; j++)
        {
            buf = mulH[i] + mulV[j];
            for (int k = 1; k < M_a; k += 2)
                buf += (A[i][k - 1] + B[k][j]) * (A[i][k] + B[k - 1][j]);

            if (M_a % 2)
                buf += A[i][M_a - 1] * B[M_a - 1][j];

            result[i][j] = buf;
        }
}

int vng_mult_par1(int** A, int** B, int** result, int N_a, int M_a, int M_b, int t_count)
{
    int* mulH = new int[N_a];
    int* mulV = new int[M_b];
    auto* threads = new std::thread[t_count];

    if (t_count > 1)
    {
        int proportion = t_count * N_a / (N_a + M_b);
        int rows_t = (proportion) ? proportion : 1;
        int cols_t = t_count - rows_t;

        int rows_per_t = N_a / rows_t;
        int cols_per_t = M_b / cols_t;

        int start_row = 0;
        for (int i = 0; i < rows_t; i++)
        {
            int end_row = (i == rows_t - 1) ? N_a : start_row + rows_per_t;
            threads[i] = std::thread(scheme1_part1, A, N_a, M_a, mulH, start_row, end_row);
            start_row = end_row;
        }

        int start_col = 0;
        for (int i = rows_t; i < t_count; i++)
        {
            int end_col = (i == t_count - 1) ? M_b : start_col + cols_per_t;
            threads[i] = std::thread(sheme1_part2, B, M_a, M_b, mulV, start_col, end_col);
            start_col = end_col;
        }

        for (int i = 0; i < t_count; i++)
        {
            threads[i].join();
        }
    }
    else
    {
        // PART 1
        int buf;
        for (int i = 0; i < N_a; i++)
        {
            buf = 0;
            for (int k = 1; k < M_a; k += 2)
                buf -= A[i][k - 1] * A[i][k];
            mulH[i] = buf;
        }

        // PART 2
        for (int j = 0; j < M_b; j++)
        {
            buf = 0;
            for (int k = 1; k < M_a; k += 2)
                buf -= B[k - 1][j] * B[k][j];
            mulV[j] = buf;
        }
    }

    int buf;
    for (int i = 0; i < N_a; i++)
        for (int j = 0; j < M_b; j++)
        {
            buf = mulH[i] + mulV[j];
            for (int k = 1; k < M_a; k += 2)
                buf += (A[i][k - 1] + B[k][j]) * (A[i][k] + B[k - 1][j]);

            if (M_a % 2)
                buf += A[i][M_a - 1] * B[M_a - 1][j];

            result[i][j] = buf;
        }

    return SUCCESS;
}

int vng_mult_par2(int** A, int** B, int** result, int N_a, int M_a, int M_b, int t_count)
{
    int* mulH = new int[N_a];
    int* mulV = new int[M_b];
    auto* threads = new std::thread[t_count];

    // PART 1
    int buf;
    for (int i = 0; i < N_a; i++)
    {
        buf = 0;
        for (int k = 1; k < M_a; k += 2)
            buf -= A[i][k - 1] * A[i][k];
        mulH[i] = buf;
    }

    // PART 2
    for (int j = 0; j < M_b; j++)
    {
        buf = 0;
        for (int k = 1; k < M_a; k += 2)
            buf -= B[k - 1][j] * B[k][j];
        mulV[j] = buf;
    }

    int rows_per_t = N_a / t_count;  // сколько строк обрабатывает один поток
    int start_row = 0;
    for (int i = 0; i < t_count; i++)
    {
        // каждому потоку делегируем срез со start_row по end_row
        int end_row = (i == t_count - 1) ? N_a : start_row + rows_per_t;
        threads[i] = std::thread(scheme_2, A, B, result, N_a, M_a, M_b, mulH, mulV, start_row, end_row);


        start_row = end_row;
    }
    for (int i = 0; i < t_count; i++)
    {
        threads[i].join();
    }

    return SUCCESS;
}

float get_time(int (*alg)(int**, int**, int**, int, int, int, int), int** A, int** B, int** result, int tcnt = 1, int size = 500, int itcnt = 1)
{
    fill_mtrx(A, size, size);
    fill_mtrx(B, size, size);

    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < itcnt; i++)
        alg(A, B, result, size, size, size, tcnt);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    float time = duration.count() / 1000 / itcnt;
    return time;
}

void analyse_time()
{
    int t_counts[6] = { 1, 2, 4, 8, 16, 32 };
    int sizes[6] = { 100, 200, 300, 400, 500 };

    float results[6][3];
    float results2[5][3];

    int** A = nullptr;
    int** B = nullptr;
    int** result = nullptr;
    int size = 500;
    int iterations = 1;
    if (create_mtrx(&A, size, size) == SUCCESS)
    {
        if (create_mtrx(&B, size, size) == SUCCESS)
        {
            if (create_mtrx(&result, size, size) == SUCCESS)
            {
                int (*algs[3])(int**, int**, int**, int, int, int, int) = { vng_mult, vng_mult_par1, vng_mult_par2 };


                for (int si = 0; si < 6; si++)
                    for (int ai = 0; ai < 3; ai++)
                    {
                        results[si][ai] = get_time(algs[ai], A, B, result, t_counts[si], size, iterations);
                    }

                std::cout << "\nResults:\n";
                for (int i = 0; i < 6; i++)
                {
                    for (int j = 0; j < 3; j++)
                        std::cout << results[i][j] << " ";
                    std::cout << std::endl;
                }

                for (int si = 0; si < 5; si++)
                    for (int ai = 0; ai < 3; ai++)
                    {
                        results2[si][ai] = get_time(algs[ai], A, B, result, 8, sizes[si], iterations);
                    }

                std::cout << "\nMORE Results:\n";
                for (int i = 0; i < 5; i++)
                {
                    for (int j = 0; j < 3; j++)
                        std::cout << results2[i][j] << " ";
                    std::cout << std::endl;
                }
            }
            else
            {
                delete_mtrx(A, size);
                delete_mtrx(B, size);
                std::cout << "Memory error" << std::endl;
            }
        }
        else
        {
            delete_mtrx(A, size);
            std::cout << "Memory error" << std::endl;
        }
    }
    else
    {
        std::cout << "Memory error" << std::endl;
    }
}

void run_all_mults()
{
    int n_a, m_a, n_b, m_b;

    std::cout << "Input sizes of first matrix, space separated: ";
    std::cin >> n_a >> m_a;

    std::cout << "Input sizes of second matrix, space separated: ";
    std::cin >> n_b >> m_b;

    if (m_a <= 0 || n_a <= 0 || m_b <= 0 || n_b <= 0)
    {
        std::cout << "Incorrect sizes of matricies: " << "(" << n_a \
			<< ", " << m_a << ") and (" << n_b << ", " << m_b << ")" << std::endl;
    }
    else if (m_a != n_b)
    {
        std::cout << "Can't multiply matricies with such sizes: " << "(" << n_a \
			<< ", " << m_a << ") and (" << n_b << ", " << m_b << ")" << std::endl;
    }
    else
    {
        int** A = nullptr;
        int** B = nullptr;
        int** result = nullptr;
        if (create_mtrx(&A, n_a, m_a) == SUCCESS)
        {
            if (create_mtrx(&B, n_b, m_b) == SUCCESS)
            {
                if (create_mtrx(&result, n_a, m_b) == SUCCESS)
                {

                    std::cout << "\nInput first matrix: " << std::endl;
                    input_mtrx(A, n_a, m_a);

                    std::cout << "\nInput second matrix: " << std::endl;
                    input_mtrx(B, n_b, m_b);

                    const char* alg_names[3] = { "Linear Vinograd algorithm", "Parallel Vinograd algorithm - scheme 1", "Parallel Vinograd algorithm - scheme 2" };
                    int (*algs[3])(int**, int**, int**, int, int, int, int) = { vng_mult, vng_mult_par1, vng_mult_par2 };

                    for (int it = 0; it < 3; it++)
                    {
                        if (algs[it](A, B, result, n_a, m_a, m_b, 2) == SUCCESS)
                        {
                            std::cout << "\nResult of multiplication with " << alg_names[it] << " :" << std::endl;
                            output_mtrx(result, n_a, m_b);
                        }
                        else
                        {
                            std::cout << "\nMultiplication failed" << std::endl;
                        }
                    }

                    delete_mtrx(A, n_a);
                    delete_mtrx(B, n_b);
                    delete_mtrx(result, n_a);

                }
                else
                {
                    delete_mtrx(A, n_a);
                    delete_mtrx(B, n_b);
                    std::cout << "Memory error" << std::endl;
                }
            }
            else
            {
                delete_mtrx(A, n_a);
                std::cout << "Memory error" << std::endl;
            }
        }
        else
        {
            std::cout << "Memory error" << std::endl;
        }
    }
}

int main()
{
    run_all_mults();
}