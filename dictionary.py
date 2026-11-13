# a = {10:100, 20:200, 30:300, 40:400}
# print(a.get(30))





# a = {1:500, 2:1000, 3:1500, 4:200}
# print(a.get(2))



# Student Information System

# student = {
#     "name": "Nishant",
#     "age": 22,
#     "course": "Python",
#     "marks": 85
# }

# # Access dictionary values
# print("Name:", student["name"])
# print("Age:", student["age"])
# print("Course:", student["course"])
# print("Marks:", student["marks"])

# # Add a new key-value pair
# student["city"] = "Bihar"

# # Update marks
# student["marks"] = 90

# # Display complete dictionary
# print("\nUpdated Student Details:")
# print(student)






# Online Shopping Cart

cart = {
    "Laptop": 50000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Headphones": 2000
}

# Display products
print("Shopping Cart:")

for product, price in cart.items():
    print(product, ":", price)

# Calculate total price
total = sum(cart.values())

print("\nTotal Amount:", total)

# Apply 10% discount
discount = total * 0.10

final_amount = total - discount

print("Discount:", discount)
print("Final Amount:", final_amount)

# Add a new product
cart["Monitor"] = 12000

print("\nUpdated Cart:", cart)
