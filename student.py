class Student:
    def __int__(self, student_id, name, grades=None):
        self.student_id = student_id
        self.name = name
        self.grades = grades if grades else []

    def add_grade(self, grade):
        """Add a grade to the student's record."""
        self.grades.append(grade)
    
    def calculate_average(self):
        """Calculate and return the average grade."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        """String representation for the student. """
        return f"ID: {self.student_id}, Name: {self.name}, Grades: {self.grades}, Average: {self.calculate_average():.2f}"