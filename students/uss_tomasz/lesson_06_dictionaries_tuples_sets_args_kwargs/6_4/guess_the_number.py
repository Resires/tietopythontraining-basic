AUGUSTUS_SECRET_NUMBER = 6
N = 10


def string_of_numbers_to_list_of_int(string_of_numbers):
    list_of_str = string_of_numbers.split()
    list_of_int = [int(i) for i in list_of_str]
    return list_of_int


remaining_numbers = set(range(1, N + 1))
while True:
    beatrice_guesses = input("Guess number from 1 to {}. Separate them with space character. "
                             "Or input 'HELP' for list of remaining numbers.".format(N))
    if beatrice_guesses == "HELP":
        print("Remaining numbers are:", remaining_numbers)
    else:
        list_of_int_guesses = string_of_numbers_to_list_of_int(beatrice_guesses)
        if AUGUSTUS_SECRET_NUMBER in list_of_int_guesses:
            print("Congratulations! The secret number was {}".format(AUGUSTUS_SECRET_NUMBER))
            break
        remaining_numbers -= set(list_of_int_guesses)
