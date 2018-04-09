#!/usv/bin/env python3.6
import random
import functools
import operator
INF = 10  # Matrix uses integers from -INF to INF for random filling


class Matrix:
    """Stands for the matrix.

    Attributes:
        ncol (int): number of columns in matrix.
        nrow (int): number of rows in matrix.
        values (list): one dimensional list of values written by rows.
    Methods:
        transpose
        is_squared
        is_symmetric

    """

    @staticmethod
    def __all_values_are_integers(args: list) -> bool:
        """Check that all values in list of lists are integers.

        :param args: list of nested lists.
        :return: True if all values are numbers, else False.
        """
        # transform list of nested lists to list containing only values
        list_of_values = functools.reduce(operator.add, args[0])
        # check instances of all elements
        return all(isinstance(item, int) for item in list_of_values)

    @staticmethod
    def __get_rows(values: list, nrow: int, ncol: int) -> list:
        """Transforms one-dimensional array of values of matrix to
        list of rows of matrix.

        :param values: list with values of matrix.
        :param nrow: number of rows in matrix.
        :param ncol: number of columns in matrix.
        :return: list of rows of matrix.
        """
        rows = []
        for i in range(nrow):
            rows.append([values[i * ncol + j] for j in range(ncol)])
        return rows

    def __init__(self, *args):
        # first case stands for initiating Matrix with list
        if (len(args) == 1 and
                isinstance(args[0], list) and
                len(set(map(len, args[0]))) == 1 and # all nested lists have the same length
                Matrix.__all_values_are_integers(args)):
            self.nrow = len(args[0])
            self.ncol = len(args[0][0])
            self.values = functools.reduce(operator.add, args[0])
        # second case stands for random initiating Matrix of given shape
        elif (len(args) == 2 and
              isinstance(args[0], int) and
              isinstance(args[1], int) and
              args[0] > 0 and
              args[1] > 0):
            self.nrow = args[0]
            self.ncol = args[1]
            self.values = [random.randint(-INF, INF) for x in range(self.ncol*self.nrow)]
        else:
            raise ValueError('Incorrect data entered')

    def __add__(self, other):
        # Matrix can be added only to another Matrix
        if not isinstance(other, Matrix):
            raise TypeError("must be a Matrix")
        # shapes should be the same
        elif (self.ncol, self.nrow) != (other.ncol, other.nrow):
            raise ValueError(f'operands could not be broadcast together with'
                             f' shapes ({self.nrow},{self.ncol})'
                             f'({other.nrow},{other.ncol})')
        else:
            # Matrix initialized with list of rows;
            # values are the sum of initial items
            return Matrix(
                Matrix.__get_rows(
                    values=[x + y for x, y in zip(self.values, other.values)],
                    nrow=self.nrow,
                    ncol=self.ncol))

    def __sub__(self, other):
        # Matrix substraction defined inly for Matrix objects
        if not isinstance(other, Matrix):
            raise TypeError("must be a Matrix")
        # shapes should be the same
        elif (self.ncol != other.ncol or
                self.nrow != other.nrow):
            raise ValueError(f'operands could not be broadcast together with'
                             f' shapes ({self.nrow},{self.ncol})'
                             f'({other.nrow},{other.ncolr}) ')
        else:
            # Matrix initialized with list of rows;
            # values are the substraction of initial items
            return Matrix(
                Matrix.__get_rows(
                    values=[x - y for x, y in zip(self.values, other.values)],
                    nrow=self.nrow,
                    ncol=self.ncol))

    def __matrix_matrix_multiply(self, other):
        """Calculate the result of multiplication of two matrices.

        :param other: Matrix to multiply on.
        :return: Matrix.
        """
        # shapes should fit next rule:
        if not self.ncol == other.nrow:
            raise ValueError(f'operands could not be broadcast together with'
                             f' shapes ({self.nrow},{self.ncol})'
                             f' ({other.nrow},{other.ncol}) ')
        else:
            # initiate new random Matrix with needed shape for result
            result = Matrix(self.nrow, other.ncol)
            for i in range(self.nrow):
                for j in range(other.ncol):
                    # fill result matrix with correct values
                    result.__set_element(row_index=i,
                                         col_index=j,
                                         value=sum(
                                             [self.__get_element(i, k) * other.__get_element(k, j)
                                              for k in range(self.ncol)])
                                         )
            return result

    def __scalar_matrix_multiply(self, scalar: int):
        """Calculates the result of multiplication scalar on matrix.

        :param scalar: int to multiply.
        :return: Matrix.
        """
        return Matrix(Matrix.__get_rows(values=[item * scalar for item in self.values],
                                        nrow=self.nrow,
                                        ncol=self.ncol))

    def __mul__(self, other):
        # there are 2 types of multiplication: matrix and scalar
        if isinstance(other, int):
            return self.__scalar_matrix_multiply(other)
        if isinstance(other, Matrix):
            return self.__matrix_matrix_multiply(other)

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.__scalar_matrix_multiply(other)

    def __set_element(self, row_index: int, col_index: int, value: int) -> None:
        """Changes one item in list with new value; the location of
        item is calculated by two indices: like in two-dimensional
        array.

        :param row_index: row index in two-dimensional array.
        :param col_index: column index in two-dimensional array.
        :param value: new value to set to item.
        :return: None
        """
        self.values[self.__get_local_index(row_index, col_index)] = value

    def __get_local_index(self, row_index: int, col_index: int) -> int:
        """Calculate the location of item in one-dimensional array by
        two indices: like in two-dimensional array.

        :param row_index: row index in two-dimensional array.
        :param col_index: column index in two-dimensional array.
        :return: int -- index of element in one-dimensional array.
        """
        return self.ncol * row_index + col_index

    def __get_element(self, row_index, col_index):
        """Returns the value of item from one-dimensional array,
        like if it was located two-dimensional array.

        :param row_index: row index in two-dimensional array.
        :param col_index: column index in two-dimensional array.
        :return: int -- value of element.
        """
        return self.values[self.__get_local_index(row_index, col_index)]

    def transpose(self):
        """Transposes matrix.

        :return: Matrix
        """
        values = [None] * self.ncol * self.nrow  # initiate list of needed shape to fill
        for row_index in range(self.nrow):
            for col_index in range(self.ncol):
                # filling it with needed values of initial Matrix
                values[self.nrow * col_index + row_index] = self.values[self.ncol * row_index + col_index]
        # Matrix with filled values
        return Matrix(Matrix.__get_rows(values=values,
                                        nrow=self.ncol,
                                        ncol=self.nrow))

    def __eq__(self, other):
        # shapes should be the same
        if (self.nrow, self.ncol) != (other.nrow, other.ncol):
            return False
        # elements should be the same
        for self_item, other_item in zip(self.values, other.values):
            if self_item != other_item:
                return False
        return True

    def is_squared(self) -> bool:
        """Returns True if Matrix is squared, False otherwise."""
        return self.nrow == self.ncol

    def __str__(self):
        # transform list with values to list with rows
        rows = Matrix.__get_rows(values=self.values,
                                 nrow=self.nrow,
                                 ncol=self.ncol)
        # concatenate rows with '\n' and brackets
        return '['+'\n'.join([str(row) for row in rows])+']'

    def __repr__(self):
        return self.__str__()

    def is_symmetric(self, side=False) -> bool:
        """Returns True if Matrix is symmetric, False otherwise.

        :param side: if True, symmetric according to the side diagonal
        is checked; by default symmetric according to the main diagonal
        is checked.
        """
        if not self.is_squared():
            return False
        if not side and self == self.transpose():
            return True
        elif side:
            rows = Matrix.__get_rows(values=self.values,
                                     nrow=self.nrow,
                                     ncol=self.ncol)
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