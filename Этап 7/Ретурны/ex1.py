def is_triangle(a: int, b: int, c: int):
    return True if a + b > c and a + c > b and b + c > a else False