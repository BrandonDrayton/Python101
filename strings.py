# # assignment operator  =
# dog = "nelson" # assigning value "nelson" to the variable 'dog'
# # introduction = 'nelson's name is nelson' # doesn't work because the string uses single quotes
# # string containing single quotes needs double quotes
# introduction = "nelson's name is nelson"
# # strings with both need triple quotes
# introduction = """nelson's name is "nelson"! """
# # characters can be "escaped" using backslash
# introduction = "my dog's name is \"nelson\""

# # multi-line strings
# # use triple quotes to use new lines
# long_introduction = """hello

# my dog's name is "nelson\""""

# # use escaped newline
# long2_introduction = "hello\n\nmy dog's name is \"nelson\""

# # passing variable to a function as an argument
# print(long_introduction)
# print(long2_introduction)
# print(dog)

# # string concatenation
# new_introduction = "My dog's name is " + dog + " and he is awesome!"
# print(new_introduction)
# dog ="toby"
# new_introduction = "My dog's name is " + dog + " and he is awesome!"
# print(new_introduction)

# user_details = 'password: helloworld!123'
# print(user_details[0:7])

divider = """ """

#  User Greeter
# Define two variables: firstname and lastname.
first_name = "Douglas"
last_name = "Nelson"
print(divider)

welcome =  "Welcome to Doggy Town " + first_name + " " + last_name + "!"
print(welcome)
print(divider)

domain_name = "@gmail.com"
company_email_address = first_name[0].lower() + "." + last_name + domain_name.lower()
print(company_email_address)
print(divider)

username = first_name[0:3].lower() + "_" + last_name[0:5].lower()
print(username)
print(divider)

contact_card = welcome + "\n" + "Email: " + company_email_address.lower() + "\n" + "Username: " + username
print(contact_card)
print(divider)
# Assign some string values to the variables.
# You can use your own name or someone else's.
#  Use those two variables to print a greeting that uses the firstname and lastname variables in the output.

#  f strings
print(f"{first_name[0]}. {last_name}")