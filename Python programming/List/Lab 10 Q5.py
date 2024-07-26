'''Write a Python program to traverse a given list in reverse order, and print the elements with the original index.

Original list: ['red', 'green', 'white', 'black']

Traverse the said list in reverse order: black white green red'''
original_list = ['red', 'green', 'white', 'black']
print("Traverse the said list in reverse order:")
for index in range(len(original_list) - 1, -1, -1):
    print(f"Original index: {index}, Element: {original_list[index]}")
