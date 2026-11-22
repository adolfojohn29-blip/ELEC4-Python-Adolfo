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


def find_student_index(students, student_id):
    for index, record in enumerate(students):
        if record[0].casefold() == student_id.casefold():
            return index

    return None


def search_student(students):
    student_id = input("Enter student ID to search: ").strip()
    index = find_student_index(students, student_id)

    if index is None:
        print("Student ID not found.")
        return

    print("Student found:")
    display_students([students[index]])


def update_student(students):
    student_id = input("Enter student ID to update: ").strip()
    index = find_student_index(students, student_id)

    if index is None:
        print("Student ID not found.")
        return

    print("Current record:")
    display_students([students[index]])

    full_name = input("New full name (Enter to keep current): ").strip() or students[index][1]
    course_section = input("New course and section (Enter to keep current): ").strip() or students[index][2]

    if any(not field or "|" in field for field in [full_name, course_section]):
        print("Fill in all fields and avoid using | in your answers.")
        return

    try:
        average = float(input("New general average: "))
    except ValueError:
        print("Please enter a number for the general average.")
        return

    if not 0 <= average <= 100:
        print("The general average must be from 0 to 100.")
        return

    updated_records = students.copy()
    saved_id = students[index][0]
    updated_records[index] = [
        saved_id, full_name, course_section, f"{average:.2f}"
    ]

    # Write the complete list before replacing students.txt.
    temporary_file = STUDENTS_FILE.with_suffix(".tmp")
    try:
        with open(temporary_file, "w", encoding="utf-8") as file:
            for record in updated_records:
                file.write("|".join(record) + "\n")

        temporary_file.replace(STUDENTS_FILE)
    except OSError as error:
        print(f"Could not update the record: {error}")
        return

    students[index] = updated_records[index]
    print("Student record updated.")


def main():
    students = load_students()
    print("=== P5 Student Information File System ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    while True:
        print("\n1. Add student")
        print("2. Display all students")
        print("3. Search by ID")
        print("4. Update student")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()