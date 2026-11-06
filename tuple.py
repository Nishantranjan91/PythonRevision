# tuple unpacking
# a,b,c = (10,11,12)
# print(a)
# print(b)
# print(c)


# type
# a = (99,)
# print(type(a)) # type of a is tuple because of comma



# list to tuple conversion:
# a = [10,20,30,40]
# b = tuple(a)
# print(b)



#Create and access elements of a tuple
# Creating a tuple
my_tuple = (10, 20, 30, 40, 50)

# Printing the tuple
# print("Tuple:", my_tuple)

# # Accessing elements
# print("First element:", my_tuple[0])
# print("Third element:", my_tuple[2])

# # Finding the length
# print("Length:", len(my_tuple))




# Tuple with different data types
# Creating a tuple with different data types
student = ("Nishant", 22, "Python", 85.5)

# Printing tuple elements
print("Student Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])
print("Marks:", student[3])

# Loop through tuple
print("All Student Details:")

for item in student:
    print(item)