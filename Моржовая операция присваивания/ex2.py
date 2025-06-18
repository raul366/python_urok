def f(x):
    return abs(x) ** 0.5 + 3.2 + x


t = tuple(map(float, input().split()))  # кортеж t в программе не менять
lst = []
# здесь продолжайте программу
for i in t:
    lst.append(b := [f(i), f(i) ** 2, f(i) ** 3])