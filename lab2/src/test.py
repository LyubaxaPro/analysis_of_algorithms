import random
import time
import main
import pylab

COUNT = 10

def make_matrix(N):
    m = []
    for i in range(N):
        arr = list(random.randint(-100, 100) for i in range(N))
        m.append(arr)
    return m

def test(N):
    time_base = 0
    time_vin = 0
    time_vin_opt = 0

    for i in range(COUNT):
        m1 = make_matrix(N)
        m2 = make_matrix(N)
        start = time.process_time()
        m_base = main.standart_multiplication_matrix(m1, m2)
        stop = time.process_time()

        time_base += stop - start

        start = time.process_time()
        m_vin = main.vinograd_multiplication_matrix(m1, m2)
        stop = time.process_time()

        time_vin += stop - start

        start = time.process_time()
        m_vin_opt = main.vinograd_optimizate_multiplication_matrix(m1, m2)
        stop = time.process_time()

        time_vin_opt += stop - start

    return (time_base / COUNT) * 1000000, (time_vin/ COUNT) * 1000000, (time_vin_opt / COUNT) * 1000000

def get_graphics(base, vin, vin_opt, xlist, str):

    pylab.xlabel('Длина массива')
    pylab.ylabel('Время, мкс')
    pylab.plot(xlist, base, color='red', label = 'Классическое умножение')
    pylab.plot(xlist, vin, color='green', label = 'Алгоритм Винограда')
    pylab.plot(xlist, vin_opt , color='blue', label = 'Оптимизированный алгоритм Винограда')
    pylab.legend(loc='upper left')
    pylab.title(str)
    pylab.show()

def get_time_by_len(l_list):
    time_base = []
    time_vin = []
    time_vin_opt = []

    for l in l_list:
        t_base, t_vin, t_vin_opt = test(l)
        time_base.append(t_base)
        time_vin.append(t_vin)
        time_vin_opt.append(t_vin_opt)

    return time_base, time_vin, time_vin_opt

if __name__ == "__main__":
    l_list_even = [2, 10, 50, 100, 200, 300, 400]
    l_list = [3, 11, 55, 101, 203, 305, 403]

    time_base_e, time_vin_e, time_vin_opt_e = get_time_by_len(l_list_even)
    get_graphics(time_base_e, time_vin_e, time_vin_opt_e, l_list_even, "Длина чётная")

    time_base, time_vin, time_vin_opt = get_time_by_len(l_list)
    get_graphics(time_base, time_vin, time_vin_opt, l_list, "Длина нечётная")

