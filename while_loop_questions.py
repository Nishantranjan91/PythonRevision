# Print each digit in reverse order:
# a = int(input("please give me a number whose reverse you want to find:- "))
# while a>0:
#     print(a%10)
#     a = a//10


# sum of digits:
# a = int(input("please give me a number whose sum of digits you to find:-"))
# sum = 0
# while a > 0:
#     sum = sum+a%10
#     a =a //10
# print(sum)    


# palindrome number check:
# a = int(input("please give me number and i will check whether it palindromic or not ? :-"))
# copy = a
# rev = 0
# while a>0:
#     rev = rev*10+a%10
#     a = a//10
# if rev == copy:    
#     print("yes your number is palindrome")
# else:
#     print("sorry your number is not palindrome")     



# Automorphic number 
a = 5
square = a**2
count = 0 
while a>0:
    count = count+1
    a = a//10
    print(count)