divider = "\n"

def hello_there(first_name, last_name):
    print(f"Hello there, {first_name} {last_name}!")

hello_there("Obi", "Wan")
hello_there("Anakin", "Skywalker")
print(divider)
def email_gen(first_name, last_name, domain):
    print(f"{first_name[0]}.{last_name}@{domain}")

email_gen("Obi", "Wan", "ihavethehighground.com")
email_gen("Anakin", "Skywalker", "isitmeorisithotinhere.com")
print(divider)
def user_gen(first_name, last_name):
    print(f"{first_name[0:3]}_{last_name[0:5]}.")

user_gen("Obi", "Wan")
user_gen("Anakin", "Skywalker")
print(divider)

def new_user_contact_info(first_name, last_name, domain):
    print(f"Hello there, {first_name} {last_name}!")
    print(f"Email:\n{first_name[0]}.{last_name}@{domain}")
    print(f"Username:\n{first_name[0:3]}_{last_name[0:5]}")

new_user_contact_info("Obi", "Wan", "ihavethehighground.com")    