score = int(input("Enter your scoreout of 100: "))
years = int(input("Enter how many years you have been working with us: "))
print("how much prices u got")
print("0. 0 prices")
print("1. 1 price")
print("2. 2 or more prices")
prices = int(input("Enter one of the choices above: "))
if prices == 1:
    score = score + (score * 0.10)
    if score >= 90 and years >= 5:
      print("u are an excellent employee")
    elif score >= 75 and years < 5 and years >= 3:
      print("u are a good employee")
    elif score >= 50 and years < 3:
      print("u are an satisfying employee")
    elif score < 50:
      print("u are a Insufficient employee")
    else:
      print("error")
elif prices >= 2:
    score = score + (score * 0.20)
    if score >= 90 and years >= 5:
      print("u are an excellent employee")
    elif score >= 75 and years < 5 and years >= 3:
      print("u are a good employee")
    elif score >= 50 and years < 3:
      print("u are a satisfying employee")
    elif score < 50:
      print("u are a Insufficient employee")
    else:
      print("error")
else:
  print("prices number is not valid")
   