# using list
in_words_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
input_num = input('Enter number: ')
in_words = ''
for digit in input_num:
    if digit.isnumeric():
        in_words += in_words_digits[int(digit)] + ' '
    else:
        in_words += '? '
print(in_words)

# using dictionary
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
input_num = input('Enter number: ')
in_words = ''
for digit in input_num:
    in_words += in_words_dictionary.get(digit, '?') + ' '
print(in_words)
