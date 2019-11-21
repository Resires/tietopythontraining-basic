import re


def is_postal_code(code):
    postal_regex = re.compile(r'\d\d-\d\d\d')
    results = re.findall(postal_regex, code)
    if len(results) == 0:
        return False
    else:
        return True


postal_codes = ['90-210', '90*210', '997-', '-666']
for postal_code in postal_codes:
    if is_postal_code(postal_code):
        print(postal_code, 'is CORRECT postal code')
    else:
        print(postal_code, 'is WRONG postal code')
