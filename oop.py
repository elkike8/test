class Person:
    def __init__(self):
        pass

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            while True:
                try:
                    age = int(input("enter a valid age: "))
                    break
                except ValueError:
                    print("invalid input")

        self.age = age

    def speak(self):
        print(f"I am a person, my name is {self.name}")

    def say_im_cool(self):
        print(f"damn {self.name}, you are a cool cat for being {self.age} years old")


class Latino(
    Person
):  # inheritance, all the functions of the class in parenthesis are available, but the functions defined here override the parent ones
    def speak(self):
        print(f"I am latino, my name is {self.name} and I'm {self.age} years old")


fer = Latino()
fer.set_name("fer")
fer.set_age(33)
fer.speak()

kaja = Person()
kaja.set_name("kaja")
kaja.set_age(38)
kaja.speak()


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):  # the student is an instance of the student object
        if len(self.students) < self.max_students:
            self.students.append(student.name())
            print(f"{student} added into the course {self.name}")
        else:
            print(f"max student exceeded, couldn't add {student.name}")

