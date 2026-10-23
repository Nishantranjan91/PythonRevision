# Python program to check palindrome number

# num = int(input("Enter a number: "))

# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print(original, "is a Palindrome number")
# else:
#     print(original, "is not a Palindrome number")



#Check whether a number is a palindrome
# num = 121
# original = num
# reverse = 0

# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# if original == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")




#Check a number using string slicing
num = 12321

reverse = int(str(num)[::-1])

if num == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")