#Wap to search a particular word in a file and also prints number of occurrences.
file_path = input("Enter the path of the file: ")
search_word = input("Enter the word to search: ")
file=open(file_path, 'r')
content = file.read()
count = content.count(search_word)
print(f"The word '{search_word}' appears {count} times in the file.")