# using only str.replace method and emoji_dictionary loop, this is efficient if the emoji dictionary is small
def emoji_converter_str_replace(user_input):
    for emoji in emoji_dictionary:
        user_input = user_input.replace(emoji, emoji_dictionary.get(emoji))
    return user_input


# using str.split method and split str loop, this is efficient if the emoji dictionary is very large
def emoji_converter_str_split(user_input):
    words = user_input.split(' ')
    output = ''
    for word in words:
        output += emoji_dictionary.get(word, word) + ' '
    return output


emoji_dictionary = {
    ':)': '😊',
    ':(': '🙁'
}

input_message = input('Welcome to Emoji Converter! Type "exit" to terminate. \n>')
while input_message != 'exit':
    print(emoji_converter_str_replace(input_message))
    # print(emoji_converter_str_split(input_message))
    input_message = input('> ')
print('Application terminated.')
