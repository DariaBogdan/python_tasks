#!/usr/bin/env python3.6
import functools

def validate(low_bound: int, upper_bound: int):
    """Calls function, if its parameters in bounds; else print message.

    :param low_bound: func parameters should be greater or equal to it.
    :type low_bound: int
    :param upper_bound: func parameters should be less or equal to it.
    :type upper_bound: int
    :return: function
    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            in_bounds = True
            for item in args[0]:
                in_bounds = in_bounds and (low_bound <= item <= upper_bound)
            if in_bounds:
                return func(*args, **kwargs)
            else:
                print('Function call is not valid.')
        return inner
    return decorator


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    """Says that pixel created.

    :param pixel_values: amount of pixels at each of three dimensions.
    :type pixel_values: tuple of three int.
    :return: None
    """
    print("Pixel created!")


def another_set_pixel(pixel_values):
    """Function to test using decorators without using symbol @.

    :param pixel_values: amount of pixels at each of three dimensions.
    :type pixel_values: tuple of three int.
    :return: None
    """
    print("Pixel created!")


if __name__ == '__main__':
    deco = validate(low_bound=0, upper_bound=256)
    another_set_pixel = deco(another_set_pixel)

    # should be equal
    set_pixel((0,0,0))
    another_set_pixel((0,0,0))

    #should be equal
    set_pixel((300,0,0))
    another_set_pixel((300,0,0))