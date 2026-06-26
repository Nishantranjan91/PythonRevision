a = 25 
dup = a
square = a**a
count = 0
while a>0:
    count = count + 1
    a = a //10
extract = square % (10**count)
if extract == dup:
    print("your number is automorphic")
else:
    print("your number is not an automorphic")    