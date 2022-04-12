customer = {
    "Name": "Brandon",
    "Phone Number": "404-333-3333",
    "Address": "123 MadeupAve",
    "Placing Order": True,
    "Promtion": True,
    "Order Shipped": True
}





def contact_card(customer):
    print(customer["Name"])
    print(customer["Phone Number"])
    print(customer["Address"])
    print(customer["Placing Order"])
    print(customer["Promtion"])
    print(customer["Order Shipped"])

contact_card(customer)