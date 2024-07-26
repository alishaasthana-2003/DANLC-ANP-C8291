#Write a Python Count vowels in a string
#input= “Welcome to Python Assignment”
#Output: Total vowels are: 8
input_str = "Welcome to Python Assignment"
vowels = "aeiouAEIOU"
vowels_count = 0

for char in input_str:
    if char in vowels:
        vowels_count += 1

print("The total vowels are:", vowels_count)
