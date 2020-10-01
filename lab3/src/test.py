import main
import random
import time

import pylab

N = 10

# def test(func, n):
#     time_bubble = 0
#     time_ins = 0
#     time_sel = 0
#
#     for i in range(N):
#         arr = func
#         arr_copy = arr.copy()
#
#         start = time.process_time()
#         main.bubble_sort(arr_copy)
#         stop = time.process_time()
#
#         time_bubble += stop - start
#
#         arr_copy = arr.copy()
#
#         start = time.process_time()
#         main.insertion_sort(arr_copy)
#         stop = time.process_time()
#
#         time_ins += stop - start
#
#         arr_copy = arr.copy()
#
#         start = time.process_time()
#         main.selection_sort(arr_copy)
#         stop = time.process_time()
#
#         time_sel += stop - start
#
#     return (time_bubble / N) * 1000000, (time_ins / N) * 1000000, (time_sel / N) * 1000000

def test(n, arr):
    time_bubble = 0
    time_ins = 0
    time_sel = 0

    for i in range(N):
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
   # arr = list(random.randint(-1000, 1000) for i in range(n))
    arr = list(random.randint(1, 3) for i in range(n))
    return arr

def get_graphics(bubble, ins, sel, xlist, str):

    pylab.xlabel('Длина массива')
    pylab.ylabel('Время, мкс')
    pylab.plot(xlist, bubble, 'r--', label = 'Сортировка пузырьком')
    pylab.plot(xlist, ins, color = 'yellow', label = 'Сортровка вставками')
    pylab.plot(xlist, sel , 'b-.', label = 'Сортировка выбором')
    pylab.legend(loc='upper left')
    pylab.title(str)
    pylab.show()

def get_graphics_comp(y1, s1, y2, s2, xlist, str):

    pylab.xlabel('Длина массива')
    pylab.ylabel('Время, мкс')
    pylab.plot(xlist, y1, 'r--', label = s1)
    pylab.plot(xlist, y2, color = 'yellow', label = s2)
    pylab.legend(loc='upper left')
    pylab.title(str)
    pylab.show()

def get_time_by_len(n, arr):
    print("\n---------------------------------------------------------------")
    print("Замеры времени для длины", n, ":")
    print("\nПроизвольный случай: ")

    time_bubble, time_ins, time_sel = test(n, arr)

    print("Время работы сортировки пузырьком(мкс): ", "{0:.5f}".format(time_bubble))
    print("Время работы сортировки вставками(мкс): ", "{0:.5f}".format(time_ins))
    print("Время работы сортировки выбором(мкс): ", "{0:.5f}".format(time_sel))

# def get_time_by_len(n, best_bubble, best_ins, best_sel, worst_bubble, worst_ins, worst_sel, rand_bubble, rand_ins, rand_sel):
#     print("\n---------------------------------------------------------------")
#     print("Замеры времени для длины", n, ":")
#     print("\nЛучший случай: ")
#
#     time_bubble, time_ins, time_sel = test(get_best_arr(n), n)
#     best_bubble.append(time_bubble)
#     best_ins.append(time_ins)
#     best_sel.append(time_sel)
#     print("Время работы сортировки пузырьком(мкс): ", "{0:.5f}".format(time_bubble))
#     print("Время работы сортировки вставками(мкс): ", "{0:.5f}".format(time_ins))
#     print("Время работы сортировки выбором(мкс): ", "{0:.5f}".format(time_sel))
#
#     print("\nХудший случай: ")
#     time_bubble, time_ins, time_sel = test(get_worst_arr(n), n)
#     worst_bubble.append(time_bubble)
#     worst_ins.append(time_ins)
#     worst_sel.append(time_sel)
#     print("Время работы сортировки пузырьком(мкс): ", "{0:.5f}".format(time_bubble))
#     print("Время работы сортировки вставками(мкс): ", "{0:.5f}".format(time_ins))
#     print("Время работы сортировки выбором(мкс): ", "{0:.5f}".format(time_sel))
#
#     print("\nПроизвольный случай: ")
#     time_bubble, time_ins, time_sel = test(get_random_arr(n), n)
#     rand_bubble.append(time_bubble)
#     rand_ins.append(time_ins)
#     rand_sel.append(time_sel)
#     print("Время работы сортировки пузырьком(мкс): ", "{0:.5f}".format(time_bubble))
#     print("Время работы сортировки вставками(мкс): ", "{0:.5f}".format(time_ins))
#     print("Время работы сортировки выбором(мкс): ", "{0:.5f}".format(time_sel))

if __name__ == "__main__":
    arr = get_random_arr(10000)
    #print(arr)
    get_time_by_len(10000, arr)
    # best_bubble = []
    # best_ins = []
    # best_sel = []
    #
    # worst_bubble = []
    # worst_ins = []
    # worst_sel = []
    #
    # rand_bubble = []
    # rand_ins = []
    # rand_sel = []
    #
    # xlist = []
    # get_time_by_len(10, best_bubble, best_ins, best_sel, worst_bubble, worst_ins, worst_sel, rand_bubble, rand_ins, rand_sel)
    # xlist.append(10)
    #
    # get_time_by_len(50, best_bubble, best_ins, best_sel, worst_bubble, worst_ins, worst_sel, rand_bubble, rand_ins, rand_sel)
    # xlist.append(50)
    #
    # get_time_by_len(100, best_bubble, best_ins, best_sel, worst_bubble, worst_ins, worst_sel, rand_bubble, rand_ins, rand_sel)
    # xlist.append(100)
    #
    # get_time_by_len(300, best_bubble, best_ins, best_sel, worst_bubble, worst_ins, worst_sel, rand_bubble, rand_ins, rand_sel)
    # xlist.append(300)
    #
    # get_time_by_len(500, best_bubble, best_ins, best_sel, worst_bubble, worst_ins, worst_sel, rand_bubble, rand_ins, rand_sel)
    # xlist.append(500)
    #
    # get_time_by_len(1000, best_bubble, best_ins, best_sel, worst_bubble, worst_ins, worst_sel, rand_bubble, rand_ins,
    #                 rand_sel)
    # xlist.append(1000)
    # #
    # # get_graphics(best_bubble, best_ins, best_sel, xlist, "Сравнение времени работы сортировок в лучшем случае")
    # #
    # # get_graphics(worst_bubble, worst_ins, worst_sel, xlist, "Сравнение времени работы сортировок в худшем случае")
    # #
    # # get_graphics(rand_bubble, rand_ins, rand_sel, xlist, "Сравнение времени работы сортировок в произвольном случае")
    #
    # get_graphics_comp(best_bubble, "Сортировка пузырьком", best_ins, "Сортировка вставками", xlist, "Сравнение времени работы сортировок вставками и пузырьком в лучшем случае")
    #
    # get_graphics_comp(worst_ins, "Сортировка вставками", worst_sel, "Сортировка выбором", xlist, "Сравнение времени работы сортировок вставками и выбором в худшем случае")
    #
    # get_graphics_comp(rand_ins, "Сортировка вставками", rand_sel, "Сортировка выбором",  xlist, "Сравнение времени работы сортировок вставками и выбором в произвольном случае")
