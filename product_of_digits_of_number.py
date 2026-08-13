a = int(input("please provide a number which digits product want to you:"))
product = 1 
while a > 0:
    digit = a % 10
    product = product *digit
    a = a//10
print(product)    