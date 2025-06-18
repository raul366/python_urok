def chet(a):
    return True if a % 2 == 0 else False


while True:
    x = int(input())
    if chet(x):
        print(x)
    elif x == 1:
        break