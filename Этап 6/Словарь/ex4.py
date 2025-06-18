import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
a = {}
# здесь продолжайте программу (используйте список lst_in)
for item in lst_in:
    key, value = item.split()  # разделяем строку на ключ и значение
    if key not in a:
        a[key] = [] 
    a[key].append(value)
for key, value in a.items():
    print(key + ":", ", ".join(value))