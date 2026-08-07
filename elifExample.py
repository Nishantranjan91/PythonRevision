# a = float(input("please provide first number:"))
# b = float(input("please provide second number:"))
# if a>b:
#     print(f"{a}is greater than {b}")
# elif b>a:
#     print(f"{b} is greater than {a}")
# else:
#     print(f"{a} and {b} both are equal") 
        

# Example 2
# gen = input("please provide your gender in terms of m or f:")
# if gen == 'm':
#     print("hello sir how are you")
# else:
#     print("hello maam how are you")    


# Example 3
gen = input("please provide your gender in terms of m or f:")
if gen == 'm' or gen == 'M':
    print("hello sir how are you")
elif gen == 'f' or gen == 'F':
    print("hello maam how are you")
else:
    print("the given character is wrong.")        