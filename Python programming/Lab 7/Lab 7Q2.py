#Write a Python program to remove duplicate characters of a given
#string.
#Input = “String and String Function”
#Output: String and Function
str=input("Enter String:")

str1=" "
for ch in str:
    if ch not in str1:
        str1 += ch

print(str1)
#remove all duplicate words from string
Input = "String and String Function"
word_split = Input.split()
word = ""
for w in word_split:
    if w not in word:
      word += w
print(word)
(space problem)
