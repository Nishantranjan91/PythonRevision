# a = (10,20,30,40)
# for i in a:
#     print(i)


# Traverse a tuple and print only even numbers
# numbers = (10, 15, 20, 25, 30, 35, 40)

# for num in numbers:
#     if num % 2 == 0:
#         print(num)



# Traverse a tuple and calculate the sum of all elements
numbers = (12, 25, 30, 45, 18, 50)

total = 0

for num in numbers:
    total = total + num

print("Tuple elements:", numbers)
print("Sum of all elements:", total)