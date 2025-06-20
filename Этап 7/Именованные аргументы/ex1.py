def check_password(a, chars = "$%!?@#"):
    a1 = list(a)
    b = 0
    for i in a1:
        if i in chars:
            b += 1
    return True if b > 0 and len(a) >= 8 else False