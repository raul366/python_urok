a = tuple(map(int, input().split()))
b = []
for i in range(len(a)):
    if a.count(a[i]) == 1 or a.count(a[i]) > 1 and a.index(a[i]) == i:
        b.append(a[i])
b = tuple(b)
print(*b)