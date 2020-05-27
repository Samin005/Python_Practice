name = 'Samin Azhan'
nickname = "Fariel"
print(nickname.upper())
print(name.title())  # first letter of every word will be upper case
print(name.replace('Samin', 'S.'))
message = name + ' (' + nickname + ') is a programmer'
print(message)

# formatted string
formatted_message = f'{name} ({nickname}) is a programmer'
print(formatted_message)
