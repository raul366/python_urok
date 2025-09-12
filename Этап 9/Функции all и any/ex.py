a = list(map(int, input().split()))
a = [i % 2 - 1 for i in a]
print(all(a))