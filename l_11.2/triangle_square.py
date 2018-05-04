"""
Asks user to enter three points and calculates the square of triangle.
"""
import math
import itertools


def validation_of_input(string):
    """ Checks if input is valid.
    If string contains two numbers separated by spaces,
    returns tuple with this numbers. Otherwise raises error.

    :param string: string from builtins.input.
    :return: tuple of two float or error.

    >>> validation_of_input('1.2 4')
    (1.2, 4.0)

    >>> validation_of_input('1 2 3')
    Traceback (most recent call last):
    ValueError: Inputted values should be separated by single space and
    there should be exactly two values. Got "1 2 3" instead.

    >>> validation_of_input('a b')
    Traceback (most recent call last):
    ValueError: Inputted values does not looks like coordinates:("could not convert string to float: 'a'",).
    Please enter integer or decimal numbers.  Use a point to separate the whole and fractional parts.
    """
    string_elems = string.split(' ')
    if len(string_elems) == 2:
        try:
            x_0, y_0 = float(string_elems[0]), float(string_elems[1])
            return x_0, y_0
        except ValueError as err:
            raise ValueError('Inputted values does not looks like coordinates:'
                             f'{err.args}.\n'                                    
                             'Please enter integer or decimal numbers.  '
                             'Use a point to separate the whole and fractional parts.')
    else:
        raise ValueError(f'Inputted values should be separated by single space and\n'
                         f'there should be exactly two values. Got "{string}" instead.')


def on_one_line(points):
    """Checks if points are on one line.

    :param points: coordinates of three points.
    :type points: list or tuple with three tuples; each tuple contains two numeric.
    :return: bool -- if points are on one line.

    >>> on_one_line([(0, 0), (0, 1), (0, 2)])
    True
    >>> on_one_line([(0, 0), (10, 0), (0, 10)])
    False
    """
    return not bool(triangle_square_by_points(points))


def input_three_points():
    """ Asks user to enter three points in sequence. If user
    input is incorrect, user have to repeat input correctly.
    The user enters data for as long as three dots are
    typed in correctly. The way of correct input is described
    in validation_of_input().
    Returns tree correct points.

    :return: list of three valid inputs.
    """
    inputted_points = []
    while len(inputted_points) < 3:
        try:
            point = validation_of_input(input(f'Already inputted points: {inputted_points}\n'
                                              f'input next point>'))
        except ValueError as err:
            print(err)
            continue

        inputted_points.append(point)

        if len(inputted_points) == 3:
            if on_one_line(inputted_points):
                print('Inputted points are on one line. Please, enter new set of points.')
                inputted_points = []

    return inputted_points


def side_length(points):
    """ Calculates length of line segment given by two points.

    :param points: coordinates of two point.
    :type points: list or tuple with two tuples; each tuple contains two numeric.
    :return: float -- length of line segment.

    >>> side_length([(0, 0), (0, 1)])
    1.0
    """
    a, b = points
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def heron_formula(sides):
    """ Calculates square of triangle using heron's formula.

    :param sides: lengths of the triangle's sides.
    :type sides: list or tuple with three non-negative numbers.
    :return: float -- rounded square of triangle with given sides length.

    >>> heron_formula([10, 10, 10*math.sqrt(2)])
    50.0
    """
    a, b, c = sides
    p = (a + b + c) / 2
    return round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)


def triangle_square_by_points(points):
    """Calculates triangle square by coordinates of points.

    :param points: coordinates of three points.
    :type points: list or tuple with three tuples; each tuple contains two numeric.
    :return: float -- rounded triangle square

    >>> triangle_square_by_points([(1, 2), (4, 5), (100, 100)])
    1.5
    """
    return heron_formula(
        [side_length(pair_of_points) for pair_of_points in itertools.combinations(points, 2)]
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(triangle_square_by_points(input_three_points()))
