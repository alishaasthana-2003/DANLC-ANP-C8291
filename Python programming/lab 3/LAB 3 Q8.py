#input bank login and password and check whether it is valid or not
#8.  input bank login and password and check whether it is valid or not
  #if login is successful, then give options to user for the following:-
  # 1. Change password
  #2. Check Balance
  #3. Deposit Amount
  #4. Withdraw Amount


login_id = "Alisha"
login_password= "123"
balance= 2000
id=str(input("Enter Login Username : "))
if id== login_id :
    password=str(input("Enter password : "))
    if password==login_password :
        print("Login Sucessfull")
        option=int(input("1. Change password \n"
                         "2. Check Balance\n"
                         "3. Deposite Amount\n"
                         "4. Withdraw Amount\n"
                         "5. Exit\n"))
        if option==1:
            password = str(input("Enter old password :"))
            if password != login_password :
                    print("Invaid password")
            else :
                new_password = str(input("Enter new password :"))
                password = new_password
                print("Password changed")

        if option==2:
            print(f"Your Current Balance is  {balance} rs.")
        if option==3:
            print(f"Your Current Balance is  {balance} rs.")
            deposite_amount=float(input("Enter the Deposite amount:"))
            new_balance= balance+ deposite_amount
            print(f"Your balance new is {new_balance} rs.")
        if option==4:

            password = str(input("Enter password : "))
            if password == login_password:
                print(f"Your Current Balance is  {balance} rs.")
                withdraw_amount = float(input("Enter the Withdraw amount: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"Your new balance is {balance} rs.")
                else:
                    print("Insufficient balance")
            else:
                print("Invalid Password")
        if option == 5:
                print("Exiting...")

    elif option<= 6:
            print("Invalid option, please try again.")
    else:
            print("Invalid Password!!")
else:
            print("Invalid I.D!!")
