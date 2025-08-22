a = map(int, input().split())
b = []
for n in a:
    b.extend([abs(i**3) for i in range(-n, n + 1, 1)])
print(*b[0:4])