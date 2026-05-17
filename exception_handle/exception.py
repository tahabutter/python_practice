try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
else:
    print(f"The result of 10 divided by {x} is: {result}")    
finally:
    print("Execution completed.")    
