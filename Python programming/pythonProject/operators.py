#Q1. Wap to check whether a number is negative or positive.
num = int(input("Enter a number: "))
result = "Positive" if num> 0 else ("Zero" if num == 0 else "Negative")
print("The number is:",result)
