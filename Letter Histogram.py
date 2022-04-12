word = input("Enter a word here: ")

cnt = {}


for letter in word:
        if letter not in cnt:
            cnt[letter] = 0
        if letter in cnt:
            cnt[letter] += 1
print(cnt)


