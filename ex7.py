b = {}
while True:
    a = int(input())
    if a == 0:
        break
    if a in b:
        print("значение из кэша:", b[a])
    else:
        b[a] = round(a ** 0.5, 2)
        print(b[a])