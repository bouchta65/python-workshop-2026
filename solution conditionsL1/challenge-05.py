while True:
    print("1. year in months")
    print("2. year in days")
    print("3. year in hours")
    print("4. year in minutes")
    print("5. year in seconds")
    choice = input("Enter your choice (1-5): ")
    year_type = input("is your year a leap year? (yes/no): ") 
    if choice == "1":
        print("1 year is equal to 12 months.")
    elif choice == "2":
            if year_type == "yes":
                print("1 leap year is equal to 366 days.")
            else:
                print("1 year is equal to 365 days.")
    elif choice == "3":
            if year_type == "yes":
                print("1 leap year is equal to 8784 hours.")
            else:
                print("1 year is equal to 8760 hours.")
    elif choice == "4":
            if year_type == "yes":
                print("1 leap year is equal to 527040 minutes.")
            else:
                print("1 year is equal to 525600 minutes.")
    elif choice == "5":
            if year_type == "yes":
                print("1 leap year is equal to 31622400 seconds.")
            else:
                print("1 year is equal to 31536000 seconds.")
    else:
            print("you must pick a number between 1 and 5  .")
            

