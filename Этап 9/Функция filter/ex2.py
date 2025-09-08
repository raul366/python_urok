a = list(map(int, input().split()))
b = list(filter(lambda x: len(str(abs(x))) == 2, a))
print(*b)