from student import Student

class GradeManager:
    def __init__(self, data_file):
        self.data_file = data_file
        self.students = []

    def load_data(self):
        """Load students' data from a file."""
        try:
            with open(self.data_file, 'r') as file:
                for line in file:
                    student_id, name, *grades = line.strip().split(',')
                    grades = list(map(int, grades)) if grades else []
                    self.students.append(Student(student_id, name, grades))
        except FileNotFoundError:
            print("Data file not found. Starting with an empty list.")

    def save_data(self):
        """Save students' data to a file."""
        with open(self.data_file, 'w') as file:
            for student in self.students:
                file.write(f"{student.student_id},{student.name},{','.join(map(str, student.grades))}\n")

    def add_student(self, student):
        """Add a new student."""
        self.students.append(student)
        print(f"Student {student.name} added successfully!")

    def display_students(self):
        """Display all students and their grades."""
        for student in self.students:
            print(student)
