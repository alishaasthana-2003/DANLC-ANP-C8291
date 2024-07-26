# Wap to check login and password.
userid = "abc@gmail.com"
pass1 = "abc#123"

uid = input("Enter user id : ")  # 46456@gmail.com

if uid == userid:   #  false
    upass = input("Enter your password : ")  # abc#123
    if upass == pass1:  # true
        print("Login Successful!!")
    else:
        print("Incorrect Password!!")
else:
    print("User does not exists!!")