a = int(input("provide first number:-"))
b = int(input("provide second number:-"))
try:
    print(a/b)
except ZeroDivisionError as err:
    print(f"sorry an error occured as {err}")
else:
    print("there was no errors")    
finally:
    print("i will execute no matter what")    
print(a+b)        