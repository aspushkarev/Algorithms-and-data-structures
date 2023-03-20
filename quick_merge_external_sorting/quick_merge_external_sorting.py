import random
import time

# from array import array

random.seed(154)

# Глобальная переменная!
# Нужен рефакторинг
compare = 0
assignment = 0

"""
https://docs.google.com/spreadsheets/d/1tmAdHXR1u9DiEL3epa4aiHA1mst1FgjTknCo9RPF4Ng/edit?usp=sharing
"""


def quick_sort(array, n):
    """
    Алгоритм быстрой сортировки O(N*LogN)
    :param array: Массив
    :param n: Число элементов массива
    :return: Отсортированный массив, метрики compare, assignment
    """
    qsort(array, 0, n - 1)
    return array, compare, assignment


def qsort(array, left, right):
    """
    Рекурсивная часть алгоритма быстрой сортировки
    :param array: Массив
    :param left: Индекс левого элемента массива
    :param right: Индекс правого элемента массива
    :return:
    """
    if left >= right:
        return
    m = split(array, left, right)  # m - Индекс последнего элемента первой части
    qsort(array, left, m - 1)
    qsort(array, m + 1, right)


def split(array, left, right):
    """
    Алгоритм разделения массива на три части
    Первая - элементы меньше p
    Вторая - элементы больше p
    Третья - неотсортированный массив
    :param array: Массив
    :param left: Индекс левого элемента массива
    :param right: Индекс правого элемента массива
    :return: m - Индекс последнего элемента первой части
    """
    global compare
    global assignment
    p = array[right]    # p - последний (опорный) элемент неотсортированной части
    m = left - 1        # m - последний элемент первой (отсортированной) части
    for j in range(left, right + 1, 1):  # j - первый элемент неотсортированной части
        if array[j] <= p:
            m += 1
            array[m], array[j] = array[j], array[m]
            compare += 1
            assignment += 3
    return m


def merge_sort(array, n):
    """
    Алгоритм сортировки, сначала сортируем (рекурсивно), потом объдиняем
    :param array: Массив
    :param n: Число элементов массива
    :return: Отсортированный массив, метрики compare, assignment
    """
    msort(array, 0, n - 1)
    return array, compare, assignment


def msort(array, left, right):
    """
    Рекурсивный вызов алгоритма merge_sort
    :param array: Массив
    :param left: Левая граница
    :param right: Правая граница
    :return: Массив
    """
    if left >= right:
        return
    medium = int((left + right) / 2)
    msort(array, left, medium)
    msort(array, medium + 1, right)
    merge(array, left, medium, right)


def merge(array, left, medium, right):
    """
    Алгоритм объединения массивов
    :param array: Массив
    :param left: Левая граница
    :param medium: Середина массива
    :param right: Правая граница
    """
    global compare
    compare = 0
    global assignment
    assignment = 0
    temp_array = list(range(right - left + 1))     # Временный список
    a = left            # Указатель на левую часть
    b = medium + 1      # Указатель на правую часть
    t = 0               # Индекс в списке temp
    # Пока в левой и правой части есть элементы
    while a <= medium and b <= right:
        if array[a] < array[b]:
            temp_array[t] = array[a]
            compare += 1
            t += 1
            a += 1
        else:
            temp_array[t] = array[b]
            t += 1
            b += 1
    # Докопируем оставшиеся элементы в левой части
    while a <= medium:
        temp_array[t] = array[a]
        t += 1
        a += 1
    # Докопируем оставшиеся элементы в правой части
    while b <= right:
        temp_array[t] = array[b]
        t += 1
        b += 1
    # Обратное копирование в массив array
    for i in range(left, right + 1, 1):
        array[i] = temp_array[i - left]
    assignment += 2 * (right - left + 1)


if __name__ == "__main__":

    numbers = [10, 100, 1000, 10_000, 100_000, 1000_000, 10_000_000]
    print('Quick sorted...')
    for n in numbers:
        arr = [random.randint(1, n) for i in range(n)]
        start = time.process_time()
        array, compare, assignment = quick_sort(arr, n)
        print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')

    print('\nMerge sorted...')
    for n in numbers:
        arr2 = [random.randint(1, n) for i in range(n)]
        start = time.process_time()
        array, compare, assignment = merge_sort(arr2, n)
        print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
