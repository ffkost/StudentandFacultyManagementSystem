# StudentandFacultyManagementSystem
This Python program models a student and faculty management system. It allows for managing student data, such as grades, average calculations, and adding/removing grades. Additionally, it manages a faculty's list of students and calculates overall averages for the faculty.

Student and Faculty Management System
Overview

This project is a Python-based system for managing student and faculty data. It uses object-oriented programming principles to create classes for Student and Faculty. The program supports managing student information (grades, averages, and corrections) and faculty operations, such as adding students and calculating overall averages.
Features

    Student Management:
        Add, update, or delete grades.
        Calculate the sum and average of grades for a student.
        Correct a specific grade.
        Display a personalized greeting and student information.
    Faculty Management:
        Add multiple students dynamically.
        Calculate the overall average grade of all students in the faculty.
        Display student details within the faculty.

Classes and Methods
1. Student Class

    Attributes:
        ime: First name of the student.
        prezime: Last name of the student.
        ocenki: List of grades.
    Methods:
        pozdrav: Greets with the student's full name and grades.
        prosek: Calculates the average of grades.
        dodadi_ocenka: Adds a grade to the student's list.
        izbrisi_ocenka: Removes a grade at a specific index.
        popravi: Corrects a grade by increasing it by 1.
        vnesi_ocenki: Allows dynamic input of grades.

2. Fakultet Class

    Attributes:
        ime: Name of the faculty.
        studenti: List of Student objects.
    Methods:
        iminja_na_studenti: Displays all students in the faculty.
        vnesi_studenti: Dynamically adds students and their grades.
        prosek: Calculates the overall average grade of the faculty.

How It Works

    Users can create Student objects with their names and grades.
    Faculty (Fakultet) manages multiple students.
    Users can dynamically input student names, grades, and manage faculty operations.

Usage

    Run the script in Python.
    Add students dynamically or hardcode them during initialization.
    Use the available methods to modify student grades, calculate averages, and display information.

Example Execution
Adding Students to Faculty:

Enter number of students to add: 2
Enter student name: John
Enter student last name: Doe
Enter number of grades: 3
Enter grade 1: 8
Enter grade 2: 9
Enter grade 3: 10

Output:

Fakultet za elektrotehnika i informaciski tehnologii 
Student: John Doe, Average Grade: 9.0
