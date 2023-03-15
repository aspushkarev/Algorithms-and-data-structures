"""
https://gekomad.github.io/Cinnamon/BitboardCalculator/
"""
from array import array


def get_king_move(position):
    """
    Функция вычисляет возможные ходы короля на шахматной доске (bitboard)
    :param position: Позиция короля
    :return: mask Маска с вариантами возможного хода
    """
    # Задаём начальную позицию короля
    king = 1 << position

    # Запрещаем королю со столбца А ходить налево, за границу bitboard
    not_a = 18374403900871474942
    king_a = king & not_a

    # Запрещаем королю ходить направо за столбец H, за границу bitboard
    not_h = 9187201950435737471
    king_h = king & not_h

    # Запрещаем королю ходить наверх за поле 8, за границу bitboard
    not_eight = 72057594037927935
    king_eight = king & not_eight

    mask = (king_a & king_eight) << 7 | king_eight << 8 | (king_h & king_eight) << 9 | \
           king_a >> 1 | king_h << 1 | \
           king_a >> 9 | king >> 8 | king_h >> 7
    return mask


def get_horse_move(position):
    """
    Функция вычисляет возможные ходы лошади на шахматной доске (bitboard)
    :param position: Позиция лошади
    :return: mask Маска с вариантами возможного хода
    """
    # Начальная позиция лошади
    horse = 1 << position

    # Запрещаем лошади со столбца А ходить налево, за границу bitboard
    not_agh = 4485090715960753726
    horse_a = horse & not_agh

    # Запрещаем лошади ходить вниз за поле 1, за границу bitboard
    not_one = 18446744073709551360
    horse_one = horse & not_one

    # К сожалению эту маску я не доделал до конца, проходят тесты 3 из 10!!!!!
    mask = horse_a << 15 | horse << 17 | \
           horse_one << 6 | horse << 10 | \
           horse_a >> 10 | horse >> 6 | \
           horse >> 17 | horse >> 15
    return mask


def get_population_count_one(mask):
    """
    Алгоритм подсчёта единичных битов в числе
    сдвигая маску вправо на 1 бит пока не будет 0: O(N)
    :param mask: Маска фигуры на bitboard
    :return: Количество единичных бит
    """
    count = 0
    while mask > 0:
        count += mask & 1
        mask >>= 1
    return count


def get_population_count_one_v2(mask):
    """
    Алгоритм подсчёта единичных битов в числе
    вычитая от маски 1 и далее делая логическое &
    между mask и (mask - 1), тем самым обращая
    младший бит в 0: O(N)
    :param mask: Маска фигуры на bitboard
    :return: Количество единичных бит
    """
    count = 0
    while mask > 0:
        count += 1
        mask &= mask - 1
    return count


def init_bits():
    """
    Функция инициализирует массив целых чисел на 256
    элементов, который будет содержать правильные ответы
    (сколько бит в каждом числе от 0 до 256)
    :return: массив бит
    """
    # Инициализируем массив целых чисел
    bits = array('L', range(256))
    for i in range(256):
        bits[i] = get_population_count_one_v2(i)
    return bits


def get_population_count_one_v3(mask, arr_bits):
    """
    Алгоритм подсчёта единичных битов в числе через кеширование
    O(√N)
    :param mask: Маска фигуры на bitboard
    :param arr_bits: массив с битами в каждом числе от 0 до 256
    :return: Количество единичных бит
    """
    count = 0
    while mask > 0:
        # Выделяем последние 8 бит и подсчитываем
        count += arr_bits[mask & 255]
        # Сдвигаем на 8 единиц вправо для перехода на следующий слой
        mask >>= 8
    return count


def test_king_move(positions):
    """
    Проверяем ходы короля
    """
    for position in positions:
        print(get_king_move(position))


def test_horse_move(positions):
    """
    Проверяем ходы лошади
    """
    for position in positions:
        print(get_horse_move(position))


def test_population_count_one(masks):
    """"
    Проверяем возможное количество единичных бит
    """
    for mask in masks:
        print(get_population_count_one(mask))


def test_population_count_one_v2(masks):
    """"
    Проверяем возможное количество единичных бит
    """
    for mask in masks:
        print(get_population_count_one_v2(mask))


def test_population_count_one_v3(masks, arr_bits):
    """"
    Проверяем возможное количество единичных бит
    """
    for mask in masks:
        print(get_population_count_one_v3(mask, arr_bits))


print('Маска короля:')
king_positions = [0, 1, 7, 8, 10, 15, 54, 55, 56, 63]
test_king_move(king_positions)
print('\n')

print('Маска коня:')
horse_positions = [0, 1, 2, 36, 47, 48, 54, 55, 56, 63]
test_horse_move(horse_positions)
print('\n')

print('Подсчёт количества бит в числе для короля через сдвиг маски вправо на 1 бит:')
masks_king = [770, 1797, 49216, 197123, 920078, 12599488,
              16186183351374184448, 13853283560024178688, 144959613005987840, 4665729213955833856]
test_population_count_one(masks_king)
print('\n')

print('Подсчёт количества бит в числе для коня через сдвиг маски вправо на 1 бит:')
masks_horse = [132096, 329728, 659712, 11333767002587136, 4620693356194824192, 288234782788157440,
               1152939783987658752, 2305878468463689728, 1128098930098176, 9077567998918656]
test_population_count_one(masks_horse)
print('\n')

print('Подсчёт количества бит в числе для короля вычитая из маски 1:')
masks_king = [770, 1797, 49216, 197123, 920078, 12599488,
              16186183351374184448, 13853283560024178688, 144959613005987840, 4665729213955833856]
test_population_count_one_v2(masks_king)
print('\n')

print('Подсчёт количества бит в числе для коня вычитая из маски 1:')
masks_horse = [132096, 329728, 659712, 11333767002587136, 4620693356194824192, 288234782788157440,
               1152939783987658752, 2305878468463689728, 1128098930098176, 9077567998918656]
test_population_count_one_v2(masks_horse)
print('\n')

print('Подсчёт количества бит в числе для короля через кеширование:')
bits = init_bits()
masks_king = [770, 1797, 49216, 197123, 920078, 12599488,
              16186183351374184448, 13853283560024178688, 144959613005987840, 4665729213955833856]
test_population_count_one_v3(masks_king, bits)
print('\n')

print('Подсчёт количества бит в числе для коня через кеширование:')
masks_horse = [132096, 329728, 659712, 11333767002587136, 4620693356194824192, 288234782788157440,
               1152939783987658752, 2305878468463689728, 1128098930098176, 9077567998918656]
test_population_count_one_v3(masks_horse, bits)
