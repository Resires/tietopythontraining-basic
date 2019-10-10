def list_to_string(list_from_user):
    """ This function takes a list value as an argument and returns a string with all the items separated by a comma
    and a space, with word 'and' insterted before the last item. Example:
    Input = ['apples', 'bananas', 'tofu', 'cats']
    Output = 'apples, bananas, tofu, and cats'
    """
    string_for_user = ''
    for index, item in enumerate(list_from_user):
        string_for_user += str(item)
        if index < len(list_from_user) - 2:
            string_for_user += ', '
        elif index == len(list_from_user) - 2:
            string_for_user += ' and '
    return string_for_user


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(list_to_string(spam))


