# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P7 - Student Management System with Classes
# Date: November 23, 2026


class Student:
    def __init__(self, student_id, full_name, grade):
        self.student_id = student_id
        self.full_name = full_name
        self.set_grade(grade)

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if not isinstance(grade, (int, float)) or not 0 <= grade <= 100:
            raise ValueError("Grade must be a number from 0 to 100.")

        self.__grade = grade

    def update_info(self, full_name, grade):
        self.set_grade(grade)
        self.full_name = full_name

    def display_info(self):
        print(f"{self.student_id} | {self.full_name} | Grade: {self.get_grade():.2f}")


class Subject:
    def __init__(self, code, title):
        self.code = code
        self.title = title


class Section:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        print(f"\nSection: {self.name}")
        print(f"Subject: {self.subject.code} - {self.subject.title}")
        for student in self.students:
            student.display_info()


def main():
    print("=== P7 Student Management System ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    subject = Subject("ELEC 4", "Python Programming")
    section = Section("IV-BSIT A", subject)

    alex = Student("ST001", "Alex Reyes", 89)
    section.add_student(alex)
    section.add_student(Student("ST002", "Sam Cruz", 90))
    section.add_student(Student("ST003", "Jamie Santos", 88))

    print("\nBefore update:")
    alex.display_info()

    alex.update_info("Alex Reyes", 94)
    print("\nUpdated ST001's grade to 94.00.")

    # Show that an invalid grade is rejected and the saved grade stays at 94.
    try:
        alex.set_grade(105)
    except ValueError as error:
        print(f"Invalid grade rejected: {error}")

    section.display_students()


if __name__ == "__main__":
    main()