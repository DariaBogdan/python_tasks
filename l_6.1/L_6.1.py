#!/usr/bin/env python3.6
class Price:
    """Descriptor for checking that price is in range 0..100"""
    def __get__(self, instance, owner):
        return instance._price

    def __set__(self, instance, value):
        assert isinstance(value, (int, float)) and 0 <= value <= 100, "value must be numeric in 0..100"
        instance._price = value

    def __delete__(self, instance):
        del instance._price


class Book:
    """Stands for the book.

    Attributes:
        author_name (str): author name.
        book_name (str): book name.
        price (int, float): price for the book.
    """
    price = Price()

    def __init__(self, author_name, book_name, price):
        self.author_name = author_name
        self.book_name = book_name
        self.price = price


if __name__ == '__main__':
    b = Book("a", "b", 12)
    c = Book("a", "b", 13)
    print(b.price)
    print(c.price)
    print(type(b.price))
    b.price = -12
