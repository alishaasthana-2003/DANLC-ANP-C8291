#. Write a Python program to reverse words in a string
#String = “Deeptech Python Training”
string ="Deeptech Python Training"
words = string.split()
reversed_words = words[: : -1]
reversed_string = " ".join(reversed_words)
print(reversed_string)
