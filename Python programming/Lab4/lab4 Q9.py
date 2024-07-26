# Wap to print all the leap years from 1 to n.
def isleap(year):
    if year%4==0 and year%100==0 and year%400==0:
        return True
    elif year%4==0 and year%100!=0 and year%400!=0:
        return True
    else:
        return False

n=int(input("Enter year:"))
for i in range(1,n+1):
    if(isleap(i)):
        print(i)