from student_manager import StudentManager
from storage import Storage
from student import Student

def display_students(students):
    if not students:
        print("No students found")
    for s in students:
        print(f"{s.id} -> {s.name}, {s.age}, {s.grade}")

def main():

    manager = StudentManager()
    storage = Storage()

    saved_data = storage.load()
    manager.load_student(saved_data)

    while True:

        print("1. Add Student")
        print("2. View All")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name    = input("Name    :")
            age     = input("Age     :")
            grade   = input("Grade   :")
            student = manager.add_student(name, age, grade)
            storage.save(manager.to_dict_list())
            print(f"Student added with ID: {student.id}")
        elif choice == '2':
            display_students(manager.get_all_student())
        elif choice == '3':
            sid = input("Enter the student ID: ")
            student = manager.find_by_id(sid)
            if student:
                print(f"{student.id} -> {student.name}, {student.age}, {student.grade}")
            else:
                print("Student not found")
        elif choice == '4':
            sid = input("Enter the student ID: ")
            if manager.delete_student(sid):
                storage.save(manager.to_dict_list())
                print("Student deleted")
            else:
                print("Student not found")
        elif choice == '5':
            print("Exiting")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()