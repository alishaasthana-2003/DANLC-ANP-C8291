def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=" ")

        for j in range(space):
            print(" ",end=" ")
        space+=2

        for j in range(n,i-1,-1):
            print(j,end=" ")
        print()
n=int(input("Enter value of n:"))
pattern(n)

