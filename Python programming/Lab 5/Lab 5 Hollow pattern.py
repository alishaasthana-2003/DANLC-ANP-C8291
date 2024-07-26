rows=int(input("enter no. of rows:"))
for r in range(1,rows+1):
    for c in range(1,r+1):
        if c==1 or c==r or r==rows:
            print(c, end=" ")

        else:
            print(end="  ")
    print()