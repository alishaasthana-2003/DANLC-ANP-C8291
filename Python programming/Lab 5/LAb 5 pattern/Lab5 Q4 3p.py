#THIRD PATTERN
def pattern3(n):
    number=1
    for i in range(1,n+1):
        for j in range(i):
            print(number, " ", end=" ")
            number+=1
        print(" ")

n=int(input("Enter the value of n:"))
pattern3(n)