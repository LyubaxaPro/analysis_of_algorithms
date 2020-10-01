import main
import string
import random
import time

import numpy as np
import matplotlib.pyplot as plt

N = 100

def test(len):
    time_lev_rec = 0
    time_lev_matrix_rec = 0
    time_lev_matrix = 0
    time_dlev = 0

    for i in range(N):
        s1 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))
        s2 = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=len))

        start = time.process_time()
        main.levinstein_matrix(s1, s2)
        stop = time.process_time()

        time_lev_matrix += stop - start

        start = time.process_time()
        main.levinstein_recursive_matrix(s1, s2)
        stop = time.process_time()

        time_lev_matrix_rec += stop - start

        start = time.process_time()
        main.levinstein_recursive(s1, s2)
        stop = time.process_time()

        time_lev_rec += stop - start

        start = time.process_time()
        main.damerau_levinstein_matrix(s1, s2)
        stop = time.process_time()

        time_dlev += stop - start

    return (time_lev_matrix / N) * 1000000, (time_lev_matrix_rec / N) * 1000000, (time_lev_rec / N) * 1000000, (time_dlev / N) * 1000000

def print_results(count):
    time_lev_matrix, time_lev_matrix_rec, time_lev_rec, time_dlev = test(count)
    print("\n--------------------------------------------------------------------------------------")
    print("Время работы функции при n = : ", count)
    print("Матричный способ нахождения расстояния Левенштейна: ", "{0:.6f}".format(time_lev_matrix), "мкс")
    print("Матричный способ нахождения расстояния Левенштейна с использованием рекурсии: ", "{0:.6f}".format(time_lev_matrix_rec), "мкс")
    print("Нахождение расстояния Левенштейна с использованием рекурсии: ", "{0:.6f}".format(time_lev_rec), "мкс")
    print("Нахождение расстояния Дамерау-Левенштейна без использования рекурсии: ", "{0:.6f}".format(time_dlev), "мкс")

    return

if __name__ == "__main__":
    # for i in range(10):
    #     print_results(i)


