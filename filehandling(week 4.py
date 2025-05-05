file = open ("test.txt", "r")
content = file.read()
print(content)

file = open ("test.txt", "w")
file.write("Hello people, this is python.")

file_name = input("Enter the name of the file you want to open: ")

try:
    file = open(file_name, "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please check the file name and try again.")

finally: 
    file.close()
    print("File closed successfully.")