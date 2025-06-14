# This class stores information about one student.
class Student:
    def __init__(self, student_id, student_name, subjects_enrolled=None, subjects_completed=None):
        # Store basic student info
        self.student_id = student_id
        self.student_name = student_name

        # If no subjects are given, use empty lists
        if subjects_enrolled is None:
            self.subjects_enrolled = []
        else:
            self.subjects_enrolled = subjects_enrolled

        if subjects_completed is None:
            self.subjects_completed = []
        else:
            self.subjects_completed = subjects_completed

    # This makes it easy to turn a Student into a string (for saving to file)
    def __str__(self):
        # Convert subject lists into strings with semicolons
        enrolled_str = ';'.join(self.subjects_enrolled)
        completed_str = ';'.join(self.subjects_completed)
        return f"{self.student_id},{self.student_name},{enrolled_str},{completed_str}"

import os   # Helps check if a file exists

# This class manages a list of students and handles saving/loading
class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename          # File to store student data
        self.students = []                # List to keep all student objects
        self.load_students()              # Load students from file when starting

    # Load students from file
    def load_students(self):
        self.students = []  # Clear list first
        if not os.path.exists(self.filename):
            print("No student file found. Starting fresh.")
            return

        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line == "":
                        continue  # Skip empty lines

                    parts = line.split(',')

                    # Make sure we have at least student ID and name
                    if len(parts) < 2:
                        print(f"Skipping invalid line (not enough parts): {line}")
                        continue

                    student_id = parts[0]
                    name = parts[1]

                    # Handle enrolled and completed subjects
                    if len(parts) > 2 and parts[2] != "":
                        enrolled = parts[2].split(';')
                    else:
                        enrolled = []

                    if len(parts) > 3 and parts[3] != "":
                        completed = parts[3].split(';')
                    else:
                        completed = []

                    # Create Student object and add to list
                    student = Student(student_id, name, enrolled, completed)
                    self.students.append(student)
        except Exception as e:
            print(f"Error loading students from file: {e}")

    # Save students to file
    def save_students(self):
        try:
            with open(self.filename, 'w') as file:
                for student in self.students:
                    file.write(str(student) + '\n')
        except Exception as e:
            print(f"Error saving students to file: {e}")

    # Add a new student
    def add_student(self, student_id, student_name):
        if not student_id or not student_name:
            print("Student ID and name cannot be empty.")
            return False

        # Check if student already exists
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists.")
                return False

        try:
            # Create and add student
            new_student = Student(student_id, student_name)
            self.students.append(new_student)
            self.save_students()
            print("Student added.")
            return True
        except Exception as e:
            print(f"Error adding student: {e}")
            return False

    # Update what subjects a student is enrolled in
    def update_enrolled_subjects(self, student_id, subjects):
        try:
            for student in self.students:
                if student.student_id == student_id:
                    student.subjects_enrolled = subjects
                    self.save_students()
                    print("Enrolled subjects updated.")
                    return True
            print("Student not found.")
            return False
        except Exception as e:
            print(f"Error updating subjects: {e}")
            return False

    # Move subjects from enrolled to completed
    def mark_subjects_completed(self, student_id, subjects):
        try:
            for student in self.students:
                if student.student_id == student_id:
                    for subject in subjects:
                        if subject not in student.subjects_completed:
                            student.subjects_completed.append(subject)
                        if subject in student.subjects_enrolled:
                            student.subjects_enrolled.remove(subject)
                    self.save_students()
                    print("Subjects marked as completed.")
                    return True
            print("Student not found.")
            return False
        except Exception as e:
            print(f"Error marking subjects as completed: {e}")
            return False

    # Find and return a student by ID
    def search_student(self, student_id):
        try:
            for student in self.students:
                if student.student_id == student_id:
                    return student
            return None
        except Exception as e:
            print(f"Error searching for student: {e}")
            return None

    # Print all students
    def list_all_students(self):
        try:
            if len(self.students) == 0:
                print("No students found.")
                return

            print("\n--- All Students ---")
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.student_name}")
                if student.subjects_enrolled:
                    print(f"  Enrolled: {', '.join(student.subjects_enrolled)}")
                else:
                    print("  Enrolled: None")

                if student.subjects_completed:
                    print(f"  Completed: {', '.join(student.subjects_completed)}")
                else:
                    print("  Completed: None")
            print("--------------------")
        except Exception as e:
            print(f"Error listing students: {e}")
