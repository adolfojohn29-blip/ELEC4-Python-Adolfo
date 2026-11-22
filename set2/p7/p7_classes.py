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
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be from 0 to 100.")

        self.__grade = grade

    def display_info(self):
        print(f"{self.student_id} | {self.full_name} | Grade: {self.get_grade():.2f}")


if __name__ == "__main__":
    print("=== P7 Student Management System ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    student = Student("ST001", "Alex Reyes", 89)
    student.display_info()