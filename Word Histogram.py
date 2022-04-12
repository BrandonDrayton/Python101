user = input("Type a sentence: ").split()


word_histo = {}


for word in user:
        if word not in word_histo:
            word_histo[word] = 0
        if word in word_histo:
            word_histo[word] += 1

print(word_histo)

# print(word_histo.sorted)


# word_hito_sort = sorted(word_histo,key = word_histo.get, reverse=True)[:3]

# Top_3 = {}

# for word in word_hito_sort:
#     Top_3[word] = word_histo[word]

# print(Top_3)





