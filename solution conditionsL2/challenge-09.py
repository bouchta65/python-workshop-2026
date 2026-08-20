base_salary = float(input("Enter the base salary (€): "))
extra_hours = float(input("Enter the number of overtime hours: "))
print("1. Junior")
print("2. Senior")
position = int(input("Choose the position: "))
hourly_rate = base_salary / 160
overtime_pay = extra_hours * hourly_rate * 1.5
if position == 1:
    bonus = base_salary * 0.10
elif position == 2:
    bonus = base_salary * 0.20
else:
    bonus = 0
    print("Invalid position")
total_salary = base_salary + overtime_pay + bonus
print("Base salary:", base_salary, "€")
print("Overtime pay:", overtime_pay, "€")
print("Bonus:", bonus, "€")
print("Total salary:", total_salary, "€")