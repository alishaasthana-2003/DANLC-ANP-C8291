# Input amount and print its denomination :-

amount=int(input("Enter the amount:"))

if amount % 100 ==0:
    if amount >= 2000:
        notes = amount // 2000
        print(f"2000 x {notes} = {2000 * notes}")
        amount = amount - (2000 * notes)

    if amount >= 500:
        notes = amount // 500
        print(f"2000 x {notes} = {500 * notes}")
        amount = amount - (500 * notes)
    if amount >= 200:
        notes = amount // 200
        print(f"2000 x {notes} = {200 * notes}")
        amount = amount - (200 * notes)
    if amount >= 100:
        notes = amount // 100
        print(f"2000 x {notes} = {100 * notes}")
        amount = amount - (100 * notes)
else:
    print("Amount should be multiple of 100 !!!")



