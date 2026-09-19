# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private variable

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         self.__balance += amount


# account = BankAccount(5000)

# account.deposit(2000)

# print(account.get_balance())






# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     def get_marks(self):
#         return self.__marks

#     def set_marks(self, marks):
#         if 0 <= marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid marks")


# student = Student("Nishant", 80)

# print(student.get_marks())

# student.set_marks(90)

# print(student.get_marks())






# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary

#     def get_salary(self):
#         return self.__salary

#     def increase_salary(self, amount):
#         if amount > 0:
#             self.__salary += amount


# emp = Employee("Rahul", 30000)

# print(emp.get_salary())

# emp.increase_salary(5000)

# print(emp.get_salary())






class ATM:
    def __init__(self, pin):
        self.__pin = pin

    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Correct PIN")
        else:
            print("Incorrect PIN")


atm = ATM(1234)

atm.check_pin(1234)
atm.check_pin(5678)







# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.__price = price

#     def get_price(self):
#         return self.__price

#     def set_price(self, new_price):
#         if new_price > 0:
#             self.__price = new_price
#         else:
#             print("Price must be greater than 0")


# product = Product("Laptop", 50000)

# print(product.get_price())

# product.set_price(55000)

# print(product.get_price())

# product.set_price(-1000)