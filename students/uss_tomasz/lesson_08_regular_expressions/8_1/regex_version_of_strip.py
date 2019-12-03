import re


def alternative_strip(user_message, characters=r"\s*"):
    regex_beginning_string = r'(^([' + characters + r']*))'
    stripping_regex = re.compile(regex_beginning_string, re.VERBOSE)
    user_message = re.sub(stripping_regex, '', user_message)
    regex_ending_string = r'(([' + characters + r']*)$)'
    stripping_regex = re.compile(regex_ending_string, re.VERBOSE)
    user_message = re.sub(stripping_regex, '', user_message)
    return user_message


message = 'this should be stripped --- this will remain --- this should be stripped'
print("                   Original message =", message, '<<END>>')
print("      Original strip with arguments =", message.strip('thishouldbestriped '), '<<END>>')
print("   Alternative strip with arguments =", alternative_strip(message, 'thishouldbestriped '), '<<END>>')
message = '         --- this will remain ---             '
print("                   Original message =", message, '<<END>>')
print("   Original strip without arguments =", message.strip(), '<<END>>')
print("Alternative strip without arguments =", alternative_strip(message), '<<END>>')
