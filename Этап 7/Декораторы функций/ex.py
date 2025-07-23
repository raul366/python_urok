def get_sq(width, height):
    return width * height

def func_show(func):
    def a(*args, **kwargs):
        print(f'Площадь прямоугольника: {func(*args, **kwargs)}')
    return a