# class Animal:
#     gender = "Male" # class attribute
#     name = "lion"
#     def __init__(self,name,age):
#         self.name = name #instance attribute
#         self.age = age
#     def info():
#         print("this is a method")    
#     def speak():
#         print("Lion is roaring")
# obj = Animal("lion",12)        
# obj.info()




# Student Class
# class Student:

#     # Attributes
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Method
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)


# # Creating an object
# s1 = Student("Nishant", 22)

# # Calling method
# s1.display()



# Car Class
class Car:

    # Attributes
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    # Method
    def start(self):
        print(self.brand, "car is starting")

    def show_details(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


# Creating an object
car1 = Car("BMW", "Black")

# Calling methods
car1.start()
car1.show_details()