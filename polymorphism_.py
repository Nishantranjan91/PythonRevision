# #Different classes can have a method with the same name but different behavior
# class Dog:
#     def sound(self):
#         print("Dog says: Woof Woof")


# class Cat:
#     def sound(self):
#         print("Cat says: Meow")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()




# The same function can work with different types of objects.
# class Dog:
#     def sound(self):
#         return "Woof"


# class Cat:
#     def sound(self):
#         return "Meow"


# def make_sound(animal):
#     print(animal.sound())


# dog = Dog()
# cat = Cat()

# make_sound(dog)
# make_sound(cat)




# # A child class can override a method of its parent class.
# class Animal:
#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):
#     def sound(self):
#         print("Dog says Woof")


# class Cat(Animal):
#     def sound(self):
#         print("Cat says Meow")


# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     animal.sound()



# Python's built-in len() function works with different types of objects.
# name = "Nishant"
# numbers = [10, 20, 30, 40, 50]
# data = (1, 2, 3)

# print(len(name))
# print(len(numbers))
# print(len(data))





# Different classes can implement the same method in their own way.
# class Car:
#     def move(self):
#         print("Car is driving")


# class Boat:
#     def move(self):
#         print("Boat is sailing")


# class Plane:
#     def move(self):
#         print("Plane is flying")


# vehicles = [Car(), Boat(), Plane()]

# for vehicle in vehicles:
#     vehicle.move()




# Number 456
# Example 1
# num = 123
# if str(num) != str(num)[::-1]:
#     print(num, "is a non-palindromic number")

# # Example 2
# num = 456
# if str(num) != str(num)[::-1]:
#     print(num, "is a non-palindromic number")



# Create different shape classes (Circle, Rectangle, Triangle). Each class should have the same method area(), but calculate the area differently. Store their objects in an array (list) and call the same method
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# class Triangle:
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height


# # Array of different objects
# shapes = [
#     Circle(5),
#     Rectangle(10, 4),
#     Triangle(6, 8)
# ]

# # Polymorphism
# for shape in shapes:
#     print("Area:", round(shape.area(), 2))




# Create three employee classes: FullTime, PartTime and Freelancer. Each employee should have the same method calculate_salary(), but the salary calculation should be different.
class FullTime:
    def calculate_salary(self):
        return 50000


class PartTime:
    def calculate_salary(self):
        hours = 80
        rate = 200
        return hours * rate


class Freelancer:
    def calculate_salary(self):
        projects = 3
        payment = 15000
        return projects * payment


# Array of employee objects
employees = [
    FullTime(),
    PartTime(),
    Freelancer()
]

# Polymorphism
for employee in employees:
    print("Salary:", employee.calculate_salary())