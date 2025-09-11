a = list(map(str, input().split()))
a = list(sorted(a,key = len, reverse = True))
print(*a)