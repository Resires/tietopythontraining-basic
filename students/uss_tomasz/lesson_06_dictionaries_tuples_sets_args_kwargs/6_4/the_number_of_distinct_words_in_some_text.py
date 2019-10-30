CODE_LINES = ['this is the first line of code',
              'this is the second line of code',
              'this is the third line of code']
SET_OF_WORDS = set()
for sentence in CODE_LINES:
    list_of_words = sentence.split()
    for word in list_of_words:
        SET_OF_WORDS.add(word)
print("Distinct words in text:", SET_OF_WORDS)
print("Number of distinct words in text:", len(SET_OF_WORDS))
