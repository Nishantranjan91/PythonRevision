# n = int(input("provide a number to find the no is prime or not "))
# count = 0
# for i in range(1,n+1,1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print(f"{n} is a prime number")   
# else:
#     print(f"{n} is not a prime number")         

    



n = int(input("provide a number to find the no is prime or not "))
count = 0
for i in range(1,n+1,1):
    if n % i == 0:
        count = count + 1
if count == 1:
    print(f"{n} is a unity number")        
elif count == 2:
    print(f"{n} is a prime number")   
else:
    print(f"{n} is not a prime number")