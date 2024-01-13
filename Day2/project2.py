#  Instructions
# If the bill was $150.00, split between 5 people,
# with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill 
# is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number.
# You might have to do some Googling to solve this.💪
# https://replit.com/@appbrewery/tip-calculator-end

print("Welcome to the tip calculator!")

bill = input("What was the total bill? $")

tip = input("How much tips would you like to give? 10, 12, or 15? ")

number_of_people = input("How many people to split the bill? ")

tip_percent = float(bill) * (float(tip)/100)

payment = (float(bill) + tip_percent)/float(number_of_people) 

final_bill = round(payment, 2)
# print(final_bill)
print(f"Each person should pay: ${final_bill}")



