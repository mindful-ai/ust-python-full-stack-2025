import json
import os

class Storage:

    def __init__(self, filepath="students.json"):
        self.filepath = filepath

    def save(self, student_list):
        with open(self.filepath, "w") as f:
            json.dump(student_list, f, indent=4)

    def load(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, "r") as f:
            return json.load(f)