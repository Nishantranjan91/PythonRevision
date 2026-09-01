# a = int(input("please provide the first number:"))
# b = int(input("please provide the second number:"))

# try:
#     print(a/b)

# except Exception as err:
#     print(f"sorry an error occured as {err}")    
# print(a+b)




a = int(input("please provide the first number:"))
b = int(input("please provide the second number:"))

try:
    print(a/b)

except ZeroDivisionError as err:
    print(f"sorry an error occured as {err}")    
else:
    print("there was no errors")    
finally:
    print("I will execute no matter what")    
print(a+b)