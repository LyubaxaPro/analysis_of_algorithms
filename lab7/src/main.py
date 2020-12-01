import csv
import time
from matplotlib import pylab

def read_data():
    players_dict = {}
    with open('players.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            players_dict[row['PLAYER_ID']] = row['PLAYER_NAME']
    return players_dict

def search_simple(key, dict):
    for dict_key in dict.keys():
        if key == dict_key:
            return dict[key]
    return None

def bin_search(key, sorted_dict):
    sorted_keys = list(sorted_dict.keys())

    i = 0
    j = len(sorted_dict) - 1
    m = int(j / 2)

    while sorted_keys[m] != key and i < j:
        if key > sorted_keys[m]:
            i = m + 1
        else:
            j = m - 1
        m = int((i + j) / 2)
    if i > j:
        return None
    else:
        return sorted_dict[sorted_keys[m]]

def frequency_analysis(dict):
    frequency_dict = {}
    for d in dict.keys():
        if d[0] in frequency_dict.keys():
            frequency_dict[d[0]] += 1
        else:
            frequency_dict[d[0]] = 1

    s = []
    for l in frequency_dict.keys():
        k = {}
        k['letter'] = l
        k['count'] = frequency_dict[l]
        k['dict'] = {}
        for d in dict.keys():
            if d[0] == l:
                k['dict'][d] = dict[d]

        sorted_list = sorted(k['dict'].items())
        sorted_dict = {}
        for i in range(len(sorted_list)):
            sorted_dict[sorted_list[i][0]] = sorted_list[i][1]
        k['dict'] = sorted_dict

        s.append(k)


    s.sort(key=lambda val: val['count'], reverse=True)
    return s


def combined_search(key, segment_list):

    segment_dict = {}
    for i in range(len(segment_list)):
        if segment_list[i]['letter'] == key[0]:
            segment_dict = segment_list[i]["dict"]

    if len(segment_dict) == 0:
        return None

    sorted_keys = list(sorted_dict.keys())

    i = 0
    j = len(sorted_dict) - 1
    m = int(j / 2)

    while sorted_keys[m] != key and i < j:
        if key > sorted_keys[m]:
            i = m + 1
        else:
            j = m - 1
        m = int((i + j) / 2)
    if i > j:
        return None
    else:
        return sorted_dict[sorted_keys[m]]

def sort(dict):
    sorted_list = sorted(dict.items())
    sorted_dict = {}
    for i in range(len(sorted_list)):
        sorted_dict[sorted_list[i][0]] = sorted_list[i][1]
    return sorted_dict

def get_time(func, arg):
    sum = 0
    for i in range(100):
        start = time.time()
        func(arg)
        sum += (time.time() - start)
    return round(sum / 100, 6)

def get_time_search(func, key, dict):
    sum = 0
    for i in range(100):
        start = time.time()
        func(key, dict)
        sum += (time.time() - start)
    return sum / 100

def test_time(dict):
    time_simple = []
    time_bin = []
    time_combined = []

    #-------------------------------------------------
    print("Лексикографическая сортировка ", get_time(sort, dict), "cекунд")
    print("Частотный анализ и лексикографическая сортировка ", get_time(frequency_analysis, dict), "cекунд")

    sorted_dict = sort(dict)
    segment_list = frequency_analysis(dict)

    print("\nЛучший случай поиска ключа")
    print("Алгоритм полного перебора", get_time_search(search_simple, '202711', dict), "cекунд")
    print('Aлгоритм бинарного поиска', get_time_search(bin_search, '201242', sorted_dict), "секунд")
    # print(list(sorted_dict.keys())[int(len(sorted_dict) / 2)]) - 201242 - лучший случай для бинарного поиска - центральный элемент отсортированного словаря

    #print(list(segment_list[0]['dict'].keys())[int(segment_list[0]['count'] / 2)]) - 203094
    print('Комбинированный алгоритм', get_time_search(combined_search, '203094', segment_list), "секунд")

    print("\nХудший случай поиска ключа")
    print("Алгоритм полного перебора", get_time_search(search_simple, '1628778', dict), "cекунд")
    print('Aлгоритм бинарного поиска', get_time_search(bin_search, '980', sorted_dict), "секунд")
    #print(list(sorted_dict.keys())[len(sorted_dict.keys()) - 1]) #- 980 - худший случай для бинарного поиска - центральный элемент отсортированного словаря

   # print(list(segment_list[len(segment_list) - 1]['dict'].keys())[int(segment_list[len(segment_list) - 1]['count'] - 1)]) #- 500032
    print('Комбинированный алгоритм', get_time_search(combined_search, '500032', segment_list), "секунд")

    print("\nПоиск несуществующего ключа")
    print("Алгоритм полного перебора", get_time_search(search_simple, '0', dict), "cекунд")
    print('Aлгоритм бинарного поиска', get_time_search(bin_search, '0', sorted_dict), "секунд")
    print('Комбинированный алгоритм', get_time_search(combined_search, '0', segment_list), "секунд")


    print("\nПоиск случайного ключа")
    print("Алгоритм полного перебора", get_time_search(search_simple, '1628935', dict), "cекунд")
    print('Aлгоритм бинарного поиска', get_time_search(bin_search, '1628935', sorted_dict), "секунд")
    print('Комбинированный алгоритм', get_time_search(combined_search, '1628935', segment_list), "секунд")

    x_list = [i for i in range(len(dict.keys()))]
    for d in list(dict.keys()):
        time_simple.append(get_time_search(search_simple,d, dict))
        time_bin.append(get_time_search(bin_search, d, sorted_dict))
        time_combined.append(get_time_search(combined_search, d, segment_list))

    pylab.xlabel('Индекс ключа')
    pylab.ylabel('Время, секунды')
    pylab.plot(x_list, time_simple, 'r--', label='Полный перебор')
    pylab.plot(x_list, time_bin, color='yellow', label='Бинарный поиск')
    pylab.plot(x_list, time_combined, 'b-.', label='Комбинированный')
    pylab.legend(loc='upper left')
    pylab.show()

    x1_list = []
    time_simple1 = []
    time_bin1 = []
    time_combined1 = []

    for i in range(len(x_list)):
        if i % 15 == 0:
            x1_list.append(i)
            time_simple1.append(time_simple[i])
            time_bin1.append(time_bin[i])
            time_combined1.append(time_combined[i])

    pylab.xlabel('Индекс ключа')
    pylab.ylabel('Время, секунды')
    pylab.plot(x1_list, time_simple1, 'r--', label='Полный перебор')
    pylab.plot(x1_list, time_bin1, color='yellow', label='Бинарный поиск')
    pylab.plot(x1_list, time_combined1, 'b-.', label='Комбинированный')
    pylab.legend(loc='upper left')
    pylab.show()

    print("\nАлгоритм перебором ")
    print("Максимальное время выполнения = ", max(time_simple))
    print("Минимальное время выполнения = ", min(time_simple))
    print("Среднее время выполнения = ", sum(time_simple) / len(time_simple))

    print("\nБинарный поиск ")
    print("Максимальное время выполнения = ", max(time_bin))
    print("Минимальное время выполнения = ", min(time_bin))
    print("Среднее время выполнения = ", sum(time_bin) / len(time_bin))

    print("\nКомбинированный алгоритм ")
    print("Максимальное время выполнения = ", max(time_combined))
    print("Минимальное время выполнения = ", min(time_combined))
    print("Среднее время выполнения = ", sum(time_combined) / len(time_combined))




if __name__ == "__main__":
    players_dict = read_data()

    sorted_list = sorted(players_dict.items())
    sorted_dict = {}
    for i in range(len(sorted_list)):
        sorted_dict[sorted_list[i][0]] = sorted_list[i][1]

    segment_list = frequency_analysis(players_dict)

    key = input("Введите ключ: ")

    print("Результат работы алгоритма полного перебора: ")
    t = search_simple(key, players_dict)
    if (t == None):
        print("Ключ не найден")
    else:
        print(t)

    print("Результат работы алгоритма бинарного поиска: ")
    t = bin_search(key, sorted_dict)
    if (t == None):
        print("Ключ не найден")
    else:
        print(t)

    print("Результат работы комбинированного алгоритма: ")
    t = combined_search(key,segment_list)
    if (t == None):
        print("Ключ не найден")
    else:
        print(t)

   # test_time(players_dict)



