# a,b,c,d = (100,200,300,400)
# print(a)
# print(b)
# print(c)
# print(d)





# Tuple Unpacking with * (Asterisk Operator)
# Original tuple
# numbers = (10, 20, 30, 40, 50, 60)

# # Tuple unpacking
# first, second, *remaining = numbers

# print("First:", first)
# print("Second:", second)
# print("Remaining:", remaining)




# Tuple Unpacking in a Function
# Function
def student_details(name, age, city):
    print("Student Name:", name)
    print("Age:", age)
    print("City:", city)


# Original tuple
student = ("Rahul", 22, "Patna")

# Tuple unpacking
student_details(*student)