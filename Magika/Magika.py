# Fireball > Frostbolt > Lightningbolt > Tornado > Fireball etc...

# import pygame
# import os

import random
import emoji
	

# Read.me file or Introduction(Explain the rules)

emoji_list = [" 🔥", " ❄️", " ⚡", " 🌪️" ]
bot_possible_actions = ["Fireball" +  emoji_list[0], "Frostbolt" + emoji_list[1], "Lightningbolt" + emoji_list[2], "Tornado" + emoji_list[3]]

computer_action = random.choice(bot_possible_actions)

def magika_level_1 (user_action, computer_action):
    if user_action == computer_action:
        print(f"Both wizards casted {user_action}. \n\nThe spells canceled each other out! Quick, cast again!!\n")
        return True
    elif user_action == "Fireball" +  emoji_list[0]:
        if computer_action == "Lightningbolt" + emoji_list[2]:
            print("Fireball 🔥 burned the wizard to death ☠️! Onto the next level!")
            menu_2
            user_action_2 = menu_2()
            computer_action_2 = random.choice(bot_possible_actions)
            magika_level_2(user_action_2, computer_action_2)  
        elif computer_action == "Frostbolt" + emoji_list[1]:
            print("Fireball 🔥 melts Frostbolt ❄️  You win!")
            menu_2
            user_action_2 = menu_2()
            computer_action_2 = random.choice(bot_possible_actions)
            magika_level_2(user_action_2, computer_action_2)  
        else:
            print("Tornado 🌪️ blew away your fire 🔥...along with your body. ☠️\n")
        return False
    elif user_action == "Frostbolt" + emoji_list[1]:
        if computer_action == "Lightningbolt" + emoji_list[2]:
            print("Frostbolt ❄️  freezes Lightningbolt ⚡ You win!")
        elif computer_action == "Tornado":
            print("Frostbolt ❄️  freezes their Tornado 🌪️!")
        else:
            print("Fireball 🔥 melted your Frostbolt ❄️   ...and then melted you. ☠️\n")
        return False
    elif user_action == "Tornado" + emoji_list[3]:
        if computer_action == "Frostbolt" + emoji_list[1]:
            print("Tornado 🌪️  blows away their Frostbolt ❄️  You win!")
        elif computer_action == "Fireball" +  emoji_list[0]:
            print("Your tornado 🌪️ snuffed out their Fireball 🔥...and then their very life. ☠️")
        else:
            print("Lightningbolt ⚡ shocked you into a delusion. You believe you are a beautiful butterfly...you die after jumping from a tree in an attempt to fly. ☠️")
        return False
    elif user_action == "Lightningbolt" + emoji_list[2]:
        if computer_action == "Tornado" + emoji_list[3]:
            print("Your Lightningbolt ⚡ was faster...he is very dead. ☠️")
        elif computer_action == "Fireball" +  emoji_list[0]:
            print("Your lightningbolt ⚡ whizzed past their Fireball 🔥 and killed them. ☠️")
        else:
            print("Their frostbolt ❄️  froze you arms off. You quipped 'Tis but a scratch' before perishing. ☠️")
        return False
def menu():
    user_action = input("""CHOOSE A SPELL:

Press1️⃣  for Fireball 🔥

Press2️⃣  for Frostbolt ❄️

Press3️⃣  for Lightningbolt ⚡

Press4️⃣  for Tornado 🌪️

    """)

    if user_action == "1":
        user_action = "Fireball" +  emoji_list[0]
        return user_action
    if user_action == "2":
        user_action = "Frostbolt" + emoji_list[1]
        return user_action
    if user_action == "3":
        user_action = "Lightningbolt" + emoji_list[2]
        return user_action
    if user_action == "4":
        user_action = "Tornado" + emoji_list[3]
        return user_action
def menu_2():

    
    
    
    print("""

888b     d8888888888888b    8888888888   888888b.   .d88888b.  .d8888b.  .d8888b. 
8888b   d8888  888  8888b   888  888     888  "88b d88P" "Y88bd88P  Y88bd88P  Y88b
88888b.d88888  888  88888b  888  888     888  .88P 888     888Y88b.     Y88b.     
888Y88888P888  888  888Y88b 888  888     8888888K. 888     888 "Y888b.   "Y888b.  
888 Y888P 888  888  888 Y88b888  888     888  "Y88b888     888    "Y88b.    "Y88b.
888  Y8P  888  888  888  Y88888  888     888    888888     888      "888      "888
888   "   888  888  888   Y8888  888     888   d88PY88b. .d88PY88b  d88PY88b  d88P
888       8888888888888    Y8888888888   8888888P"  "Y88888P"  "Y8888P"  "Y8888P" 
                                                                                  
                                                                         
    """)
    user_action_2 = input("""Choose a spell:

Press 1 for Fireball

Press 2 for Frostbolt

Press 3 for Lightningbolt

Press 4 for Tornado

    """)

    if user_action_2 == "1":
        user_action_2 = "Fireball"
        return user_action_2
    if user_action_2 == "2":
        user_action_2 = "Frostbolt"
        return user_action_2
    if user_action_2 == "3":
        user_action_2 = "Lightningbolt"
        return user_action_2
    if user_action_2 == "4":
        user_action_2 = "Tornado"
        return user_action_2
def magika_level_2(user_action_2, computer_action_2):
    if user_action_2 == computer_action_2:
        print(f"Both wizards casted {user_action_2}. The spells canceled each other out! Quick, cast again!!")
        return True
    elif user_action_2 == "Fireball":
        if computer_action_2 == "Lightningbolt":
            print("Fireball burned the wizard to death! You win!")
        elif computer_action_2 == "Frostbolt":
            print("Fireball melts Frostbolt! You win!")
        else:
            print("Tornado blew away your fire...along with your body. R.I.P")
        return False
    elif user_action_2 == "Frostbolt":
        if computer_action_2 == "Lightningbolt":
            print("Frostbolt freezes Lightningbolt! You win!")
        elif computer_action_2 == "Tornado":
            print("Tornado blows away your Frostbolt! You lose.")
        else:
            print("Fireball melted your Frostbolt...and then melted you. R.I.P.")
        return False
    elif user_action_2 == "Tornado":
        if computer_action_2 == "Frostbolt":
            print("Tornado blows away their Frostbolt! You win!")
        elif computer_action_2 == "Fireball":
            print("Your tornado snuffed out their fireball...and then their very life.")
        else:
            print("Lightningbolt shocked you into a delusion. You believe you are a beautiful butterfly...you die after jumping from a tree in an attempt to fly. R.I.P.")
        return False
    elif user_action_2 == "Lightningbolt":
        if computer_action_2 == "Tornado":
            print("Your Lightningbolt was faster...he is very dead")
        elif computer_action_2 == "Fireball":
            print("Your lightningbolt whizzed past their fireball and killed them.")
        else:
            print("Their frostbolt froze you arms off. You quipped 'Tis but a scratch' before perishing.")
        return False


print("""


888       8888888888888888      .d8888b.  .d88888b. 888b     d8888888888888      88888888888 .d88888b.       888b     d888       d8888 .d8888b. 8888888888    d8P        d8888
888   o   888888       888     d88P  Y88bd88P" "Y88b8888b   d8888888                 888    d88P" "Y88b      8888b   d8888      d88888d88P  Y88b  888  888   d8P        d88888
888  d8b  888888       888     888    888888     88888888b.d88888888                 888    888     888      88888b.d88888     d88P888888    888  888  888  d8P        d88P888
888 d888b 8888888888   888     888       888     888888Y88888P8888888888             888    888     888      888Y88888P888    d88P 888888         888  888d88K        d88P 888
888d88888b888888       888     888       888     888888 Y888P 888888                 888    888     888      888 Y888P 888   d88P  888888  88888  888  8888888b      d88P  888
88888P Y88888888       888     888    888888     888888  Y8P  888888                 888    888     888      888  Y8P  888  d88P   888888    888  888  888  Y88b    d88P   888
8888P   Y8888888       888     Y88b  d88PY88b. .d88P888   "   888888                 888    Y88b. .d88P      888   "   888 d8888888888Y88b  d88P  888  888   Y88b  d8888888888
888P     Y888888888888888888888 "Y8888P"  "Y88888P" 888       8888888888888          888     "Y88888P"       888       888d88P     888 "Y8888P888888888888    Y88bd88P     888
                                                                                                                                                                              

""")
game_running = True
while game_running:
    user_action = menu()


    print(f"\nYou casted {user_action}\n")
    computer_action = random.choice(bot_possible_actions)
    print(f"The computer casted {computer_action}\n")
    game_running = magika_level_1(user_action, computer_action)
    if game_running == False:
        replay = input("Would you like to play again?\nEnter Yes/No ")
        if replay == "Yes" or replay == "yes":
            game_running = True
        else:
            print("Thanks for playing. Have a magika day!")
            break
              



# Game idea is to have wizards fight each other using elements:
    # Each wizard would select a spell and fire it each other
    # Certain spells would cancel and/or defeat others.
# Next would be to generate different levels eventually ending with a boss
        