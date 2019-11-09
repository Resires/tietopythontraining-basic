import pyperclip
text = pyperclip.paste()
lines = text.split('\n')
text = ''
for line in lines:
    text += '* ' + line + '\n'
print(text)
pyperclip.copy(text)
