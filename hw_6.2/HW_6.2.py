#!/usr/bin/env python3.6


class prop(object):
    """Emulate property."""
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, instance, a):
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)

    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        return self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        return self.fdel(instance)

    def setter(self, fset):
        self.fset = fset

    def getter(self, fget):
        self.fget = fget

    def deleter(self, fdel):
        self.fdel = fdel


class Something:
    """Tests prop."""
    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        return self.x ** 2

    @attr.setter
    def attr_setter(self, update):
        self.x = update


if __name__ == '__main__':
    s = Something(10)
    print(s.attr)
    s.attr = 3
    print(s.attr)