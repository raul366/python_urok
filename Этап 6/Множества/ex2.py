a = set(input())
b = set()
for i in a:
    for j in range(10):
        if str(j) in i:
            b.add(j)
if len(b)>0:
    print(*sorted(b))
else:
    print("НЕТ")