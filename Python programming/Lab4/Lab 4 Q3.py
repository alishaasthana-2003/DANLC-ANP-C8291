#Wap to input  10 numbers from user and find their sum and average.
sum=0
for i in range(1,11):
    num=int(input("Enter the number:"))
    sum=sum+1
print("The sum of 10 number is : ", sum)
avg=sum/10
print("The average of 10 number is :", avg)