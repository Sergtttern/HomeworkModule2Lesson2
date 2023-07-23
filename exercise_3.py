"""
Модуль 2 Урок Вправа 3
Напишіть програму, яка відкриває файл для читання
та обробляє помилку FileNotFoundError, якщо файл не знайдено.
"""


try:
    filename = "main.py"
    first_f = open(filename, "r")
except FileNotFoundError as e:
    print(e, type(e))
    print(f"Файл {filename} не відкрито")
else:
    print(f"Файл {filename} відкрито")


try:
    filename = "main5.py"
    second_f = open(filename, "r")
except FileNotFoundError as e:
    print(e, type(e))
    print(f"Файл {filename} не відкрито")
else:
    print(f"Файл {filename} відкрито")
