a = set(list(map(str, input().split())))
b = set(list(map(str, input().split())))
b = a & b
if a == b:
    print("ДА")
else:
    print("НЕТ")