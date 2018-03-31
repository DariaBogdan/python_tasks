def union(*args) -> list:
    """Allows to union any number of sets.
    ​
    :param *args: 'sets' to union.​
    :type *args: any iterable​
    :returns: list -- elements of resulted set.
    :raises: nothing
    """
    res = set()
    for s in args:
        for item in s:
            res.add(item)
    return list(res)


def intersect(*args) -> list:
    """Allows to intersect any number of sets.
    ​
    :param *args: 'sets' to intersect.​
    :type *args: any iterable​
    :returns: list -- elements of resulted set.
    :raises: nothing
    """
    res = set(union(*args))
    # we pass throw all the pairs of sets
    for s in args:
        for t in list(args[1:]) + [args[0]]:

            for item in s:
                if item not in t:
                    res.discard(item)

    return list(res)