"""
Модуль 2 Урок 2 Вправа 4
Реалізуйте функцію, яка ділить два числа, але обробляє помилку **`ZeroDivisionError`**,
якщо друге число дорівнює нулю.
"""


first_num = float(input("Введіть перше число\n"))
second_num = float(input("Введіть друге число\n"))


def divide_two_numbers(first_num_param: float, second_num_param:float):
    """
    ділить два числа, але обробляє помилку **`ZeroDivisionError`**,
    якщо друге число дорівнює нулю.
    :param first_num_param:
    :param second_num_param:
    :return: None
    """

    try:
        result_of_division = first_num_param / second_num_param
        return result_of_division
    except ZeroDivisionError as e:
        print(e, type(e))


print(divide_two_numbers(first_num, second_num))
