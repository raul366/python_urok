a = tuple(map(str, input().split()))
b = []
for i in a:
    if i not in "Ульяновск":
        b.append(i)
b = tuple(b)
print(*b)