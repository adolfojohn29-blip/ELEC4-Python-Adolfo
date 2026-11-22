# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P8 - Inheritance and Polymorphism
# Date: November 23, 2026


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, course):
        # Let Person initialize the shared attributes.
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        print(
            f"Hi, I'm {self.name}, a {self.age}-year-old student "
            f"taking {self.course}."
        )


if __name__ == "__main__":
    print("=== P8 Inheritance and Polymorphism ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    person = Person("Jamie Santos", 22)
    student = Student("Alex Reyes", 21, "BS Information Technology")

    person.introduce()
    student.introduce()
    