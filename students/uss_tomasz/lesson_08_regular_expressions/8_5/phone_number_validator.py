import re


def is_phone_number(number):
    phone_regex = re.compile(r'''(
        (\+\d{2}\s)?
        (
        \d{3}
        [\s-]?
        \d{3}
        [\s-]?
        \d{3}
        )
        )''', re.VERBOSE)
    results = re.findall(phone_regex, number)
    if len(results) == 0:
        return False
    else:
        return True


numbers = ['12345678', '123456789',
           '1234 567 89', '123 456 789',
           '1234-56789', '123-456-789',
           '+48 123456789', '+48 123 456 789', '+48 123-456-789']

for number in numbers:
    if is_phone_number(number):
        print(number, 'is CORRECT phone number')
    else:
        print(number, 'is WRONG phone number')
