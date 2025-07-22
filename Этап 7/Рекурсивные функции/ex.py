# считывание числа N
N = int(input())

#здесь продолжайте программу
def get_rec_N(N):
    print(*range(1, N +1 ), sep = '\n')


get_rec_N(N) # вызов рекурсивной функции