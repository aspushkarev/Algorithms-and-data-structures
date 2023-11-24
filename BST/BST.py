import random
import time


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert_node(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert_node(node.left, key)
    elif key > node.key:
        node.right = insert_node(node.right, key)
    return node


def search(root, key):
    if root is None or root.key == key:
        return root

    if root.key < key:
        return search(root.right, key)
    return search(root.left, key)


def delete_node(root, key):
    # Базовый случай
    if root is None:
        return root

    # Рекурсивно вызываем предка узла, который хотим удалить
    if root.key > key:
        root.left = delete_node(root.left, key)
        return root
    if root.key < key:
        root.right = delete_node(root.right, key)
        return root

    # Случай, когда один ребёнок
    if root.left is None:
        tmp = root.right
        del root
        return tmp
    elif root.right is None:
        tmp = root.left
        del root
        return tmp

    # Случай, когда оба ребёнка существуют
    else:
        successor_parent = root

        # Поиск максимального элемента слева (делаем шаг влево и затем максимум вправо)
        successor = root.left
        while successor.right is not None:
            successor_parent = successor
            successor = successor.right

        if successor_parent != root:
            successor_parent.right = successor.left
        else:
            successor_parent.left = successor.left

        # Копируем найденный элемент в корень
        root.key = successor.key

        del successor
        return root


def get_data(root):
    if root:
        get_data(root.left)
        print(root.key, end=' ')
        get_data(root.right)


def find_key(root, n):
    # Ищем N/10 случайных чисел в каждом дереве
    start = time.process_time()
    keys = [x for x in random.sample(range(N), k=n)]
    while n != 0:
        for key in keys:
            search(root, key)
        n -= 1
    print(f'N: {N} {(time.process_time() - start):.5f} seconds')


def delete_key(root, n):
    start = time.process_time()
    keys = [x for x in random.sample(range(N), k=n)]
    while n != 0:
        for key in keys:
            delete_node(root, key)
        n -= 1
    print(f'N: {N} {(time.process_time() - start):.5f} seconds')


if __name__ == '__main__':
    root1 = root2 = None
    N = 990
    n = int(N / 10)

    for i in range(N):
        # Добавляем N чисел в случайном порядке
        root1 = insert_node(root1, random.randint(1, 100_000))
        # Добавляем N чисел в возрастающем порядке
        root2 = insert_node(root2, i + 1)

    # Здесь мы можем вывести на печать наше бинарное дерево
    print('Бинарное дерево с неупорядоченными числами:')
    get_data(root1)
    print('\nБинарное дерево с числами в упорядоченном порядке:')
    get_data(root2)

    # Поиск случайных чисел в деревьях
    print(f'\n\nИщем N/10 случайных чисел в дереве с неупорядоченными числами...')
    find_key(root1, n)
    print(f'Ищем N/10 случайных чисел в дереве с упорядоченными числами...')
    find_key(root2, n)

    # Удаление случайных чисел в деревьях
    print(f'Удаляем N/10 случайных чисел в дереве с неупорядоченными числами...')
    delete_key(root1, n)
    print(f'Удаляем N/10 случайных чисел в дереве с упорядоченными числами...')
    delete_key(root2, n)
