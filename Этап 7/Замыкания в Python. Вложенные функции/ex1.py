def counter_add(n):
    def a(b):
        nonlocal n
        return b + n
    return a
cnt = counter_add(2)
k = int(input())
print(cnt(k))