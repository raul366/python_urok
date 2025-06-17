a = list(map(str, input().split()))
b = int(a[0])
c = {b + i - 1: a[i] for i in range(1, len(a))}
print(c[4])