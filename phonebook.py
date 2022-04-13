# phone_number = {}


phonebook = []


while True:
    print("""Electronic Phone Book
=====================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
""")



# What do you want to do (1-5)?
    user_input = input("What do you want to do? (1-5) ")
# If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
    if user_input == "1":
        option_validation = input(f"Was {user_input} correct? ")
        if option_validation == "Yes" or option_validation == "yes":
            user_name = input("Enter a name: ")
            for contact in phonebook:
              if user_name == contact["name"]:
                  print(contact)
        if option_validation == "No" or option_validation == "no":
          print("Try again")

# If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
    if user_input == "2":
        option_validation = input(f"Was {user_input} correct? ")
        if option_validation == "Yes" or option_validation == "yes":
          name = input("Enter a name: ")
          number = input("Enter a phone number: ")
          new_entry = {"name": name, "number": number}
          phonebook.append(new_entry)
        #   print(phonebook)
        if option_validation == "No" or option_validation == "no":
          print("Try again")
# If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
    if user_input == "3":
        option_validation = input(f"Was {user_input} correct? ")
        if option_validation == "Yes" or option_validation == "yes":
          user_name = input("Enter a name: ")
          for contact in phonebook:
              if user_name == contact["name"]:
                  i = phonebook.index(contact)
                  del phonebook[i]
                #   print(phonebook)
        if option_validation == "No" or option_validation == "no":
          print("Try again")
# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
    if user_input == "4":
        for contact in phonebook:
           print("name: "
           + contact["name"]
           + "\nnumber: "
           + contact["number"]
           )
# If they choose to quit, end the program.
    if user_input == "5":
        break

