#Write a Python program to count and display the vowels of a given text
#String=”Welcome to python Training
string = "Welcome to python Training"
vowels = "aeiouAEIOU"

vowel_counts = {vowel: 0 for vowel in vowels}
for char in string:
    if char in vowels:
        vowel_counts[char] += 1
for vowel, count in vowel_counts.items():
    if count > 0:
        print(f"{vowel}: {count}")
