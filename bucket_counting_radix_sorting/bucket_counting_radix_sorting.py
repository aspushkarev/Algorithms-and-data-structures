import random
import time

# from quick_merge_external_sorting import quick_sort, qsort, split

# from array import array

random.seed(154)


"""
https://docs.google.com/spreadsheets/d/1tmAdHXR1u9DiEL3epa4aiHA1mst1FgjTknCo9RPF4Ng/edit?usp=sharing
"""


def bucket_sort(array, n):
    """
    Алгоритм блочной сортировки BucketSort O(N)
    :param array: Массив
    :param n: Число элементов массива
    :return: Отсортированный массив
    """
    sorted_array = []
    # Находим максимальное число во всём массиве
    maximum = array[0]
    for j in range(1, n):
        if maximum < array[j]:
            maximum = array[j]
    maximum += 1

    # Создаём массив вёдер (как список списков)
    bucket_list = [[] for z in range(n)]
    # Находим номер ведра
    for j in range(n):
        bucket_number = int((array[j] * n) / maximum)
        bucket_list[bucket_number].append(array[j])
        if len(bucket_list[bucket_number]) > 1:
            bucket_list[bucket_number].sort()
            # arr, x, y = quick_sort(bucket_list[bucket_number], len(bucket_list[bucket_number]))
            # bucket_list[bucket_number] = arr
    # выписываем все элементы по порядку
    for buckets in bucket_list:
        for number in buckets:
            sorted_array.append(number)
    return sorted_array


def counting_sort(array, n, digit):
    """
    Алгоритм сортировки подсчётом O(N)
    :param array: Массив
    :param n: Число элементов массива
    :param digit: Разряды
    :return: Отсортированный массив
    """

    sorted_array = [0] * n

    # Инициализируем список для хранения сумм по каждому разряду
    digits_counts = [0] * 10
    for i in range(0, n):
        index = array[i] // digit
        digits_counts[index % 10] += 1

    # Суммируем все разряды в digits_counts
    for number in range(1, 10):
        digits_counts[number] += digits_counts[number - 1]

    # Движемся по каждому индексу справо налево и проверяем цифры
    i = n - 1
    while i >= 0:
        index = array[i] // digit
        # Сначало уменьшаем сумму на 1 там, где хранится этот разряд
        digits_counts[index % 10] -= 1
        # Присваиваем значение из array[i] в тот индекс массива sorted_array,
        # что равен найденному разряду из digits_counts[array[i]]
        sorted_array[digits_counts[index % 10]] = array[i]
        i -= 1
    return sorted_array


def radix_sort(array, n):
    """
    Алгоритм поразрядной сорттировки O(N)
    :param array:  Массив
    :param n: Число элементов массива
    :return:Отсортированный массив
    """
    maximum = max(array)
    digit = 1
    sorted_array = array
    while maximum // digit > 0:
        sorted_array = counting_sort(sorted_array, n, digit)
        digit *= 10
    return sorted_array


if __name__ == "__main__":

    compare = 0
    assignment = 0
    numbers = [10, 100, 1000, 10000, 10_0000, 1000_000, 10_000_000]
    print('Bucket sorted...')
    for n in numbers:
        arr = [random.randint(1, n) for i in range(n)]
        start = time.process_time()
        # array, compare, assignment = bucket_sort(arr, n)
        array = bucket_sort(arr, n)
        print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')

    print('\nCounting sorted...')
    numbers = [10]
    for n in numbers:
        arr2 = [random.randint(0, n - 1) for i in range(n)]
        start = time.process_time()
        array = counting_sort(arr2, n, 1)
        print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')

    print('\nRadix sorted...')
    numbers = [10, 100, 1000, 10000, 10_0000, 1000_000, 10_000_000]
    for n in numbers:
        arr3 = [random.randint(0, n - 1) for i in range(n)]
        start = time.process_time()
        array = radix_sort(arr3, n)
        print(f'N: {n}\t compare: {compare}\t assignment: {assignment} \t {(time.process_time() - start):.5f} seconds')
