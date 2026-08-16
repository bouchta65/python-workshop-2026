n = int(input("Enter a 4 numbers number: "))
n1 = n // 1000
n2 = (n // 100) % 10
n3 = (n // 10) % 10
n4 = n % 10
reverse_n = n4 * 1000 + n3 * 100 + n2 * 10 + n1
print("The reverse of the number is: ", reverse_n)
