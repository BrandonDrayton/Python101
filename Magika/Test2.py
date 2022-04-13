import random

possible_actions = ["Fireball", "Frostbolt", "Lightningbolt", "Tornado"]

# computer_action_2 = random.choice(possible_actions)

def menu():
    user_action_2 = input("""Choose a spell:

Press 1 for Fireball

Press 2 for Frostbolt

Press 3 for Lightningbolt

Press 4 for Tornado

    """)

    if user_action_2 == "1":
        user_action_2 = "Fireball"
        return
    if user_action_2 == "2":
        user_action_2 = "Frostbolt"
        return
    if user_action_2 == "3":
        user_action_2 = "Lightningbolt"
        return
    if user_action_2 == "4":
        user_action_2 = "Tornado"
        return



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
user_action_2 = menu()

computer_action_2 = random.choice(possible_actions)
magika_level_2(user_action_2, computer_action_2)