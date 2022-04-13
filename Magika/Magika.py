# Fireball > Frostbolt > Lightningbolt > Tornado > Fireball etc...



import random

possible_actions = ["Fireball", "Frostbolt", "Lightningbolt", "Tornado"]

computer_action = random.choice(possible_actions)

def magika (user_action, computer_action):
    if user_action == computer_action:
        print(f"Both wizards casted {user_action}. The spells canceled each other out! Quick, cast again!!")
        return True
    elif user_action == "Fireball":
        if computer_action == "Lightningbolt":
            print("Fireball burned the wizard to death! You win!")
        elif computer_action == "Frostbolt":
            print("Fireball melts Frostbolt! You win!")
        else:
            print("Tornado blew away your fire...along with your body. R.I.P")
        return False
    elif user_action == "Frostbolt":
        if computer_action == "Lightningbolt":
            print("Frostbolt freezes Lightningbolt! You win!")
        elif computer_action == "Tornado":
            print("Tornado blows away your Frostbolt! You lose.")
        else:
            print("Fireball melted your Frostbolt...and then melted you. R.I.P.")
        return False
    elif user_action == "Tornado":
        if computer_action == "Frostbolt":
            print("Tornado blows away their Frostbolt! You win!")
        elif computer_action == "Fireball":
            print("Your tornado snuffed out their fireball...and then their very life.")
        else:
            print("Lightningbolt shocked you into a delusion. You believe you are a beautiful butterfly...you die after jumping from a tree in an attempt to fly. R.I.P.")
        return False
    elif user_action == "Lightningbolt":
        if computer_action == "Tornado":
            print("Your Lightningbolt was faster...he is very dead")
        elif computer_action == "Fireball":
            print("Your lightningbolt whizzed past their fireball and killed them.")
        else:
            print("Their frostbolt froze you arms off. You quipped 'Tis but a scratch' before perishing.")
        return False




print(""""
____    __    ____ _______ __      _______  ______  ______  .___  ___. _______  .___________. ______    .___  ___.     ___      _______ __  __  ___     ___     
\   \  /  \  /   /|   ____|  |    |   ____|/      |/  __  \ |   \/   ||   ____| |           |/  __  \   |   \/   |    /   \    /  _____|  ||  |/  /    /   \    
 \   \/    \/   / |  |__  |  |    |  |__  |  ,----|  |  |  ||  \  /  ||  |__    `---|  |----|  |  |  |  |  \  /  |   /  ^  \  |  |  __ |  ||  '  /    /  ^  \   
  \            /  |   __| |  |    |   __| |  |    |  |  |  ||  |\/|  ||   __|       |  |    |  |  |  |  |  |\/|  |  /  /_\  \ |  | |_ ||  ||    <    /  /_\  \  
   \    /\    /   |  |____|  `----|  |____|  `----|  `--'  ||  |  |  ||  |____      |  |    |  `--'  |  |  |  |  | /  _____  \|  |__| ||  ||  .  \  /  _____  \ 
    \__/  \__/    |_______|_______|_______|\______|\______/ |__|  |__||_______|     |__|     \______/   |__|  |__|/__/     \__\\______||__||__|\__\/__/     \__\
                                                                                                                                                                
""")

game_running = True
while game_running:

    user_action = input("""Choose a spell: 
Press 1 for Fireball
Press 2 for Frostbolt
Press 3 for Lightningbolt
Press 4 for Tornado

    """)

    if user_action == "1":
        user_action = "Fireball"

    if user_action == "2":
        user_action = "Frostbolt"

    if user_action == "3":
        user_action = "Lightningbolt"

    if user_action == "4":
        user_action = "Tornado"

    print(f"You casted {user_action}")
    computer_action = random.choice(possible_actions)
    print(f"The computer casted {computer_action}")
    game_running = magika(user_action, computer_action)
    if game_running == False:
        replay = input("Would you like to play again? ")
        if replay == "Yes" or replay == "yes":
            game_running == True
        if replay == "No" or replay == "no":
            game_running == False





# Game idea is to have wizards fight each other using elements:
    # Each wizard would combine two elements which then would fire the combined spell towards the other wizard
    # Certain spells would cancel and/or defeat others (The thinking here is to creat something roughly Fireball/paper/scissors)

        # Create elements list which could be referenced
        # Create combination list?
        # 