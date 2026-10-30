# ran = range(1,11,1)
# for i in ran:
#     print("nishant ranjan")

#     # or


# for i in range(1,11,1):
#     print("nishant ranjan")




# table of 5
for i in range(5,51,5):
    print(i)






    # Write a Python program to find the second-largest number from a list using a for loop.
    numbers = [10, 25, 45, 30, 50, 15]

largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Largest number:", largest)
print("Second largest number:", second_largest)