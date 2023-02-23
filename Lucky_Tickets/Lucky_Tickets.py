def lucky_tickets():
    """
    Junior level
    Посчитать, сколько существует счастливых 6-значных билетов
    O(10^N)
    """

    score = 0
    for a1 in range(10):
        for a2 in range(10):
            for a3 in range(10):
                for b1 in range(10):
                    for b2 in range(10):
                        for b3 in range(10):
                            if a1 + a2 + a3 == b1 + b2 + b3:
                                score += 1
    print('Счастливых 6-значных билетов', score)


lucky_tickets()
