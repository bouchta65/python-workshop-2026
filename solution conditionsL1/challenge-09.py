c = input("Enter a character: ")
if c.isalpha():
    if c.isupper():
        print("The character is a capital letter.")
    else:
        print("The character is a lowercase letter.")
else:
    print("The character is not a letter.")