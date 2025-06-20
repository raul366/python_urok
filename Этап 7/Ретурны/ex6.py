def prov_chten(a):
    return True if len(a) >= 6 else False


cities = list(map(str, input().split()))
lst = [a for a in cities if prov_chten(a)]
print(*lst)