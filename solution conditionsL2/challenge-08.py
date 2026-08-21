age = int(input("Enter your age: "))
print("0. No problem")
print("1. Minor problem")
print("2. Major problem")
medical_history = int(input("Choose your medical history: "))
print("1. Basic")
print("2. Extended")
coverage = int(input("Choose your coverage type: "))
if age < 30:
    plan = "Basic plan"
elif age >= 30 and medical_history == 0:
    plan = "Basic plan"
elif age >= 30 and medical_history >= 1:
    plan = "Extended plan"
else:
    plan = "Invalid choice"
if medical_history == 2:
    extra = "Additional coverage for major problems"
else:
    extra = "No additional coverage"
print("Plan:", plan)
print(extra)