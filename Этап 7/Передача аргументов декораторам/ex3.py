from functools import wraps

def sum_decorator(func):
    @wraps(func)  # Сохраняем свойства оригинальной функции
    def wrapper(string):
        numbers = func(string)  # Получаем список чисел
        return sum(numbers)  # Возвращаем сумму чисел
    return wrapper

@sum_decorator
def get_list(string):
    '''Функция для формирования списка целых значений'''
    return list(map(int, string.split()))