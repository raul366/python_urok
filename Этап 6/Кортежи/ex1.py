a = tuple(map(str, input().split()))

if "Москва" not in a:
    a += "Москва",
print(*a)