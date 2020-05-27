# A simple solution
def char_print():
    for code in char_codes:
        print('*' * code)


# using nested loops
def char_print_using_nested_loops():
    for code in char_codes:
        output = ''
        for num in range(code):
            output += '*'
        print(output)


char_codes = [5, 2, 4, 2, 2]  # F
# char_print()
char_print_using_nested_loops()
