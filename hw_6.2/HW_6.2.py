#!/usr/bin/env python3.6


class prop(object):
    """Emulate property."""
    def __init__(self, fget):
        self.fget = fget

    def __get__(self, obj, a):
        return self.fget(obj)

    def setter(self, fset):
        self.fset = fset

    def __set__(self, smth, value):
        return self.fset(smth, value)


class Something:
    """Tests prop."""
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def set_attr(self, update):
        self.x = update


if __name__ == '__main__':
    s = Something(10)
    print(s.attr)
    s.attr = 3
    print(s.attr)