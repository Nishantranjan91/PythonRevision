# a = {10:100,20:200,30:300,40:400}
# a.pop(30)
# print(a)




# a = {10:100,20:200,30:300,40:400}
# popped = a.pop(30)
# print(popped)




# a = {10:100,20:200,30:300,40:400}
# popped = a.popitem()
# print(popped)



# emove a specific key
# student = {
#     "name": "Nishant",
#     "age": 22,
#     "course": "Python"
# }

# result = student.pop("age")

# print(result)
# print(student)





# Remove a key with a default value
student = {
    "name": "Nishant",
    "age": 22,
    "course": "Python"
}

result = student.pop("city", "Not Found")

print(result)
print(student)