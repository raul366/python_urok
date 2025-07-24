s = input()  # Читаем строку из входного потока

# Словарь для транслитерации
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}

def replace_chars(chars=" !?"):
    def decorator(func):
        def wrapper(text):
            # Транслитерируем строку
            translit_text = func(text)
            # Заменяем указанные символы на дефисы
            for char in chars:
                translit_text = translit_text.replace(char, '-')
            # Удаляем повторяющиеся дефисы
            while '--' in translit_text:
                translit_text = translit_text.replace('--', '-')
            return translit_text
        return wrapper
    return decorator

@replace_chars(chars="?!:;,. ")  # Применяем декоратор с указанными символами
def transliterate(text):
    text = text.lower()  # Переводим в нижний регистр
    result = []
    for char in text:
        # Заменяем русские буквы согласно словарю
        if char in t:
            result.append(t[char])
        else:
            result.append(char)
    return ''.join(result)

result = transliterate(s)  # Вызываем декорированную функцию
print(result)  # Выводим результат