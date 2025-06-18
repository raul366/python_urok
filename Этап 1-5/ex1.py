a = list(map(str, input().split()))
i = 0
c = []
for i in range(0, len(a)):
    c.append(list(a[i].replace('=', ' ').split()))
for i in range(0, len(c)):
    c[i][1] = int(c[i][1])
b = dict(c)
print(*sorted(b.items()))