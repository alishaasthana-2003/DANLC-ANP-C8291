# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
num1 = 10
num2 = 0
divide_numbers(num1, num2)
num2 = 2
divide_numbers(num1, num2)
num1 = "ten"
divide_numbers(num1, num2)
