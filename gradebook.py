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
    teach_id = {'instructor_id': int, 'teacher_name': str}

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
    def __init__(self, college, first_name, last_name, dob, status):
        super().__init__(first_name, last_name, dob, status)
        person_arr = super().person_arr
        student_id = {'Student_': s_id}
        # college_name = {'university': college}
        person_arr.update(student_id)
        # college_name = "University"
    # pass


class CollegeStudent(Student):
    def __init__(self, college, first_name, last_name, dob, status):
        super().__init__(first_name, last_name, dob, status)
        person_arr = super().person_arr
        college_name = {'university': college}
        person_arr.update(college_name)
        # college_name = "University"


class Classroom:
    student_name = ''
    student_id = 0
    student_dict = {'student_name': student_name, 'student_id': student_id}
    # 0 should eventually be student ID
    teacher_name = ''
    teach_id = 0
    teach_dict = {'teacher_name': teacher_name, 'teacher_id': teach_id}
    class_address = 0

    def __init__(self):
        new_class = Classroom()  # because nothing happens there is an error here.
        self.class_address += 1
        class_id = self.class_address
        self.teach_dict.update()
        self.student_dict.update()

        # 'teacher_name': teach_id,

    def add_instructor(self, teaching_id, teacher_name):
        self.teach_dict['teacher_id'] = teaching_id
        self.teach_dict['teacher_name'] = teacher_name
        # Instructor.teach_id
        return
        pass

    def remove_instructor(self, teach_id):
        self.teach_dict.pop(teach_id)
        pass

    def add_student(self, student_name, student_id):
        self.student_dict['student_name'] = student_name
        self.student_dict['student_id'] = student_id
        pass

    def remove_student(self, student_id):
        self.student_dict.pop(student_id)
        pass

    def print_instructors(self):
        print(self.teach_dict)
        pass

    def print_students(self):
        print(self.student_dict)
        pass

