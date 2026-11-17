
# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P3 - Student Record Manager
# Date: November 16, 2026


students = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
    elif name.lower() in {student.lower() for student in students}:
        print("Student already exists!")
    else:
        students.append(name)
        print("Student added successfully!")


def remove_student():
    name = input("Enter student name to remove: ").strip()

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            print("Student removed successfully!")
            return

    print("Student not found.")


def search_student():
    name = input("Enter name to search: ").strip().lower()

    matches = [student for student in students if name in student.lower()]

    if matches:
        print("\nSearch Results:")
        for student in matches:
            print(student)
    else:
        print("No matching students found.")


def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n=== STUDENT LIST ===")
    for number, student in enumerate(sorted(students, key=str.lower), 1):
        print(f"{number}. {student}")

    print(f"Total Students: {len(students)}")


def main():
    while True:
        print("\n=== STUDENT RECORD MANAGER ===")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            display_students()
        elif choice == "5":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()


# A list stores student names and keeps their order.
# A set stores unique values and does not allow duplicates.
# In this program, I used a list to store student records.
# I used a set during duplicate checking to compare names.
# This helps prevent the same student from being added twice.
