"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""

class ListContainsNotOnlyNumbersError(Exception):
    def __init__(self, text):
        self.text = text



def num_check(nums = []):
    num = input('Введите число, либо нажмите Enter, если хотите закончить:')    

    if not num:
        return f'Получился следующий список: {nums}'

    try:
        if num.isnumeric():

            nums.append(int(num))
            return num_check(nums)
        
        else:
            raise ListContainsNotOnlyNumbersError(text=f'{num} не является числом') 

    except ListContainsNotOnlyNumbersError as err:
        print(err.text)

        return num_check(nums)


print(num_check())