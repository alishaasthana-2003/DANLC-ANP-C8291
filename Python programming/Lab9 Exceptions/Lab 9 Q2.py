#Write a Python program that prompts the user to input an integer and raises(use custom exception to raise this error: it will be raised if the value provided is not between 1 to 1000) aValueError exception if the input is not a valid integer.
class OutOfRangeError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
def get_user_input():
    while True:
        try:
            user_input = input("Please enter an integer between 1 and 1000: ")
            value = int(user_input)
            if value < 1 or value > 1000:
                raise OutOfRangeError("The value is out of the allowed range (1-1000).")
            return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
        except OutOfRangeError as e:
            print(e)
value = get_user_input()
print(f"You entered: {value}")
