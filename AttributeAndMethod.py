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
class Student:

    # Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Creating an object
s1 = Student("Nishant", 22)

# Calling method
s1.display()