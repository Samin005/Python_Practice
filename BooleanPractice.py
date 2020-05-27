temp = True and 1
print(temp)
if temp:
    print('true')
else:
    print('false')

temp = not None or 1
print(temp)

num = 5
print(1 < num < 10)

num1 = 3
num2 = 3.0
print(num1 is num2)

numbers = [1, 3, 4, 7]
print(3 in numbers)

num = 6
is_float = False
if num > 5 and not is_float:
    result = 'Greater!'
else:
    result = 'Less'
print(result)

num = 5
num2 = 3
if num == 3:
    result = 'three!'
elif num is num2:
    result = 'not three'
else:
    result = 'something else'
print(result)
