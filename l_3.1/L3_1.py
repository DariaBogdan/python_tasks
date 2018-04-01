def str_to_num_rec(s: str):
    """Recursive replaces each character in string with it's ASCII code

    :param s: string to transform
    :return: None if string is empty, else int
    """
    if len(s) == 0:
        return None

    if len(s) == 1:
        return ord(s)

    cur_res = ord(s[-1])

    # calculate length of ord of last element
    len_cur_res = 1
    while cur_res // 10:
        len_cur_res += 1
        cur_res = cur_res // 10

    # last ord + result of remaining string shifted on len of last ord
    return str_to_num_rec(s[:-1]) * (10 ** len_cur_res) + ord(s[-1])