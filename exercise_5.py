"""
Модуль 2 Урок 2 Вправа 5
Напишіть програму, яка читає вміст текстового файлу та виводить кількість слів у ньому.
"""

try:
    filename = "test.txt"
    f = open(filename, "r")
except FileNotFoundError as e:
    print(e, type(e))
    print(f"Файл {filename} не відкрито")
else:
    print(f"Файл {filename} відкрито")

text_from_file = f.read()


def word_numbers(text_param:str):
    """
    функція, отримує текст як рядок і
    повертає кількість слів у цьому реченні.

    :param sentence:
    :return:int
    """
    return len(text_param.split())


print(word_numbers(text_from_file))

f.close()
