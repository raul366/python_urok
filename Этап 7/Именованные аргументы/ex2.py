def perevod(a: str, sep = "-"):
    a = a.lower()
    t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
         'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
         'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    a = list(a)
    b = []
    for i in a:
        if i in t:
            b.append(t[i])
        elif i == " ":
            b.append(sep)
        else:
            b.append(i)
    return "".join(map(str, b))


a = input()
print(perevod(a))
print(perevod(a, "+"))