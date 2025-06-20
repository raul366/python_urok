def dlin(a):
    return (a, len(a))


cities = list(map(str, input().split()))
d = dict(dlin(a) for a in cities)
a = sorted(d, key=d.get)
print(*a)