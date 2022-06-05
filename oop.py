class Person:
    number_of_people = 0  # class attribute

    def __init__(self, name: str, address: int):
        self.name = name
        self.address = address
        Person.add_person()

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

    def say_your_name(self):
        print(f"Hi, my name is {self.name}")

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


class Nordic(Person):
    def __init__(self, name, address, eye_color: str):
        super().__init__(name, address)
        # super calls the parent class
        # super method ensure the inheritance of the parent class while adding initial parametrization
        self.eye_color = eye_color


fer = Latino("fer", 33)
kaja = Person("kajs", "bajs")

# since number of people is a class attribute, it can be used both with an instance or the general class
print(fer.number_of_people)
print(Person.number_of_people)


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

