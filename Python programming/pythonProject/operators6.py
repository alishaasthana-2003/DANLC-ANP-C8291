#wap to calculate the salary slip
#Basic  salary : input from user  // salary=60000
#Da     :    2% of basic   // da=0.02*salary
#Ta      :   3% of salary
#Hra  :      10% salary
#PF     :    15% of salary
# Total salary=    basic+da+ta+hra+pf;’
#Net salary =   total-pf;
#Calculate bonus of employee to 25 % of salary by shift operators.
Basic_salary=float(input("Enter the salary"))
Da=0.02*Basic_salary
Ta=0.03*Basic_salary
Hra=0.10*Basic_salary
Pf=0.15*Basic_salary
Total_Salary= Basic_salary+Da+Ta+Hra+Pf
Net_Salary = Total_Salary-Pf
bonus = Basic_salary * (1 << 1) // 4
print("Basic Salary is :", Basic_salary)
print("Da is:", Da)
print("Ta is :", Ta)
print("Hra is :", Hra)
print("Pf is :", Pf)
print("Total salary is :", Total_Salary)
print("Net Salary is :", Net_Salary)
print("Bonus is", bonus)


