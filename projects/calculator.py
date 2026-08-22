while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 5:
        print("Goodbye!")
        break
    if choice < 1 or choice > 4:
        print("Invalid option!")
        continue
    print("Enter numbers one by one.")
    print("Type (done) when you are finished.")
    numbers = []
    while True:
        number = input("Enter number: ")
        if number == "done":
            break
        try:
            number = float(number)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if choice == 4 and number == 0:
            print("Cannot divide by zero!")
            continue
        numbers.append(number)
    if len(numbers) == 0:
        print("No numbers were entered.")
        continue
    result = numbers[0]
    if choice == 1:
        operation = " + "
        for number in numbers[1:]:
            result = result + number
    elif choice == 2:
        operation = " - "
        for number in numbers[1:]:
            result = result - number
    elif choice == 3:
        operation = " * "
        for number in numbers[1:]:
            result = result * number
    else:
        operation = " / "
        for number in numbers[1:]:
            result = result / number
    calcul = operation.join(str(number) for number in numbers)
    print(calcul, "=", result)
    print("Number of inputs:", len(numbers))
    print("smalest number:", min(numbers))
    print("bigest number:", max(numbers))
    print("Average:", sum(numbers) / len(numbers))