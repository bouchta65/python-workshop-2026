x1 = float(input("first point of the segment x: "))
y1 = float(input("first point of the segment y: "))
x2 = float(input("second point of the segment x: "))
y2 = float(input("second point of the segment y: "))
x = float(input("point x: "))
y = float(input("point y: "))
if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
    print("The point is on the segment.")
else:
    print("The point is not on the segment.")