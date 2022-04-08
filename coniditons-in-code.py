# print("hello")
# name = input("Who shot first? ")

# # if the name is Han Solo   side note: if you put or name the if condition will meet any of those names

# if name == "Han Solo":
#     print("You're cool")

# # side note: if you put or name the if condition will meet any of those names

# if name == "Han Solo" or name == "Han":
#     print("You're cool")

# print("Bye!")

# name = "Steve"
# print(name == "Nelson")

# age = int(input("What is your age? "))
# if age < 21:
#     print("You will not be entering this establishment young padawan! ")

# else:
#     print('Come on in Jedi scum!')

# choice = input("""
# choose an option:
# A) say nothing
# B) pull out your lightsaber
# C) stare menacingly 
# """)

# if choice == 'A':
#     print('The man becomes nervous')
# elif choice == 'B':
#     print("The man backs away nervously...")
# elif choice == 'C':
#     print('The man becomes agitated')
# else:
#     print('That is not an option Jedi Scum')

# num = int(input('pick a number: '))

# if num > 5 and num <= 10:
#     print('ok, bigger than 5')

# elif num > 10 and num <= 8999:
#     print('getting bigger...')

# elif num > 9000:
#     print("THATS OVER 9000!!!")

# Work or Sleep In

# day = input("What day is it? ")
# business_day = "Monday" or "Tuesday" or "Wednesday" or "Thursday" or "Friday"
# weekend_day = "Saturday" or "Sunday"

# if day == business_day:
#     print("go to work")
# if day == weekend_day:
#     print("go to sleep")
# elif day != business_day or weekend_day:
#     print("Please enter a valid day of the week. ")

# # Secret Password

# password = input("What is the password? ")

# if password == "Move along":
#     print("Welcome!")
# else:
#     print("Try again!")

# Day of the week

# number = int(input("Enter a number from 1 to 7: "))
# if number == 1:
#     print(f"{number} = 'Monday")
# if number == 2:
#     print(f"{number} = 'Tuesday")    
# if number == 3:
#     print(f"{number} = 'Wednesday")
# if number == 4:
#     print(f"{number} = 'Thursday")
# if number == 5:
#     print(f"{number} = Friday")
# if number == 6:
#     print(f"{number} = 'Saturday'")
# if number == 7:
#     print(f"{number} = 'Sunday'")
# elif number < 0 or number > 7:
#     print("Do you not know how to count from 1 to 7?")

#  Letter Grade

# number_grade = int(input("Enter your number score from 1 - 100: "))
# if number_grade < 60:
#     print("F")
# if number_grade >= 60 and number_grade < 70:
#     print("D")
# if number_grade >= 70 and number_grade < 80:
#     print("C")
# if number_grade >= 80 and number_grade < 90:
#     print("B")
# if number_grade >= 90 and number_grade <= 100:
#     print("A")
# if number_grade < 1 or number_grade > 100:
#     print("You did not enter a number from 1 - 100")

# Tip Calculator

# Mad Libs

# Ask the user for three inputs (a noun, a present-tense verb, and a name) and store the values in appropriately named variables.
# Next, write a function called madlib that takes three parameters: a noun, a present-tense verb, and a name. The function should print a story that uses these parameters to the console.
# Lastly, pass the three user inputs to the madlib function, so that when you execute the script, it asks the user for input, and then prints out the madlib story

def percentage_plus(bill_total, tip_percentage):
    tip_amount = bill_total * (tip_percentage / 100)
    return bill_total + tip_amount


def tip_calculator():
    bill_total = float(input(" What is your bill total? "))
    tip_percentage = int(input(" What percentage tip did you want to leave? "))
    print("Your total bill is " + str(percentage_plus(bill_total, tip_percentage)))

tip_calculator()

# group_tip_calculator

def group_tip_calculator():
    bill_total = float(input(" What is your bill total? "))
    tip_percentage = int(input(" What percentage tip did you want to leave? "))
    group_size = int(input( "How many people do you have in your group? "))
    print("Your total is  " + str(percentage_plus(bill_total, tip_percentage)))
    print("Your total per person is " + str(percentage_plus(bill_total, tip_percentage) / group_size))

group_tip_calculator()
