a = tuple(list(map(str.lower, input().split())))
b = {i: a.count(i) for i in a}
if "и" in b:
    print(b["и"])
else:
    print(0)