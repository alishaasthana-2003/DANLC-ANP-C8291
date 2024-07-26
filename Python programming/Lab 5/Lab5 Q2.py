#Wap to print all the Armstrong numbers between a given range.

start=int(input("Enter the start of the range:"))
end=int(input("Enter the end of the range: "))

print(f"Armstrong numbers between {start} and {end}:")

for number in range(start, end+1):
    num_str=str(number)
    num_digits=len(num_str)
    sum_of_powers=0

    for digit in num_str:
        sum_of_powers += int(digit) ** num_digits
    if sum_of_powers == number:
        print(number,end=" ")