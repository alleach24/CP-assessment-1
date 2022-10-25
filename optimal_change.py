############
# Optimal Change solution
# Code Platoon, Sierra Platoon, Assessment 1
# Andrea Leach
# 17 October, 2022
############


## PSEUDOCODE
# 0) sanitize input
# 1) calculate the difference - CHANGE_OWED
# 2) initilize an empty dictionary - OPT_CHANGE - to keep track of what denominations and how many of each are owed
# 3) Starting with the largest bill - DENOM - and going through each subsequent denomination:
    # 3.1) determine if the denomination is needed (subtract DENOM from CHANGE_OWED, if it's > 0 then proceed to step 3.2, if not then move on to the next denomination in step 3)
    # 3.2) calculate the quotient (rounding down) - QUOTIENT - of DENOM into CHANGE_OWED to determine how many DENOMs are required.
    # 3.3) add {DENOM : QUOTIENT} to OPT_CHANGE
    # 3.4) subtract (DENOM * QUOTIENT) from CHANGE_OWED to account for that change being paid. Then, send the new CHANGE_OWED amount back to step 3 for the next denomination
# 4) Format the output: OPT_CHANGE contains all of the change we need, so now we have to format the output
    # 4.1) create a formatted string (f"The optimal change for an item that costs {ITEM_COST} with an amount paid of {AMOUNT_PAID} is ")
    # 4.2) oh goodness somehow format the rest of the string
# 5) return the string formatted in step 4


# import statements
import math


def optimal_change(item_cost, amount_paid):
    # print(item_cost)
    # print(amount_paid)

    # Ensure proper input is provided.
    if not sanitize_input(item_cost, amount_paid):
        return 'Invalid amounts.'

    # Computing the change in cents prevents rounding errors because multiplying by 100 ensures only whole numbers are being used in the calculations.
    item_cost_in_cents = item_cost * 100
    amount_paid_in_cents = amount_paid * 100

    # Determine the total change owed.
    change_owed = amount_paid_in_cents - item_cost_in_cents

    # Account for special cases where exact funds were paid or payment was less than the cost of the item.
    if change_owed == 0:
        return 'Exact funds were paid, no change needed.'
    if change_owed < 0:
        debt = item_cost - amount_paid
        return (f"Insufficient funds paid, customer owes ${f'{debt:.0f}' if debt % 1 == 0 else f'{debt:.2f}'}.")

    # Determine the optimal change owed by starting with the largest denomination (in cents) and assessing whether it's needed. If it is not needed, 
    # move on to the next denomination. If it is needed, add that value to OPTIMAL_CHANGE_TRACKER along with the number of that denominations needed, then reduce
    # CHANGE_OWED by that amount to determine the rest of the change needed.
    optimal_change_tracker = {}
    for denom in [10000, 5000, 2000, 1000, 500, 100, 25, 10, 5, 1]:
        if change_owed >= denom:
            optimal_change_tracker[denom] = math.floor(change_owed / denom)
            change_owed -= math.floor(change_owed / denom) * denom

    # Use the WRITE_STRING function to format the output using the given inputs and calculated optimal change
    return write_string(optimal_change_tracker, item_cost, amount_paid)


def sanitize_input(item_cost, amount_paid):
    good_input = True

    # Return True for BAD_INPUT if any input is not a float or int
    if not (type(item_cost) == float or type(item_cost) == int) or not (type(amount_paid) == float or type(amount_paid) == int):
        return not good_input

    # Return True for BAD_INPUT if any input is negative
    if item_cost < 0 or amount_paid < 0:
        return not good_input

    # Return True for BAD_INPUT if any input has percentages of cents (i.e. more than 2 decimal places)
    item_cost_decimal = str(item_cost).split('.')
    if len(item_cost_decimal) == 2:
        if len(item_cost_decimal[1]) > 2:
            return not good_input
    amount_paid_decimal = str(amount_paid).split('.')
    if len(amount_paid_decimal) == 2:
        if len(amount_paid_decimal[1]) > 2:
            return not good_input

    # If the input passes all those tests, return NOT BAD_INPUT
    return good_input


def write_string(denom_dict, cost_of_item, paid_amount):

    # Format the first half of the string using the given inputs, accounting for if the cost is a whole number or has cents.
    str_answer = f"The optimal change for an item that costs ${f'{cost_of_item:.0f}' if cost_of_item % 1 == 0 else f'{cost_of_item:.2f}'} with an amount paid of ${f'{paid_amount:.0f}' if paid_amount % 1 == 0 else f'{paid_amount:.2f}'} is "

    # Build a dictionary that converts the denominations value in cents to the name of the denomination
    converter = {
        10000: '$100 bill',
        5000: '$50 bill',
        2000: '$20 bill',
        1000: '$10 bill',
        500: '$5 bill',
        100: '$1 bill',
        25: 'quarter',
        10: 'dime',
        5: 'nickel',
        1: 'penn'
    }

    # Make a list of the denominations that are part of the optimal change
    denoms = list(denom_dict.keys()) 

    # Account for the 3 possible different scenarios: only one type of change is needed, two types of change are needed, or three or more types of change are needed.
    # All of the if/else statements account for whether the only/last denomination is a penny, as pennies break the pattern for plurality
    match len(denom_dict):

        case 1:
            if not denoms[0] == 1:
                str_answer += f"{denom_dict[denoms[0]]} {converter[denoms[0]]}{'' if denom_dict[denoms[0]] == 1 else 's'}."
            else:
                str_answer += f"{denom_dict[denoms[0]]} {converter[denoms[0]]}{'y' if denom_dict[denoms[0]] == 1 else 'ies'}."

        case 2:
            str_answer += f"{denom_dict[denoms[0]]} {converter[denoms[0]]}{'' if denom_dict[denoms[0]] == 1 else 's'} "
            
            if not denoms[1] == 1:
                str_answer += f"and {denom_dict[denoms[1]]} {converter[denoms[1]]}{'.' if denom_dict[denoms[1]] == 1 else 's.'}"
            else:
                str_answer += f"and {denom_dict[denoms[1]]} {converter[denoms[1]]}{'y.' if denom_dict[denoms[1]] == 1 else 'ies.'}"

        case _:
            for index in range(0,len(denoms) -1):
                str_answer += f"{denom_dict[denoms[index]]} {converter[denoms[index]]}{', ' if denom_dict[denoms[index]] == 1 else 's, '}"

            if not denoms[-1] == 1:
                str_answer += f"and {denom_dict[denoms[-1]]} {converter[denoms[-1]]}{'.' if denom_dict[denoms[-1]] == 1 else 's.'}"
            else:
                str_answer += f"and {denom_dict[denoms[-1]]} {converter[denoms[-1]]}{'y.' if denom_dict[denoms[-1]] == 1 else 'ies.'}"
        
    return str_answer