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
# import random

# # Generate a random integer between 1 and 10
# print(random.randint(1, 10))

# # Select a random item from a list
# fruits = ["Apple", "Banana", "Mango", "Orange"]
# print(random.choice(fruits))

# # Shuffle a list
# numbers = [1, 2, 3, 4, 5]
# random.shuffle(numbers)
# print(numbers)



# The datetime module helps you work with the current date, time, and dates in the past or future.
import datetime

# Get the current date
today = datetime.date.today()
print("Today's date:", today)

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Create a specific date
my_date = datetime.date(2026, 10, 19)
print("My date:", my_date)