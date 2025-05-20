a = list(map(str, input().split()))
i = 0
c = []
for i in range(0, len(a)):
    c.append(list(a[i].replace('=', ' ').split()))
b = dict(c)
i = True
while i:
    if 'house' not in b:
        print("НЕТ")
        break
    if 'True' not in b:
        print("НЕТ")
        break
    if '5' not in b:
        print("НЕТ")
        break
    i = False
else:
    print("ДА")