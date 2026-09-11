# class Student:
#     def __init__(self, name, age):
#         self.name = name       # Attribute
#         self.age = age         # Attribute

#     def study(self):           # Method
#         print(self.name, "is studying.")

# s1 = Student("Rahul", 20)

# print(s1.name)
# print(s1.age)
# s1.study()




class Car:
    def __init__(self, brand, color):
        self.brand = brand      # Attribute
        self.color = color      # Attribute

    def drive(self):            # Method
        print("The car is driving.")

car1 = Car("Toyota", "Red")

print(car1.brand)
print(car1.color)
car1.drive()