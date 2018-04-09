#!/usv/bin/env python3.6
import random
import functools
import operator
INF = 10


class Matrix:
    """Stands for the matrix.

    Attributes:
        col_number (int): number of columns in matrix.
        row_number (int): number of rows in matrix.
        values (list): one dimensional list of values written by rows.
    Methods:
        transpose
        is_squared
        is_symmetric

    """

    @staticmethod
    def __all_values_are_numbers(args: list) -> bool:
        list_of_values = functools.reduce(operator.add, args[0])
        return all(isinstance(item, int) for item in list_of_values)

    @staticmethod
    def __get_rows(values, row_number, col_number):
        rows = []
        for i in range(row_number):
            rows.append([values[i * col_number + j] for j in range(col_number)])
        return rows

    def __init__(self, *args):
        if (len(args) == 1 and
                isinstance(args[0], list) and
                len(set(map(len, args[0]))) == 1 and
                Matrix.__all_values_are_numbers(args)):
            self.row_number = len(args[0])
            self.col_number = len(args[0][0])
            self.values = functools.reduce(operator.add, args[0])
        elif (len(args) == 2 and
              isinstance(args[0], int) and
              isinstance(args[1], int) and
              args[0] > 0 and
              args[1] > 0):
            self.row_number = args[0]
            self.col_number = args[1]
            self.values = [random.randint(-INF, INF) for x in range(self.col_number*self.row_number)]
        else:
            raise ValueError('Incorrect data entered')

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("must be a Matrix")
        elif (self.col_number != other.col_number or
                self.row_number != other.row_number):
            raise ValueError(f'operands could not be broadcast together with'
                             f' shapes ({self.row_number},{self.col_number})'
                             f'({other.row_number},{other.col_number}) ')
        else:
            return Matrix(Matrix.__get_rows(values=[x + y for x, y in zip(self.values, other.values)],
                                            row_number=self.row_number,
                                            col_number=self.col_number))

    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError("must be a Matrix")
        elif (self.col_number != other.col_number or
                self.row_number != other.row_number):
            raise ValueError(f'operands could not be broadcast together with'
                             f' shapes ({self.row_number},{self.col_number})'
                             f'({other.row_number},{other.col_number}) ')
        else:
            return Matrix(Matrix.__get_rows(values=[x - y for x, y in zip(self.values, other.values)],
                                            row_number=self.row_number,
                                            col_number=self.col_number))

    def __matrix_matrix_multiply(self, other):
        if not self.col_number == other.row_number:
            raise ValueError(f'operands could not be broadcast together with'
                             f' shapes ({self.row_number},{self.col_number})'
                             f' ({other.row_number},{other.col_number}) ')
        else:
            result = Matrix(self.row_number, other.col_number)
            for i in range(self.row_number):
                for j in range(other.col_number):
                    result.__set_element(row_index=i,
                                         col_index=j,
                                         value=sum(
                                             [self.__get_element(i, k) * other.__get_element(k, j)
                                              for k in range(self.col_number)])
                                         )
            return result

    def __scalar_matrix_multiply(self, scalar: int):
        return Matrix(Matrix.__get_rows(values = [item * scalar for item in self.values],
                                        row_number=self.row_number,
                                        col_number=self.col_number))

    def __mul__(self, other):
        if isinstance(other, int):
            return self.__scalar_matrix_multiply(other)
        if isinstance(other, Matrix):
            return self.__matrix_matrix_multiply(other)

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.__scalar_matrix_multiply(other)

    def __set_element(self, row_index, col_index, value):
        self.values[self.__get_local_index(row_index, col_index)] = value

    def __get_local_index(self, row_index, col_index):
        return self.col_number * row_index + col_index

    def __get_element(self, row_index, col_index):
        return self.values[self.__get_local_index(row_index, col_index)]

    def transpose(self):
        values = [None] * self.col_number * self.row_number
        for row_index in range(self.row_number):
            for col_index in range(self.col_number):
                values[self.row_number * col_index + row_index] = self.values[self.col_number * row_index + col_index]
        return Matrix(Matrix.__get_rows(values=values,
                                        row_number=self.col_number,
                                        col_number=self.row_number))

    def __eq__(self, other):
        for self_row, other_row in zip(self.values, other.values):
            if self_row != other_row:
                return False
        return True

    def is_squared(self) -> bool:
        return self.row_number == self.col_number

    def __str__(self):
        rows = Matrix.__get_rows(values=self.values,
                                 row_number=self.row_number,
                                 col_number=self.col_number)
        return '['+'\n'.join([str(row) for row in rows])+']'

    def __repr__(self):
        return self.__str__()

    def is_symmetric(self, side=False):
        if not self.is_squared():
            return False
        if not side and self == self.transpose():
            return True
        elif side:
            rows = Matrix.__get_rows(values=self.values,
                                     row_number=self.row_number,
                                     col_number=self.col_number)
            for row in rows:
                for i in range(len(row) // 2):
                    row[i], row[-i-1] = row[-i-1], row[i]
            if Matrix(rows) == Matrix(rows).transpose():
                return True
        return False


if __name__ == '__main__':
    # creating matricies
    print('creating')
    print('input: 1, 3; result:')
    print(Matrix(1, 3))
    print('input: 3, 1; result:')
    print(Matrix(3, 1))
    print('input: 3, 3; result:')
    print(Matrix(3, 3))
    print('input: [[1, 2], [3, 4]]; result:')
    print(Matrix([[1, 2], [3, 4]]))
    print('input: None')
    try:
        print(Matrix(None))
    except Exception as e:
        print(e)
    try:
        print(Matrix())
    except Exception as e:
        print(e)
    print("input: [['a', 'b'], ['c', 'd']]")
    try:
        print(Matrix([['a', 'b'], ['c', 'd']]))
    except Exception as e:
        print(e)
    # adding and substracting matricies
    print('........\nadding\n.........')
    a = Matrix(2, 4)
    b = Matrix(2, 4)
    print(a)
    print('+'.ljust(8))
    print(b)
    print('='.ljust(8))
    print(a + b)
    print('-----------------------')
    print(a)
    print('-'.ljust(8))
    print(b)
    print('='.ljust(8))
    print(a - b)
    print('-----------------------')
    a = Matrix(4, 4)
    print(a)
    print('+'.ljust(8))
    print(b)
    print('='.ljust(8))
    try:
        print(a + b)
    except Exception as e:
        print(e)
    # transpose and symmetric
    b_tr = b.transpose()
    print('-------transposed----------------')
    print(b_tr)
    symm = Matrix([[1,0,2],[0,1,8],[2,8,1]])
    print(symm.is_symmetric())
    side_symm = Matrix([[1,2,8],[5,5,2],[8,5,1]])
    print(side_symm.is_symmetric(side=True))
    print(symm.is_symmetric(side=True))
    print('....')
    print(side_symm)
    print(side_symm.is_symmetric())
    # multiplication
    print('-------mult----------')
    a = Matrix(2,4)
    b = Matrix(4,3)
    print(a)
    print('*'.ljust(6))
    print(b)
    print('='.ljust(8))
    print(a*b)
    print('.............')
    print(a)
    print('*'.ljust(6))
    print(3)
    print('='.ljust(8))
    print(3*a)