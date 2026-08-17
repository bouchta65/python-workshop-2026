time1 = input("Enter the first time (HH:MM:SS): ")
time2 = input("Enter the second time (HH:MM:SS): ")
h1, m1, s1 = map(int, time1.split(":"))
h2, m2, s2 = map(int, time2.split(":"))
seconds1 = h1 * 3600 + m1 * 60 + s1
seconds2 = h2 * 3600 + m2 * 60 + s2
if seconds1 < seconds2:
    print("The first time comes before the second.")
elif seconds2 < seconds1:
    print("The second time comes before the first.")
else:
    print("They are the same time.")
