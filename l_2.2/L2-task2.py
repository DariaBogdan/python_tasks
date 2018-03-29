def str_to_num(s: str) -> int:
    """Replaces each character in string with it's ASCII code.
    ​
    :param s: The string to transform.​
    :type s: str.​
    :returns: int -- sequentially written numbers from the ASCII.
    :raises: IndexError if string == ''
    """
    res = ord(s[-1])
    for char in s[-2 : -(len(s) + 1): -1]:
        nnn = ord(char)
        k = 1
        curres = res
        while curres // 10 != 0:
            k = k + 1
            curres = curres // 10
        res = nnn * (10 ** k) + res
    return res