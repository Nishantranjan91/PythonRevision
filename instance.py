    class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):       # Instance method
        print("Name:", self.name)
        print("Age:", self.age)


# Creating an object (instance)
s1 = Student("Rahul", 20)

# Calling instance method
s1.display()