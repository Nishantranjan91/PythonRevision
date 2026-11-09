# 




# Given an array, find all elements that occur exactly once.
# arr = [10, 20, 30, 20, 40, 10, 50, 60, 30]

# unique = []

# for num in arr:
#     if arr.count(num) == 1:
#         unique.append(num)

# print("Unique elements:", unique)





# Given two arrays, find elements that are present in both arrays without duplicates.
arr1 = [10, 20, 30, 40, 50, 20]
arr2 = [20, 30, 60, 70, 30]

unique = []

for num in arr1:
    if num in arr2 and num not in unique:
        unique.append(num)

print("Common unique elements:", unique)