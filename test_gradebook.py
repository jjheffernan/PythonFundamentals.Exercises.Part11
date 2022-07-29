import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import gradebook

"""
Migrated from PythonFundamentals.Exercises.Part8 
Use the below fileReader Test class to work develop framework for 
"""


class GradebookTest(unittest.TestCase):

    # @patch('sys.stdout', new_callable=StringIO)
    def test_create_person(self, mock_stdout):
        test_cases = [
            (
                (),
                (),
                (),
                ()
            )
        ]  # updated with tuples for names
        for test_person, expected in test_cases:
            with self.subTest(f"{test_person}"):
                expected = {} # person array of person details

                actual = gradebook.Person(test_cases[test_person])
                self.assertEqual(expected, actual)
                # - format for nested test case
                # file_reader.reckless_file_reader(file_path)
                # actual = mock_stdout.getvalue()
                # self.assertEqual(expected, actual)

    def test_update_Person_first_name(self):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)

    # @unittest.skip("Useless test. This exists simply to trigger and demo the function under test.")
    def test_update_Person_last_name(self):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)

    def test_update_Student_dob(self):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)

    def test_update_Teacher_status(self):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)

    def test_null_constructor_mixin(self):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)

    # @patch('sys.stdout', new_callable=StringIO)
    def test_create_Instructor(self, mock_stdout):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)

    # @patch('sys.stdout', new_callable=StringIO)
    def test_create_Zipcoder(self, mock_stdout):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)

    # @patch('sys.stdout', new_callable=StringIO)
    def test_test_create_college_student(self, mock_stdout):
        def test_create_person(self, mock_stdout):
            test_cases = [
                (
                    (),
                    (),
                    (),
                    ()
                )
            ]  # updated with tuples for names
            for test_person, expected in test_cases:
                with self.subTest(f"{test_person}"):
                    expected = {}  # person array of person details

                    actual = gradebook.Person(test_cases[test_person])
                    self.assertEqual(expected, actual)


class ClassRoomTest(unittest.TestCase):

    def test_create_classrom(self):
        test_classroom = gradebook.Classroom()
        test_cases = [
            (
                (),
                (),
                (),
                ()
            )
        ]  # updated with tuples for names
        expected = test_cases
        actual = test_classroom
        self.assertEqual(expected, actual)

    def test_add_instructor(self):

        pass

    def test_remove_instructor(self):
        pass

    def test_add_student(self):
        pass

    def test_remove_student(self):
        pass

    def test_print_instructors(self):
        # test case of teachers
        test_cases = []

        expected_results = []
        for school_room in test_cases:
            #     with self.subTest()
            expected_results[school_room] = gradebook.Classroom.print_instructors(test_cases[school_room])
        self.assertEquals(test_cases, expected_results)
        # pass
        pass

    # def test_list_instructors(self):
    #     pass

    def test_print_students(self):
        test_cases = []
        expected_results = []
        for school_room in test_cases:
            #     with self.subTest()
            expected_results[school_room] = gradebook.Classroom.print_students(test_cases[school_room])
        self.assertEquals(test_cases, expected_results)
        # pass


