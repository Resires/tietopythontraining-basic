# msb.pyw - saves and loads pieces of text to the clipboard.
# usage: py.exe msb.pyw save <keyword> - saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - loads keyword to clipboard.
#        py.exe mcb.pyw list - loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - delete keyword from shelve
#        py.exe mcb.pyw delete - delete all content from shelve

import pyperclip
import shelve
import sys
mcb_shelf = shelve.open('mcb')
if len(sys.argv) == 3:
    # Save clipboard content
    if sys.argv[1].lower() == 'save':
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    # Delete keyword from shelve
    elif sys.argv[1].lower() == 'delete':
        try:
            del(mcb_shelf[sys.argv[2]])
        except KeyError:
            print('"{}" does not exist'.format(sys.argv[2]))
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # Delete all content from shelve
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    # Loads keyword to clipboard
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
else:
    print('Wrong command.')
mcb_shelf.close()
