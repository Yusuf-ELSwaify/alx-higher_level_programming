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
