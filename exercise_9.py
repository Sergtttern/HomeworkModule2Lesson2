"""
Модуль 2 Урок 2 Вправа 9
Створіть функцію, яка видаляє вказаний рядок з текстового файлу.
"""
import os

file_name = "test.txt"

abs_path = os.path.abspath(__file__)

base_dir = os.path.dirname(abs_path)

file_itself_by_absolute_path = os.path.join(base_dir, file_name)


def open_file_exeption_handler(file_name_param: str, mod_param: str):
    """
    open file, handles exceptions
    :param file_name_param:
    :return: file
    """
    try:
        f = open(file_name_param, mod_param)
        print(f"Файл {file_name_param} відкритий вдало з модом {mod_param}")
    except FileNotFoundError as e:
        print(e, type(e))
        print(f"При відкритті файлу {file_name_param} з модом {mod_param} виникла помилка")


    return f


def close_file_exeption_handler(file_param):
    """
    close file, handles exceptions
    :param file_param:
    :return: None
    """
    try:
        file_param.close()
        print(f"Файл {file_param.name} закрито вдало")
    except Exception as e:
        print(e, type(e))
        print(f"При закритті файлу {file_param.name} виникла помилка")


def readlines_file_exeption_handler(file_param):
    """
    readline in file, handles exceptions
    :param file_name_param:
    :return: str
    """
    try:
        line_content = file_param.readlines()
        print(f"Рядок у файлі {file_param.name} зчитано вдало")
    except FileNotFoundError as e:
        print(e, type(e))
        print(f"При зчитуванні рядку у файлі {file_param.name} виникла помилка")

    return line_content


def readlines_file_exeption_handler(file_param):
    """
    readline in file, handles exceptions
    :param file_name_param:
    :return: str
    """
    try:
        line_content = file_param.readlines()
        print(f"Рядок у файлі {file_param.name} зчитано вдало")
    except FileNotFoundError as e:
        print(e, type(e))
        print(f"При зчитуванні рядку у файлі {file_param.name} виникла помилка")

    return line_content


file = open_file_exeption_handler(file_itself_by_absolute_path, "r")

line_content = readlines_file_exeption_handler(file)

print(line_content)

line_number_to_delete = int(input("Введіть номер рядка який слід видалити \n")) - 1

line_content.pop(line_number_to_delete)

print(line_content)

close_file_exeption_handler(file)

file = open_file_exeption_handler(file_itself_by_absolute_path, "w")

file.write("")

file.writelines(line_content)

close_file_exeption_handler(file)
