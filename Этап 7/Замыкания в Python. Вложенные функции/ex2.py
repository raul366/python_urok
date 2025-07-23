def a():
    def b(c):
        return f'<h1>{c}</h1>'
    return b

d = a()
e = input()
print(d(e))