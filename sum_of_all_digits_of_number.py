n = int(input("please provide the number which sum is want to you: "))
sum = 0
while n>0:
    sum = sum +n % 10
    n = n//10
print(f"your total sum is {sum}")    
