t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))
n = int(input())
a = []
b = []
for i in range(n):
    for j in range(n):
        b.append(t[i][j])
    a.append(tuple(b))
    b.clear()
t2 = tuple(a)
for row in t2:
    print(' '.join(map(str, row)))