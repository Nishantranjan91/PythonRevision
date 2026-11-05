# a = {12,11,23,34,45,67,78,90}
# b = {10,19,22,12,13,23,59,89}
# print(a^b)



# Using symmetric_difference() method
# Creating two sets
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# # Finding symmetric difference
# result = A.symmetric_difference(B)

# print("Symmetric Difference:", result)




# Using ^ operator
# Creating two sets
# X = {"Apple", "Banana", "Mango"}
# Y = {"Banana", "Orange", "Grapes"}

# # Finding symmetric difference
# result = X ^ Y

# print("Symmetric Difference:", result)




# Bubble Sort in Ascending Order

# arr = [5, 3, 8, 2, 1]

# n = len(arr)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]

# print("Sorted Array:", arr)



#Bubble Sort in Descending Order

arr = [10, 4, 7, 2, 9]

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:", arr)

