import random
import time
from array import array

random.seed(154)

"""
https://docs.google.com/spreadsheets/d/1tmAdHXR1u9DiEL3epa4aiHA1mst1FgjTknCo9RPF4Ng/edit?usp=sharing
"""


def init(n):
    """
    Функция инициализирует массив целых чисел
    диапазоном от 1 до n
    :param n: Целое число для инициализации размера массива
    :return: Массив со случайно сгенерированными целыми числами
    """
    return array('l', (random.randint(1, n) for i in range(n)))


def bubble_sort(array, n):
    """
    Функция сортировки пузырьковым методом
    O(N^2)
    :param array: Массив для сортировки
    :param n: Число элементов массива
    :return: Отсортированный массив, число сравнений и число вставок
    """
    compare = 0
    assignment = 0
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if array[i] > array[i + 1]:
                compare += 1
                assignment += 2
                array[i], array[i + 1] = array[i + 1], array[i]
    return array, compare, assignment


def insertion_sort(array, n):
    """
    Функция сортировки методом вставки
    O(N^2)
    :param array: Массив для сортировки
    :param n: Число элементов массива
    :return: Отсортированный массив, число сравнений и число вставок
    """
    compare = 0
    assignment = 0
    for j in range(n):
        for i in range(j - 1, -1, -1):
            if array[i] > array[i + 1]:
                compare += 1
                assignment += 2
                array[i], array[i + 1] = array[i + 1], array[i]
    return array, compare, assignment


def insertion_shift_sort(array, n):
    """
    Функция сортировки методом вставки со сдвигом
    O(N^2)
    :param array: Массив для сортировки
    :param n: Число элементов массива
    :return: Отсортированный массив, число сравнений и число вставок
    """
    # Алгоритм ещё не доделан. Работает с ошибкой!
    compare = 0
    assignment = 0
    # i = 0
    for j in range(n):
        # k - временная переменная для сохранения элемента j
        k = array[j]
        assignment += 1
        i = 0
        for i in range(j - 1, 0, -1):
            if array[i] > k:
                compare += 1
                assignment += 1
                array[i + 1] = array[i]
        array[i + 1] = k
        assignment += 1
    return array, compare, assignment


def shell_sort(array, n):
    """
    Алгоритм сравнивает элементы отстоящие друг от друга
    на большом расстоянии O(N^1.6)
    :param array: Массив для сортировки
    :param n: Число элементов массива
    :return: Отсортированный массив, число сравнений и число вставок
    """
    compare = 0
    assignment = 0
    gap = int(n / 2)
    while gap > 0:
        for i in range(gap, n, 1):
            j = i
            while j >= gap and array[j - gap] > array[j]:
                compare += 1
                assignment += 2
                array[j - gap], array[j] = array[j], array[j - gap]
                j -= gap
        gap = int(gap / 2)
    return array, compare, assignment


numbers = [10, 100, 1000, 10_000]
print('Bubble sorted...')
for n in numbers:
    arr = [random.randint(1, n) for i in range(n)]
    start = time.process_time()
    array, compare, assignment = bubble_sort(arr, n)
    print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')

print('\nInsertion sorted...')
for n in numbers:
    arr2 = [random.randint(1, n) for j in range(n)]
    start = time.process_time()
    array, compare, assignment = insertion_sort(arr2, n)
    print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
#
# print('\nInsertion shift sorted...')
# for n in numbers:
#     # arr3 = init(n)
#     arr3 = [random.randint(1, n) for j in range(n)]
#     # print(arr3[0:20])
#     start = time.process_time()
#     array, compare, assignment = insertion_shift_sort(arr3, n)
#     print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
#     # print(array[0:20])

print('\nShell sorted...')
numbers = [10, 100, 1000, 10_000, 100_000, 1000_000]
for n in numbers:
    arr4 = [random.randint(1, n) for j in range(n)]
    start = time.process_time()
    array, compare, assignment = shell_sort(arr4, n)
    print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
