import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)

lst = []
zv = ["рядовой", "сержант", "старшина", "прапорщик", "лейтенант", "капитан", "майор", "подполковник", "полковник"]

for i in lst_in:
    lst.append(list(map(str, i.split("="))))

lst = sorted(lst,key = lambda x: zv.index(x[1]))