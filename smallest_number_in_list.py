# Using the min() function
# numbers = [45, 12, 78, 5, 23, 9]

# smallest = min(numbers)

# print("Smallest number is:", smallest)




# Using a for loop
numbers = [45, 12, 78, 5, 23, 9]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)