# Two lists
# names = ["Alice", "Bob", "Charlie"]
# marks = [85, 90, 78]

# Using zip() to combine the lists
# result = zip(names, marks)

# Convert the zip object to a list
# zipped_list = list(result)

# Display the result
# print("Zipped List:")
# print(zipped_list)



# Using zip() with two lists

# names = ["Rahul", "Amit", "Priya"]
# marks = [85, 90, 95]

# result = zip(names, marks)

# print(list(result))




# Using zip() in a for loop

fruits = ["Apple", "Banana", "Mango"]
prices = [100, 40, 80]

for fruit, price in zip(fruits, prices):
    print(fruit, "costs", price, "rupees")
