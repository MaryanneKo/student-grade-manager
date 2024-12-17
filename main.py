from grade_manager import GradeManager
from student import Student

def main():
    data_file = "data.txt"
    manager = GradeManager(data_file)
    manager.load_data()

    while True:
        print("\n--- Student Grade Management System ---")
        print("1. Add Student")
        print("2. Add Grade to Student")
        print("3. Display All Students")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            student = Student(student_id, name)
            manager.add_student(student)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            for student in manager.students:
                if student.student_id == student_id:
                    grade = int(input("Enter grade: "))
                    student.add_grade(grade)
                    print(f"Grade {grade} added for {student.name}.")
                    break
            else:
                print("Student not found.")
        elif choice == "3":
            manager.display_students()
        elif choice == "4":
            manager.save_data()
            print("Data saved successfully. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
