import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

a = tuple([tuple(list(i.split('='))) for i in lst_in])
b = list(filter(lambda x: int(x[1]) >= 500, a))
c = []
for i in b:
    c.append(i[0])
print(*c)