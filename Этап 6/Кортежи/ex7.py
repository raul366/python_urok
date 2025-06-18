import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

a = []
b = []
for i in lst_in:
    b.append(i[0:i.index(" ")])
    b.append(i[i.index(" ")+1:])
    a.append(tuple(b))
    b.clear()
t2 = tuple(a)
print(t2)