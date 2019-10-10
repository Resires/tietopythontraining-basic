# Problem - Numbers filter
def strings_list_to_integers_list(strings_list_from_user, filter_range):
    """Using list comprehensions write a function that casts list of strings to list of integers and
    filters numbers within supplied range. Example data:
    list_of_strings = ['2', '0', '8', '3']
    to_filter_range = range(3)
    expected_output = [8, 3]
    """
    integers_list_for_user = []
    for element in strings_list_from_user:
        integers_list_for_user.append(int(element))
    for i in filter_range:
        while i in integers_list_for_user:      # The same item can exist multiple times
            integers_list_for_user.remove(i)
    return integers_list_for_user


if __name__ == '__main__':
    list_of_strings = ['2', '0', '8', '3', '2']
    to_filter_range = range(3)
    # expected_output = [8, 3]
    print(strings_list_to_integers_list(list_of_strings, to_filter_range))
