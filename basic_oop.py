# Concept: A class is a blueprint, and an object is an instance of that class.
class Student:
    def display(self):
        print("Hello, I am a student")


# Creating object
s1 = Student()

# Calling method
s1.display()




# Concept: __init__() is a constructor. It automatically runs when an object is created.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Nishant", 22)
s1.display()




# Concept: Encapsulation means keeping data and methods together and restricting direct access to internal data.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def show_balance(self):
        print("Balance:", self.__balance)


account = BankAccount(5000)

account.show_balance()