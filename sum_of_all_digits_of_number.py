# n = int(input("please provide the number which sum is want to you: "))
# sum = 0
# while n>0:
#     sum = sum +n % 10
#     n = n//10
# print(f"your total sum is {sum}")    




# Sum of digits of 1234

num = 1234
total = 0

while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10

print("Sum of digits:", total)
