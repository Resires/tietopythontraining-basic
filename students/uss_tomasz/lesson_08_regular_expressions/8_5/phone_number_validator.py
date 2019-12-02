import re
PHONE_REGEX = re.compile(r'''(
    (\+\d{2}\s)?
    (
    \d{3}
    [\s-]?
    \d{3}
    [\s-]?
    \d{3}
    )
    )''', re.VERBOSE)


def is_phone_number(number):
    return re.match(PHONE_REGEX, number) is not None


phone_numbers_list = ['12345678', '123456789',
                      '1234 567 89', '123 456 789',
                      '1234-56789', '123-456-789',
                      '+48 123456789', '+48 123 456 789', '+48 123-456-789']
for phone_number in phone_numbers_list:
    if is_phone_number(phone_number):
        print(phone_number, 'is CORRECT phone number')
    else:
        print(phone_number, 'is WRONG phone number')
