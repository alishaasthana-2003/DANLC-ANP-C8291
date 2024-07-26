#Wap to print the factorial of a number. N=6  fact= 6*5*4*3*2*1
num=int(input("Enter the number :"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)