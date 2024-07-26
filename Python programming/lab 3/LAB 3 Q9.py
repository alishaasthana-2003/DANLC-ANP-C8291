# write a program to generate the following payslip for an employee:-
userid= 11003421
pin= 1234
balance= 53400

uid = int(input("Enter userid:"))
if uid == userid:
    upass = input("Enter your pin : ")
    if upass == pin:
        print("Login Successful!!")
        print("----------------------------")
        print("1. Change Password")
        print("2. Check Balance")
        print("3. Deposit Amount")
        print("4. Withdraw Amount")
        print("5. Exit")
        print("Enter your choice :")
        choice = int(input())

        if choice == 1:
            # change password
        elif choice == 2:
            # check balance
            print("your saving Account balance is Rs. ", balance)
        elif choice == 3:
            #deposit
        elif choice == 4:
            #withdraw
        elif choice == 5:
            print("Good Bye !!")
        else:
            print("Please Enter a valid choice")
