import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

# Преобразуем каждую строку в список чисел
lst = [list(map(int, line.split())) for line in lst_in]

# Находим минимальную длину строки
min_len = min(len(line) for line in lst)

# Транспонируем таблицу, обрезаем до min_len и транспонируем обратно
rectangular = list(zip(*(line[:min_len] for line in lst)))
rectangular = list(zip(*rectangular))

# Выводим результат
for row in rectangular:
    print(' '.join(map(str, row)))