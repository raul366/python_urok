a = int(input())
b = []
c = a >> 3

if c % 2 != 0:
    b.append(True)
else:
    b.append(False)

a = a >> 6

if a % 2 != 0:
    b.append(True)
else:
    b.append(False)

d = all(b)

print("ДА" if d else "НЕТ")