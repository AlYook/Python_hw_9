"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByZeroError(Exception):
    def __init__(self, text):
        self.text = text



def division():
    num1 = int(input('Введите делимое: '))
    num2 = int(input('Введите делитель: '))

    try:
        if num2 == 0:
            raise DivisionByZeroError(text='На ноль делить нельзя!')
    except DivisionByZeroError as err:
        return err.text

    return num1 / num2


print(division())