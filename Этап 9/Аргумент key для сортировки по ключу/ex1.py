import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

# Преобразуем список в словарь {предмет: вес}
items = {}
for line in lst_in:
    name, weight = line.split('=')
    items[name] = int(weight)

# Сортируем предметы по убыванию веса
sorted_items = sorted(items.items(), key=lambda x: -x[1])

# Формируем список названий предметов в порядке убывания веса
result = [item[0] for item in sorted_items]

# Выводим результат
print(' '.join(result))