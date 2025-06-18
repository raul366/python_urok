def vich(a):
    min_a = min(a)
    max_a = max(a)
    sum_a = sum(a)
    print(f"Min = {min_a}, max = {max_a}, sum = {sum_a}")


a = list(map(int, input().split()))
vich(a)