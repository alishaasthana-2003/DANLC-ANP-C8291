r=int(input("Enter no. of rows:"))
for r in range(1,6):
    for s in range(5,r,-1):
        print(end="  ")
    for c in range(1,r+1):
        print(c,end=" ")
    for c1 in range(c-1,0,-1):
        print(c1, end=" ")
    print()
for r in range(4,0,-1):
    for s in range(5,r,-1):
        print(end="  ")
    for c in range(1,r+1):
        print(c,end=" ")
    for c1 in range(c-1,0,-1):
        print(c1, end=" ")
    print()

