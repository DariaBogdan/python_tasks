#!/usr/bin/env python3.6
import time
import functools

def decorator(func):
    """Calculates and displays the program execution time.

    :param func: time of execution of this function is calculated.
    :type func: function.
    :return: function.
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        func_result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Time of execution of function "{func.__name__}": {end_time - start_time}')
        return func_result
    return inner


@decorator
def test_function(time_to_sleep):
    time.sleep(time_to_sleep)


if __name__ == '__main__':
    test_function(1)