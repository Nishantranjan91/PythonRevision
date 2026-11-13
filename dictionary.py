# a = {10:100, 20:200, 30:300, 40:400}
# print(a.get(30))





# a = {1:500, 2:1000, 3:1500, 4:200}
# print(a.get(2))



# Student Information System

student = {
    "name": "Nishant",
    "age": 22,
    "course": "Python",
    "marks": 85
}

# Access dictionary values
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])
print("Marks:", student["marks"])

# Add a new key-value pair
student["city"] = "Bihar"

# Update marks
student["marks"] = 90

# Display complete dictionary
print("\nUpdated Student Details:")
print(student)
