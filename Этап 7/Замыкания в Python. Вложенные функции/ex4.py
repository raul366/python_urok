def a(tp):
    def b(c):
        nonlocal tp
        if tp == 'list':
            return list(c)
        else:
            return tuple(c)
    return b


p = input()
c = a(p)
b = map(int, input().split())
lst = c(b)
print(lst)