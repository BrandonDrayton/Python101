# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }


# foods = [
#     'pancakes',
#     'waffles',
#     'bagles',
#     'waffles'
# ]


# orders = {}

# for food in foods:
#     orders[food] = 1
#     print(orders)


# orders = {}

# for food in foods:
#     if food not in orders:
#         orders[food] = 0
#     orders[food] =+ 1


word = input("Enter a word here: ")

cnt = {}


for letter in word:
        if letter not in word:
            cnt[letter] = 0
        if letter in word:
            cnt[letter] =+ 1
        print(cnt)