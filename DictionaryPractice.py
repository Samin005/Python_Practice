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
