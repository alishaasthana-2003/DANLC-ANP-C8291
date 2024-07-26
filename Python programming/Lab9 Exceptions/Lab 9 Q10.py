#Write a function convert_to_float that takes a list of strings and attempts to convert each string to a float. Use exception handling to manage:
#Value errors (e.g., strings that cannot be converted to float).
#Any other unexpected errors.
#The function should return a list of successfully converted floats and a list of errors (with the original string and the error message).

def convert_to_float(strings):
    converted_floats = []
    errors = []

    for s in strings:
        try:
            converted_floats.append(float(s))
        except ValueError:
            errors.append((s, "Value error: cannot convert to float"))
        except Exception as e:
            errors.append((s, f"An unexpected error occurred: {e}"))

    return converted_floats, errors
strings = ["3.14", "42", "hello", "5.0", "", "NaN", "123abc", "0.001"]
converted_floats, errors = convert_to_float(strings)

print("Converted floats:", converted_floats)
print("Errors:", errors)
