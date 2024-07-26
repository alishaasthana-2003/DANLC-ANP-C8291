#Write a Python program to count Uppercase, Lowercase, special
#character and numeric values in a given string
#Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
#Output:
#UpperCase : 5
#LowerCase : 18
#NumberCase : 5
#SpecialCase : 11
input_str="Hell0 W0rld ! 123 *"
upper_count=0
lower_count=0
digit_count=0
special_count=0
for char in input_str:
    if char.isupper():
        upper_count+=1
    elif char.islower():
        lower_count+=1
    elif char.isdigit():
        digit_count+=1
    else:
        special_count+=1
print("Uppercase", upper_count)
print("Lowercase",lower_count)
print("Digits",digit_count)
print("special character",special_count)

