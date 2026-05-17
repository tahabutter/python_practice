# problem solve by using Abstraction
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):

    def __init__(self, stipend):
        self.stipend = stipend

    def calculate_salary(self):
        print("Intern Salary:", self.stipend)

class FullTimeEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        print("Full Time Employee Salary:", self.monthly_salary)

class ContractEmployee(Employee):
    def __init__(self, hour, rate):
        self.hour = hour
        self.rate = rate
    def calculate_salary(self):
        print("Contract Employee Salary:", self.hour * self.rate)

 
i1 = Intern(15000)
f1 = FullTimeEmployee(80000)
c1 = ContractEmployee(40, 500)

i1.calculate_salary()
f1.calculate_salary()
c1.calculate_salary()
                     