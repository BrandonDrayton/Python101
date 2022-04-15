# Fireball > Frostbolt > Lightningbolt > Tornado > Envenom

emoji_list = [" 🔥", " ❄️", " ⚡", " 🌪️",]
bot_possible_actions = ["Fireball" +  emoji_list[0], "Frostbolt" + emoji_list[1], "Lightningbolt" + emoji_list[2], "Tornado" + emoji_list[3]]

import sys,time,random
typing_speed = 50 
from Typing import slow_type_title
from Typing import slow_type
computer_action = random.choice(bot_possible_actions)
from Functions import menu, slow_type_input
from Functions import magika_level_1
from Functions import menu_2
from Functions import magika_level_2


slow_type_title("""


888       8888888888888888      .d8888b.  .d88888b. 888b     d8888888888888      88888888888 .d88888b.       888b     d888       d8888 .d8888b. 8888888888    d8P        d8888
888   o   888888       888     d88P  Y88bd88P" "Y88b8888b   d8888888                 888    d88P" "Y88b      8888b   d8888      d88888d88P  Y88b  888  888   d8P        d88888
888  d8b  888888       888     888    888888     88888888b.d88888888                 888    888     888      88888b.d88888     d88P888888    888  888  888  d8P        d88P888
888 d888b 8888888888   888     888       888     888888Y88888P8888888888             888    888     888      888Y88888P888    d88P 888888         888  888d88K        d88P 888
888d88888b888888       888     888       888     888888 Y888P 888888                 888    888     888      888 Y888P 888   d88P  888888  88888  888  8888888b      d88P  888
88888P Y88888888       888     888    888888     888888  Y8P  888888                 888    888     888      888  Y8P  888  d88P   888888    888  888  888  Y88b    d88P   888
8888P   Y8888888       888     Y88b  d88PY88b. .d88P888   "   888888                 888    Y88b. .d88P      888   "   888 d8888888888Y88b  d88P  888  888   Y88b  d8888888888
888P     Y888888888888888888888 "Y8888P"  "Y88888P" 888       8888888888888          888     "Y88888P"       888       888d88P     888 "Y8888P888888888888    Y88bd88P     888
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You are a harry wizard trying to get home. Magic users stand in your way. You must fight to leave the forest....TO THE DEATHHHHHHHHHHH ☠️ ☠️ ☠️ ☠️ ☠️ ☠️ ☠️


""") # Read.me file or Introduction(Explain the rules)\

game_running = True
while game_running:
    user_action = menu() 
    slow_type(f"\nYou casted {user_action}\n")
    computer_action = random.choice(bot_possible_actions)
    slow_type(f"The computer casted {computer_action}\n")
    game_running = magika_level_1(user_action, computer_action)
    if game_running == True:
        slow_type("\nFrom your mighty battle you have learned a new spell!!\n")
        slow_type("Envenom learned! 🐍")
        bot_possible_actions.append("Envenom" +  "🐍")
        bot_possible_actions.append("Glachlan" +  "🔫")
        user_action_2 = menu_2()
        computer_action_2 = random.choice(bot_possible_actions)
        slow_type(f"\nYou casted {user_action_2}\n")
        slow_type(f"The computer casted {computer_action_2}\n")
        magika_level_2(user_action_2, computer_action_2)
    if game_running == False:
        replay = slow_type_input("Would you like to play again?\n\nEnter Yes/No\n\n ")
        if replay == "Yes" or replay == "yes":
            game_running = True
        else:
            slow_type("Thanks for playing. Have a magika day!")
            break
              