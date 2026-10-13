# read a file:
# file = open("C:\Users\HP\Downloads\result.pdf.PythonRevision.py")
# print(file.read())



# creating a file:
# open("push.txt","x")




# creating a file using 'w':
# file = open("pull.txt","w")
# file.write("hello I am Nishant Ranjan")
# file.close()




with open("demo.txt", "w") as file:
    file.write("Hello, Nishant!\n")
    file.write("I am learning Python file handling.")

print("File created successfully!")