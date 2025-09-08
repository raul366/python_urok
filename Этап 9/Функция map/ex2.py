import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
# переменную lst_in не менять!

lst2D = []
for i in lst_in:
    lst2D.append(list(map(int,i.split())))