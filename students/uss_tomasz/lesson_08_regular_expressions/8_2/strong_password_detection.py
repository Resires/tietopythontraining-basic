import re
PASSWORD_REGEX = re.compile(r'''
        (?=.*[A-Z]) # positive look ahead assertions
        (?=.*[0-9])
        (?=.*[a-z])
        .{8}
        ''', re.VERBOSE)


def is_password_strong(password):
    return re.match(PASSWORD_REGEX, password) is not None


print(is_password_strong('Admin11'))  # too short
print(is_password_strong('password'))  # only small letters
print(is_password_strong('password1'))  # only small letters and digits
print(is_password_strong('Password1'))  # strong password
print(is_password_strong('Password11'))  # also strong password (9 characters)
