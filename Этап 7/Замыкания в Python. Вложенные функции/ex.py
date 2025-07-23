def counter_add():
    def a(b):
        return b + 5
    return a

cnt = counter_add()
k = int(input())
print(cnt(k))