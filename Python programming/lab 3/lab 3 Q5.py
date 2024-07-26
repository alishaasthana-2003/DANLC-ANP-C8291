#Wap to check whether a character is alphabet, number or special character.
char=input("Enter the character")
if char.isalpha():
    print(f"The given character {char} is an alphabet")
elif char.isdigit():
    print(f"The given character {char} is number")
else:
    print(f"the given character {char} is a special character")

