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





# a = [15,20,25,30,35,40,45,50]
# max = a[0]
# index = 0
# for i in range(len(a)):
#     if a[i]>max:
#         max =  a[i]
#         index = i
# print(f"your largest element is {max} and its index is {index}")        





#Second greatest element
a = [10,23,49,40,39,48,50]
max = a[0]
max2 = a[0]
index = 0
index2 = 0
for i in range(len(a)):
    if a[i]>max:
        max2 = max
        max = a[i]
        index2 = index
        index = i
    elif a[i]>max2:
        max2 = a[i]
        index2 = i    
print(f"max is {max} at {index} and max2 is {max2} at {index2}")        

