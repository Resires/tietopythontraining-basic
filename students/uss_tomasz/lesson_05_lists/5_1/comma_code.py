def list_to_string(input_list):
    """ This function takes a list value as an argument and returns a string with all the items separated by a comma
    and a space, with word 'and' insterted before the last item. Example:
    Input = ['apples', 'bananas', 'tofu', 'cats']
    Output = 'apples, bananas, tofu, and cats'
    """
    output_string = ''
    for index, item in enumerate(input_list):
        output_string += str(item)
        if index < len(input_list) - 2:
            output_string += ', '
        elif index == len(input_list) - 2:
            output_string += ' and '
    return output_string


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(list_to_string(spam))


