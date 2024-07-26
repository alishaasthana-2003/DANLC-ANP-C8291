# Wap to check whether an year is leap or not.
a=int(input("Enter the year"))
print(a, "is a leap year.") if (a % 4 == 0 and (a% 100 != 0 or a% 400 == 0)) else print(a, "is not a leap year.")
