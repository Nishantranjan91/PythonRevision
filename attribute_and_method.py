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






# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient balance")

#     def show_balance(self):
#         print("Current Balance:", self.balance)






# class Car:
#     def __init__(self, brand, model, speed):
#         self.brand = brand
#         self.model = model
#         self.speed = speed

#     def accelerate(self, increase):
#         self.speed += increase

#     def brake(self, decrease):
#         self.speed -= decrease

#     def display_speed(self):
#         print("Current speed:", self.speed)






# class Employee:
#     def __init__(self, name, employee_id, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary

#     def display_details(self):
#         print("Name:", self.name)
#         print("Employee ID:", self.employee_id)
#         print("Salary:", self.salary)

#     def increase_salary(self, percentage):
#         self.salary += self.salary * percentage / 100

#     def annual_salary(self):
#         return self.salary * 12


# emp = Employee("Amit", 102, 30000)

# emp.display_details()
# emp.increase_salary(10)

# print("New Salary:", emp.salary)
# print("Annual Salary:", emp.annual_salary())






class MobilePhone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def make_call(self, number):
        print("Calling", number)

    def charge(self, amount):
        self.battery += amount

        if self.battery > 100:
            self.battery = 100

    def show_battery(self):
        print("Battery:", self.battery, "%")


phone = MobilePhone("Samsung", "Galaxy S24", 50)

phone.make_call("9876543210")
phone.charge(30)
phone.show_battery()