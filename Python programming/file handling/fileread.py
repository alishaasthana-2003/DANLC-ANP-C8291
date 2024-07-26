filename= "C:\\Users\\0013tu\\Downloads\\Fa2 syllabus class 2222.docx"

fp=open(filename, "r")
if fp:
    print("File found!!")
else:
    print("File not found")
fp.close()

with open("employee.txt","r")as fp1:
    print(fp1.read())
print(fp1.read())

