import re


def is_password_strong(password):
    length_regex = re.compile(r'[a-zA-Z0-9]{8,}')
    if len(re.findall(length_regex, password)) == 0:
        return False
    lowercase_regex = re.compile(r'[a-z]')
    if len(re.findall(lowercase_regex, password)) == 0:
        return False
    uppercase_regex = re.compile(r'[A-Z]')
    if len(re.findall(uppercase_regex, password)) == 0:
        return False
    digits_regex = re.compile(r'\d')
    if len(re.findall(digits_regex, password)) == 0:
        return False
    return True


print(is_password_strong('Admin11'))  # too short
print(is_password_strong('password'))  # only small letters
print(is_password_strong('password1'))  # only small letters and digits
print(is_password_strong('Password1'))  # strong password