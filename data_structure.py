# A List stores multiple items in a single variable. It is ordered, changeable, and allows duplicate values
# Example of List
# fruits = ["Apple", "Banana", "Mango", "Apple"]
# print(fruits)
# print(fruits[0])

# # Add a new item
# fruits.append("Orange")

# print(fruits)




#A Tuple stores multiple items in an ordered collection, but you cannot change its items after creation
# Example of Tuple
colors = ("Red", "Green", "Blue")

# print(colors)
# print(colors[1])
# print(len(colors))




#A Set stores unique items. It automatically removes duplicate values, and its items do not have a fixed order
# Example of Set
# numbers = {10, 20, 30, 20, 40}

# print(numbers)

# # Add a new item
# numbers.add(50)

# print(numbers)




#A Dictionary stores data in key: value pairs. It is useful when you want to access information using a key.
# Example of Dictionary
student = {
    "name": "Rahul",
    "age": 21,
    "course": "Python"
}

print(student)
print(student["name"])

# Update a value
student["age"] = 22

print(student)