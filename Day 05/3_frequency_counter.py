word = "banana"
letter_freq = dict()

for letter in word:
    if letter in letter_freq:
        letter_freq[letter] += 1
    else:
        letter_freq[letter] = 1

print("Frequency of each letter: ",letter_freq)