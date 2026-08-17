average = int(input("What's your average: "))
if average < 0 or average > 20:
    print("Type an average between 0 and 20")
elif average < 10:
    print("You are rejected")
elif average < 12:
    print("You passed your grade")
elif average < 14:
    print("You got a pretty good mention")
elif average < 16:
    print("You got a good mention")
else:
    print("You got a very good mention")
