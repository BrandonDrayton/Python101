# import numbers


# Dice Roller
# Write a function that takes two numbers as arguments, then returns a random whole number between those two numbers.

# Write a script that tells the user that we are going to roll the dice but we need to know how many sides they have. Ask them for a number between 2 and 20. Pass the number 1 and the number from the user to the function, then print a message that shows the result

# Example Output:

# Let's roll a dice!
# How many sides should it have? (2-20): 10
# It's rolling...
# It's a 7!

from random import randint


def roll (number, user_number):
    result = randint((number + 1), user_number)
    print("It's rolling...")
    print("It's a " + str(result))
    
print("Let's roll dice!")
user_number = int(input("How many sides should the dice have? Enter a number between 2 and 20: "))
number = 1

roll(number, user_number)