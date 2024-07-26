#SECOND PATTERN
def pattern2(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end=" ")
        print(" ")
n=int(input("Enter value of n :"))
pattern2(n)