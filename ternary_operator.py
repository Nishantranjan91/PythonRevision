# age = int(input("please tell me your age -"))

# print("vote") if age >= 18 else print("not vote")


# A ternary operator is a shortcut for writing an if-else statement in a single line.
# age = 20

# result = "Adult" if age >= 18 else "Minor"

# print(result)




# Check Even or Odd
# num = 10

# result = "Even" if num % 2 == 0 else "Odd"

# print(result)




# Check Positive or Negative
# num = -5

# result = "Positive" if num > 0 else "Negative"

# print(result)





# Find the Greater Number
# a = 20
# b = 15

# result = a if a > b else b

# print(result)





# Check Voting Eligibility
# age = 17

# result = "Eligible" if age >= 18 else "Not Eligible"

# print(result)





# Check Pass or Fail
# marks = 45

# result = "Pass" if marks >= 40 else "Fail"

# print(result)





# Find the Greatest Among Three Numbers
# a = 10
# b = 25
# c = 15

# result = a if a > b and a > c else (b if b > c else c)

# print(result)




# Check Positive, Negative or Zero
# num = 0

# result = "Positive" if num > 0 else ("Negative" if num < 0 else "Zero")

# print(result)




# Assign Grade Based on Marks
# marks = 85

# grade = "A" if marks >= 90 else ("B" if marks >= 75 else ("C" if marks >= 50 else "Fail"))

# print(grade)




# Check Leap Year
# year = 2024

# result = "Leap Year" if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) else "Not Leap Year"

# print(result)





# Calculate Discount
price = 2000

discount = price * 0.20 if price >= 1000 else price * 0.10

final_price = price - discount

print("Discount:", discount)
print("Final Price:", final_price)