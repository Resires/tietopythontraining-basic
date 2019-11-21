# write email validator that checks if supplied string is valid e-mail address
import re


def is_email(user_email):
    email_regex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+  
        @
        [a-zA-Z0-9.-]+  
        .
        \.[a-zA-Z]{2,4}
        )''', re.VERBOSE)
    result = re.findall(email_regex, user_email)
    if len(result) == 0:
        return False
    else:
        return True


print(is_email('$@gmail.com'))
print(is_email('tomo@$.com'))
print(is_email('tomo@gmail.com'))
