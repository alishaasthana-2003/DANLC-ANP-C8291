#Write a function in Python to count and display the total number of words in a text file “ABC.txt”
filename="C:\\Users\\0013tu\\Downloads\\Sale.txt"
total_words=0
with open("C:\\Users\\0013tu\\Downloads\\Sale.txt",'r') as file:
    for line in file:
        words=line.split()
        total_words+=len(words)
print(f"The total no. of words are: {total_words}")
