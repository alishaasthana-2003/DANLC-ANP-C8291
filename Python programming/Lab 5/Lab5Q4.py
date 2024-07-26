#Create Following Patterns using functions in a single program:-
# 1
# 22
# 333
# 4444
# 55555

def pattern1(n):
    for i in range(n+1):
        for j in range(i):
            print(i, end=" ")
        print(" ")
n=int(input("Enter the value of n :"))
pattern1(n)


