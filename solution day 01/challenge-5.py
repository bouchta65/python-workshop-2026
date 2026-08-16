C = float(input("Enter the temperature in Celsius: "))
if C < 0:
    print("The water is solid.")
elif 0 <= C < 100:
    print("The water is liquid.")
else:
    print("The water is gas.")
