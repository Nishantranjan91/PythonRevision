a = int(input("provide first number:-"))
b = int(input("provide second number:-"))
try:
    print(a/b)
except Exception as err:
    print(f"sorry an error occured as {err}")
print(a+b)        