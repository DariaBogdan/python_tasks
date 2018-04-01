import time
import functools

def decorator(func):
    """Calculates and displays the program execution time.

    :param func: time of execution of this function is calculated
    :type func: function
    :return: function
    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        t1 = time.time()
        print(f'Time of execution of this function: {t1 - t0}')
        return res
    return inner
