# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name          # Attribute
#         self.roll_no = roll_no    # Attribute
#         self.marks = marks        # Attribute

#     def display_details(self):    # Method
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Marks:", self.marks)

#     def calculate_grade(self):    # Method
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 75:
#             return "B"
#         elif self.marks >= 60:
#             return "C"
#         else:
#             return "D"


# s1 = Student("Rahul", 101, 82)

# s1.display_details()
# print("Grade:", s1.calculate_grade())






class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Current Balance:", self.balance)