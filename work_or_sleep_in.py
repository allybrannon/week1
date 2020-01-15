# User will be told to go to work if Mon-Friday or sleep if Sat or Sund

day = int(input("Enter day (Sunday = 0 to Friday = 6)? "))

if day == 0:
    print ("Sleep in!")
elif day <=5:
    print ("Go to work.")
elif day == 6:
    print ("Sleep in!")
else: 
    print ("Oops! Pick 0-6")
