def invertedHalfPyramid(n):
    for i in range(1,n+1):
        for j in range(1,n-i+2):
            if j==1 or i==1 or i+j==6:
                print(j,end=" ")
            else:
                print(" ",end=" ")
        print(" ")

n=int(input("Enter the value of n:"))
invertedHalfPyramid(n)