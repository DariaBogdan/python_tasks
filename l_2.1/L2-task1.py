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
        res = res.union(s)
    return list(res)

def intersect(*args):
    """Allows to intersect any number of sets.
    ​
    :param *args: 'sets' to intersect.​
    :type *args: any iterable​
    :returns: list -- elements of resulted set.
    :raises: nothing
    """
    res = set(args[0])
    for s in args[1:]:
        res = res.intersection(s)
    return list(res)