base = int(input("Enter your number: "))
power = int(input("Enter the power: "))
for i in range(1, power + 1):
    result = base ** i
print(base, "raised to the power of", power, "is:", result)