#     class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):       # Instance method
#         print("Name:", self.name)
#         print("Age:", self.age)


# # Creating an object (instance)
# s1 = Student("Rahul", 20)

# # Calling instance method
# s1.display()






class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):           # Instance method
        return self.a + self.b

    def multiply(self):      # Instance method
        return self.a * self.b


c1 = Calculator(10, 5)

print("Addition:", c1.add())
print("Multiplication:", c1.multiply())