def ball():
    i = 2
    b = 0
    while True:
        a = 0
        for j in range(i, 0, -1):
            if i % j == 0:
                a +=1
        if a == 1 or a == 2:
            yield i
            b += 1
            if b == 20:
                break
        i += 1


c = ball()
for x in c:
    print(x, end = " ")