a = list(map(float, input().split()))
print(any([True if i < 0 else False for i in a]))