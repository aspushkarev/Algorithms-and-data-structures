import time
from array import array
from random import random


# вставить item в конце массива
# def add_item(arr, item):
#     return arr.append(item)


# вставить item в конце массива
def add_item(arr, item):
    arr = resize(arr)
    arr[len(arr) - 1] = item
    return arr


# вставить item в конце массива
def add_item_vector_array(arr, item, size, vector):
    if size == len(arr):
        arr = resize_vector(arr, vector)
    arr[len(arr) - 1] = item
    size += 1
    return arr


# вставить item в конце массива
def add_item_factor_array(arr, item, size, factor):
    if size == len(arr):
        arr = resize_factor(arr, factor)
    arr[len(arr) - 1] = item
    size += 1
    return arr


# вставить item по index
def add_item_to_index(arr, item, index):
    return arr.insert(item, index)


# удаление элемента по index
def del_element(arr, index):
    return arr.pop(index)


# Проверка длины массива
def is_empty(arr):
    return len(arr) == 0


# Увеличиваем длину массива на 1
def resize(arr):
    new_array = array('d', range(len(arr) + 1))
    if is_empty(arr):
        new_array = arr
    else:
        for j in range(len(arr)):
            new_array[j] = arr[j]
    arr = new_array
    return arr


# Увеличиваем длину массива на vector
def resize_vector(arr, vector):
    new_array = array('d', range(len(arr) + vector))
    if is_empty(arr):
        new_array = arr
    else:
        for j in range(len(arr)):
            new_array[j] = arr[j]
    arr = new_array
    return arr


# Увеличиваем длину массива умножим на factor
def resize_factor(arr, factor):
    new_array = array('d', range(int(len(arr) * (factor + 1.0))))
    if is_empty(arr):
        new_array = arr
    else:
        for j in range(len(arr)):
            new_array[j] = arr[j]
    arr = new_array
    return arr


# получение элемента массива
def get_item(arr, item):
    return arr[item]


# удаление item из массива
def remove_item(arr, item):
    return arr.pop(item)


# single_array O(n)=N^2
def single_array(total):
    start = time.process_time()
    # my_arr = array('d')     # Пустой массив с плавающей точкой двойной точности
    my_arr = array('d', (random() for i in range(total)))  # массив чисел с плавающей точкой двойной точности
    for i in range(total):
        add_item(my_arr, i)
    print(f'Single_array {total} -> {(time.process_time() - start):.5f} seconds')


# vector_array O(n)=N^2 / 10    vector = 10
def vector_array(total, vector):
    size = 1
    start = time.process_time()
    # my_arr = array('d')     # Пустой массив с плавающей точкой двойной точности
    my_arr = array('d', (random() for i in range(size)))  # массив чисел с плавающей точкой двойной точности
    for i in range(total):
        add_item_vector_array(my_arr, i, size, vector)
    print(f'Vector_array {total} -> {(time.process_time() - start):.5f} seconds')


# factor_array O(n)=logN
def factor_array(total, factor):
    size = 1
    start = time.process_time()
    # my_arr = array('d')     # Пустой массив с плавающей точкой двойной точности
    my_arr = array('d', (random() for i in range(size)))  # массив чисел с плавающей точкой двойной точности
    for i in range(total):
        add_item_factor_array(my_arr, i, size, factor)
    print(f'Factor_array {total} -> {(time.process_time() - start):.5f} seconds')


single_array(5_000)
vector_array(1_000_000, 10)
factor_array(1_000_000, 1.8)
