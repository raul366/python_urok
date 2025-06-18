def prosba(name: str, familia: str):
    print(f"Уважаемый, {name} {familia}! Вы верно выполнили это задание!")


a = list(map(str, input().split()))
prosba(a[0], a[1])