n = int(input("Enter a positive integer: "))
n2 = 0
while n > 0:
    n = n // 10
    n2 = n2 + 1
print("Number of digits =", n2)