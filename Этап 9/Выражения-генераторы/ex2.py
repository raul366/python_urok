from string import ascii_lowercase
a = []
for i in ascii_lowercase:
    for j in ascii_lowercase:
        a.append(i + j)
print(*a[0:50])