# Problem - Numbers filter
def strings_list_to_integers_list(input_strings_list, filter_range):
    """Using list comprehensions write a function that casts list of strings to list of integers and
    filters numbers within supplied range. Example data:
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)
    expected_output = [8, 3]
    """
    return [int(i) for i in input_strings_list if int(i) not in list(filter_range)]


if __name__ == '__main__':
    list_of_strings = ['2', '0', '8', '3', '2']
    to_filter_range = range(3)
    # expected_output = [8, 3]
    print(strings_list_to_integers_list(list_of_strings, to_filter_range))
