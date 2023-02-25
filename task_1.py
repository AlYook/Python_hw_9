"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    

    def __str__(self):
        matrix = ''

        for line in self.matrix:
            matrix += ' '.join(map(str, line)) + '\n'
        
        return matrix
    
    def __add__(self, another):

        if len(self.matrix) != len(another.matrix):
            print('Нельзя склаывать матрицы разного размера')
            return None

        result_matrix = copy.deepcopy(self.matrix) 
        
        for i in range(len(self.matrix)):

            for j in range(len(self.matrix[i])):
                result_matrix[i][j] = self.matrix[i][j] + another.matrix[i][j]
        

        return Matrix(result_matrix)


m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m1)
print(m2)

m3 = m1 + m2

print(m3)