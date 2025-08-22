N = int(input())

def balak_seq(max_len):
    a = 0
    b = 0
    c = 0
    j = 0
    for i in range(max_len ):
        if i == 0:
            j = 1
        elif i == 1:
            a = j
            j = 1
        elif i == 2:
            b = a
            a = j
            j = 1
        else:
            c = b
            b = a
            a = j
            j = a + b + c
        yield j

d = balak_seq(N)
for i in d:
    print(i, end = " ")