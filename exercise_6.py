"""
Модуль 2 Урок 2 Вправа 6
Створіть функцію, яка приймає рядок від користувача та записує його у файл.
"""


filename = "test.txt"
user_input = input(f"Введіть текст який необхідно записати у файл {filename}\n")


def append_text_to_the_file(text_param: str):
    """
    приймає рядок від користувача та записує його у файл
    :param text_param:
    :return: None
    """
    try:
        f = open(filename, "a")
        print(f"Файл {filename} відкритий вдало")
    except FileNotFoundError as e:
        print(e, type(e))
        print(f"При відкритті файлу {filename} виникла помилка")


    try:
        f.write(text_param)
        print(f"Запис до файлу {filename} відбувся вдало")
    except Exception as e:
        print(e, type(e))
        print(f"При запису до файлу {filename} виникла помилка")

    try:
        f.close()
        print(f"Файл {filename} закритий вдало")
    except Exception as e:
        print(f"При закритті файлу {filename} виникла помилка")


append_text_to_the_file(user_input)

