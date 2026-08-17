a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))
print("The equation is: ", a, "x**2 + ", b, "x + ", c)
delta = (b**2) - (4*a*c)
print("The value of delta is:", delta)
if delta > 0:
    solution1 = (-b + (delta**0.5)) / (2*a)
    solution2 = (-b - (delta**0.5)) / (2*a)
    print("The equation has two real roots:", solution1, "and", solution2)
elif delta == 0:
    solution1 = -b / (2*a)
    print("The equation has one real root:", solution1)
else:
    print("The equation has no real roots.")