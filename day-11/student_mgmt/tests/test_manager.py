import unittest
from student_mgmt.student_manager import StudentManager

class TestStudentManager(unittest.TestCase):

    def setUp(self):
        self.manager = StudentManager()

    def test_add_student(self):
        s = self.manager.add_student("Sunil", 18, "C")
        self.assertEqual(s.name, "Sunil")

    def test_find_by_id(self):
        s = self.manager.add_student("Vinil", 19, "A")
        found = self.manager.find_by_id(s.id)
        self.assertEqual(found.name, "Vinil")

    def test_delete_student(self):
        s = self.manager.add_student("Vinil", 19, "A") 
        self.assertTrue(self.manager.delete_student(s.id))
        self.assertIsNone(self.manager.find_by_id(s.id))