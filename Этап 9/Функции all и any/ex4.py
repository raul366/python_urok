a = list(map(int, input().split()))
a = any([True if i < 3 else False for i in a])
print(*["отчислен" if a else "учится"])