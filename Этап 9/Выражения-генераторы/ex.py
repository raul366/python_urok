a, b = map(int, input().split())
c = range(a, b + 1, 1)
for i in range(5):
    print(abs(c[i]))