#Wap to input 10 numbers from user and find the minimum and maximum number.
num1= int(input("Enter the number 1:"))
mx= num1
mn= num1

for i in range(9):
    num=int(input("Enter the number {i+2} : "))
    if num>mx:
        mx=num
    if num<mn:
        mn=num
print("Maximum number is :", mx)
print("Minimum number is :", mn)