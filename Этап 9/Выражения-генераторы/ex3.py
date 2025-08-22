cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]
a = []
i = 0
j = 0
while True:
    if i <= 1000000:
        a.append(cities[j])
        i += 1
        j += 1
        if j >= len(cities):
            j = 0
    else:
        break
print(*a[0:20])