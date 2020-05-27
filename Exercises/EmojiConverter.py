emoji_dictionary = {
    ':)': '😊',
    ':(': '☹'
}

# using only str.replace method and emoji_dictionary loop, this is efficient if the emoji dictionary is small
input_message = input('Welcome to Emoji Converter! Type "exit" to terminate. \n>')
while input_message != 'exit':
    for emoji in emoji_dictionary:
        input_message = input_message.replace(emoji, emoji_dictionary.get(emoji))
    print(input_message)
    input_message = input('> ')
print('Application terminated.')

# using str.split method and split str loop, this is efficient if the emoji dictionary is very large
# input_message = input('Welcome to Emoji Converter! Type "exit" to terminate. \n>')
# words = input_message.split(' ')
# while input_message != 'exit':
#     output = ''
#     for word in words:
#         output += emoji_dictionary.get(word, word) + ' '
#     print(output)
#     input_message = input('> ')
#     words = input_message.split(' ')
# print('Application terminated.')
