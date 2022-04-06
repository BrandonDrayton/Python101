def hello_there(first_name, last_name):
    print(f"Hello there, {first_name} {last_name}!")

hello_there("Obi", "Wan")
hello_there("Anakin", "Skywalker")

def email_gen(first_name, last_name, domain):
    print(f"{first_name[0]}, {last_name}@{domain}")

email_gen("Obi", "Wan", "ihavethehighground.com")
email_gen("Anakin", "Skywalker", "isitmeorisithotinhere.com")




# domain = "@ihavethehighground.com"
# email_gen = print(f"{first_name[0]}. {last_name} {domain}")
# user_gen = print(f"{first_name[0:3]}_{last_name[0:5]}")



# def new_contact_card(first_name, last_name, domain):
#     hello_there(first_name, last_name)
#     email_gen(first_name, last_name, domain)
#     user_gen(first_name, last_name)
