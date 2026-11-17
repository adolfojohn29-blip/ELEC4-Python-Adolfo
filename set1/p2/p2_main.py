
# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P2 - Custom Module
# Date: November 16, 2026

import student_utils
from student_utils import check_status
from datetime import datetime


def enter_grades():
    grades = []

    while True:
        try:
            grade = float(input("Enter grade (0-100): "))

            if grade < 0 or grade > 100:
                print("Invalid grade! Enter 0 to 100.")
                continue

            grades.append(grade)

            again = input("Add another grade? (yes/no): ").lower()
            if again == "no":
                break

        except ValueError:
            print("Invalid input! Numbers only.")

    return grades


def main():
    print("=== STUDENT GRADE REPORT ===")

    grades = enter_grades()

    print("\n=== RESULTS ===")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest_grade(grades)}")
    print(f"Lowest: {student_utils.get_lowest_grade(grades)}")
    print(f"Status: {check_status(grades)}")
    print(f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


if __name__ == "__main__":
    main()
