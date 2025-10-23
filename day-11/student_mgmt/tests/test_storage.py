import unittest
import os
from student_mgmt.storage import Storage


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.file = "test_students.json"
        self.storage = Storage(self.file)

    def test_save_and_load(self):
        data = [ {"id": 1, "name" : "Geetha", "age": 12, "grade": "A"}]
        self.storage.save(data)
        loaded = self.storage.load()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["name"], "Geetha")

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)