number = int(input().strip())
mask1 = 1 << 1
mask5 = 1 << 5

if (number & mask1) or (number & mask5):
    print("ДА")
else:
    print("НЕТ")