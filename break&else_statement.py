# prime number or not ?
n = int(input("please tell me the number which is prime or not ?"))
for i in range(2,n):
    if n%i == 0:
        print("the number given is composite not prime ")
        break
else:
    print("your number is prime.")    