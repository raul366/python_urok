words = input().split()

# Группируем слова по три в строку
table = list(zip(*[iter(words)] * 3))

# Выводим результат
for row in table:
    print(' '.join(row))