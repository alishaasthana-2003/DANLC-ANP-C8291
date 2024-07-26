#Write a Python program that prompts the user to input two numbers and raises aTypeError exception if the inputs are not numerical
def is_numerical(value):
    try:
        a=float(value)
        return True

    except ValueError:
        return False

def numerical_value(prompt):
    while True:
        n1=input(prompt)
        if is_numerical(n1):
            return float(n1)
        else:
            raise TypeError("Error : Non numerical value found!!!")

n1=numerical_value("Enter first value :")
n2=numerical_value("Enter second value :")
print("Numerical inputs are received !!")




