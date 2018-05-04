from unittest.mock import patch
import unittest

import triangle_square


class TestHeronFormula(unittest.TestCase):
    """Assuming that given arguments are correct (non-negative int),
    because it is inner function.
    """
    def test_correct_heron_formula(self):
        length = triangle_square.heron_formula((3, 5, 6))
        self.assertEqual(length, 7.48)


class TestSideLength(unittest.TestCase):
    """Assuming that given arguments are correct (list or tuple with two tuples of numeric),
    because it is inner function.
    """
    def test_correct_side_length(self):
        length = triangle_square.side_length(((0, 0), (0, 2)))
        self.assertEqual(length, 2)


class TestValidationOfInput(unittest.TestCase):
    """Allowed input: any string. Assuming that only string is given.
    It is inner function.
    """
    def test_inputted_point_is_correct_coordinates_are_integers_separated_by_one_space(self):
        point = triangle_square.validation_of_input('1 2')
        self.assertEqual(point, (1, 2))

    def test_inputted_point_is_incorrect_coordinates_are_integers_separated_by_several_spaces(self):
        with self.assertRaises(ValueError) as raised_exception:
            triangle_square.validation_of_input('1   2')
        self.assertEqual(len(raised_exception.exception.args), 1)
        self.assertRegex(raised_exception.exception.args[0], 'Inputted values should be separated by single space '
                                                             'and there should be exactly two values.')

    def test_inputted_point_is_correct_coordinates_are_floats_separated_by_one_space(self):
        point = triangle_square.validation_of_input('1.1 2.2')
        self.assertEqual(point, (1.1, 2.2))

    def test_inputted_point_is_incorrect_coordinates_are_floats_separated_by_comma(self):
        with self.assertRaises(ValueError) as raised_exception:
            triangle_square.validation_of_input('1.1,2.2')
        self.assertEqual(len(raised_exception.exception.args), 1)
        self.assertRegex(raised_exception.exception.args[0], 'Inputted values should be separated by single space '
                                                             'and there should be exactly two values.')


class TestOnOneLine(unittest.TestCase):
    """Assuming that given arguments are correct (list or tuple with tthree tuples of numeric),
    because it is inner function.
    """
    def test_correct_on_one_line_true(self):
        self.assertEqual(True, triangle_square.on_one_line(((0, 0), (0, 1), (0, 2))))

    def test_correct_on_one_line_false(self):
        self.assertEqual(False, triangle_square.on_one_line(((0, 0), (1, 1), (10, 0))))


class TestInputThreePoints(unittest.TestCase):
    """Among list of user inputs there should be three
    correct inputs and may be any number of incorrect inputs.
    So we will mock several variants of correct inputs.
    There is no way for incorrect input, because if
    user enters wrong line, he has to repeat the input.
    """
    def test_inputting_three_correct_point(self):
        user_input = [
            '0.1 4.456',
            '10 10',
            '0 12'
        ]
        expected_output = [
            (0.1, 4.456),
            (10, 10),
            (0, 12),
        ]
        with patch('builtins.input', side_effect=user_input):
            stacks = triangle_square.input_three_points()
        self.assertEqual(stacks, expected_output)

    def test_inputting_several_incorrect_inputs_but_at_least_three_correct(self):
        user_input = [
            '0.1 4.456',
            '0, 1',
            '0;1',
            '(0,1)',
            '(0;1)',
            'hello',
            '1,2 2,2',
            '10 10',
            '1     1',
            '',
            '1e3 1e-5'
        ]
        expected_output = [
            (0.1, 4.456),
            (10, 10),
            (1000, 0.00001),
        ]
        with patch('builtins.input', side_effect=user_input):
            stacks = triangle_square.input_three_points()
        self.assertEqual(stacks, expected_output)


class TestTriangleSquareByPoints(unittest.TestCase):
    """Assuming that given arguments are correct (list or tuple with three tuples of numeric),
    because it is inner function.
    """
    def test_positive(self):
        square = triangle_square.triangle_square_by_points(
            [(1, 2), (4, 5), (100, 100)]
        )
        self.assertEqual(square, 1.5)


if __name__ == '__main__':
    unittest.main()
