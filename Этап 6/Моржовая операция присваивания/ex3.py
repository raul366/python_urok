s = 1
while (a := int(input())) > 0:
    if a % 3 == 0:
        s *= a
print(s)