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


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age}-year-old teacher of {self.subject}.")


if __name__ == "__main__":
    print("=== P8 Inheritance and Polymorphism ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    people = [
        Person("Jamie Santos", 22),
        Student("Alex Reyes", 21, "BS Information Technology"),
        Teacher("Morgan Cruz", 35, "Python Programming"),
    ]

    for person in people:
        person.introduce()


# Student and Teacher inherit the shared name and age attributes from Person.
# Both child classes call super().__init__() to set those attributes.
# Each child class overrides introduce() to include details about its role.
# The loop shows polymorphism by calling introduce() on every object in the list.