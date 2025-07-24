t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

# здесь продолжайте программу

def decor(func):
    def deco(*args, **kwargs):
        b = func(*args, **kwargs)
        while True:
            if '--' in b:
                b = b.replace('--', '-')
            else:
                break
        return b
    return deco

@decor
def perevod(a, t):
    b = ''
    a = a.lower()
    for i in a:
        if i in t:
            b += t[i]
        elif i in ': ;.,_':
            b += '-'
        else:
            b += i
    return b


s = input()
print(perevod(s, t))