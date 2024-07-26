#Q6. Wap to find the binary number of the given integer.
#1.      Input a number
#2.      Find the modulus of this number by 2 and save it into a array
#3.      After the loop is finished, print the array in reverse.

num=int(input("Enter a number : "))
bin= []
while (num):
    bin.append(num%2)
    num//2

bin=bin[: : -1]
for i in bin:
    print(i,end=" ")