code_lines = ['this is the first line of code',
              'this is the second line of code',
              'this is the third line of code']
set_of_words = set()
for sentence in code_lines:
    list_of_words = sentence.split()
    for word in list_of_words:
        set_of_words.add(word)
print("Distinct words in text:", set_of_words)
print("Number of distinct words in text:", len(set_of_words))
