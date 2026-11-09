# 




# Given an array, find all elements that occur exactly once.
arr = [10, 20, 30, 20, 40, 10, 50, 60, 30]

unique = []

for num in arr:
    if arr.count(num) == 1:
        unique.append(num)

print("Unique elements:", unique)