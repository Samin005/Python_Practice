secret_number = 6
guess_used = 0
guess_limit = 3
print('Guess a number between 0 to 9!')
while guess_used < guess_limit:
    input_number = int(input('Enter Number: '))
    guess_used += 1
    if input_number is secret_number:
        print('You guessed right!')
        break
    elif secret_number > input_number:
        print(f'The number is greater than {input_number}')
    elif secret_number < input_number:
        print(f'The number is less than {input_number}')
else:
    print("Sorry, you've failed.")
