# Wap to check if the user has provided the correct currency note for deposit or not.
currency_notes=int(input("Enter the currency notes"))
if currency_notes=="50" or currency_notes=="100" or currency_notes=="200" or currency_notes=="500" or currency_notes=="2000":
    print("given currency is valid")
else:
    print("given currency is not valid")

