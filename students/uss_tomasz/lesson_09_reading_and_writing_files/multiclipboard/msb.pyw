# msb.pyw - saves and loads pieces of text to the clipboard.
# usage: py.exe msb.pyw save <keyword> - saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - loads keyword to clipboard.
#        py.exe mcb.pyw list - loads all keywords to clipboard.
#        py.exe mcb.pyw delete <keyword> - delete keyword from shelve
#        py.exe mcb.pyw delete - delete all content from shelve

import pyperclip
import shelve
import sys

if len(sys.argv) < 2:
    print('Missing command')
    sys.exit(1)
mcb_shelf = shelve.open('mcb')
command = sys.argv[1].lower()
if command == 'save':
    if len(sys.argv) == 2:
        print('Missing keyword for saving')
    elif len(sys.argv) == 3:
        # Save clipboard content
        mcb_shelf[sys.argv[2]] = pyperclip.paste()
    else:
        print('Too much input arguments')
elif command == 'delete':
    if len(sys.argv) == 2:
        # Delete all content from shelve
        mcb_shelf.clear()
    elif len(sys.argv) == 3:
        # Delete keyword from shelve
        try:
            del (mcb_shelf[sys.argv[2]])
        except KeyError:
            print('"{}" does not exist'.format(sys.argv[2]))
    else:
        print('Too much input arguments')
elif command == 'list':
    # List keywords and load content
    pyperclip.copy(str(list(mcb_shelf.keys())))
elif sys.argv[1] in mcb_shelf:
    # Loads keyword to clipboard
    pyperclip.copy(mcb_shelf[sys.argv[1]])
else:
    print("Unknown command")
mcb_shelf.close()
