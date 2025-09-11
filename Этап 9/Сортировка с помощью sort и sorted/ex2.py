a = set(list(map(int, input().split())))
a = sorted(a, reverse = True)
print(*a[0:4])