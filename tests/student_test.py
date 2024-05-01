import unittest
from student_repository import (
    save_student_record,
    get_student_record,
    update_student_record,
    get_all_students_record,
    delete_student_record,
    create_test_data_file,
    delete_test_data_file
)


class TestStudentRepository(unittest.TestCase):
    test_data_file = "students_test_data.json"
    student_record = {
        "name": "Ali Naqi Al-Musawi",
        "department": "Software Engineering",
        "program": "BSSE"
    }

    @classmethod
    def setUpClass(cls):
        # Create test data file before running tests
        create_test_data_file(
            {"student1": cls.student_record}, cls.test_data_file)

    @classmethod
    def tearDownClass(cls):
        # Delete test data file after running tests
        delete_test_data_file(cls.test_data_file)

    def test_save_student_record(self):
        # Test saving a new student record
        save_student_record(self.student_record, self.test_data_file)
        result = get_all_students_record(self.test_data_file)
        self.assertIn("student2", result)

    def test_get_student_record(self):
        # Test getting a student record
        student_id = "student1"
        result = get_student_record(student_id, self.test_data_file)
        self.assertEqual(result, self.student_record)

    def test_update_student_record(self):
        # Test updating a student record
        student_id = "student1"
        result = update_student_record(
            student_id, self.student_record, self.test_data_file)
        self.assertEqual(result[student_id], self.student_record)

    def test_get_all_students_record(self):

        create_test_data_file(
            {"student1": self.student_record}, self.test_data_file)

        # Test getting all student records
        result = get_all_students_record(self.test_data_file)
        self.assertIn("student1", result)
        self.assertEqual(result["student1"], self.student_record)

    def test_delete_student_record(self):
        # Test deleting a student record
        student_id = "student1"
        result = delete_student_record(student_id, self.test_data_file)
        self.assertNotIn(student_id, result)


if __name__ == "__main__":
    unittest.main()
