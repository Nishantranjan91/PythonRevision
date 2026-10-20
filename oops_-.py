# A class is a blueprint, and an object is an instance of that class.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# # Creating an object
# s1 = Student("Rahul", 21)

# s1.display()




# Encapsulation means keeping data and the methods that operate on it together, while controlling how the data is accessed.
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print("Balance:", self.__balance)

# account = BankAccount(1000)

# account.deposit(500)
# account.show_balance()




# Inheritance allows one class to reuse and extend the functionality of another class.
# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()

# d.eat()
# d.bark()




# Polymorphism means that the same method name can have different behavior in different classes.
# class Addition:
#     def calculate(self, a, b):
#         print("Sum:", a + b)

# class Multiplication:
#     def calculate(self, a, b):
#         print("Product:", a * b)

# obj1 = Addition()
# obj2 = Multiplication()

# obj1.calculate(5, 3)
# obj2.calculate(5, 3)




# Abstraction means hiding implementation details and exposing only the essential functionality.
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):
    def pay(self, amount):
        print("Paid Rs.", amount, "using UPI")

class Card(Payment):
    def pay(self, amount):
        print("Paid Rs.", amount, "using Card")

p1 = UPI()
p2 = Card()

p1.pay(500)
p2.pay(1000)