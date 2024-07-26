#  wap to print the following pattern(min 10 elements)A      1 8 27 64 125 --------
n=int(input("Enter the number:"))
for i in range(1,n):
    print(i**3, end=" ")