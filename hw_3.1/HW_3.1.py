#!/usr/bin/env python3.6
import functools
import random


def off():
    """Changes field 'disabled' in fabric decorator to True.

    :return: None
    """
    fabric.disabled = True


def on():
    """Changes field 'disabled' in fabric decorator to False.

    :return: None
    """
    fabric.disabled = False


def fabric(func):
    """Decorator factory takes function as an argument and than takes
    decorator. Returns the decorator that should apply the function
    to the result of the decorator being decorated. If the function is
    inapplicable, the error will raise.

    :param func: function that should be apply.
    :type func: function.
    :return: function (decorator).
    """

    @functools.wraps(func)
    def inner_1(deco):
        def inner_2(deco_args):
            def inner_3(deco_func):
                def inner_4(*args, **kwargs):
                    if fabric.disabled:
                        return func(deco_func(*args, **kwargs))
                    return func(deco(deco_args)(deco_func)(*args, **kwargs))
                return inner_4
            return inner_3
        return inner_2
    return inner_1


@fabric(lambda x: x ** 2)
def repeat(times):
    """Calls function for 'times' times and returns the mean.
    The function should return number. If it does not, the
    error will raise.

    :param times: times to call the function
    :type times: int
    """
    def deco(func):
        def inner(*args, **kwargs):
            mean = 0
            for i in range(times):
                mean += func(*args, **kwargs)
            return mean / times
        return inner
    return deco


@repeat(3)
def foo(*args, **kwargs):
    """Function that works.

    :*args: anything
    :**kwargs: anything
    """
    print("Foo called!")
    return 3


@repeat(2)
def random_int(*args, **kwargs):
    """Returns random int from 1 to 10"""
    a = random.randint(1,10)
    print("Foo called!", a)
    return a


if __name__ == '__main__':
    # setting attribute that stands for turn on and off inner decorator
    fabric.disabled = False
    # setting functions to change field .disabled
    fabric.off = off
    fabric.on = on

    # example with foo
    print(foo([1, 3, 5]))
    fabric.off()
    print(foo([1, 3, 5]))

    # example with random_int
    print(random_int([1, 3, 5]))
    fabric.on()
    print(random_int('hello'))
    print(random_int(a=8, b=(1, 2, 3), c={1: 'a', 2: 'b'}))
    print(random_int())
    print(random_int(None))
    print(random_int(print))
    fabric.off()
    print(random_int(3, [4, 5], a='hello'))

