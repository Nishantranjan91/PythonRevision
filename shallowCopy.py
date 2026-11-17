# a = [10,20,30,40,50]
# b = a
# b[0] = 100
# print(a)
# print(b)



# a = [10,20,30,40,50]
# b = a.copy()
# b[0]=100
# print(a)
# print(b)




# a = [10,20,30,40,50,30]
# b = a.copy()
# b[0]=30
# print(a)
# print(b)




# a = [10,20,30,40,50,30,50,100,10]
# b = a.copy()
# b[0]=30
# print(a)
# print(b)




#Shallow copy using copy() method

# import copy

# original = [10, 20, 30]
# copied = copy.copy(original)

# copied[0] = 100

# print("Original list:", original)
# print("Copied list:", copied)





#Shallow copy with a nested list

# import copy

# original = [[1, 2], [3, 4]]
# copied = copy.copy(original)

# copied[0][0] = 100

# print("Original list:", original)
# print("Copied list:", copied)





# Shallow Copy using copy() method
# Original nested list
# original = [[10, 20], [30, 40], [50, 60]]

# # Creating shallow copy
# copied = original.copy()

# # Modifying the nested list
# copied[0][0] = 999

# # Adding a new element to the outer list
# copied.append([70, 80])

# print("Original List:", original)
# print("Copied List:", copied)




#Shallow Copy using copy module
import copy

# Original dictionary
original = {
    "name": "Rahul",
    "marks": [85, 90, 95],
    "city": "Patna"
}

# Creating shallow copy
copied = copy.copy(original)

# Modifying nested list
copied["marks"][0] = 100

# Modifying outer dictionary
copied["city"] = "Delhi"

print("Original Dictionary:", original)
print("Copied Dictionary:", copied)