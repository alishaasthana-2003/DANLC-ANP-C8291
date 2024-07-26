babies=0
students=0
adults=0

for i in range(15):
    age=int(input("Enter the age  :"))
    if age<=5:
        babies=babies+1
    elif age>=18:
        adults=adults+1
    else:
        students=students+1
print("babies are :",babies)
print("students are ", students)
print("adults are", adults)