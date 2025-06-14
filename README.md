# Student-manager
This console-based Python program efficiently manages student records, allowing for the tracking of current subject enrolments and previously completed subjects. It features a clear separation of concerns with a frontend module for user interaction and a backend module for persistent data handling using file storage.


#Project Overview
This console-based Python program efficiently manages student academic records. Developed as a collaborative group project by three students, it allows for the tracking of current subject enrolments and previously completed subjects for individual students. Designed with a focus on clear structure and data persistence, this project demonstrates fundamental programming concepts, including object-oriented programming and file handling within a team environment.

#Features
Student Data Management:
Add new students to the system.
View details for individual students or a list of all enrolled students.
Update student information, including subjects enrolled this year and subjects completed previously.
Subject Tracking:
Enroll students in new subjects.
Mark subjects as completed.

#Persistent Storage: All student data is automatically saved to a local file, ensuring information is retained between program sessions.
Modular Design: A clear separation between the user-facing frontend and the data-handling backend, promoting maintainability and scalability for team development.

#Technical Details
Language: Python 3
Core Concepts:
Object-Oriented Programming (OOP): Students are represented as objects of a Student class, encapsulating their ID, enrolled subjects, and completed subjects.
File I/O: Student data is read from and written to a text file (e.g., students.txt) to ensure persistence.
Modular Programming: The project is structured into distinct modules for frontend (user interaction) and backend (data logic and storage), facilitating parallel development within the team.
