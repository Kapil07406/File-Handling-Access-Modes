# File Handling - Access Modes

# "w" = Write mode
file = open("student.txt", "w")
file.write("Hello Student")
file.close()

# "r" = Read mode
file = open("student.txt", "r")
print(file.read())
file.close()

# "a" = Append mode
file = open("student.txt", "a")
file.write("\nWelcome to Python")
file.close()

print("File operation completed!")