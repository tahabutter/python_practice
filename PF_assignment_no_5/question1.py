f = open("names.txt", "w") 
for i in range(5):
    name = input("Enter a name: ")
    f.write(name + "\n")
f.close()

f = open("names.txt", "r")
data =f.read()
print("\nNames in File:\n")

print(data)

f.close()
