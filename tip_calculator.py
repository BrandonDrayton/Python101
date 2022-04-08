def percentage_plus(bill_total, tip_percentage):
    tip_amount = bill_total * (tip_percentage / 100)
    return bill_total + tip_amount


def tip_calculator():
    bill_total = float(input(" What is your bill total? "))
    tip_percentage = int(input(" What percentage tip did you want to leave? "))
    print("Your total bill is " + str(percentage_plus(bill_total, tip_percentage)))

tip_calculator()