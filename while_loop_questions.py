# Print each digit in reverse order:
a = int(input("please give me a number whose reverse you want to find:- "))
while a>0:
    print(a%10)
    a = a//10