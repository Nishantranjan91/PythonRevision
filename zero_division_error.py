# a = int(input("provide first number:"))
# b = int(input("provide second number:"))
# print(a/b) #here if the value of b is zero



# Dividing a number by zero

# a = 10
# b = 0

# print(a / b)




#Handling ZeroDivisionError using try-except

try:
    a = 20
    b = 0
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
