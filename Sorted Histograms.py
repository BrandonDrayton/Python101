words = "To be or not to be do be do be do".split()

freq = {}

for words in words:
    if words not in freq:
        freq[words] = 0
    freq[words] += 1

print(freq)

highest = None

for word in freq:
    current_word = freq[word]
    if (highest == None):
        highest = word

    if current_word > freq[highest]:
        highest = word
    
    
print(highest)

del freq[highest]

second_highest = None

for word in freq:
    current_word = freq[word]
    if (second_highest == None):
        second_highest = word

    if current_word > freq[second_highest]:
        second_highest = word

print(second_highest)