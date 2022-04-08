# group_tip_calculator

def percentage_plus(bill_total, tip_percentage):
    tip_amount = bill_total * (tip_percentage / 100)
    return bill_total + tip_amount


def group_tip_calculator():
    bill_total = float(input(" What is your bill total? "))
    tip_percentage = int(input(" What percentage tip did you want to leave? "))
    group_size = int(input( "How many people do you have in your group? "))
    print("Your total is  " + str(percentage_plus(bill_total, tip_percentage)))
    print(f"Your total per person is " + str(percentage_plus(bill_total, tip_percentage) / group_size))

group_tip_calculator()