# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P5 - Student Information File System
# Date: November 23, 2026

from pathlib import Path

STUDENTS_FILE = Path(__file__).with_name("students.txt")


def load_students():
    # Look for students.txt beside this Python file.
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
            return [line.strip().split("|") for line in file if line.strip()]
    except FileNotFoundError:
        return []


def display_students(students):
    if not students:
        print("No student records yet.")
        return

    for student_id, full_name, course_section, average in students:
        print(f"{student_id} | {full_name} | {course_section} | {average}")


def add_student(students):
    student_id = input("Student ID: ").strip()
    full_name = input("Full name: ").strip()
    course_section = input("Course and section: ").strip()

    fields = [student_id, full_name, course_section]
    if any(not field or "|" in field for field in fields):
        print("Fill in all fields and avoid using | in your answers.")
        return

    if any(record[0].casefold() == student_id.casefold() for record in students):
        print("A student with that ID already exists.")
        return

    try:
        average = float(input("General average: "))
    except ValueError:
        print("Please enter a number for the general average.")
        return

    if not 0 <= average <= 100:
        print("The general average must be from 0 to 100.")
        return

    record = [student_id, full_name, course_section, f"{average:.2f}"]

    # Append one record while keeping the existing records in the file.
    try:
        with open(STUDENTS_FILE, "a", encoding="utf-8") as file:
            file.write("|".join(record) + "\n")
    except OSError as error:
        print(f"Could not save the record: {error}")
        return

    students.append(record)
    print("Student record saved.")


def main():
    students = load_students()
    print("=== P5 Student Information File System ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    while True:
        print("\n1. Add student")
        print("2. Display all students")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
