# problem solved Constructor Overloading (with Default Parameters) 
class Person:
    def __init__(self, name, age=None, address=None):
         self.name = name
         self.age = age
         self.address = address

    def display_info(self):
         print(f"Name: {self.name}")
         print("Age:", self.age)
         print("Address:", self.address)
         print()

p1 = Person("Taha")
p2 = Person("Ali", 22)
p3 = Person("Ahmed", 25, "Lahore")

p1.display_info()
p2.display_info()
p3.display_info()         

