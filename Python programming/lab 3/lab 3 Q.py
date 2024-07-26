#1.	Wap to check whether a character is alphabet or not.

a=input("Enter a character:")
if ((ord(a)>=97 and ord(a)<=122) or (ord(a)>=65 and ord(a)<=90)):
    print("it is a alphabet")
else :
    print("it is not alphabet ")