#! python3
# bullet_point_adder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()
# text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'
lines = text.split('\n')
text = ''
for line in lines:
    text += '* ' + line + '\n'
print(text)
pyperclip.copy(text)
