income = float(input("Enter your annual income (€): "))
print("1. Single")
print("2. Married")
print("3. Head of household")
status = int(input("Choose your fiscal status: "))
deductions = float(input("Enter additional deductions (€): "))
if status == 1:
    standard_deduction = 1000
elif status == 2:
    standard_deduction = 2000
elif status == 3:
    standard_deduction = 3000
else:
    print("Invalid fiscal status")
    standard_deduction = 0
taxable_income = income - standard_deduction - deductions
if taxable_income < 0:
    taxable_income = 0
if taxable_income <= 20000:
    tax_rate = 0.05
elif taxable_income <= 50000:
    tax_rate = 0.10
else:
    tax_rate = 0.20
tax = taxable_income * tax_rate
print("Taxable income:", taxable_income, "€")
print("Tax rate:", tax_rate * 100, "%")
print("Tax to pay:", tax, "€")