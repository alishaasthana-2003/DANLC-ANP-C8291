year=int(input("Enter Year:"))
result="Leap Year" if year % 4 ==0 else "Not Leap Year"
print(result)

salary=float(input("Enter your salary"))
exp=int(input("Enter experience"))
bonus=0.25 * salary if exp >= 25 else 0.15*salary

print("Your Bonus", bonus)