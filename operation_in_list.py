#find the sum of every elements of a list
# a = [22,32,42,52,62,72]
# sum = 0
# for i in a:
#     sum = sum+i
# print(sum)    




# a = [22,32,42,52,62,72]
# sum = 0
# for i in a:
#     sum = sum+i
# print(f"average ot the total elements in this list is {sum/len(a)}")





a = [15,20,25,30,35,40,45,50]
max = a[0]
index = 0
for i in range(len(a)):
    if a[i]>max:
        max =  a[i]
        index = i
print(f"your largest element is {max} and its index is {index}")        