class bankaccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")



b1 = bankaccount("1234567", "Taha", 10000)

b1.check_balance()

b1.deposit(5000)

b1.withdraw(2000)
 
        
             
     