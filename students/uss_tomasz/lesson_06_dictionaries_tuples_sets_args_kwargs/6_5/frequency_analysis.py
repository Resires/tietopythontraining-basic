TEXT = ['given a number n followed by n lines of text ',
        'print all words encountered in the text one per line',
        'the words should be sorted in descending order according ',
        'to their number of occurrences in the text',
        'and all words with the same frequency should be printed in lexicographical order']
DICT_OF_WORDS_WITH_OCCURRENCE = {}
for sentence in TEXT:
    for word in sentence.split():
        if word in DICT_OF_WORDS_WITH_OCCURRENCE.keys():
            DICT_OF_WORDS_WITH_OCCURRENCE[word] += 1
        else:
            DICT_OF_WORDS_WITH_OCCURRENCE[word] = 1
LIST_OF_WORDS_WITH_OCCURRENCE = []
for word, occurrence in DICT_OF_WORDS_WITH_OCCURRENCE.items():
    LIST_OF_WORDS_WITH_OCCURRENCE.append((occurrence, word))
# Specify the index of tuple, and direction of sorting True/False
sort_spec = ((1, False), (0, True))
for index, reverse_value in sort_spec:
    LIST_OF_WORDS_WITH_OCCURRENCE.sort(key = lambda x: x[index], reverse=reverse_value)
print(LIST_OF_WORDS_WITH_OCCURRENCE)
