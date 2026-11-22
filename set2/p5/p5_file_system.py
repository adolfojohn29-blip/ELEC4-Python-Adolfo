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


if __name__ == "__main__":
    print("=== P5 Student Information File System ===")
    print("John Nicole R Adolfo | IV-BSIT A")
    display_students(load_students())
    