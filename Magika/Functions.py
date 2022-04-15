import sys,time,random
emoji_list = [" 🔥", " ❄️", " ⚡", " 🌪️" ]
bot_possible_actions = ["Fireball" +  emoji_list[0], "Frostbolt" + emoji_list[1], "Lightningbolt" + emoji_list[2], "Tornado" + emoji_list[3]]
computer_action = random.choice(bot_possible_actions)
typing_speed = 50 #wpm
def slow_type_input(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2.0/typing_speed)
    input("")

def slow_type_menu(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2.0/typing_speed)
        menu()
typing_speed = 50 #wpm
def slow_type_title(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*0.1/typing_speed)
    print ("")

def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*2.0/typing_speed)
    print("")

def magika_level_1 (user_action, computer_action):
    if user_action == computer_action:
        print(f"Both wizards casted {user_action}. \n\nThe spells canceled each other out! Quick, cast again!!\n\n")
        return menu
    elif user_action == "Fireball" +  emoji_list[0]:
        if computer_action == "Lightningbolt" + emoji_list[2]:
            print("Fireball 🔥 burned the wizard to death ☠️! Onto the next level!")
            return True 
        elif computer_action == "Frostbolt" + emoji_list[1]:
            print("Fireball 🔥 melts Frostbolt ❄️  The wizard cries 'I am melting'. You continue through the forest.") 
            return True
        else:
            print("Tornado 🌪️  blew away your fire 🔥...along with your body. ☠️\n")
        return False
    elif user_action == "Frostbolt" + emoji_list[1]:
        if computer_action == "Lightningbolt" + emoji_list[2]:
            print("Frostbolt ❄️  freezes Lightningbolt ⚡ You forze the wizard!!\n")
        elif computer_action == "Tornado" + emoji_list[3]:
            print("Frostbolt ❄️  freezes the wind around the wizard. You see his arms fall away from his body and move forward. 🌪️!")
        else:
            print("Fireball 🔥 melted your Frostbolt ❄️   ...and then melted you. ☠️\n")
        return False
    elif user_action == "Tornado" + emoji_list[3]:
        if computer_action == "Frostbolt" + emoji_list[1]:
            print("Tornado 🌪️  blows away their Frostbolt ❄️  You move past the wizard and belch onto the road! Killing really is a nasty buisness")
        elif computer_action == "Fireball" +  emoji_list[0]:
            print("Your tornado 🌪️ snuffed out their Fireball 🔥...and then their very life. ☠️\n")
        else:
            print("Lightningbolt ⚡ shocked you into a delusion. You believe you are a beautiful butterfly...you die after jumping from a tree in an attempt to fly. ☠️")
        return False
    elif user_action == "Lightningbolt" + emoji_list[2]:
        if computer_action == "Tornado" + emoji_list[3]:
            print("Your Lightningbolt ⚡ was faster...he is very dead. ☠️")
        elif computer_action == "Fireball" +  emoji_list[0]:
            print("Your lightningbolt ⚡ whizzed past their Fireball 🔥 and then shockingly killed them. ☠️")
        else:
            print("Their frostbolt ❄️  froze you arms off. You quipped 'Tis but a scratch' before perishing. ☠️")
        return False
def menu():
    user_action = input("""\nCHOOSE A SPELL:

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
    else:
        print("YOU MUST CHOOSE A SPELL FOOL!")
        menu()
     
def menu_2():

    slow_type_title("""

    You have defeated the wizard but a warlock has appeared...AND HE IS HOLDING A GLOCK 🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫🔫
-----------------------------------------------------------------------------------------

                                                                                                                                                                                                      
                                                                                                                                                                                                      
        GGGGGGGGGGGGGLLLLLLLLLLL                            AAA                  CCCCCCCCCCCCCHHHHHHHHH     HHHHHHHHHLLLLLLLLLLL                            AAA               NNNNNNNN        NNNNNNNN
     GGG::::::::::::GL:::::::::L                           A:::A              CCC::::::::::::CH:::::::H     H:::::::HL:::::::::L                           A:::A              N:::::::N       N::::::N
   GG:::::::::::::::GL:::::::::L                          A:::::A           CC:::::::::::::::CH:::::::H     H:::::::HL:::::::::L                          A:::::A             N::::::::N      N::::::N
  G:::::GGGGGGGG::::GLL:::::::LL                         A:::::::A         C:::::CCCCCCCC::::CHH::::::H     H::::::HHLL:::::::LL                         A:::::::A            N:::::::::N     N::::::N
 G:::::G       GGGGGG  L:::::L                          A:::::::::A       C:::::C       CCCCCC  H:::::H     H:::::H    L:::::L                          A:::::::::A           N::::::::::N    N::::::N
G:::::G                L:::::L                         A:::::A:::::A     C:::::C                H:::::H     H:::::H    L:::::L                         A:::::A:::::A          N:::::::::::N   N::::::N
G:::::G                L:::::L                        A:::::A A:::::A    C:::::C                H::::::HHHHH::::::H    L:::::L                        A:::::A A:::::A         N:::::::N::::N  N::::::N
G:::::G    GGGGGGGGGG  L:::::L                       A:::::A   A:::::A   C:::::C                H:::::::::::::::::H    L:::::L                       A:::::A   A:::::A        N::::::N N::::N N::::::N
G:::::G    G::::::::G  L:::::L                      A:::::A     A:::::A  C:::::C                H:::::::::::::::::H    L:::::L                      A:::::A     A:::::A       N::::::N  N::::N:::::::N
G:::::G    GGGGG::::G  L:::::L                     A:::::AAAAAAAAA:::::A C:::::C                H::::::HHHHH::::::H    L:::::L                     A:::::AAAAAAAAA:::::A      N::::::N   N:::::::::::N
G:::::G        G::::G  L:::::L                    A:::::::::::::::::::::AC:::::C                H:::::H     H:::::H    L:::::L                    A:::::::::::::::::::::A     N::::::N    N::::::::::N
 G:::::G       G::::G  L:::::L         LLLLLL    A:::::AAAAAAAAAAAAA:::::AC:::::C       CCCCCC  H:::::H     H:::::H    L:::::L         LLLLLL    A:::::AAAAAAAAAAAAA:::::A    N::::::N     N:::::::::N
  G:::::GGGGGGGG::::GLL:::::::LLLLLLLLL:::::L   A:::::A             A:::::AC:::::CCCCCCCC::::CHH::::::H     H::::::HHLL:::::::LLLLLLLLL:::::L   A:::::A             A:::::A   N::::::N      N::::::::N
   GG:::::::::::::::GL::::::::::::::::::::::L  A:::::A               A:::::ACC:::::::::::::::CH:::::::H     H:::::::HL::::::::::::::::::::::L  A:::::A               A:::::A  N::::::N       N:::::::N
     GGG::::::GGG:::GL::::::::::::::::::::::L A:::::A                 A:::::A CCC::::::::::::CH:::::::H     H:::::::HL::::::::::::::::::::::L A:::::A                 A:::::A N::::::N        N::::::N
        GGGGGG   GGGGLLLLLLLLLLLLLLLLLLLLLLLLAAAAAAA                   AAAAAAA   CCCCCCCCCCCCCHHHHHHHHH     HHHHHHHHHLLLLLLLLLLLLLLLLLLLLLLLLAAAAAAA                   AAAAAAANNNNNNNN         NNNNNNN
                                                                                                                                                                                                      
has appeared!                                                                                 
                                                                         
    """)
    user_action_2 = input("""Choose a spell:

Press 1 for Fireball 🔥

Press 2 for Frostbolt ❄️

Press 3 for Lightningbolt ⚡

Press 4 for Tornado 🌪️

Press 5 for Envenom 🐍

    """)

    if user_action_2 == "1":
        user_action_2 = "Fireball" +  emoji_list[0]
        return user_action_2
    if user_action_2 == "2":
        user_action_2 = "Frostbolt" + emoji_list[1]
        return user_action_2
    if user_action_2 == "3":
        user_action_2 = "Lightningbolt" + emoji_list[2]
        return user_action_2
    if user_action_2 == "4":
        user_action_2 = "Tornado" + emoji_list[3]
        return user_action_2
    if user_action_2 == "5": 
        user_action_2 ="Envenom" +  "🐍"
        return user_action_2

def magika_level_2(user_action_2, computer_action_2):
    if user_action_2 == computer_action_2:
        print(f"Both wizards casted {user_action_2}. The spells canceled each other out! Quick, cast again!!")
        return True
    if computer_action_2 == "Glachlan" + "🔫":
        print("WOW! YOU BROUGHT A SPELL TO A GUN FIGHT AND DIED FOOL!")
        return menu()
    elif user_action_2 == "Fireball" +  emoji_list[0]:
        if computer_action_2 == "Lightningbolt" + emoji_list[2]:
            print("Fireball burned the wizard to death! You win!")
        elif computer_action_2 == "Frostbolt" + emoji_list[1]:
            print("Fireball melts Glachan! You win!....Im not sure why he didnt use his Glock...")
        elif computer_action_2 =="Envenom" +  "🐍":
            print("Holy crap I can't belive he didn't use his glock!")
        else:
            print("OMG GLACHLAN BLEW YOUR FIRE AWAY...along with your body. R.I.P")
            print("Do you want to play again?")
            menu()
        return False
    elif user_action_2 == "Frostbolt" + emoji_list[1]:
        if computer_action_2 == "Lightningbolt" + emoji_list[2]:
            print("Frostbolt freezes Lightningbolt! OMG You win!")
        elif computer_action_2 == "Tornado":
            print("Tornado blows away your Frostbolt! You lose.")
        elif computer_action_2 =="Envenom" +  "🐍":
            print("Holy crap I can't belive he didn't use his glock!")
        else:
            print("Fireball melted your Frostbolt...and then melted you. R.I.P.")
        return False
    elif user_action_2 == "Tornado":
        if computer_action_2 == "Frostbolt" + emoji_list[1]:
            print("Tornado blows away their Frostbolt! You win!")
        elif computer_action_2 == "Fireball" +  emoji_list[0]:
            print("Your tornado snuffed out their fireball...and then their very life.")
        elif user_action_2 =="Envenom" +  "🐍":
            print("Lightningbolt shocked you into a delusion. You believe you are a beautiful butterfly...you die after jumping from a tree in an attempt to fly. R.I.P.")
        else:
            print("You were so shocked that the wind was knocked out of you")
            return False
    elif user_action_2 == "Lightningbolt" + emoji_list[2]:
        if computer_action_2 == "Tornado":
            print("Your Lightningbolt was faster...he is very dead")
        elif computer_action_2 =="Envenom" +  "🐍":
            print("Your Lightningbolt didn't know how to conduct itself taking out the wizard as soon as you uttered the spell. Whoops.")
        elif computer_action_2 == "Fireball" +  emoji_list[0]:
            print("Your lightningbolt whizzed past their fireball and killed them.")
        else:
            print("Their frostbolt froze you arms off. You quipped 'Tis but a scratch' before perishing.")
        return False
    elif user_action_2 =="Envenom" +  "🐍":
        if computer_action_2 == "Lightningbolt" + emoji_list[2]:
            print("You spit venom on the ")
        elif computer_action_2 == "Fireball" +  emoji_list[0]:
            print("")
        elif computer_action_2 == "Frostbolt" + emoji_list[1]:
            print("")
        else:
            print("You is dead")
        return False