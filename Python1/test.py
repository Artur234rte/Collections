def char_frequency(s: str) -> dict:
    """Функция, возвращающая словарь с частотой символов в строке."""
    dict_of_letters = {}
    for i in set(s):
        dict_of_letters[i] = s.count(i)
    return dict_of_letters


# Тест
s = "abracadabra"

print(char_frequency(s)) # Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}