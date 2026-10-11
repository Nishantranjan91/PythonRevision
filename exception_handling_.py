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
try:
    num = int(input("Enter a number: "))
    print("Number is:", num)

except ValueError:
    print("Please enter a valid number!")