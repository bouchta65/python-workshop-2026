c = input("Enter a character: ")
match c:
    case "a" | "e" | "i" | "o" | "u":
        print("your character is a vowel.")
    case _:
        print("your character is not a vowel.")