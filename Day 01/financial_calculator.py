"""
    This script takes three input variables
        -- Pricipal : Initial Amount
        -- Interest : Interest Rate
        -- Time : Time Period
    Then calculates the simple interest for the given time period and interest rate.
"""

raw_principal = input("Enter principal: ")
try:
    principal = float(raw_principal)
except ValueError:
    print('Error: Inavalid Number')

raw_interest = input("Enter Interest: ")
try:
    interest = float(raw_interest)
except ValueError:
    print('Error: Inavalid Number')

raw_time = input("Enter time: ")
try:
    time = int(raw_time)
except ValueError:
    print('Error: Inavalid Number')

SI = (principal*interest*time)/100
print(f"The simple interest is ${SI:,.2f}")
