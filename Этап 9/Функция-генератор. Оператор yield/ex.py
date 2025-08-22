# ввод значения N (эту переменную не менять)
N = int(input())

# здесь продолжайте программу
def get_sum(total):
    j = 0
    for i in range(1, total + 1):
        j += i
        yield j