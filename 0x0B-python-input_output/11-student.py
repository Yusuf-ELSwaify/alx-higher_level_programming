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

    def reload_from_json(self, json):
        """replaces all attributes of the Student"""
        for k, v in json.items():
            setattr(self, k, v)


if __name__ == "__main__":
    import os
    import sys

    Student = __import__('11-student').Student
    read_file = __import__('0-read_file').read_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    path = sys.argv[1]

    if os.path.exists(path):
        os.remove(path)

    student_1 = Student("John", "Doe", 23)
    j_student_1 = student_1.to_json()
    print("Initial student:")
    print(student_1)
    print(type(student_1))
    print(type(j_student_1))
    print("{} {} {}".format(student_1.first_name, student_1.last_name, student_1.age))


    save_to_json_file(j_student_1, path)
    read_file(path)
    print("\nSaved to disk")


    print("Fake student:")
    new_student_1 = Student("Fake", "Fake", 89)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))


    print("Load dictionary from file:")
    new_j_student_1 = load_from_json_file(path)

    new_student_1.reload_from_json(j_student_1)
    print(new_student_1)
    print(type(new_student_1))
    print("{} {} {}".format(new_student_1.first_name, new_student_1.last_name, new_student_1.age))
