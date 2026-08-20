annual_income = float(input("Enter your annual income (euros): "))
credit_score = int(input("Enter your credit score (out of 1000): "))
loan_term = int(input("Enter the loan term (in years): "))
if annual_income >= 300000 and credit_score >= 700 and loan_term <= 10:
    print("You are eligible for the loan.")
elif annual_income >= 300000 and credit_score >= 650 and loan_term <= 15:
    print("You are eligible for the loan with some conditions.")
elif annual_income <  300000 or credit_score < 650 or loan_term > 15:
    print("You are not eligible for the loan.") 
else: 
    print(" error.")    