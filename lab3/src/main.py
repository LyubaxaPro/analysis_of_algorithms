def bubble_sort(arr):
    i = 0
    flag = False
    while (i < len(arr)):
        if (i + 1 != len(arr) and arr[i] > arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            flag = True
        i += 1

        if (i == len(arr) and flag):
            flag = False
            i = 0
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

if __name__ == "__main__":
    print("Введите массив:")
    arr = list(int(i) for i in input().split())
    arr_copy = arr.copy()

    print("\nРезультат сортировки пузырьком c флагом: ")
    bubble_sort(arr_copy)
    print(arr_copy)

    # arr_copy = arr.copy()
    #
    # print("\nРезультат сортировки вставками: ")
    # insertion_sort(arr_copy)
    # print(arr_copy)
    #
    # arr_copy = arr.copy()
    #
    # print("\nРезультат сортировки выбором: ")
    # selection_sort(arr_copy)
    # print(arr_copy)