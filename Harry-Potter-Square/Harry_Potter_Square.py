print('Square #1')
for x in range(25):
    for y in range(25):
        if x <= y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #2')
for x in range(25):
    for y in range(25):
        if x == y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #3')
for x in range(25):
    for y in range(25):
        if x == 24 - y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #8')
for x in range(25):
    for y in range(25):
        if x == x + y or y == x + y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #9')
for x in range(25):
    for y in range(25):
        if x >= y + 11 or y >= x + 11:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #11')
for x in range(25):
    for y in range(25):
        if x + 1 == x + y or x + 23 == x + y or y + 23 == x + y or y + 1 == x + y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #18')
for x in range(25):
    for y in range(25):
        if x == x + y or x + 1 == x + y or y == x + y or y + 1 == x + y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #19')
for x in range(25):
    for y in range(25):
        if x == x + y or x + 24 == x + y or y + 24 == x + y or y == x + y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')

print('Square #24')
for x in range(25):
    for y in range(25):
        if x == y or x == 24 - y:
            print('#', end=' ')
        else:
            print('.', end=' ')
    print('\t')
