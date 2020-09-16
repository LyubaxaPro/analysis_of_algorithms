import sys

def print_matrix(s1, s2, matrix):
    print('0 0 ' + ' '.join([s for s in s2]))
    for i in range(len(s1) + 1):
        print(s1[i - 1] if i != 0 else '0', end='')
        for j in range(len(s2) + 1):
            print(' ' + str(matrix[i][j]), end='')
        print('')


def create_matrix(n, m):
    matrix = [[0] * m for i in range(n)]

    for j in range(m):  # заполняем 0 строку
        matrix[0][j] = j

    for i in range(n):  # заполняем 0 столбец
        matrix[i][0] = i

    return matrix


def levinstein_matrix(s1, s2):
    n = len(s1)
    m = len(s2)

    matrix = create_matrix(n + 1, m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            add, delete, change = matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1]
            if s2[j - 1] != s1[i - 1]:
                change += 1
            matrix[i][j] = min(add, delete, change)

    # print("\nМатрица расстояния Левенштейна")
    # print_matrix(s1, s2, matrix)
    # print("Расстояние Левенштейна = ", matrix[n][m])

    return matrix[n][m]


def levinstein_recursive_matrix(s1, s2):
    n, m = len(s1), len(s2)

    def recursive(s1, s2, n, m, matrix):
        if (matrix[n][m] != -1):
            return matrix[n][m]

        if (n == 0):
            matrix[n][m] = m
            return matrix[n][m]

        if (m == 0 and n > 0):
            matrix[n][m] = n
            return matrix[n][m]

        delete = recursive(s1, s2, n - 1, m, matrix) + 1  # удаление
        add = recursive(s1, s2, n, m - 1, matrix) + 1  # вставка
        flag = 0
        if (s1[n - 1] != s2[m - 1]):
            flag = 1
        change = recursive(s1, s2, n - 1, m - 1, matrix) + flag  # замена
        matrix[n][m] = min(delete, change, add)

        return matrix[n][m]

    matrix = create_matrix(n + 1, m + 1)

    for i in range(n + 1):
        for j in range(m + 1):
            matrix[i][j] = -1

    recursive(s1, s2, n, m, matrix)
    # print("\nМатрица заполненная рекурсивно: ")
    # print_matrix(s1, s2, matrix)
    # print("Расстояние Левенштейна = ", matrix[n][m])

    return matrix[n][m]

def levinstein_recursive(s1, s2):
    n = len(s1)
    m = len(s2)

    if n == 0 or m == 0:
        return abs(n - m)

    flag = 0
    if s1[-1] != s2[-1]:  #если последние символы не равны
        flag = 1

    return min(levinstein_recursive(s1[:- 1], s2) + 1,
               levinstein_recursive(s1, s2[:- 1]) + 1,
               levinstein_recursive(s1[:- 1], s2[:- 1]) + flag)

def damerau_levinstein_matrix(s1, s2):
    n = len(s1)
    m = len(s2)

    matrix = create_matrix(n + 1, m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            add, delete, change = matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1]
            if s2[j - 1] != s1[i - 1]:
                change += 1
            matrix[i][j] = min(add, delete, change)
            if ((i > 1 and j > 1) and s1[i - 1] == s2[j - 2] and s1[i - 2] == s2[j - 1]):
                matrix[i][j] = min(matrix[i][j], matrix[i - 2][j - 2] + 1)
    # print("\nМатрица расстояния Дамерау-Левенштнейна")
    # print_matrix(s1, s2, matrix)
    # print("Расстояние Дамерау-Левенштейна = ", matrix[n][m])

    return matrix[n][m]

def get_distance(s1, s2):
    t1 = levinstein_matrix(s1, s2)

    t2 = levinstein_recursive_matrix(s1, s2)

    t3 = levinstein_recursive(s1, s2)
    print("\nРасстрояние Левенштейна, полученное с использованием рекурсии: ", t3)

    t4 = damerau_levinstein_matrix(s1, s2)

if __name__ == "__main__":
    s1 = input("Введите первую строку: ")
    s2 = input("Введите вторую строку: ")

    get_distance(s1, s2)
