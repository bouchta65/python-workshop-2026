days = int(input("Enter the number of your days off: "))
days_off = int(input("Enter the number of your days off spent :"))
print("1. partial time")
print("2. full time")
status = int(input("Enter your status (1 or 2): "))
if days > days_off:
    if status == 2:
        rested_days = days - days_off
        print("You still have", rested_days, "days of rest.")
    elif status == 1:
        rested_days = days / 2 - days_off
        print("You still have", rested_days, "days of rest.")
    else:
        print("Invalid status entered(1 or 2 only).")
else:
    print("You past ur days off limit.")
    