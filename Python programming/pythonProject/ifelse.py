basic_salary=float(input('Enter the Salary'))
exp=int(input("Enter your experience"))
if (exp>=20):
    bonus=0.20*basic_salary
else:
    bonus=0.10*basic_salary
print(f"Your bonus is :{bonus}")


