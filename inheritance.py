# class Animal:
#     def __init__(self,name,age):
#             self.name = name
#             self.age = age
#     def info(self):
#           print(f"your name is {self.name} and your age is {self.age}")        
# obj1 = Animal("Lion",12)

# class Human(Animal):
#     def __init__(self, name, age,number,group):
#           super().__init__(name, age) 
#           self.number = number      

# obj = Animal("Lion",12)
# obj2 = ("Nishant",27,1212454515,"B+")
      



# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

#     def info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Year: {self.year}")


# class Car(Vehicle):
#     def __init__(self, brand, year, model, price):
#         super().__init__(brand, year)
#         self.model = model
#         self.price = price

#     def details(self):
#         self.info()   # Calling parent class method
#         print(f"Model: {self.model}")
#         print(f"Price: ₹{self.price}")


# # Object of Parent Class
# obj1 = Vehicle("Toyota", 2022)
# obj1.info()

# print("--------------------")

# # Object of Child Class
# obj2 = Car("Honda", 2024, "City", 1500000)
# obj2.details()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")


class Student(Person):
    def __init__(self, name, age, roll, course):
        super().__init__(name, age)
        self.roll = roll
        self.course = course

    def student_info(self):
        self.display()
        print(f"Roll   : {self.roll}")
        print(f"Course : {self.course}")


student = Student("Nishant", 22, 101, "B.Tech")

student.student_info()