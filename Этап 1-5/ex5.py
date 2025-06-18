a = ["+71234567890", "+71234567854", "+61234576890", "+52134567890", "+21235777890", "+21234567110", "+71232267890"]
c = []
b = []
for i in range(0, len(a)):
    c.append(a[i][0:2])
c = list(set(c))
for i in range(0, len(c)):
    b.append([c[i]])
    for j in range(0, len(a)):
        if c[i] in a[j]:
            b[i].append(a[j])
d = {}
for i in range(len(b)):
    d[b[i][0]] = b[i][1:]
print(*sorted(d.items()))
print(d.items())
print(d)