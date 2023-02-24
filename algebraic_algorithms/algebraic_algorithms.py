import time
import numpy as np


def expon_through_multiplication(a, n):
    """
    Вещественное число a > 0.
    Целое число n >= 0.
    Вычислить a^n. Результат вывести на экран в стандартном виде.
    Алгоритм возведения в степень через степень двойки с домножением O(N/2+LogN) = O(N).
    :return: a^n
    """
    if n == 1:
        return a
    return (1 if n == 0
            else expon_through_multiplication(a * a, n // 2) if n % 2 == 0
    else a * expon_through_multiplication(a, n - 1))


def binary_expansion_exponent(a, n):
    """
    Вещественное число a > 0.
    Целое число n >= 0.
    Вычислить a^n. Результат вывести на экран в стандартном виде.
    Алгоритм возведения в степень через двоичное разложение показателя степени O(2LogN) = O(LogN).
    :return: a^n
    """
    degree = a  # Возможные степени a
    result = 1  # Результат (a^n)
    while n >= 1:
        if n % 2 != 0:
            result *= degree  # Если остаток от деления не равен нулю, то умножаем нужные степени двойки
        n //= 2
        degree *= degree
    return result


def fibonacci_iter(n):
    """
    Найти и вывести на экран точное значение N-ого числа Фибоначчи
    Решение задачи через итерацию O(n)
    :param n: целое число N >= 0
    :return: значение N-ого числа Фибоначчи
    """
    a = 0  # Первое слагаемое Фибоначчи
    b = 1  # Второе слагаемое Фибоначчи
    fibonacci = 0  # Результат, число Фибоначчи
    if n <= 1:
        return n
    for i in range(2, n + 1):
        fibonacci = a + b
        a = b
        b = fibonacci
    return fibonacci


def fibonacci_recursive(n):
    """
    Найти и вывести на экран точное значение N-ого числа Фибоначчи
    Решение задачи через рукурсию O(2^n)
    :param n: целое число N >= 0
    :return: значение N-ого числа Фибоначчи
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_matrix(n):
    """
    Алгоритм поиска чисел Фибоначчи O(LogN) через умножение матриц
    :param n: целое число N >= 0
    :return: значение N-ого числа Фибоначчи
    """
    a = b = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    if n in [1, 2]:
        return 1
    for i in range(3, n + 1):
        a1 = (a[0][0] * b[0][0]) + (a[0][1] * b[1][0])
        a2 = (a[0][0] * b[0][1]) + (a[0][1] * b[1][1])
        a3 = (a[1][0] * b[0][0]) + (a[1][1] * b[1][0])
        a4 = (a[1][0] * b[0][1]) + (a[1][1] * b[1][1])
        b = [[a1, a2], [a3, a4]]
    fibonacci = b[0][0]
    return fibonacci


def prime_count(n):
    """
    Найти количество простых чисел от 1 до N
    Решение задачи через несколько оптимизаций перебора делителей O(n^2)
    :param n: Целое число N >= 1
    :return: Число простых чисел
    """
    # start = time.process_time()
    result = 0
    for i in range(n + 1):
        count = 0
        if i == 1:          # 1 сразу не походит
            continue
        if i == 2:          # если пришла 2, то плюсуем к счётчику и переходим к следующей итерации
            result += 1
            continue
        if i % 2 == 0:      # если без остатка делится на два, то число не простое, переход к след. итерации
            continue
        for number in range(1, i + 1, 2):   # шаг 2, так как уже исключили деление без остатка на 2
            if i % number == 0:
                count += 1
        if count == 2:
            result += 1
    # time_job = time.process_time() - start
    # print(f'{n} -> {(time.process_time() - start):.4f} ms')
    return result


def func1():
    print(expon_through_multiplication(2, 10))
    print(expon_through_multiplication(123456789, 0))
    print(expon_through_multiplication(1.001, 1_000))
    print(expon_through_multiplication(1.0001, 10_000))
    print(expon_through_multiplication(1.00001, 100_000))
    print(expon_through_multiplication(1.000001, 1_000_000))
    print(expon_through_multiplication(1.0000001, 10_000_000))
    print(expon_through_multiplication(1.00000001, 100_000_000))
    print(expon_through_multiplication(1.000000001, 1_000_000_000))
    print(expon_through_multiplication(1.0000000001, 10_000_000_000))


def func2():
    print(binary_expansion_exponent(2, 10))
    print(binary_expansion_exponent(123456789, 0))
    print(binary_expansion_exponent(1.001, 1_000))
    print(binary_expansion_exponent(1.0001, 10_000))
    print(binary_expansion_exponent(1.00001, 100_000))
    print(binary_expansion_exponent(1.000001, 1_000_000))
    print(binary_expansion_exponent(1.0000001, 10_000_000))
    print(binary_expansion_exponent(1.00000001, 100_000_000))
    print(binary_expansion_exponent(1.000000001, 1_000_000_000))
    print(binary_expansion_exponent(1.0000000001, 10_000_000_000))


def func3():
    print(fibonacci_iter(0))
    print(fibonacci_iter(1))
    print(fibonacci_iter(2))
    print(fibonacci_iter(3))
    print(fibonacci_iter(4))
    print(fibonacci_iter(5))
    print(fibonacci_iter(10))
    print(fibonacci_iter(100))
    print(fibonacci_iter(1000))
    print(fibonacci_iter(10_000))
    print(fibonacci_iter(100_000))
    # print(fibonacci_iter(1000_000))   # Вычисляет, но очень долго, поэтому закоментировал
    # print(fibonacci_iter(10_000_000)) # Вычисляет, но очень долго, поэтому закоментировал


def func4():
    print(fibonacci_recursive(0))
    print(fibonacci_recursive(1))
    print(fibonacci_recursive(2))
    print(fibonacci_recursive(3))
    print(fibonacci_recursive(4))
    print(fibonacci_recursive(5))
    print(fibonacci_recursive(10))
    # print(fibonacci_recursive(100))         # Вычисляет, но очень долго, поэтому закоментировал
    # print(fibonacci_recursive(1000))        # Вычисляет, но очень долго, поэтому закоментировал
    # print(fibonacci_recursive(10_000))      # Вычисляет, но очень долго, поэтому закоментировал
    # print(fibonacci_recursive(100_000))     # Вычисляет, но очень долго, поэтому закоментировал
    # print(fibonacci_recursive(1000_000))    # Вычисляет, но очень долго, поэтому закоментировал
    # print(fibonacci_recursive(10_000_000))  # Вычисляет, но очень долго, поэтому закоментировал


def func5():
    print(fibonacci_matrix(0))
    print(fibonacci_matrix(1))
    print(fibonacci_matrix(2))
    print(fibonacci_matrix(3))
    print(fibonacci_matrix(4))
    print(fibonacci_matrix(5))
    print(fibonacci_matrix(10))
    print(fibonacci_matrix(100))
    print(fibonacci_matrix(1000))
    print(fibonacci_matrix(10_000))
    print(fibonacci_matrix(100_000))
    # print(fibonacci_matrix(1000_000))     # Вычисляет, но очень долго, поэтому закоментировал
    # print(fibonacci_matrix(10_000_000))   # Вычисляет, но очень долго, поэтому закоментировал


def func6():
    print(prime_count(10))
    print(prime_count(1))
    print(prime_count(2))
    print(prime_count(3))
    print(prime_count(4))
    print(prime_count(5))
    print(prime_count(100))
    print(prime_count(1000))
    print(prime_count(10_000))
    # print(prime_count(1_000_000))         # Вычисляет, но очень долго, поэтому закоментировал
    # print(prime_count(10_000_000))        # Вычисляет, но очень долго, поэтому закоментировал
    # print(prime_count(100_000_000))       # Вычисляет, но очень долго, поэтому закоментировал
    # print(prime_count(1_000_000_000))     # Вычисляет, но очень долго, поэтому закоментировал
    # print(prime_count(123456789))         # Вычисляет, но очень долго, поэтому закоментировал


if __name__ == "__main__":
    func1()
    func2()
    func3()
    func4()
    func5()
    func6()

