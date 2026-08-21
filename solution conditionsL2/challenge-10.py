age = int(input("Enter your age: "))
years = int(input("Enter your years of contributions: "))
savings = float(input("Enter your total savings (€): "))
if age < 65:
    plan = "Savings plan not yet available"
elif age >= 65 and years >= 30 and savings >= 100000:
    plan = "Full plan with high pension"
elif age >= 65 and years >= 20 and savings >= 50000:
    plan = "Partial plan with average pension"
else:
    plan = "No retirement plan available"
if savings > 50000:
    bonus = int((savings - 50000) // 10000) * 5
else:
    bonus = 0
print("Plan:", plan)
print("Bonus:", bonus, "%")