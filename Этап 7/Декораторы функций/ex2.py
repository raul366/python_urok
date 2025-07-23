a = map(int, input().split())

def sortf(func):
    def b(*args, **kwargs):
        return sorted(func(*args, **kwargs))
    return b

@sortf
def get_list(a):
    return list(a)

lst = get_list(a)
print(*lst)