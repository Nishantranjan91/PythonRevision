# Print each digit in reverse order:
# a = int(input("please give me a number whose reverse you want to find:- "))
# while a>0:
#     print(a%10)
#     a = a//10


# sum of digits:
a = int(input("please give me a number whose sum of digits you to find:-"))
sum = 0
while a > 0:
    sum = sum+a%10
    a =a //10
print(sum)    