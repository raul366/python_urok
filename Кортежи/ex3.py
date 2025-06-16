a = tuple(map(str, input().split()))
b = []
for i in a:
    if "ва" in i.lower():
        b.append(i.lower())
b = tuple(b)
print(*b)