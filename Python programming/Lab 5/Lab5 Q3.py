#Wap to print multiplication tables from a given range.

start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
for j in range(1,10+1):
    for i in range(start, end+1):
        print(i*j, "\t", end=" ")
    print()