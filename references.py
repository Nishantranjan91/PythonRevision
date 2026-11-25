# a = [10,20,30,40,50]
# b = a
# b[2] = 35
# print(b)
# print(a)


# Two variables referencing the same list
# list1 = [10, 20, 30]
# list2 = list1

# list2.append(40)

# print("List 1:", list1)
# print("List 2:", list2)



# Checking whether two variables reference the same object
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)
# print(a is c)




# ultiple variables referencing the same list
# list1 = [10, 20, 30]
# list2 = list1

# list2.append(40)

# print("List 1:", list1)
# print("List 2:", list2)





# Comparing is and ==
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# print(a == b)
# print(a is b)
# print(a is c)




# Shallow Copy
# import copy

# original = [[1, 2], [3, 4]]

# new_list = copy.copy(original)

# new_list[0].append(100)

# print("Original:", original)
# print("New List:", new_list)






# Function and Mutable References
# def update_list(numbers):
#     numbers.append(500)

# my_list = [100, 200, 300]

# update_list(my_list)

# print(my_list)




# Deep Copy vs Shallow Copy
import copy

original = {
    "name": "Nishant",
    "skills": ["Python", "SQL"]
}

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original["skills"].append("Power BI")

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)