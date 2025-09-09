import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

# Преобразуем каждую строку в список чисел
lst = [list(map(int, line.split())) for line in lst_in]

# Транспонируем таблицу с помощью zip
transposed = list(zip(*lst))

# Выводим результат
for row in transposed:
    print(' '.join(map(str, row)))