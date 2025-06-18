a = list(map(int, input().split()))
b = dict.fromkeys(a)
c = list(b.keys())
print(*c)