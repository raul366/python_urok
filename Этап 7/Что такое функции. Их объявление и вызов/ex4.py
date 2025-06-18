def perim(width, height):
    print(f"Периметр прямоугольника, равен {width * 2 + height * 2}")


a = list(map(int, input().split()))
perim(a[0], a[1])