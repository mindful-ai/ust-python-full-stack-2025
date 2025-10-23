import uuid

class Student:

    def __init__(self, name, age, grade, student_id=None):
        self.id = student_id if student_id else str(uuid.uuid4())
        self.name = name
        self.age = age
        self.grade = grade

    def to_dict(self):
        return {
            "id":self.id,
            "name": self.name,
            "age":self.age,
            "grade": self.grade
        }
    
    @staticmethod
    def from_dict(data):
        return Student(
            name=data["name"],
            age=data["age"],
            grade=data["grade"],
            student_id=data["id"]
        )
    
if __name__ == "__main__":
    # add your tests here
    pass