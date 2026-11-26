# a = [10,15,20,25,30,35,40,45,50]
# search = 30
# for i in range(len(a)):
#     if a[i] == search:
#         print(f"element fount at index {i}")
#         break
# else:
#     print("sorry no search element is exist.")    




# Find all positions where the number 20 appears in a list.
# numbers = [10, 20, 30, 20, 40, 20, 50]

# target = 20

# positions = []

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         positions.append(i)

# print("Positions:", positions)




# Find the second largest unique number without using sort().
# numbers = [45, 12, 78, 34, 89, 78, 56]

# largest = float('-inf')
# second_largest = float('-inf')

# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num

#     elif num > second_largest and num != largest:
#         second_largest = num

# print("Second largest:", second_largest)




# Search for 35 in a list and display whether it exists.
numbers = [12, 25, 35, 48, 56, 67]

target = 35
found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Element found!")
else:
    print("Element not found!")