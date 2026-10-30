# a = [1,2,3,4,5]
# l = map(lambda x :x**2,a)
# print(list(l))




# a = [1,2,3,4,5,6]
# l = []
# for i in a:
#     if i%2 == 0:
#         l.append(i)
# print(l)        



#You have a list of numbers stored as strings. Convert all of them into integers using map().
numbers = ["10", "20", "30", "40", "50"]

result = list(map(int, numbers))

print("Original List:", numbers)
print("Converted List:", result)