# a = [10,15,20,25,30,35,40,45,50]
# search = 30
# for i in range(len(a)):
#     if a[i] == search:
#         print(f"element fount at index {i}")
#         break
# else:
#     print("sorry no search element is exist.")    




# Find all positions where the number 20 appears in a list.
numbers = [10, 20, 30, 20, 40, 20, 50]

target = 20

positions = []

for i in range(len(numbers)):
    if numbers[i] == target:
        positions.append(i)

print("Positions:", positions)