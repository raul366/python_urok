t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]
lst = [t[i].split(sep=None, maxsplit=-1) for i in range(len(t))]
for i in range(len(lst)-1, -1, -1):
    for j in range(len(lst[i])-1, -1, -1):
        if len(lst[i][j]) <= 3:
            lst[i].pop(j)
print(lst)