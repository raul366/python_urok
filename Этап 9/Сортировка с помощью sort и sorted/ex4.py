import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))

# Преобразуем список в словарь {цена: название}
price_to_name = {}
for line in lst_in:
    name, price = line.split(':')
    price_to_name[int(price)] = name

# Функция для получения трёх самых дешёвых товаров
def get_three_cheapest(prices_dict):
    # Сортируем цены и берём три минимальные
    sorted_prices = sorted(prices_dict.keys())
    return [prices_dict[price] for price in sorted_prices[:3]]

# Получаем и выводим результат
cheapest = get_three_cheapest(price_to_name)
print(' '.join(cheapest))