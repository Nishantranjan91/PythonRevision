# A class is a blueprint, and an object is an instance of that class.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("Nishant", 21)
s1.display()