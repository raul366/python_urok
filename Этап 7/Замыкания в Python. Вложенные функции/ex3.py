def a(b):
    def c(d):
        nonlocal b
        return f'<{b}>{d}</{b}>'
    return c


b = input()
e = a(b)
d = input()
print(e(d))