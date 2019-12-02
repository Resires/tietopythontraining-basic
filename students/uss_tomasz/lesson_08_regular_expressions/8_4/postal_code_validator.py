import re
POSTAL_REGEX = re.compile(r'\d\d-\d\d\d')


def is_postal_code(code):
    return re.match(POSTAL_REGEX, code) is not None


postal_codes = ['90-210', '90*210', '997-', '-666']
for postal_code in postal_codes:
    if is_postal_code(postal_code):
        print(postal_code, 'is CORRECT postal code')
    else:
        print(postal_code, 'is WRONG postal code')
