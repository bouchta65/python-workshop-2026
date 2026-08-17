date = input("Enter a date (DD/MM/YYYY): ")
day, month, year = date.split("/")
if month == "01":
    month_name = "January"
elif month == "02":
    month_name = "February"
elif month == "03":
    month_name = "March"
elif month == "04":
    month_name = "April"
elif month == "05":
    month_name = "May"
elif month == "06":
    month_name = "June"
elif month == "07":
    month_name = "July"
elif month == "08":
    month_name = "August"
elif month == "09":
    month_name = "September"
elif month == "10":
    month_name = "October"
elif month == "11":
    month_name = "November"
elif month == "12":
    month_name = "December"
else:
    month_name = "not a real month"
print("the date is" , day, month_name, year)