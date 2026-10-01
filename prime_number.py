n = int(input("please tell a number which is know you prime or not:-"))
count = 0
for i in range(1,n+1,1):
    if n%i == 0:
        print(i)
        count = count+1
if count == 2:
    print("the given number is prime") 
else:
    print("the given number is composit that means not prime")           