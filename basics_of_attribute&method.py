class Student:
    def __init__(self, name, age):
        self.name = name       # Attribute
        self.age = age         # Attribute

    def study(self):           # Method
        print(self.name, "is studying.")

s1 = Student("Rahul", 20)

print(s1.name)
print(s1.age)
s1.study()