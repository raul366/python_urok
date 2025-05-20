import sys
a = list(map(str.strip, sys.stdin.readlines()))
i = 0
c = []
b = {}
for i in range(0, len(a)):
    c.append(list(a[i].replace('=', ' ').split()))
    b[int(c[i][0])] = c[i][1]
print(*sorted(b.items()))