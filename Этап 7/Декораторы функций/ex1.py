menu = input() # чтение пунктов меню (переменную menu не менять)

def show_menu(func):
    def a(*args, **kwargs):
        b = func(*args, **kwargs)
        for i in range(len(b)):
            print(f'{i + 1}. {b[i]}')
    return a

@show_menu
def get_menu(s):
    return list(menu.split())