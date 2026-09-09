# Create a class Student with name and roll_no. Display the student details.
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)


# Creating object
s1 = Student("Rahul", 101)

s1.display()