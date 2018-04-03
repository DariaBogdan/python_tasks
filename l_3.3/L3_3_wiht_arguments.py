#!/usr/bin/env python3.6
import functools

def with_arguments(deco):
    """Allows to set arguments to another decorator.

    :param deco: decorator to set arguments in.
    :return: decorator with setted arguments.
    """
    @functools.wraps(deco)
    def wrapper(*dargs,**dkwargs):
        def decorator(func):
            result = deco(func,*dargs,**dkwargs)
            functools.update_wrapper(result, func)
            return result
        return decorator
    return wrapper


@with_arguments
def validate(func, low_bound: int, upper_bound: int):
    """Calls function, if its parameters in bounds; else print message.

    :param func: function to call if the condition is met.
    :type func: function.
    :param low_bound: func parameters should be greater or equal to it.
    :type low_bound: int.
    :param upper_bound: func parameters should be less or equal to it.
    :type upper_bound: int.
    :return: function.
    """
    def inner(*args, **kwargs):
        in_bounds = True
        for item in args[0]:
            in_bounds = in_bounds and (low_bound <= item <= upper_bound)
        if in_bounds:
            return func(*args, **kwargs)
        else:
            print('Function call is not valid.')
    return inner


@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    """Says that pixel created.

    :param pixel_values: amount of pixels at each of three dimensions.
    :type pixel_values: tuple of three int.
    :return: None
    """
    print("Pixel created!")


if __name__ == '__main__':
    set_pixel((0,0,0))
    set_pixel((300,0,0))
