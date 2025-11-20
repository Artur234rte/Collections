import random
import string

symbols = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(random.choice(symbols) for _ in range(10))

print("Ваш пароль:", password)


def reverse_words(s: str) -> str:
    """Функция, которая переворачивает слова в строке."""
    return ' '.join(s.split()[::-1])

# Тест
s = "Hello world from Python"

print(reverse_words(s))

def char_frequency(s: str) -> dict:
    """Функция, возвращающая словарь с частотой символов в строке."""
    dict_of_letters = {}
    for i in set(s): # В условие не сказано что буквы должны идти по порядку
        dict_of_letters[i] = s.count(i)
    return dict_of_letters


# Тест
s = "abracadabra"

print(char_frequency(s))