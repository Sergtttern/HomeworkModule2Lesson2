"""
 Модуль 2 Урок Вправа 1
 Обробіть виняток IndexError, коли програма намагається отримати доступ
 до неправильного індексу в списку.
"""


list_example = ['apple','banana','mango','peach']

try:
    print(list_example[10])

except IndexError as e:
    print(e, type(e))
