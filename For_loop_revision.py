# n = int(input("provide a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your total sum is {sum}")    




# n = int(input("please give a number: "))
# fact = 1
# for i in range(n,0,-1):
#     fact = fact*i
# print(f"factorial of {n} is {fact}.")    






n = int(input("please give a number: "))
even_sum = 0
odd_sum = 0
for i in range(1,n+1,1):
    if i%2 == 0:
      even_sum =even_sum+i   
    else:
       odd_sum = odd_sum+i       
print(f"sum  of odd is {odd_sum} and sum of even is {even_sum}")     