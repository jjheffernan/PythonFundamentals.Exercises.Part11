from enum import Enum
import collections


class AliveStatus(Enum):
    Deceased = 0
    Alive = 1


class Person:
    def __init__(self, first_name, last_name, dob, status):
        self.person_arr = {
            'firstname': first_name,
            'lastname': last_name,
            'dateofbirth': dob,
            'status': AliveStatus.Alive
                      }
        # person = Person()
        # firstname = ''
        # lastname = ''
        # dob = ''
        # is_alive = AliveStatus.Alive

    def update_first_name(self, first_name):
        new_name = {'firstname': first_name}
        self.person_arr.update(new_name)
        return self.person_arr
        # pass # escape pass

    def update_last_name(self, last_name):
        new_name = {'lastname': last_name}
        self.person_arr.update(new_name)
        return self.person_arr
        # pass

    def update_dob(self, new_date):
        new_dob = {'dateofbirth': new_date}
        self.person_arr.update(new_dob)
        return self.person_arr
        # pass # escape return

    def update_status(self, new_status):
        event = {'status': new_status}
        self.person_arr.update(event)
        return self.person_arr
        # pass


class PersonMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Instructor(Person, PersonMixin):
    def __init__(self, instructor_id, first_name, last_name, dob, status):
        super().__init__(first_name, last_name, dob, status)
        person_arr = super().person_arr
        teach_id = {'instructor_id': instructor_id}
        person_arr.update(teach_id)
        # self, first_name, last_name , dob , status

        # instructor_id = "Instructor_", 0
    # need to implement super class calls


class Student(Person):
    def __init__(self, s_id, first_name, last_name, dob, status):
        super().__init__(first_name, last_name, dob, status)
        person_arr = super().person_arr
        student_id = {'Student_': s_id}
        person_arr.update(student_id)
        # student_id = "Student_", 0


class ZipCodeStudent(Student):
    pass


class CollegeStudent(Student):
    def __init__(self, college, first_name, last_name, dob, status):
        super().__init__(first_name, last_name, dob, status)
        person_arr = super().person_arr
        college_name = {'university': college}
        person_arr.update(college_name)
        # college_name = "University"


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

