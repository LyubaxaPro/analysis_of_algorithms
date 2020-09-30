import main
import random
import time

N = 100

def test(func, n):
    time_bubble = 0
    time_ins = 0
    time_sel = 0

    for i in range(N):
        arr = func
        arr_copy = arr.copy()

        start = time.process_time()
        main.bubble_sort(arr_copy)
        stop = time.process_time()

        time_bubble += stop - start

        arr_copy = arr.copy()

        start = time.process_time()
        main.insertion_sort(arr_copy)
        stop = time.process_time()

        time_ins += stop - start

        arr_copy = arr.copy()

        start = time.process_time()
        main.selection_sort(arr_copy)
        stop = time.process_time()

        time_sel += stop - start

    return (time_bubble / N) * 1000000, (time_ins / N) * 1000000, (time_sel / N) * 1000000

def get_best_arr(n):
    x = random.randint(-1000, 1000)
    arr = list(x + i for i in range(n))
    return arr

def get_worst_arr(n):
    x = random.randint(-1000, 1000)
    arr = list(x - i for i in range(n))
    return arr

def get_random_arr(n):
    arr = list(random.randint(-1000, 1000) for i in range(n))
    return arr

def get_time_by_len(n):
    print("\n---------------------------------------------------------------")
    print("Замеры времени для длины", n, ":")
    print("\nЛучший случай: ")
    time_bubble, time_ins, time_sel = test(get_best_arr(n), n)
    print("Время работы сортировки пузырьком(мкс): ", "{0:.5f}".format(time_bubble))
    print("Время работы сортировки вставками(мкс): ", "{0:.5f}".format(time_ins))
    print("Время работы сортировки выбором(мкс): ", "{0:.5f}".format(time_sel))

    print("\nХудший случай: ")
    time_bubble, time_ins, time_sel = test(get_worst_arr(n), n)
    print("Время работы сортировки пузырьком(мкс): ", "{0:.5f}".format(time_bubble))
    print("Время работы сортировки вставками(мкс): ", "{0:.5f}".format(time_ins))
    print("Время работы сортировки выбором(мкс): ", "{0:.5f}".format(time_sel))

    print("\nПроизвольный случай: ")
    time_bubble, time_ins, time_sel = test(get_random_arr(n), n)
    print("Время работы сортировки пузырьком(мкс): ", "{0:.5f}".format(time_bubble))
    print("Время работы сортировки вставками(мкс): ", "{0:.5f}".format(time_ins))
    print("Время работы сортировки выбором(мкс): ", "{0:.5f}".format(time_sel))

if __name__ == "__main__":
    get_time_by_len(10)
    get_time_by_len(50)
    get_time_by_len(100)
    get_time_by_len(300)
    get_time_by_len(500)


