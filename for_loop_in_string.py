# s = "nishant ranjan"
# for i in s:
#     print(i)



# s = "nishant ranjan"
# for i in range(0,len(s),1):
#     print(i)



# s = "nishant ranjan"
# for i in range(0,len(s),1):
#     print(s[i])



# s = "nishant ranjan"
# for i in range(0,len(s),1):
#     print(s[i])



# s = "nishant ranjan"
# for i in range(len(s)):
#     print(s[i])




# s = "nishant ranjan"
# for i in range(len(s)):
#     print(s[i],2)




# Count the frequency of each character in a string

# text = "programming"

# frequency = {}

# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1

# for char, count in frequency.items():
#     print(char, ":", count)





# Find the first non-repeating character

text = "swiss"

for char in text:
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break
