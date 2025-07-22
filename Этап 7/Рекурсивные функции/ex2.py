# ввод числа N
N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)

def fib_rec(N, f = [1, 1]):
    if N > len(f):
        f.append(f[-1] + f[-2])
        fib_rec(N, f)
        return f
    else:
        return f

print(*fib_rec(7))