from student import Student

class StudentManager:

    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        return student

    def get_all_student(self):
        return self.students

    def find_by_id(self, student_id):
        return next((s for s in self.students if s.id == student_id), None)

    def delete_student(self, student_id):
        student = self.find_by_id(student_id)
        if student:
            self.students.remove(student)
            return True
        else:
            return False

    def load_student(self, student_dicts):
        self.students = [Student.from_dict(d) for d in student_dicts]

    def to_dict_list(self):
        return [s.to_dict() for s in self.students]