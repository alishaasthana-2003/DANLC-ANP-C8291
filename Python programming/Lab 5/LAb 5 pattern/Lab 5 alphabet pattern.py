rows=int(input("Enter no. of rows:"))
for r in range(65,91):
    for s in range(90,r,-1):
        print(end="  ")
    for c in range(65,r+1):
        print(chr(c),end=" ")
    for c1 in range(c-1,64,-1):
        print(chr(c1), end=" ")
    print()