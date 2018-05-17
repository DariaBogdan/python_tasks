import unittest

from stats import stats


class TestMean(unittest.TestCase):
    """Assuming that given argument is numeric iterable.
    """
    def test_correct_mean(self):
        sample = range(10)
        self.assertEqual(stats.mean(sample), 4.5)

    def test_incorrect_mean_empty_sample(self):
        self.assertRaises(ZeroDivisionError, stats.mean, [])

    def test_incorrect_mean__wrong_type(self):
        with self.assertRaises(TypeError) as err:
            stats.mean(['a', 'b', 'c'])
        self.assertEqual(len(err.exception.args), 1)
        self.assertEqual(err.exception.args[0], "unsupported operand type(s) for +: 'int' and 'str'")
