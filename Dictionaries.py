# Dictionary syntax


# # empty
# breakfast_order = {}

# # define data with KEY and VALUE
breakfast_order = {
    "main": "Short Stack",
    "seat": 3,
    "table": 10,
    "paid": False,
}

if (breakfast_order["paid"]):
    print("thank you for paying!")
else:
    print("THIEF")

# # access data inside a dictionary with the key name inside of sqaure brackets
# # print(f'the main for seat {breakfast_order["seat"]} is {breakfast_order["main"]}')

# # access data using vaule of variable as key
# key = "main"
# print(breakfast_order["table"])

# breakfast_order["main"] = "eggs over easy"
# print(breakfast_order["main"]) # eggs over easy

# # adding another value to an object

# breakfast_order["side"] = "hash brown and bacon"

# # removing items from a dictionary
# # del breakfast_order["main"]

# side = breakfast_order.pop("side")

# nesting data inside another dictionary
user = {
    "email": "tony@starkindusries.com",
    "name": {
        "first": "Tony",
        "last": "Stark"
    }
}

print(user["email"])
print(user["name"]["first"])

# accessing nested data
# first = user["name"]["first"]
# last = user["name"]["last"]


print(f"Hello {user['name']['first']} {user['name']['last']}")