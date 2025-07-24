numbers = input()  # Читаем строку с числами

def sum_decorator(start):
    def decorator(func):
        def wrapper(string):
            numbers_list = func(string)  # Получаем список чисел из функции
            return sum(numbers_list) + start  # Добавляем начальное значение к сумме
        return wrapper
    return decorator

@sum_decorator(start=5)  # Применяем декоратор с параметром start=5
def str_to_num_list(string):
    return list(map(int, string.split()))  # Преобразуем строку в список чисел

result = str_to_num_list(numbers)  # Вызываем декорированную функцию
print(result)  # Выводим результат