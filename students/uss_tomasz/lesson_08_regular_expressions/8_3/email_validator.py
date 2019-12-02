# write email validator that checks if supplied string is valid e-mail address
import re
EMAIL_REGEX = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  
    @
    [a-zA-Z0-9.-]+  
    .
    \.[a-zA-Z]{2,4}
    )''', re.VERBOSE)


def is_email(user_email):
    return re.match(EMAIL_REGEX, user_email) is not None


print(is_email('$@gmail.com'))
print(is_email('tomo@$.com'))
print(is_email('tomo@gmail.com'))
