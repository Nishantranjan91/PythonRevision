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

import copy

original = [10, 20, 30]
copied = copy.copy(original)

copied[0] = 100

print("Original list:", original)
print("Copied list:", copied)
