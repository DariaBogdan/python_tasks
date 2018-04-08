#!/usr/bin/env python3.6
class SchoolMember:
    """ Stands for school member and shows its fields.

    Attributes:
        name (str): the name of school member.
        age (int): the age of school member.

    Methods:
        show: displays all attributes.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f'Created SchoolMember: {name}')

    def show(self):
        print(f'Name:"{self.name}" Age:"{self.age}"')


class Teacher(SchoolMember):
    """ Stands for teacher and shows its fields.

    Attributes:
        name (str): the name of teacher.
        age (int): the age of teacher.
        salary (int): the teacher's salary.

    Methods:
        show: displays all attributes.
    """

    def __init__(self, name, age, salary):
        self.salary = salary
        super().__init__(name, age)
        print(f'Created Teacher: {name}')

    def show(self):
        print(f'Name:"{self.name}" Age:"{self.age}" Salary:"{self.salary}"')


class Student(SchoolMember):
    """ Stands for student and shows its fields.

    Attributes:
        name (str): the name of school member.
        age (int): the age of school member.
        marks (int): stusent's marks.

    Methods:
        show: displays all attributes.
    """

    def __init__(self, name, age, marks):
        self.marks = marks
        super().__init__(name, age)
        print(f'Created Student: {name}')

    def show(self):
        print(f'Name:"{self.name}" Age:"{self.age}" Marks:"{self.marks}"')


if __name__ == '__main__':
    persons = [Teacher("Mr. Poopybutthole", 40, 3000), Student("Morty", 16, 75)]
    for person in persons:
        person.show()