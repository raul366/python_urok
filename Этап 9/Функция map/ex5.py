a = list(map(lambda x: x if len(x) > 5 else '-', input().split()))
print(*a)