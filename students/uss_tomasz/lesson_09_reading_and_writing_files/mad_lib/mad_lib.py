import re
try:
    mad_lib_file = open('text.txt', 'r')
    mad_lib_text = mad_lib_file.read()
    mad_lib_file.close()
    # regex is needed, because string.split() method is not handling 'NOUN.' and 'VERB?' cases
    word_list = re.split(r'(\W)', mad_lib_text)
    new_word_list = []
    part_of_speech = {'ADJECTIVE': 'Enter an adjective:', 'NOUN': 'Enter a noun:', 'ADVERB': 'Enter an adverb:',
                      'VERB': 'Enter a verb:'}
    for word in word_list:
        if word in part_of_speech:
            new_word_list.append(input(part_of_speech[word]))
        else:
            new_word_list.append(word)
    new_mad_lib_text = ''.join(new_word_list)
    print(new_mad_lib_text)
    new_mad_lib_file = open('new_text.txt', 'w')
    new_mad_lib_file.write(new_mad_lib_text)
    new_mad_lib_file.close()
except FileNotFoundError:
    print('Text file does not exist')
