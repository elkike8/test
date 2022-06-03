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

    def say_im_cool(self):
        print(f"damn {self.name}, you are a cool cat for being {self.age} years old")


fer = Person()
fer.set_name("fer")
fer.set_age("ham")
fer.say_im_cool()

fer.set_age(33)
print(fer.age)
