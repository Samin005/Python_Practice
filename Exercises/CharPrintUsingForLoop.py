char_codes = [5, 2, 4, 2, 2]  # F
# using nested loops
for code in char_codes:
    output = ''
    for num in range(code):
        output += '*'
    print(output)

# A simpler solution
# for code in char_codes:
#     print('*' * code)
