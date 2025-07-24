s = input()  # Читаем строку из входного потока

def tag_wrapper(tag="h1"):
    def decorator(func):
        def wrapper(text):
            # Получаем строку в нижнем регистре из функции
            lower_text = func(text)
            # Оборачиваем в тег
            return f"<{tag}>{lower_text}</{tag}>"
        return wrapper
    return decorator

@tag_wrapper(tag="div")  # Применяем декоратор с параметром tag="div"
def to_lower_case(text):
    return text.lower()  # Переводим строку в нижний регистр

result = to_lower_case(s)  # Вызываем декорированную функцию
print(result)  # Выводим результат