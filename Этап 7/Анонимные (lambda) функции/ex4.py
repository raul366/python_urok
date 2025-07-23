def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

# здесь продолжайте программу
digs = list(map(int, input().split()))
f = [lambda x: True, lambda x: True if x < 0 else False, lambda x: True if x>= 0 else False, lambda x: True if 3 <= x <= 5 else False]
for a in f:
    print(*filter_lst(digs, a))