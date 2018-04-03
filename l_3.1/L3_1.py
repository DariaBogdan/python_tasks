#!/usr/bin/env python3.6
def digits_count(number: int):
    """Calculate digits amount of entered number
    by consistently dividing it by 10.

    :param number: integer number.
    :return: int.
    """
    digits_amount = 1
    while number // 10:
        digits_amount += 1
        number = number // 10
    return digits_amount


def to_int(string: str) -> int:
    """Recursive replaces each character in string
    with it's ASCII code.

    :param string: string to transform.
    :type string: str.
    :return: None if string is empty, else int.
    """
    if len(string) == 0:
        return None

    if len(string) == 1:
        return ord(string)

    # I had to divide return row  into parts
    shift = 10 ** digits_count(ord(string[-1]))
    # result of remaining string shifted on len of last ord + last ord
    return to_int(string[: -1]) * shift + ord(string[-1])


if __name__ == '__main__':
    print(to_int('abcd'))
    print(to_int(''))
