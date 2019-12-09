import os
import re
user_regex = r'\d{3}'
text_file_names = [f for f in os.listdir(os.curdir) if os.path.isfile(f) and f.endswith('.txt')]
if len(text_file_names) == 0:
    print('There are no text files')
else:
    print('In current working directory there are following text files:', text_file_names)
    for text_file_name in text_file_names:
        text_file = open(text_file_name, 'r')
        text = text_file.read()
        results = re.findall(user_regex, text)
        if len(results) > 0:
            print('In file named "{}" there were following occurrences:'.format(text_file_name))
            for result in results:
                print(result)
