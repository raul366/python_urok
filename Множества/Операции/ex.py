a = set(list(map(int, input().split())))
b = set(list(map(int, input().split())))
s = a & b
print(*sorted(s))