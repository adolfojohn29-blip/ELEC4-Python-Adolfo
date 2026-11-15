
# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 15, 2026



def enter_grades():
    grades = []

    while True:
        try:
            grade = float(input("Enter grade (0-100): "))

            if not 0 <= grade <= 100:
                print("Invalid grade! Enter a number from 0 to 100.")
                continue

            grades.append(grade)

            again = input("Enter another grade? (yes/no): ").lower()

            if again == "no":
                break
            elif again != "yes":
                print("Invalid choice! Please enter yes or no.")

        except ValueError:
            print("Invalid input! Numbers only.")

    return grades



def calculate_average(grades):
    return sum(grades) / len(grades)


def get_highest_grade(grades):
    return max(grades)


def get_lowest_grade(grades):
    return min(grades)


def check_status(grades):
    if calculate_average(grades) >= 75:
        return "PASS"
    else:
        return "FAIL"


def main():
    grades = []

    while True:
        print("\n=== STUDENT GRADE CALCULATOR ===")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            grades = enter_grades()

        elif choice == "2":
            if len(grades) == 0:
                print("Please enter grades first.")
            else:
                print("\n=== GRADE RESULTS ===")
                print(f"Average Grade: {calculate_average(grades):.2f}")
                print(f"Highest Grade: {get_highest_grade(grades)}")
                print(f"Lowest Grade: {get_lowest_grade(grades)}")
                print(f"Status: {check_status(grades)}")

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()


# Local variables are created inside a function.
# For example, grades inside main() is a local variable.
# Global variables are declared outside functions.
# A global variable can be accessed by different functions.
# This program uses local variables to organize the grades.
