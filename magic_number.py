#prompt the user for a number
#compare the number to a predefined value
# if the numbers match, tell the user they are a mind reader
# if they don't match, tell the user "thanks for playing"

user_input = int(input("What number am I thinking of?"))

MAGICNUMBER = 9

if user_input == MAGICNUMBER:
    print("ARE YOU A MIND READER?")
else:
    print("Sorry! Try Again!")