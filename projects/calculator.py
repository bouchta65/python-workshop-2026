while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Choose an option: "))
    if choice == 5:
        break
    n = int(input("How many numbers? "))
    result = float(input("Enter a number: "))
    for i in range(n - 1):
        number = float(input("Enter a number: "))
        if choice == 1:
            print("Result:", result)
            result += number
            print("Result:", result)
        elif choice == 2:
            result -= number
            print("Result:", result)
        elif choice == 3:
            result *= number
            print("Result:", result)
        elif choice == 4:
            result /= number
            print("Result:", result)
        else:
            print("Invalid choice")