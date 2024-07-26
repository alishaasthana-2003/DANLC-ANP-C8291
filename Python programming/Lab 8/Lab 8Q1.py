#Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.
with open("C:\\Users\\0013tu\\Downloads\\Sale.txt", 'r') as file:
    for line in file:
        print(line, end='')
