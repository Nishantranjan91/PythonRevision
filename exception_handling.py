a = int(input("please provide the first number:"))
b = int(input("please provide the second number:"))

try:
    print(a/b)

except Exception as err:
    print(f"sorry an error occured as {err}")    
print(a+b)