""" Pseudocode 

Print options to choose one of 'Investment' or 'bond' by user

ask user to input choosen, should read all ways of input otherwise show Error

if investement:
    # ask user for input
    Amount of money deposit
    The interest rate (%)
    How many years
    'Simple' or 'compound'

    if simple:
        use formula
        print rate of interest
    elif compound
        use formula
        print rate of interest
    
if bond:
    #ask user for input
    Value of house
    interest rate
    number of month
    use formula
    print how much money user have to repay each month

else:
        use formula
        print rate of interest
"""

# Error handling required 
# import the math module
import math

# Asking user to input his choice from 'investment' or 'bond'
print()
print("Hi! Make your choice:")
print()
print("Investment - to calculate the amount of interest you will earn on your investment")
print("Bond - to calculate the amount you will have to repay on a home loan")
print()
choice_option = input("""Enter your choise 'investment' or 'bond'
from the menu above to commence calculations, please: """)

""" If user choose 'investment', asking him to input required data and make a choise
between 'simple' and 'compound'
"""
if choice_option.lower() == "investment":
    money_amount = float(input("Declare the amount of money you are depositing, please: "))
    interest_rate_deposit = float(input("Declare the rate of interest, please: "))
    how_many_years = int(input("Declare how many years, please: "))
    simple_compound = str(input("Tell us a bit more. Is it 'simple' or 'compound' deposit? "))
    
    # If user choose 'simple', calculate total amount by formula and print a result
    if simple_compound.lower() == "simple":
        total_amount = money_amount * (1 + (interest_rate_deposit / 100) * how_many_years)
        total_amount_rounded = round(total_amount, 2) # Rounds total amount to 2 decimal places
        print(f"The total amount after {how_many_years} years will be {total_amount_rounded}")

    # If user choose 'compound', calculate total amount by formula and print a result
    elif simple_compound.lower() == "compound":
        total_amount = money_amount * math.pow((1 + (interest_rate_deposit / 100)), how_many_years)
        total_amount_rounded = round(total_amount, 2) # Rounds total amount to 2 decimal places
        print(f"The total amount after {how_many_years} years will be {total_amount_rounded}")

    # If user type with mistakes, error message appears
    else:
        print("Error!!! Could you please check the spelling?")    

# If user choose 'bond', asking user to input required data 
elif choice_option.lower() == "bond":
    house_value = float(input("Declare value of a house, please: "))
    annual_interest_rate = float(input("Declare the rate of interest, please: "))
    how_many_month = int(input("Declare how many month, please: "))

  
    # Calculate total repayment by formula and print a result
    monthly_interest_rate = (annual_interest_rate / 100) / 12 # Converts to monthly rate 
    repayment = (monthly_interest_rate * house_value) / (1 - (1 + monthly_interest_rate) ** -how_many_month)
    repayment_rounded = round(repayment, 2) # Rounds monthly repayment to 2 decimal place
    print(f"Your repayment is {repayment_rounded}")

# If user type with mistakes, error message appears
else:
    print("Error!!! Could you please check the spelling?")
