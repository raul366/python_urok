a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse = True)
c = list(zip(a,b))
d = []
for i in c:
    d.append(i[0] + i[1])
print(*d)