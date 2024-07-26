#Input units of electricity from user and print the bill according to the following criteria
#a.Less than 200 : no bill
#b.Next 200-300  -   1.2/perunit       100*1
#c.Next 300-400  -1.5/perunit           100*2
#d.Next 400-500  - 2.5/perunit          100*3
#e.Above 500 -   8/per unit
electricity_unit=int(input("Enter the units of electricity"))
if bill<=200:
    print("No Bill")
if 200<bill<300