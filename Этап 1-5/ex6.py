a = ["+71234567890 Сергей", "+71234567810 Сергей", "+51234567890 Михаил", "+72134567890 Николай"]
c = []
b = []
for i in range(0, len(a)):
    c.append(a[i][a[i].index(" ") + 1:])
c = list(set(c))
for i in range(0, len(c)):
    b.append([c[i]])
    for j in range(0, len(a)):
        if c[i] in a[j]:
            b[i].append(a[j][0:a[j].index(" ")])
d = {}
for i in range(len(b)):
    d[b[i][0]] = b[i][1:]
print(*sorted(d.items()))