def nechet(a):
    return True if a % 2 != 0 else False


lst_d = list(map(int, input().split()))
lst = [a for a in lst_d if nechet(a)]
print(*lst)