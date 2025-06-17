a = list(map(str.lower, input().split()))
a = set([i for i in a if len(i) >= 3])
print(len(a))