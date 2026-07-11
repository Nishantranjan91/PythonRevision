# a = int(input("provide your numbers:-"))
# b = int(input("provide your numner:"))

# try:
#     print(a/b)
# except Exception as err:
#     print(f"sorry an error occured as {err}") 
# print(a+b)       




a = int(input("provide your numbers:-"))
b = int(input("provide your numner:"))

try:
    print(a/b)
except ZeroDivisionError as err:
    print(f"sorry an error occured as {err}") 
print(a+b)   




# a = int(input("provide your numbers:-"))
# b = int(input("provide your numner:"))

# try:
#     print(a/b)
# except Exception as err:
#     print(f"sorry an error occured as {err}") 
# print(a+b)       




#  a = int(input("provide your numbers:-"))
# # b = int(input("provide your numner:"))

# try:
#     print(a/b)
# except ZeroDivisionError as err:
#     print(f"sorry an error occured as {err}") 
# else:
#     print("There was no errors")    
# print(a+b)  





#  a = int(input("provide your numbers:-"))
# # b = int(input("provide your numner:"))

# try:
#     print(a/b)
# except ZeroDivisionError as err:
#     print(f"sorry an error occured as {err}") 
# else:
#     print("There was no errors")  
# finally:
#     print("I will execute no matter what !!")
# print(a+b)





# try:
#     age = int(input("Enter age:"))
#     if age < 18:
#         raise Exception("You must be 18+")
#     print("access granted")
# except Exception as e:
#     print("Error:", e)