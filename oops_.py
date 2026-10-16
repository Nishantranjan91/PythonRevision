# A class is a blueprint, and an object is an instance of that class.
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# s1 = Student("Nishant", 21)
# s1.display()



# Encapsulation means combining data and methods in a class and controlling access to the data.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance:", self.__balance)

account = BankAccount(1000)
account.deposit(500)
account.show_balance()