# Exception Handling

try:
    with open('file.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("The file 'file.txt' was not found.") 

else:
    print("File read successfully.")