#!/usr/bin/python3
"""Define class Student"""


class Student:
    """Blueprint for a student"""
    def __init__(self, first_name, last_name, age):
        """initialize a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of a Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.
        """
        if (type(attrs) != list or
                any(type(ele) != str for ele in attrs)):
            return self.__dict__

        return {k: getattr(self, k) for k in attrs if hasattr(self, k)}


if __name__ == "__main__":
    student_1 = Student("John", "Doe", 23)
    student_2 = Student("Bob", "Dylan", 27)

    j_student_1 = student_1.to_json()
    j_student_2 = student_2.to_json(['first_name', 'age'])
    j_student_3 = student_2.to_json(['middle_name', 'age'])

    print(j_student_1)
    print(j_student_2)
    print(j_student_3)
