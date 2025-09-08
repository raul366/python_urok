a = list(input().split())
b = map(str, filter(lambda x: len(x) > 5, a))
print(next(b), next(b), next(b))