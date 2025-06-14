# main.py

# Import the StudentManager class from the students_manager.py file.
from students_manager import StudentManager

# Function to display the main menu options.
def display_menu():
    print("\n--- Welcome to the Student Management System ---")
    print("1. Add a New Student")
    print("2. Update Enrolled Subjects")
    print("3. Mark Subjects as Completed")
    print("4. Search for a Student")
    print("5. Show All Students")
    print("6. Exit")
    print("-----------------------------------------------")

# This is the main function that runs the application.
def main():
    # Create an instance of StudentManager to manage student data.
    manager = StudentManager()

    # Keep the program running until the user chooses to exit.
    while True:
        # Show the menu to the user.
        display_menu()

        # Ask the user to pick an option.
        choice = input("Enter your choice (1-6): ")

        # Option 1: Add a new student
        if choice == "1":
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            manager.add_student(student_id, student_name)

        # Option 2: Update enrolled subjects
        elif choice == "2":
            student_id = input("Enter student ID: ")
            student = manager.search_student(student_id)

            if student is not None:
                print("Current enrolled subjects:")
                for subject in student.subjects_enrolled:
                    print("- " + subject)

                new_subjects_str = input("Enter new subjects (separated by commas): ")
                new_subjects = []
                for subject in new_subjects_str.split(","):
                    subject = subject.strip()
                    if subject != "":
                        new_subjects.append(subject)

                manager.update_enrolled_subjects(student_id, new_subjects)
            else:
                print("Student not found.")

        # Option 3: Mark subjects as completed
        elif choice == "3":
            student_id = input("Enter student ID: ")
            student = manager.search_student(student_id)

            if student is not None:
                print("Subjects currently enrolled:")
                for subject in student.subjects_enrolled:
                    print("- " + subject)

                completed_subjects_str = input("Enter subjects to mark as completed (separated by commas): ")
                completed_subjects = []
                for subject in completed_subjects_str.split(","):
                    subject = subject.strip()
                    if subject != "":
                        completed_subjects.append(subject)

                manager.mark_subjects_completed(student_id, completed_subjects)
            else:
                print("Student not found.")

        # Option 4: Search for a student
        elif choice == "4":
            student_id = input("Enter student ID: ")
            student = manager.search_student(student_id)

            if student is not None:
                print("\n--- Student Found ---")
                print("ID: " + student.student_id)
                print("Name: " + student.student_name)

                print("Enrolled Subjects:")
                if len(student.subjects_enrolled) == 0:
                    print("None")
                else:
                    for subject in student.subjects_enrolled:
                        print("- " + subject)

                print("Completed Subjects:")
                if len(student.subjects_completed) == 0:
                    print("None")
                else:
                    for subject in student.subjects_completed:
                        print("- " + subject)
            else:
                print("Student not found.")

        # Option 5: Show all students
        elif choice == "5":
            manager.list_all_students()

        # Option 6: Exit the program
        elif choice == "6":
            print("Goodbye! Thanks for using the Student Management System.")
            break

        # If the user enters something invalid
        else:
            print("Invalid choice. Please choose a number from 1 to 6.")

# This makes sure the main function runs when you start the program.
if __name__ == "__main__":
    main()
