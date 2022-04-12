# Coin Flipper
# Write a script that tells the user they have 1 coin and asks them if they want another. Keep adding coins until they say 'no'. Flip each coin print the result for each (coins are 50/50 chance of heads vs tails).

# You have 1 coin.
# Do you want another? yes
# You have 2 coins.
# Do you want another? yes
# You have 3 coins.
# Do you want another? no
# Let's flip them!
# Coin 1 - Heads
# Coin 2 - Heads
# Coin 3 - Tails

import random

print("You have 1 coin! ")

coins = 1 
while True:
    answer = input("Would you like another coin? Please enter yes or no: ")
    if answer.lower() == "yes":
        coins += 1
        print(f"You now have {coins} coin.")
    elif answer.lower() == "no":
        break
    else:
        print("Please enter 'yes' or 'no'.")

for coin in range(coins):
    coin = random.randint(0, 1)
    print(f'Coin flip {coin + 1}: ', end='')
    if coin == 0:
        print("Heads")
    else:
        print("Tails")


# coin_flip = random.randint(0, 1)

# if coin_flip == 0:
#     print("It is heads")
# elif num == 1:
#     print("It it tails")
