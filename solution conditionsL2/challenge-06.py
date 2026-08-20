consumption = float(input("Enter electricity consumption (kWh): "))
print("1. Residential")
print("2. Commercial")
user_type = int(input("Choose user type: "))
print("0. Standard")
print("1. Reduced")
contract = int(input("Choose contract type: "))
if user_type == 1:
    if contract == 0:
        price = 0.20
    elif contract == 1:
        price = 0.15
    else:
        print("Invalid contract type")
        price = 0
elif user_type == 2:
    if contract == 0:
        price = 0.30
    elif contract == 1:
        price = 0.25
    else:
        print("Invalid contract type")
        price = 0
else:
    print("Invalid user type")
    price = 0
bill = consumption * price
if consumption > 500:
    bill = bill * 1.10
print("Consumption:", consumption, "kWh")
print("Price per kWh:", price, "€")
print("Total bill:", bill, "€")