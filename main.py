from Coinflip import flip_coin
from Dice import roll





def main():
    while True:
      user_input = (input("""Choose an option:
Press 1.) flip a coin
Press 2.) roll a die
press q.) quit
      """))
      if user_input == str(1):
        option_validation = input(f"Was {user_input} correct? ")
        if option_validation == "Yes" or option_validation == "yes":
          print("Success! ")
          flip_coin()
        if option_validation == "No" or option_validation == "no":
          print("Try again")
      if user_input == str(2):
        option_validation = input(f"Was {user_input} correct? ")
        if option_validation == "Yes" or option_validation == "yes":
          print("Success! ")
          number = 1
          user_number = int(input("How many sides should the dice have? Enter a number between 2 and 20: "))
          roll(number, user_number)
        elif option_validation == "No" or option_validation == "no":
          print("Try again")
      if user_input == "q":
        break
main()




      # if user_input == str(3):
      #   option_validation = input(f"Was {user_input} correct? ")
      #   if option_validation == "Yes" or option_validation == "yes":
      #     print("Success! ")
      #     number = 1
      #     user_number = int(input("How many sides should the dice have? Enter a number between 2 and 20: "))