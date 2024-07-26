#Write a Python program to remove a newline in Python
#String = "\nBest \nDeeptech \nPython \nTraining\n"
String = "\nBest \nDeeptech \nPython \nTraining\n"
char_list=[]
for char in String:
    if char!= '\n':
        char_list.append(char)
clrstr=' '.join(char_list).strip()
print(clrstr)


