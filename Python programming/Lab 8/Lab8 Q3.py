#Write a function in Python to count uppercase character in a text file “ABC.txt”
filename="C:\\Users\\0013tu\\Downloads\\Sale.txt"
word_count=0
with open("C:\\Users\\0013tu\\Downloads\\Sale.txt",'r') as file:
    line=file.read()
    for char in line:
        if char.isupper():
            word_count+=1
print(f"The Uppercase characters are:{ word_count}")
