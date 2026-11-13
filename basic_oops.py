# a = 11
# b = 29
# print(a+b)



# def addition(a,b):
#     print(a+b)
# # addition(11,29)
# addition(22,23)    




# Banking Management System

# from abc import ABC, abstractmethod

# class BankAccount(ABC):

#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance  # Encapsulation

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposited: ₹{amount}")
#         else:
#             print("Invalid deposit amount")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdrawn: ₹{amount}")
#         else:
#             print("Insufficient balance or invalid amount")

#     def get_balance(self):
#         return self.__balance

#     def transfer(self, amount, other_account):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             other_account.deposit(amount)
#             print("Transfer successful!")
#         else:
#             print("Transfer failed!")

#     @abstractmethod
#     def calculate_interest(self):
#         pass


# class SavingsAccount(BankAccount):

#     def calculate_interest(self):
#         return self.get_balance() * 0.05


# class CurrentAccount(BankAccount):

#     def calculate_interest(self):
#         return 0


# # Creating objects
# account1 = SavingsAccount("Nishant", 10000)
# account2 = CurrentAccount("Rahul", 5000)

# account1.deposit(2000)
# account1.withdraw(1000)

# account1.transfer(3000, account2)

# print("Nishant Balance:", account1.get_balance())
# print("Rahul Balance:", account2.get_balance())

# print("Nishant Interest:", account1.calculate_interest())
# print("Rahul Interest:", account2.calculate_interest())





# Employee Management System

from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid salary")

    @abstractmethod
    def calculate_bonus(self):
        pass

    def display_details(self):
        print("\nEmployee:", self.name)
        print("ID:", self.employee_id)
        print("Salary:", self.get_salary())
        print("Bonus:", self.calculate_bonus())


class Manager(Employee):

    def calculate_bonus(self):
        return self.get_salary() * 0.20


class Developer(Employee):

    def calculate_bonus(self):
        return self.get_salary() * 0.15


class Intern(Employee):

    def calculate_bonus(self):
        return self.get_salary() * 0.05


# Creating employee objects
employees = [
    Manager("Nishant", 101, 80000),
    Developer("Rahul", 102, 60000),
    Intern("Nidhi", 103, 20000)
]

# Display employee details
for emp in employees:
    emp.display_details()

# Calculate total salary expense
total_expense = sum(
    emp.get_salary() + emp.calculate_bonus()
    for emp in employees
)

print("\nTotal Company Expense:", total_expense)
