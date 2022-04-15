# Write a function that will "flip a coin" and print the result. There should be a 50/50 chance of getting heads or tails.

# Example Output:

# You flipped a coin!
# It is heads!
# You flipped a coin!
# It is tails!

import random



def flip_coin():
    num=random.randint(0,1)
    if num == 0:
        print("It is heads")
    elif num == 1:
        print("It it tails")

# flip_coin()
