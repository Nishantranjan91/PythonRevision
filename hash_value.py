# Using the built-in hash() function
# num = 100

# result = hash(num)

# print(result)




# Creating a hash using SHA-256
import hashlib

text = "Hello"

result = hashlib.sha256(text.encode())

print(result.hexdigest())