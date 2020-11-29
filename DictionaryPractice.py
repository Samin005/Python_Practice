customer = {
    'name': 'Samin Azhan',
    'age': 26,
    'is_verified': True
}
print(customer['name'])
print(customer.get('name'))
# print(customer['Name'])  # will give an error if 'Name' does not exist in dictionary
print(customer.get('Name'))  # will return None if 'Name' does not exist in dictionary
print(customer.get('Name', 'Default Name'))  # can also return default value
print(customer.get('AGE', 30))

# can add new key value pairs
customer['birth_year'] = 1994
print(customer.values())
print(customer)

# problem 1
# input:
# a: 100, b: 100, c: 200, d: 300
# a: 300, b: 200, d: 400, e: 200
user_input_1 = input().split(', ')
user_input_2 = input().split(', ')
output_dictionary = {}
for item in user_input_1:
    key = item.split(':')[0]
    value = int(item.split(': ')[1])
    output_dictionary[key] = value
for item in user_input_2:
    key = item.split(':')[0]
    value = int(item.split(': ')[1])
    if output_dictionary.get(key) is not None:
        output_dictionary[key] = output_dictionary.get(key) + value
    else:
        output_dictionary[key] = value
print(output_dictionary)
values_list = []
for item in output_dictionary.values():
    if item not in values_list:
        values_list.append(item)
values_list.sort()
print(tuple(values_list))

# problem 2
# input:
# 10
# 20
# 20
# 30
# 10
# 50
# 90
# STOP
output_dictionary = {}
user_input = input()
while user_input != "STOP":
    if user_input not in output_dictionary:
        output_dictionary[user_input] = 1
    else:
        output_dictionary[user_input] = output_dictionary.get(user_input) + 1
    user_input = input()
for item in output_dictionary:
    print(item, "-", output_dictionary.get(item), "times")
