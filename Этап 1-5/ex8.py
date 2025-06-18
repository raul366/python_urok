a = ["osnovy-raboty-so-strokami", "indeksy-i-srezy-strok", "algoritmy-obrabotki-spiskov", "osnovy-raboty-so-strokami", "algoritm-evklida", "instrument-list-comprehensions", "indeksy-i-srezy-strok", "dekoratory-funkciy-i-zamykaniya"]
b = {}
for i in range(len(a)):
    if a[i] in b:
        print("Взято из кэша:", b[a[i]])
    else:
        b[a[i]] = "HTML-страница для адреса " + a[i]
        print(b[a[i]])