"""
Модуль 2 Урок 2 Вправа 7
Реалізуйте програму, яка копіює вміст одного файлу в інший.
"""


import os

first_file_name = "test.txt"
second_file_name = "test2.txt"

abs_path = os.path.abspath(__file__)

base_dir = os.path.dirname(abs_path)

first_file_by_absolute_path = os.path.join(base_dir, first_file_name)
second_file_by_absolute_path = os.path.join(base_dir, second_file_name)


def open_file_exeption_handler(file_name_param: str, mod_param: str):
    """
    open file, handles exceptions
    :param file_name_param:
    :return: None
    """
    try:
        f = open(file_name_param, mod_param)
        print(f"Файл {file_name_param} відкритий вдало з модом {mod_param}")
    except FileNotFoundError as e:
        print(e, type(e))
        print(f"При відкритті файлу {file_name_param} з модом {mod_param} виникла помилка")


    return f


def read_file_exeption_handler(file_param):
    """
    read file, handles exceptions
    :param file_name_param: file
    :return: str
    """
    try:
        content = file_param.read()
        print(f"Файл {file_param.name} зчитано вдало")
    except FileNotFoundError as e:
        print(e, type(e))
        print(f"При відкритті файлу {file_param.name} виникла помилка")

    return content


def close_file_exeption_handler(file_param):
    """
    close file, handles exceptions
    :param file_name_param:
    :return: None
    """
    try:
        file_param.close()
        print(f"Файл {file_param.name} закритий вдало")
    except Exception as e:
        print(f"При закритті файлу {file_param.name} виникла помилка")


 def copy_content_from_first_file_to_second_file(first_file_name_param:str, second_file_name_param:str):
    """
    копіює вміст одного файлу в інший.
    :param first_file_name_param: 
    :param second_file_name_param: 
    :param content_param: 
    :return: None
    """

    first_file = open_file_exeption_handler(first_file_name_param, "r")

    content = read_file_exeption_handler(first_file)

    second_file = open_file_exeption_handler(second_file_name_param, "w")

    try:
        second_file.write(content)
        print(f"Запис до файлу {second_file.name} відбувся вдало")
    except Exception as e:
        print(e, type(e))
        print(f"При запису до файлу {second_file.name} виникла помилка")

    close_file_exeption_handler(first_file)
    close_file_exeption_handler(second_file)


copy_content_from_first_file_to_second_file(first_file_by_absolute_path, second_file_by_absolute_path)
