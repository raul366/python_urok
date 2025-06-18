import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
a = []
for i in lst_in:
    a.append(i[0:i.index(":")])
a = set(a)
print(len(a))