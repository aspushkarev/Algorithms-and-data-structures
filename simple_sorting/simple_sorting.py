import random
import time
from array import array

random.seed(154)


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


numbers = [10, 100, 1000, 10_000]
print('Bubble sorted...')
for n in numbers:
    # arr = init(n)
    arr = [random.randint(1, n) for i in range(n)]
    # print(arr[0:20])
    start = time.process_time()
    array, compare, assignment = bubble_sort(arr, n)
    print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
    # print(array[0:20])

print('\nInsertion sorted...')
for n in numbers:
    # arr2 = init(n) 
    arr2 = [random.randint(1, n) for j in range(n)]
    # print(arr2[0:20])
    start = time.process_time()
    array, compare, assignment = insertion_sort(arr2, n)
    print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
    # print(array[0:20])
