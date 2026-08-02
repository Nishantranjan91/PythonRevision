# Function that returns the sum of two numbers
# def add(a, b):
#     return a + b

# # Call the function
# result = add(10, 20)

# # Print the returned value
# print("Sum =", result)


# Function that checks if a number is even
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# Test
num = 8

if is_even(num):
    print(num, "is even")
else:
    print(num, "is odd")