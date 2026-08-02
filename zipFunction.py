# Two lists
names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]

# Using zip() to combine the lists
result = zip(names, marks)

# Convert the zip object to a list
zipped_list = list(result)

# Display the result
print("Zipped List:")
print(zipped_list)