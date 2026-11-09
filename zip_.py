# name = ["nishant", "santosh","sonu"]
# age = [27,22,20]
# combined = zip(name,age)
# print(list(combined))




# name = ["nishant", "santosh","sonu"]
# age = [27,22,20]
# combined = zip(name,age)
# print(dict(list(combined)))




# You are given two lists: student names and their marks. Use zip() to combine them and calculate the total marks after adding theory and practical marks
students = ["Rahul", "Amit", "Priya", "Neha"]

theory_marks = [75, 80, 85, 70]

practical_marks = [20, 15, 10, 25]

for name, theory, practical in zip(students, theory_marks, practical_marks):
    total = theory + practical

    print(name, "=", total)