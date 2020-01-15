# will calculate the tip amount based on the level of service provided (good, fair, bad)

totalbill = float(input("Enter the total bill amount."))

servicelevel = input("Enter the level of service: good, fair, or bad.")

if servicelevel == "good":
    tipamount = float(totalbill * 1.2)
    print("Total amount: " + str(tipamount))
elif servicelevel == "fair":
    tipamount = float(totalbill * 1.15)
    print("Total amount: " + str(tipamount))
elif servicelevel == "bad":
    tipamount = float(totalbill * 1.10)
    print("Total amount: " + str(tipamount))
else:
    print("Hmmm. Please select level of service!")