#Write a Python program to Count all letters, digits, and special
#symbols from the given string
#Input = “P@#yn26at^&i5ve”
#Output: Chars = 8 Digits = 2 Symbol = 3
input_string = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0

for char in input_string:
    if char.isalpha():
        chars += 1
    elif char.isdigit():
        digits += 1
    else:
        symbols += 1
print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")