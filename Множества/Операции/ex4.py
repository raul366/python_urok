a = tuple(set(list(map(int, input().split()))))
if a.count(2) > 0:
    print("НЕ ДОПУЩЕН")
else:
    print("ДОПУЩЕН")