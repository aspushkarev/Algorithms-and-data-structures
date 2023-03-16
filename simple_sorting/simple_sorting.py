import random
import time
from array import array

random.seed(154)


def init(n) -> array:
    """
    Функция инициализирует массив целых чисел
    диапазоном от 1 до n
    :param n: Целое число для инициализации размера массива
    :return: Массив со случайно сгенерированными целыми числами
    """
    arr = array('L', range(n))
    for i in range(n):
        arr[i] = random.randint(1, n)
    return arr


def bubble_sort(array, n):
    """
    Функция сортировки пузырьковым методом
    :return:
    """
    compare = 0
    assignment = 0
    for j in range(n - 1, 0, -1):
        for i in range(j):
            if array[i] > array[i + 1]:
                compare += 1
                assignment += 2
                array[i], array[i + 1] = array[i + 1], array[i]
    return arr, compare, assignment


n = 10
arr = init(n)
start = time.process_time()
array, compare, assignment = bubble_sort(arr, n)
print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
