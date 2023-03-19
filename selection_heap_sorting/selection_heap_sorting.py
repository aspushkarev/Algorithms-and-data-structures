import random
import time

# from array import array

random.seed(154)

# Пришлось объявить глобальную переменную, что ни есть хорошо!
# В таком алгоритме считает без ошибок, но нужен рефакторинг
compare = 0
assignment = 0

"""
https://docs.google.com/spreadsheets/d/1tmAdHXR1u9DiEL3epa4aiHA1mst1FgjTknCo9RPF4Ng/edit?usp=sharing
"""


def selection_sort(array, n):
    """
    Алгоритм сортировки выбором (поиск максимального элемента в неотсортированной части массива
    и перенос его в отсортированную часть)
    O(N^2)
    :param array: Массив для сортировки
    :param n: Число элементов массива
    :return: Отсортированный массив, число сравнений и число вставок
    """
    global compare
    compare = 0
    global assignment
    assignment = 0
    for j in range(n - 1, 0, -1):
        maximum = 0
        for i in range(j + 1):
            if array[i] > array[maximum]:
                maximum = i
                compare += 1
        array[maximum], array[j] = array[j], array[maximum]
        assignment += 3
    return array, compare, assignment


def heap_sort(array, n):
    """
    Алгоритм пирамидальной сортировки
    O(N*LogN)
    :param array: Массив для сортировки
    :param n: Число элементов массива
    :return: Отсортированный массив, число сравнений и число вставок
    """
    global compare
    compare = 0
    global assignment
    assignment = 0
    for h in range(int((n / 2)) - 1, -1, -1):
        heapify(array, h, n)
    for j in range(n - 1, 0, -1):
        array[0], array[j] = array[j], array[0]
        assignment += 1
        heapify(array, 0, j)
    return array, compare, assignment


def heapify(array, root, n):
    global compare
    global assignment
    x = root
    l = 2 * x + 1  # индекс левого элемента
    r = 2 * x + 2  # индекс правого элемента
    if l < n and array[l] > array[x]:
        x = l
        compare += 1
    if r < n and array[r] > array[x]:
        x = r
        compare += 1
    if x == root:
        return
    array[root], array[x] = array[x], array[root]
    assignment += 1
    heapify(array, x, n)
    return array


if __name__ == "__main__":

    numbers = [10, 100, 1000, 10_000]  # , 100_000]
    print('Selection sorted...')
    for n in numbers:
        arr = [random.randint(1, n) for i in range(n)]
        start = time.process_time()
        array, compare, assignment = selection_sort(arr, n)
        print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')

    numbers = [10, 100, 1000, 10_000, 100_000, 1000_000]
    print('\nHeap sorted...')
    for n in numbers:
        arr2 = [random.randint(1, n) for i in range(n)]
        start = time.process_time()
        array, compare, assignment = heap_sort(arr2, n)
        print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
