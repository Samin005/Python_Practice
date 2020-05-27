# using list
def convert_in_words_using_list(input_num):
    in_words = ''
    for digit in input_num:
        if digit.isnumeric():
            in_words += in_words_digits[int(digit)] + ' '
        else:
            in_words += '? '
    return in_words


# using dictionary
def convert_in_words_using_dictionary(input_num):
    in_words = ''
    for digit in input_num:
        in_words += in_words_dictionary.get(digit, '?') + ' '
    return in_words


in_words_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
in_words_dictionary = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

input_number = input('Enter number: ')
# print(convert_in_words_using_list(input_number))
print(convert_in_words_using_dictionary(input_number))
