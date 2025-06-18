import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
d = {}
# здесь продолжайте программу (используйте список lst_in)
for item in lst_in:
    key, value = item.split(": ")
    if key not in d:
        d[key] = {value}
    else:
        d[key] |= {value}