import main
import string
import random
import time
N = 100

def test(len):
    time_lev_rec = 0
    time_lev_matrix_rec = 0
    time_lev_matrix = 0
    time_dlev = 0

    for i in range(N):
        s1 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))
        s2 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))

        start = time.time()
        main.levinstein_matrix(s1, s2)
        stop = time.time()

        time_lev_matrix += stop - start

        start = time.time()
        main.levinstein_recursive_matrix(s1, s2)
        stop = time.time()

        time_lev_matrix_rec += stop - start

        start = time.time()
        main.levinstein_recursive(s1, s2)
        stop = time.time()

        time_lev_rec += stop - start

        start = time.time()
        main.damerau_levinstein_matrix(s1, s2)
        stop = time.time()

        time_dlev += stop - start

    return time_lev_matrix / N, time_lev_matrix_rec / N, time_lev_rec / N, time_dlev / N


if __name__ == "__main__":

    time_lev_matrix5, time_lev_matrix_rec5, time_lev_rec5, time_dlev5 = test(5)
    print("Количество тиков при n = 5: ")
    print("Матричный способ нахождения расстояния Левенштейна: ", time_lev_matrix5)
    print("Матричный способ нахождения расстояния Левенштейна с использованием рекурсии: ", time_lev_matrix_rec5)
    print("Нахождение расстояния Левенштейна с использованием рекурсии: ", time_lev_rec5)
    print("Нахождение расстояния Дамерау-Левенштейна без использования рекурсии: ", time_dlev5)

    print("\n------------------------------------------------------------------------------------------------------")
    time_lev_matrix10, time_lev_matrix_rec10, time_lev_rec10, time_dlev10 = test(10)
    print("Количество тиков при n = 10: ")
    print("Матричный способ нахождения расстояния Левенштейна: ", time_lev_matrix10)
    print("Матричный способ нахождения расстояния Левенштейна с использованием рекурсии: ", time_lev_matrix_rec10)
    print("Нахождение расстояния Левенштейна с использованием рекурсии: ", time_lev_rec10)
    print("Нахождение расстояния Дамерау-Левенштейна без использования рекурсии: ", time_dlev10)

    print("\n------------------------------------------------------------------------------------------------------")
    time_lev_matrix20, time_lev_matrix_rec20, time_lev_rec20, time_dlev20 = test(20)
    print("Количество тиков при n = 20: ")
    print("Матричный способ нахождения расстояния Левенштейна: ", time_lev_matrix20)
    print("Матричный способ нахождения расстояния Левенштейна с использованием рекурсии: ", time_lev_matrix_rec20)
    print("Нахождение расстояния Левенштейна с использованием рекурсии: ", time_lev_rec20)
    print("Нахождение расстояния Дамерау-Левенштейна без использования рекурсии: ", time_dlev20)

    print("\n------------------------------------------------------------------------------------------------------")
    time_lev_matrix50, time_lev_matrix_rec50, time_lev_rec50, time_dlev50 = test(50)
    print("Количество тиков при n = 50: ")
    print("Матричный способ нахождения расстояния Левенштейна: ", time_lev_matrix50)
    print("Матричный способ нахождения расстояния Левенштейна с использованием рекурсии: ", time_lev_matrix_rec50)
    print("Нахождение расстояния Левенштейна с использованием рекурсии: ", time_lev_rec50)
    print("Нахождение расстояния Дамерау-Левенштейна без использования рекурсии: ", time_dlev50)

    print("\n------------------------------------------------------------------------------------------------------")
    time_lev_matrix100, time_lev_matrix_rec100, time_lev_rec100, time_dlev100 = test(100)
    print("Количество тиков при n = 100: ")
    print("Матричный способ нахождения расстояния Левенштейна: ", time_lev_matrix100)
    print("Матричный способ нахождения расстояния Левенштейна с использованием рекурсии: ", time_lev_matrix_rec100)
    print("Нахождение расстояния Левенштейна с использованием рекурсии: ", time_lev_rec100)
    print("Нахождение расстояния Дамерау-Левенштейна без использования рекурсии: ", time_dlev100)


