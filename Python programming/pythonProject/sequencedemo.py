empnames= ["Harsh", "Lalit", "Alisha", "Dinesh", "Tarun"]
ename= input("Enter employee name:")

result= ename in empnames
print("status", result)

result= ename not in empnames
print("not in status", result)

employees= empnames
print(empnames in employees)

c=["A","b","c"]
print(empnames is not c)