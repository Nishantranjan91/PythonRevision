# def Shiv():
#     return "hello I am Nishant Ranjan"
# result = Shiv()
# print(result)




# def Shiv():
#     return "hello I am Nishant Ranjan"
# result = Shiv()
# print(Shiv())




# Create a function that calculates an employee's annual salary using their monthly salary.
# def calculate_salary(monthly_salary):
#     annual_salary = monthly_salary * 12
#     return annual_salary

# result = calculate_salary(30000)

# print("Annual Salary:", result)




# Create a function that accepts a list of student marks, finds the highest marks, and displays a message.
def highest_marks(marks):
    highest = max(marks)

    if highest >= 90:
        return "Excellent Performance"
    elif highest >= 75:
        return "Good Performance"
    else:
        return "Needs Improvement"


student_marks = [65, 82, 95, 78, 88]

result = highest_marks(student_marks)

print("Student Result:", result)