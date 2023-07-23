"""
Модуль 2 Урок 2 Вправа 2
Обробка винятків
Створіть функцію, яка приймає два числа від користувача та обробляє помилку,
якщо введені дані не є числами.
"""


user_input1 = input("Введіть перше число\n")
user_input2 = input("Введіть друге число\n")


def type_exception_handler(first_number_param:float, second_number_param:float):
    """
    приймає два числа від користувача та обробляє помилку, якщо введені дані не є числами.
    :param first_number_param:
    :param second__number_param:
    :return: None
    """

    try:
        first_number = float(first_number_param)
        print(f"Перше значення це число: {first_number}")
    except ValueError as e:
        print(e, type(e))
        print("Введене перше значення не є числом")

    try:
        second_number = float(second_number_param)
        print(f"Друге значення це число: {second_number}")
    except ValueError as e:
        print(e, type(e))
        print("Введене друге значення не є числом")

type_exception_handler(user_input1, user_input2)
