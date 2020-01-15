# will calculate the tip amount based on the level of service provided (good, fair, bad)

totalbill = float(input("Enter the total bill amount."))

servicelevel = input("Enter the level of service: good, fair, or bad.")

splitcheck = int(input("Split how many ways?"))

if servicelevel == "good":
    tipamount = round((totalbill * 1.2), 2)
    print("Total amount: " + str(tipamount))
    print("Amount per person: " + str(tipamount/splitcheck))
elif servicelevel == "fair":
    tipamount = round((totalbill * 1.15), 2)
    print("Total amount: " + str(tipamount))
    print("Amount per person: " + str(tipamount/splitcheck))
elif servicelevel == "bad":
    tipamount = round((totalbill * 1.10), 2)
    print("Total amount: " + str(tipamount))
    print("Amount per person: " + str(tipamount/splitcheck))
else:
    print("Hmmm. Please select level of service!")

