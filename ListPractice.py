course_name = 'Python for Beginners'
print(course_name[-1])
print(course_name[0:5])
print(course_name[5:])
print(course_name[:6])
print(course_name[-9:-1])
if 'Python' in course_name:
    print('Course Contains Python!')
else:
    print('No Python')

temp_list_int = [1, 2, 9, [3, 4], 5]
print(temp_list_int[-2])
print(temp_list_int[2:])
print(len(temp_list_int))
if [3, 4] in temp_list_int:
    print('Contains nested list!')

# tuples
# tuple_int = (1, 4, 7)  # tuples are list that cannot be modified, so the are immutable

# unpacking (works for both lists and tuples)
numbers = [1, 9, 5]
x, y, z = numbers
print(y)

# list methods
list_string = ['a', 'b', 'e', 'j']
print(list_string)
list_string.append('h')
print("Appended 'h' : ", list_string)
list_string.remove('b')
print("Removed 'b' : ", list_string)
list_string.insert(2, 'a')
print("Inserted 'a' at index 2: ", list_string)
a_count = list_string.count('a')
print("Total 'a's in list: ", a_count, '!')
print(f"Total 'a's in list: {a_count}!")
e_index = list_string.index('e')
print(f"index of 'e': {e_index}")
x_exists = 'x' in list_string
print(f"'x' exists in list: {x_exists}")
list_string.sort()
print('After sorting list:', list_string)
list_string.reverse()
print('After reversing list:', list_string)
# another_list = list_string  # points to the same list, all changes will affect both lists
another_list = list_string.copy()
list_string.clear()
print('After clearing list:', list_string)
print('The other list:', another_list)


# removing duplicates from a list
temp_list = [1, 2, 3, 1, 5, 1, 9, 5, 4, 3]
for num in temp_list:
    num_count = temp_list.count(num)
    while num_count > 1:
        temp_list.remove(num)
        num_count = temp_list.count(num)
print(temp_list)

# A better solution:
temp_list = [1, 2, 3, 1, 5, 1, 9, 5, 4, 3]
no_duplicates = []
for num in temp_list:
    if num not in no_duplicates:
        no_duplicates.append(num)
print(no_duplicates)

# # for loops
# print('--- For Loop ---')
# nums = [2, 5, 98, 56]
# for num in nums:
#     print(num)
# print('------')
#
# # for num in range(5)  # this will print 0 to 4
# starting_num = 5
# ending_num = 10
# for num in range(starting_num, ending_num):
#     print(num)
# print('------')
#
# step = 2
# for num in range(starting_num, ending_num, step):
#     print(num)
# print('------')
#
# # while loops
# print('--- While Loop ---')
# counter = 4
# while counter < 7:
#     print('counter:', counter)
#     counter += 1
# print('------')
#
# counter = 5
# break_number = 10  # if set to 12 or above, it will not break and reach else
# while counter < 12:
#     if counter is break_number:
#         print(f"Counter is now {break_number}, so exiting loop.")
#         break
#     counter += 1
# else:
#     print('Loop completed without break with counter:', counter)
