ASCII_SPACING = ord('a') - ord('A')


def capitalize(lower_case_word):
    if not isinstance(lower_case_word, str):
        return None
    else:
        if len(lower_case_word) == 0:
            return ''
        else:
            first_letter_code = ord(lower_case_word[0])
            if first_letter_code > ord('Z'):
                first_letter_code -= ASCII_SPACING
            capitalized_word = chr(first_letter_code) + lower_case_word[1:]
            return capitalized_word


if __name__ == '__main__':
    print(capitalize('Example'))
    print(capitalize('example'))
