############
# Optimal Change testing program
# Code Platoon, Sierra Platoon, Assessment 1
# Andrea Leach
# 17 October, 2022
############

from optimal_change import optimal_change

# given tests
print("checking given tests")
print(optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print(optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print()

# tests that check for formatting of ITEM_COST and AMOUNT_PAID
print("checking for formatting of ITEM_COST and AMOUNT_PAID")
print(optimal_change(31.50, 50) == "The optimal change for an item that costs $31.50 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, and 2 quarters.")
print(optimal_change(62.10, 100.01) == "The optimal change for an item that costs $62.10 with an amount paid of $100.01 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, 1 nickel, and 1 penny.")
print(optimal_change(31.50, 50.50) == "The optimal change for an item that costs $31.50 with an amount paid of $50.50 is 1 $10 bill, 1 $5 bill, and 4 $1 bills.")
print(optimal_change(62, 100) == "The optimal change for an item that costs $62 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, and 3 $1 bills.")
print(optimal_change(62, 100.18) == "The optimal change for an item that costs $62 with an amount paid of $100.18 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 dime, 1 nickel, and 3 pennies.")
print(optimal_change(62, 100.10) == "The optimal change for an item that costs $62 with an amount paid of $100.10 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 3 $1 bills, and 1 dime.")
print(optimal_change(10.04, 100) == "The optimal change for an item that costs $10.04 with an amount paid of $100 is 1 $50 bill, 1 $20 bill, 1 $10 bill, 1 $5 bill, 4 $1 bills, 3 quarters, 2 dimes, and 1 penny.")
print(optimal_change(10.06, 30.05) == "The optimal change for an item that costs $10.06 with an amount paid of $30.05 is 1 $10 bill, 1 $5 bill, 4 $1 bills, 3 quarters, 2 dimes, and 4 pennies.")
print(optimal_change(10.02, 30.40) == "The optimal change for an item that costs $10.02 with an amount paid of $30.40 is 1 $20 bill, 1 quarter, 1 dime, and 3 pennies.")
print()

# tests where only one type of change is given
print("checking for one type of change given")
print(optimal_change(6, 10) == "The optimal change for an item that costs $6 with an amount paid of $10 is 4 $1 bills.")
print(optimal_change(90, 100) == "The optimal change for an item that costs $90 with an amount paid of $100 is 1 $10 bill.")
print()

# tests where two types of change are given
print("checking for two types of change given")
print(optimal_change(6, 12) == "The optimal change for an item that costs $6 with an amount paid of $12 is 1 $5 bill and 1 $1 bill.")
print(optimal_change(90, 100.50) == "The optimal change for an item that costs $90 with an amount paid of $100.50 is 1 $10 bill and 2 quarters.")
print(optimal_change(.01, .07) == "The optimal change for an item that costs $0.01 with an amount paid of $0.07 is 1 nickel and 1 penny.")
print(optimal_change(3.98, 5) == "The optimal change for an item that costs $3.98 with an amount paid of $5 is 1 $1 bill and 2 pennies.")
print()

# tests where exact change was paid
print('checking for exact funds paid')
print(optimal_change(6, 6) == 'Exact funds were paid, no change needed.')
print(optimal_change(3.98, 3.98) == 'Exact funds were paid, no change needed.')
print()

# tests where insufficient funds were paid
print('checking for insufficient funds paid')
print(optimal_change(6, 5) == 'Insufficient funds paid, customer owes $1.')
print(optimal_change(3.98, 3) == 'Insufficient funds paid, customer owes $0.98.')
print(optimal_change(3.50, 0) == 'Insufficient funds paid, customer owes $3.50.')
print(optimal_change(200, 100.00) == 'Insufficient funds paid, customer owes $100.')
print(optimal_change(200.00, 100.00) == 'Insufficient funds paid, customer owes $100.')
print(optimal_change(200.0, 100) == 'Insufficient funds paid, customer owes $100.')
print()

# tests where bad input was provided (such as a string or percentages of cents ($0.001) or negative numbers)
print('checking for bad input')
print(optimal_change(6.024, 15) == 'Invalid amounts.')
print(optimal_change(3.98, 30.014) == 'Invalid amounts.')
print(optimal_change(-3.50, 50) == 'Invalid amounts.')
print(optimal_change(3.50, -50) == 'Invalid amounts.')
print(optimal_change('test', 50) == 'Invalid amounts.')
print(optimal_change('test', 'blah') == 'Invalid amounts.')
print(optimal_change(100.02, 'test') == 'Invalid amounts.')
print()

# random additional tests 
print('checking random additional tests to catch errors')
print(optimal_change(62.14, 100.00) == "The optimal change for an item that costs $62.14 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 1 penny.")
print(optimal_change(31.51, 150) == "The optimal change for an item that costs $31.51 with an amount paid of $150 is 1 $100 bill, 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print(optimal_change(0, 100) == "The optimal change for an item that costs $0 with an amount paid of $100 is 1 $100 bill.")
print(optimal_change(0, .02) == "The optimal change for an item that costs $0 with an amount paid of $0.02 is 2 pennies.")
print(optimal_change(0.01, .02) == "The optimal change for an item that costs $0.01 with an amount paid of $0.02 is 1 penny.")
print(optimal_change(100000, 100000.25) == "The optimal change for an item that costs $100000 with an amount paid of $100000.25 is 1 quarter.")
print()