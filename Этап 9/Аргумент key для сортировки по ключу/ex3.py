import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)

a = []

for i in lst_in:
    a.append(list(map(str, i.split(';'))))

for i in range(len(a)):
    a[i][0], a[i][1], a[i][2], a[i][3] = a[i][1], a[i][3], a[i][2], a[i][0]

for i in range(len(a)):
    for j in range(4):
        if a[i][j].isnumeric():
            a[i][j] = int(a[i][j])

t_sorted = tuple(tuple(i) for i in a)