#4. Wap to check if the user has provided the correct currency note for deposit or not.
note=int(input("Enter Note:"))
if note==2000 or note ==500 or note==200 or note==100 or note==50:
    print("Valid currency")
else:
    print("Invalid currency")