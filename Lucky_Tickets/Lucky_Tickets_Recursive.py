def lucky_tickets_recursive(n: int, sum_a: int, sum_b: int):
    """
    Счастливые билеты 20

    Билет с 2N значным номером считается счастливым,
    если сумма N первых цифр равна сумме последних N цифр.
    Посчитать, сколько существует счастливых 2N-значных билетов.

    Начальные данные: число N от 1 до 10.
    Вывод результата: количество 2N-значных счастливых билетов.
    """
    global count
    if n == 0:
        if sum_a == sum_b:
            count += 1
        return
    for a in range(10):
        for b in range(10):
            lucky_tickets_recursive(n - 1, sum_a + a, sum_b + b)
    return count


count = 0
number = int(input('Введите натуральное число от 1 до 10: '))
print(lucky_tickets_recursive(number, 0, 0))
