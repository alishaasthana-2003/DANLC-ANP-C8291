rows=int(input("Enter no. of rows:"))
for r in range(rows,0,-1):
    for s in range(rows,r,-1):
        print(end="  ")
    for c in range(1,r+1):
        print(c, end=" ")
    print()