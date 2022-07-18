from enum import Enum
import collections

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person:
    def __init__(self):
        person = Person()
        firstname = ''
        lastname = ''
        dob = ''

    def update_first_name(self):
        pass

    def update_last_name(self):
        pass

    def update_dob(self):
        pass

    def update_status(self):
        pass


class Instructor(Person):
    def __init__(self):
        instructor_id = "Instructor_", 0
    # need to implement super class calls


class Student(Person):
    def __init__(self):
        student_id = "Student_", 0


class ZipCodeStudent(Student):
    pass


class CollegeStudent(Student):
    def __init__(self):
        college_name = "University"


class Classroom:
    student_dict = {'student_tuple': 0}
    # 0 should eventually be student ID

    def __init__(self):
        new_class = Classroom()

    def add_instructor(self):
        pass

    def remove_instructor(self):
        pass

    def add_student(self):
        pass

    def remove_student(self):
        pass

    def print_instructors(self):
        pass

    def print_students(self):
        pass

