# ввод строки (переменную s не менять)
s = input()
s_lst = s.split()

# здесь продолжайте программу
tp = tuple([tuple(list(i.split('='))) for i in s_lst])