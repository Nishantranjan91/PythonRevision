# The math module helps you perform mathematical calculations like square roots, powers, and factorials
# import math

# # Square root
# print(math.sqrt(25))

# # Power
# print(math.pow(2, 3))

# # Factorial
# print(math.factorial(5))

# # Value of pi
# print(math.pi)




# The random module generates random numbers and selects random items.
import random

# Generate a random integer between 1 and 10
print(random.randint(1, 10))

# Select a random item from a list
fruits = ["Apple", "Banana", "Mango", "Orange"]
print(random.choice(fruits))

# Shuffle a list
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)