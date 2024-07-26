#Wap to print the sum of the series 1  4 9 16 25 36 49 64
n=int(input("Enter the number"))
sum=0
for i in range(1,n+1):
    sum=sum+i**2
print("Sum of Series is:" , sum)