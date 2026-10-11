# a = int(input("provide first number:-"))
# b = int(input("provide second number:-"))
# try:
#     print(a/b)
# except ZeroDivisionError as err:
#     print(f"sorry an error occured as {err}")
# else:
#     print("there was no errors")    
# finally:
#     print("i will execute no matter what")    
# print(a+b)        



# raise
# try:
#     age = int(input("please give me your age:-"))
#     if age < 18:
#         raise Exception("you must be 18+")
#     print("access granted")
# except Exception as e:
#     print("error",e)    




# ZeroDivisionError
# try:
#     a = 10
#     b = 0
#     print(a / b)

# except ZeroDivisionError:
#     print("Cannot divide by zero!")




# ValueError
# try:
#     num = int(input("Enter a number: "))
#     print("Number is:", num)

# except ValueError:
#     print("Please enter a valid number!")




# FileNotFoundError
# try:
#     file = open("data.txt", "r")
#     print(file.read())
#     file.close()

# except FileNotFoundError:
#     print("File not found!")




# IndexError
# try:
#     numbers = [10, 20, 30]
#     print(numbers[5])

# except IndexError:
#     print("Index is out of range!")



# Multiple Exceptions with finally
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    print("Please enter a valid number!")

except ZeroDivisionError:
    print("Number cannot be zero!")

finally:
    print("Program execution completed.")