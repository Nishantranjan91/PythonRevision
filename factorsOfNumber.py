# n = int(input("please provide a number: "))
# for i in range(1,n+1,1):
#     if n%i == 0:
#         print(i) 

    

n = int(input("please provide a number: "))
sum = 0
for i in range(1,n+1,1):
    if n%i == 0:
        sum = sum + i
print(f"sum of total factors is {sum}")        


