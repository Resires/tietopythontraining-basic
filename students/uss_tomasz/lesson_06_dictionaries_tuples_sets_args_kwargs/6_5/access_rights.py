FILES = {'file1': {'w', 'r', 'x'},
         'file2': {'w'},
         'file3': {},
         'file4': {'r', 'x'}}
OPERATIONS_TO_PERFORM_ON_FILES = [('file1', 'w'),
                                  ('file1', 'x'),
                                  ('file2', 'r'),
                                  ('file3', 'w'),
                                  ('file4', 'x')]
for operation in OPERATIONS_TO_PERFORM_ON_FILES:
    print("There is request for", operation[0], "for the operation type", operation[1])
    print("This file contains following access:", FILES[operation[0]])
    if operation[1] in FILES[operation[0]]:
        print("Access granted")
    else:
        print("Access denied")
    print()
