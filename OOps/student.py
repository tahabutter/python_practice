class student:
    def __init__(self, name, roll_no, marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def set_name(self, name):
        if name != "":
            self.__name = name
        else:
            print("Name cannot be empty.")

    def set_roll_no(self, roll_no):
        if roll_no >= 1 and roll_no <=  100:
            self.__roll_no = roll_no
        else:
            print("Roll number must be between 1 and 100.")  

    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks
        else:
            print("Marks must be a positive number.")

    def getter(self):
        print(f"Name: {self.__name}")
        print(f"Roll No: {self.__roll_no}")
        print(f"Marks: {self.__marks}")

     


s1 = student("Taha", 123, 85)
s1.getter()  
          