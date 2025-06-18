a = list(map(str, input().split()))
i = 0
c = []
for i in range(0, len(a)):
    c.append(list(a[i].replace('=', ' ').split()))
b = dict(c)
if 'False' in b:
    del(b['False'])
if '3' in b:
    del(b['3'])
print(*sorted(b.items()))