"""
Модуль 2 Урок 2 Вправа 8
Напишіть програму, яка відкриває два файли для читання та порівнює їх вміст, виводячи рядки,
які є у першому файлі, але відсутні у другому.
"""

import os

first_file_name = "test.txt"
second_file_name = "test2.txt"

abs_path = os.path.abspath(__file__)

base_dir = os.path.dirname(abs_path)

first_file_itself_by_absolute_path = os.path.join(base_dir, first_file_name)
second_file_itself_by_absolute_path = os.path.join(base_dir, second_file_name)


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


def strips_new_lines(list_with_new_lines: list):
    """
    remove all new lines from list
    :param list_with_new_lines:
    :return: list
    """
    list_without_new_lines = []
    for line in list_with_new_lines:
        element_without_new_line = line.rstrip('\n')
        list_without_new_lines.append(element_without_new_line)

    return list_without_new_lines


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


def strings_which_is_present_in_the_first_file_but_missing_in_the_second(first_file_param, second_file_param):
    """
    B
    :param first_file_param: file
    :param second_file_param: file
    :return: str
    """
    first_file = open_file_exeption_handler(first_file_param, "r")
    second_file = open_file_exeption_handler(second_file_param, "r")
    lines_list_from_first_file = readlines_file_exeption_handler(first_file)
    lines_list_from_second_file = readlines_file_exeption_handler(second_file)

    lines_list_from_first_file = strips_new_lines(lines_list_from_first_file)

    lines_list_from_second_file = strips_new_lines(lines_list_from_second_file)

    for line_in_first_file in lines_list_from_first_file:
        line_present_in_second_file_flag = False
        for line_in_second_file in lines_list_from_second_file:
            if line_in_first_file == line_in_second_file:
                line_present_in_second_file_flag = True
                print("Знайдено співпадіння рядків")

        if line_present_in_second_file_flag == False:
            print(f"Цей рядок є у першому файлі і одночасно відсутній у другому файлі : {line_in_first_file} ")

    close_file_exeption_handler(first_file)
    close_file_exeption_handler(second_file)


strings_which_is_present_in_the_first_file_but_missing_in_the_second(first_file_itself_by_absolute_path,
                                                                     second_file_itself_by_absolute_path)
