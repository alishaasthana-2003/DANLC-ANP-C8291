rows = int(input("Enter no. of rows:"))

for r in range(1,rows+1):
    for c in range(rows,r-1,-1):
        print(c,end=" ")
    print()