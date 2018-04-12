#!/usv/bin/env python3.6
import abc
import decimal

NDIGITS = 2  # for beauty in print() all currencies will be rounded to NDIGITS


class Course:
    """Descriptor for course field of class Currency."""
    def __get__(self, instanse, owner):
        """Returns class attribute if called from instance.
        Calculates coeffitient between courses if called from class
        and has another class as an argument."""
        if instanse:
            return owner._course

        def inner(other):
            return owner._course / other._course
        return inner

    def __set__(self, instance, value):
        assert 0 < value, "value must be greater than 0"
        instance.__class__._course = value


class Currency(metaclass=abc.ABCMeta):
    """Abstract class stands for currency."""
    def __init__(self, value):
        if isinstance(value, (int, float)):
            self.value = decimal.Decimal(str(value))
        if isinstance(value, decimal.Decimal):
            self.value = value

    @abc.abstractmethod
    def __str__(self):
        pass

    def to(self, other_cls):
        """Transfers instanse to another class."""
        return other_cls(float(self.value) * self.course / other_cls(0).course)

    def __add__(self, other):
        if isinstance(other, Currency):
            return self.__class__(self.value + other.to(self.__class__).value)
        raise TypeError(
            f"TypeError: unsupported operand type(s) for +: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __sub__(self, other):
        if isinstance(other, Currency):
            return self.__class__(self.value - other.to(self.__class__).value)
        raise TypeError(
            f"TypeError: unsupported operand type(s) for -: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value * other)
        raise TypeError(
            f"TypeError: unsupported operand type(s) for *: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return self.__class__(self.value / other)
        raise TypeError(
            f"TypeError: unsupported operand type(s) for /: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __lt__(self, other):
        if isinstance(other, Currency):
            return self.value < other.to(self.__class__).value
        raise TypeError(
            f"TypeError: '<' not supported between instances of: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __le__(self, other):
        if isinstance(other, Currency):
            return self.value <= other.to(self.__class__).value
        raise TypeError(
            f"TypeError: '<=' not supported between instances of: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __gt__(self, other):
        if isinstance(other, Currency):
            return self.value > other.to(self.__class__).value
        raise TypeError(
            f"TypeError: '>' not supported between instances of: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __ge__(self, other):
        if isinstance(other, Currency):
            return self.value >= other.to(self.__class__).value
        raise TypeError(
            f"TypeError: '>=' not supported between instances of: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __eq__(self, other):
        if isinstance(other, Currency):
            return self.value == other.to(self.__class__).value
        raise TypeError(
            f"TypeError: '==' not supported between instances of: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __ne__(self, other):
        if isinstance(other, Currency):
            return self.value != other.to(self.__class__).value
        raise TypeError(
            f"TypeError: '!=' not supported between instances of: "
            f"'{self.__class__.__name__}' and '{other.__class__.__name__}'")

    def __radd__(self, other):  # to have an opportunity to call sum()
        if other == 0:
            return self
        else:
            return self.__add__(other)


class Dollar(Currency):
    """Stands for dollar.

    Attributes:
        currency (int): the name of the class.
        course (int or float): coefficient needed to transform
            instance of this class to Dollar (default 1).

    Note:
        instanses are printed as rounded to DECIMAL float.
    """
    def __init__(self, value):
        super().__init__(value)
        self.currency = self.__class__.__name__
        if not hasattr(self.__class__, '_course'):
            course = Course()
            self.__class__.course = course
            self.course = 1

    def __str__(self):
        return f'{str(round(self.value, NDIGITS))} $'


class Euro(Currency):
    """Stands for dollar.

    Attributes:
        currency (int): the name of the class.
        course (int or float): coefficient needed to transform
            instance of this class to Dollar (default 80/65).

    Note:
        instanses are printed as rounded to DECIMAL float.
    """
    def __init__(self, value):
        super().__init__(value)
        self.currency = self.__class__.__name__
        if not hasattr(self.__class__, '_course'):
            course = Course()
            self.__class__.course = course
            self.course = 80/65

    def __str__(self):
        return f'{str(round(self.value, NDIGITS))} €​​'


class Rubble(Currency):
    """Stands for dollar.

    Attributes:
        currency (int): the name of the class.
        course (int or float): coefficient needed to transform
            instance of this class to Dollar (default 1/65).

    Note:
        instanses are printed as rounded to DECIMAL float.
    """
    def __init__(self, value):
        super().__init__(value)
        self.currency = self.__class__.__name__
        if not hasattr(self.__class__, '_course'):
            course = Course()
            self.__class__.course = course
            self.course = 1/65

    def __str__(self):
            return f'{str(round(self.value, NDIGITS))} ₽'


Euro(0)
Dollar(0)
Rubble(0)

if __name__ == '__main__':
    e = Euro(5)
    print(e)
    print(e.to(Dollar))
    print(sum([Euro(i) for i in range(5)]))
    print(e > Euro(6))
    print(e + Dollar(10))
    print(Dollar(10) + e)
    e.course = 79/63
    print(e.to(Dollar))
    print(1, Euro.course(Dollar))
    print(2, Euro.course(Rubble))
    print(3, Rubble.course(Euro))
    print(4, Rubble.course(Dollar))
    print(e.currency)
    print(0 + Euro(3))

    print(9 * Euro(7))
    print(Euro(7) * 9)
    print(Euro(8) / 3)
    print(e > Euro(2))
    print(e == Euro(1))
    print(Dollar(9).currency)
    print(Rubble(7).currency)