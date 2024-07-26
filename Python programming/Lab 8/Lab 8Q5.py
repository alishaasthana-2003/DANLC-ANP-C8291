# wap to copy the contents of one file into another. input both file names with path from user
input_file_path = input("Enter the path of the input file: ")
output_file_path = input("Enter the path of the output file: ")
input_file =open(input_file_path, 'r')
output_file= open(output_file_path, 'w')
for line in input_file :
 output_file.write(line)
 print(f"Contents from {input_file_path} copied to {output_file_path} successfully.")
if FileNotFoundError:
    print("File not found. Please check the file paths and try again!!")

