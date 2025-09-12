import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = ["# x o", "x # x", "o o #"] #list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)

pole = []

for i in lst_in:
    pole.append(list(map(str, i.split())))

def is_free(lst):
    return any([True if lst[i][j] == "#" else False for i in range(len(lst)) for j in range(len(lst[i]))])