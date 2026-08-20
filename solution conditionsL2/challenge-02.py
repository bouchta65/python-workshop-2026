age = int(input("Enter your age: "))
print("1. sportive car")
print("2. commercial vehicle")
print("3. family car")
vehicle_choice = int(input("Enter your choice (1-3): "))
accidents = int(input("Enter the number of accidents you have had in the last 5 years: "))
base_prime = 5000
if age < 25 and vehicle_choice == 1 and accidents > 1:
    base_prime = (base_prime * 3) + (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age < 25 and vehicle_choice == 1 and accidents <= 1:
    base_prime = base_prime * 3
    print("Your prime is: ", base_prime)
elif age < 25 and vehicle_choice == 2 and accidents > 1:
    base_prime = (base_prime * 1.2) * 1.5 + (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age < 25 and vehicle_choice == 2 and accidents <= 1:
    base_prime = base_prime * 1.2 * 1.5
    print("Your prime is: ", base_prime)
elif age < 25 and vehicle_choice == 3 and accidents > 1:
    base_prime = (base_prime * 1.1) * 1.5 + (base_prime * 0.3)
    print("Your prime is: ", base_prime)  
elif age < 25 and vehicle_choice == 3 and accidents <= 1:
    base_prime = base_prime * 1.1
    print("Your prime is: ", base_prime)
elif age >= 25 and age <= 65 and vehicle_choice == 1 and accidents > 1:
    base_prime = base_prime * 2 + (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age >= 25 and age <= 65 and vehicle_choice == 2 and accidents > 1:
    base_prime = (base_prime * 1.2) + (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age >= 25 and age <= 65 and vehicle_choice == 2 and accidents <= 1:
    base_prime = base_prime * 1.2
    print("Your prime is: ", base_prime)
elif age >= 25 and age <= 65 and vehicle_choice == 3 and accidents > 1:
    base_prime = (base_prime * 1.1) + (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age >= 25 and age <= 65 and vehicle_choice == 3 and accidents <= 1:
    base_prime = base_prime * 1.1
    print("Your prime is: ", base_prime)
if age > 65 and vehicle_choice == 1 and accidents > 1:
    base_prime = (base_prime * 1.5) *1.2+ (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age > 65 and vehicle_choice == 1 and accidents <= 1:
    base_prime = base_prime * 1.5 * 1.2
    print("Your prime is: ", base_prime)
elif age > 65 and vehicle_choice == 2 and accidents > 1:
    base_prime = (base_prime * 1.2) * 1.2 + (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age > 65 and vehicle_choice == 2 and accidents <= 1:
    base_prime = base_prime * 1.2 * 1.2
    print("Your prime is: ", base_prime)
elif age > 65 and vehicle_choice == 3 and accidents > 1:
    base_prime = (base_prime * 1.1) * 1.2 + (base_prime * 0.3)
    print("Your prime is: ", base_prime)
elif age > 65 and vehicle_choice == 3 and accidents <= 1:
    base_prime = base_prime * 1.1 * 1.2
    print("Your prime is: ", base_prime)