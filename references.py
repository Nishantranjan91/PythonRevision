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
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)