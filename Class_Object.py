# Create a class Student with name and roll_no. Display the student details.
# class Student:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no

#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)


# # Creating object
# s1 = Student("Rahul", 101)

# s1.display()





# Create a class Rectangle with length and breadth. Calculate and display the area.
# class Rectangle:
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def area(self):
#         print("Area =", self.length * self.breadth)


# # Creating object
# r1 = Rectangle(10, 5)

# r1.area()




# Create a class Employee with name and salary. Display employee details
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print("Employee Name:", self.name)
#         print("Salary:", self.salary)


# # Creating object
# e1 = Employee("Amit", 30000)

# e1.display()
# Create a class Circle with radius. Calculate the area of the circle
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        result = 3.14 * self.radius * self.radius
        print("Area of Circle =", result)


# Creating object
c1 = Circle(5)

c1.area()