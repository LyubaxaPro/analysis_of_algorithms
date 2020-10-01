def print_matrix(matrix):
   for i in range (len(matrix)):
      print(matrix[i])


def read_matrix():
    row_num = int(input("Введите количество строк: "))
    column_num = int(input("Введите количество столбцов: "))
    m = []
    for i in range(row_num):
        arr = list(int(i) for i in input("Введите строку: ").split())
        if (len(arr) != column_num):
            print("Не все столбцы заполнены! Ошибка!")
            i -= 1
        else:
            m.append(arr)
    return m

def standart_multiplication_matrix(m1, m2):
    if len(m2) != len(m1[0]):
        print("Size error!")
        return -1
    else:
        n = len(m1)
        q = len(m2[0])
        m = len(m1[0])
        m3 = [[0] * q for i in range(n)]

        for i in range(0, n):
            for j in range(0, q):
                for k in range(0, m):
                    m3[i][j] = m3[i][j] + m1[i][k] * m2[k][j]
    return m3


def vinograd_multiplication_matrix(m1, m2):
    if len(m2) != len(m1[0]):
        print("Size error!")
        return -1
    else:
        m = len(m1)
        n = len(m1[0])
        q = len(m2[0])
        m3 = [[0] * q for i in range(m)]

        row = [0] * m
        for i in range(0, m):
            for j in range(0, n // 2, 1):
                row[i] = row[i] + m1[i][2 * j] * m1[i][2 * j + 1]

        col = [0] * q
        for j in range(0, q):
            for i in range(0, n // 2, 1):
                col[j] = col[j] + m2[2 * i][j] * m2[2 * i + 1][j]

        for i in range(0, m):
            for j in range(0, q):
                m3[i][j] = -row[i] - col[j]
                for k in range(0, n // 2, 1):
                    m3[i][j] = m3[i][j] + (m1[i][2 * k + 1] + m2[2 * k][j]) * (m1[i][2 * k] + m2[2 * k + 1][j])

        if n % 2 == 1:
            for i in range(0, m):
                for j in range(0, q):
                    m3[i][j] = m3[i][j] + m1[i][n - 1] * m2[n - 1][j]

    return m3


def vinograd_optimizate_multiplication_matrix(m1, m2):
    if len(m2) != len(m1[0]):
        print("Size error!")
        return -1
    else:
        m = len(m1)
        n = len(m1[0])
        q = len(m2[0])
        m3 = [[0] * q for i in range(m)]

        row = [0] * m
        for i in range(0, m):
            for j in range(1, n, 2):
                row[i] -= m1[i][j] * m1[i][j - 1]

        col = [0] * q
        for j in range(0, q):
            for i in range(1, n, 2):
                col[j] -= m2[i][j] * m2[i - 1][j]

        flag = n % 2
        for i in range(0, m):
            for j in range(0, q):
                m3[i][j] = row[i] + col[j]
                for k in range(1, n, 2):
                    m3[i][j] += (m1[i][k - 1] + m2[k][j]) * (m1[i][k] + m2[k - 1][j])
                if (flag):
                    m3[i][j] += m1[i][n - 1] * m2[n - 1][j]
    return m3

if __name__ == "__main__":
    print("Введите матрицу1: ")
    m1 = read_matrix()

    print("Введите матрицу2: ")
    m2 = read_matrix()

    print("Результат, посчитанный классическим алгоритмом: ")
    m_base = standart_multiplication_matrix(m1, m2)
    print_matrix(m_base)

    print("Результат, посчитанный алгоритмом Винограда: ")
    m_vin = vinograd_multiplication_matrix(m1, m2)
    print_matrix(m_vin)

    print("Результат, посчитанный оптимизированным алгоритмом Винограда: ")
    m_opt_vin = vinograd_optimizate_multiplication_matrix(m1, m2)
    print_matrix(m_opt_vin)