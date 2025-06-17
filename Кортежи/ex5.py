a = tuple(map(int, input().split()))
b = ()
for i in range(len(a)):
    if a.count(a[i]) > 1:
        b += i,
print(*b)