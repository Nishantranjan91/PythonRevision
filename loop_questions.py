# print "nishant" n times
# n = int(input("please tell me how many times you want to print - "))
# for i in range(n):
#     print(f"{i+1}:nishant")



# print 28 to 1
# n = int(input("please tell me how many times you want to print - "))
# for i in range(n,0,-1):
#     print(i)     



# sum of natural numbers
# n = int(input("please tell me how many times you want to print - "))
# s = 0
# for i in range(1,n+1,1):
#     s = s+i
# print(s)    




# factorial of a number
# n = int(input("please tell me which number of factorial you want to print - "))
# m = 1
# for i in range(1,n+1,1):
#     m = m*i
# print(m)    




# sum of even and odd numbers in a range 
# n = int(input("please tell me a number upto the sum of even and odd you want to print - "))
# sum_even = 0
# sum_odd = 0
# for i in range(1,n+1,1):
#     if i%2 == 0:
#         sum_even = sum_even+i
#     else:
#         sum_odd = sum_odd+i
# print(f"your even sum is {sum_even} and odd sum is {sum_odd}")    




# print all factors of a number
n = int(input("please tell me a number which factors are you want to print - "))
for i in range(1,n+1,1):
    if n%i == 0:
        print(i)
