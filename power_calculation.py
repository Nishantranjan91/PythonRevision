a = int(input("provide a number: "))
b = int(input("provide the exponent: "))
power = a
for i in range(b-1):
    power = power*a
print(f"{power}")    
    