def get_add(a, b):
    if type(a) in (float, int) and type(b) in (float, int):
        return a + b
    elif type(a) is str and type(b) is str:
        return a + b
    else:
        return None