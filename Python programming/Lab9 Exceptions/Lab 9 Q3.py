#  Write a Python program that opens a file and handles a FileNotFoundError exception
# if the file does not exist.
def open_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")




