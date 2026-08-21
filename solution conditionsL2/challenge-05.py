budget = float(input("Enter your budget (€): "))
people = int(input("Enter the number of people: "))
print("1. Beach")
print("2. Mountain")
print("3. City")
destination = int(input("Choose your destination: "))
if budget >= 1000:
    trip = "Luxury trip"
elif budget >= 500:
    trip = "Medium trip"
else:
    trip = "Economic trip"
if destination == 1:
    if budget >= 1000 and people > 2:
        place = "Beach"
    else:
        place = "Beach is not recommended"
elif destination == 2:
    if budget >= 500 and people <= 2:
        place = "Mountain"
    else:
        place = "Mountain is not recommended"
elif destination == 3:
    place = "City"
else:
    place = "Invalid destination"
print("Trip type:", trip)
print("Destination:", place)