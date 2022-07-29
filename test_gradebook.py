import unittest
from unittest.mock import patch, mock_open
from io import StringIO
import gradebook

"""
Migrated from PythonFundamentals.Exercises.Part8 
Use the below fileReader Test class to work develop framework for 
"""


class GradebookTest(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
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
        test_cases = [
            ("locked_out_file.txt", PermissionError),
            ("file_that_does_not_exist.txt", FileNotFoundError)
        ]
        for file_path, expected in test_cases:
            with self.subTest(f"{file_path}"):
                with self.assertRaises(expected):
                    file_reader.reckless_file_reader(file_path)

    # @unittest.skip("Useless test. This exists simply to trigger and demo the function under test.")
    def test_update_Person_last_name(self):
        with self.assertRaises(PermissionError):
            file_reader.quick_way_to_get_fired("locked_out_file.txt")

    def test_update_Student_dob(self):
        with self.assertLogs() as cm:
            file_reader.single_exception_handling_reader("file_that_does_not_exist.txt")
            self.assertIn("No such file or directory: 'file_that_does_not_exist.txt'", cm.output[0])

    def test_update_Teacher_status(self):
        with self.assertRaises(PermissionError):
            file_reader.single_exception_handling_reader("locked_out_file.txt")

    def test_null_constructor_mixin(self):
        test_cases = [
            (
                "file_that_does_not_exist.txt",
                "No such file or directory: 'file_that_does_not_exist.txt'"
            ),
            (
                "locked_out_file.txt",
                "Permission denied: 'locked_out_file.txt'"
            )
        ]
        for file_path, message in test_cases:
            with self.subTest(f"{file_path} -> {message}"):
                with self.assertLogs() as cm:
                    file_reader.multiple_exception_handling_reader(file_path)
                    self.assertIn(message, cm.output[0])

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_Instructor(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.base_class_exception_handling_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_Zipcoder(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.tuple_exception_handling_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    @patch('sys.stdout', new_callable=StringIO)
    def test_test_create_college_student(self, mock_stdout):
        test_cases = [
            "locked_out_file.txt",
            "file_that_does_not_exist.txt"
        ]
        for file_path in test_cases:
            with self.subTest(f"{file_path}"):
                file_reader.better_file_reader(file_path)
                self.assertIn(
                    "Error opening the file. Please ensure the file exists and has appropriate permissions.",
                    mock_stdout.getvalue()
                )

    def test_create_classrom(self):
        test_classroom = gradebook.Classroom()

        with patch('file_reader.process_file') as cm:
            file_reader.better_file_reader("my_awesome_file.txt")
        cm.assert_called_once()

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


