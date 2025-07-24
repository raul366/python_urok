a = map(str, input().split())
b = map(str, input().split())

def sorting(func):
    def c(*args, **kwargs):
        a, b = (func(*args, **kwargs))
        e = {}
        for i in range(len(a)):
            e[a[i]] = b[i]
        return e
    return c

@sorting
def obied(a,b):
    return list(a), list(b)


d = obied(a, b)
print(*sorted(d.items()))