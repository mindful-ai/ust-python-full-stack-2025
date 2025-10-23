import unittest
from student_mgmt.student import Student

class TestStudent(unittest.TestCase):

    def test_create_student(self):
        s = Student("Anil", 20, "A")
        self.assertEqual(s.name, "Anil")
        self.assertEqual(s.age, 20)
        self.assertEqual(s.grade, "A")

    def test_dict_conversion(self):
        s = Student("Anil", 20, "A")
        d = s.to_dict()
        s2 = Student.from_dict(d)
        self.assertEqual(s.id, s2.id)