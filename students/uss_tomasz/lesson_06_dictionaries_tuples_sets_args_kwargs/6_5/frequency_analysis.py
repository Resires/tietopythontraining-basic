text = ['given a number n followed by n lines of text ',
        'print all words encountered in the text one per line',
        'the words should be sorted in descending order according ',
        'to their number of occurrences in the text',
        'and all words with the same frequency should be printed in lexicographical order']
dict_of_words_with_occurrence = {}
for sentence in text:
    for word in sentence.split():
        if word in dict_of_words_with_occurrence.keys():
            dict_of_words_with_occurrence[word] += 1
        else:
            dict_of_words_with_occurrence[word] = 1
list_of_words_with_occurrence = []
for word, occurrence in dict_of_words_with_occurrence.items():
    list_of_words_with_occurrence.append((occurrence, word))
# Specify the index of tuple, and direction of sorting True/False
sort_spec = ((1, False), (0, True))
for index, reverse_value in sort_spec:
    list_of_words_with_occurrence.sort(key=lambda x: x[index], reverse=reverse_value)
print(list_of_words_with_occurrence)
