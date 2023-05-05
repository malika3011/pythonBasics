# Object - abstract data
# An object is simply a collection of data (variables) and methods (functions).

# Data Structures: list [v1,v2], tuple (v1,v2), set {v1,v2}, dictionary {k1:v1, k2:v2}
# We will learn followings for each data structure:
# difference than other DS,
# Operations: create, read, update, delete  (CRUD)
# Each DS has mostly used builtin functions

# list - list of values (similar data types) separating with comma
# list covered with square brackets -> [value1, value2 ... ]

print("# CREATE ******************************")
friends = []
nums = list()
my_info = ['jane', 'doe', 25, 'dubai', True, '04/15/1998']
cities = ['brooklyn', 'manhattan', 'los angeles']

print("my_info:", my_info)
print("cities:", cities)
print("friends:", friends)
print("nums:", nums)

print("# READ **********************************")
print(my_info[0]) # 'john'
print(f'First element of my_info list is: {my_info[0]}')  # 'john'
print(f'First element of my_info list is: {my_info[0].title()}')  # 'john'
print(f'The Last element of cities list is: {  cities[-1].title() }')  # los angeles
print(f'The Last element of cities list is: { cities[2].title() }')  # los angeles
print(f'{ my_info[0].title() } will be {   my_info[2] + 5   } years old in 5 years.')  # los angeles

print("### creating a list from user input ---------------")
# name = input('Enter your name: ')  # user inputs the value then that value will be saved as name='value'
# # age = int(input('enter your age: '))  # option 1
#
# # option 2: right side of the equal sign will be executed first and set as a new value to age variable
# age = input('enter your age: ')
# age = int(age)
#
# city = input('enter city you are reside: ')
# user_info = [name, age, city]
#
# print(f'User info: {user_info}')
# print(f'Name of the user: {user_info[0].title()}')
# print(f'Age of the user, 2 years ago: {user_info[1] - 2 }')
# print(f'Location of the user: {user_info[2].upper()}')

print("# UPDATE ************************************")
print('original list', cities)  # ['brooklyn', 'manhattan', 'los angeles']
print("# Inserting the elements to the list -----------")
cities.insert(1, 'houston')
print('updated list', cities)  # ['brooklyn', 'houston', 'manhattan', 'los angeles']
print('# updating the existing element value (setting new value to the element) -----------')
cities[2] = 'new york'
print('updated manhattan:', cities[2])  # ['brooklyn', 'houston', 'manhattan', 'los angeles']
print('# add new element to the end of the list (append) ----------')
cities.append('seattle')   # MOSTLY USED
print(f'new city added to the list: {cities}')
print(f'new city added to the list: {cities[-1]}')
print(f'new city added to the list: {cities[ len(cities) -1 ]}') # the same logic as above line

print('index of houston', cities.index('houston'))
print('counting the elements of cities list: ', len(cities))

print('# DELETE elements -----------------------')
print('original before deleting:', cities)  # ['brooklyn', 'houston', 'new york', 'los angeles', 'seattle']
del cities[0]  # just removes, only delete action
print('after deleting the first element with del', cities)  # ['houston', 'new york', 'los angeles', 'seattle']
deleted_city = cities.pop(2)  # Remove and return item at index (default last)
print('after deleting the element with pop()', cities)  # ['houston', 'new york', 'los angeles']
print("deleted_city:", deleted_city)

cities.append('new york')
print('before deleting with remove ', cities)
cities.remove('new york') # Remove first occurrence of value.
print('after deleting the new york with remove()', cities)  # ['houston', 'los angeles']

print('hello'.title())

# 04/16/2023
# table.column - using dot for parent child relationship
# string.functions() --> function actions on the string
# column vs row -> no parent child relationship

print("# Sorting in lists ---------------------------")
cars = ['lexus', 'bmw', 'toyota', 'tesla']
print(f'cars list: {cars}')
print("## temporary sorting of list with sorted() -----------")

print(f'sorted list with sorted(): {sorted(cars)}')
print(f' list after sorted(): {cars}')
print(f'sorted list with sorted(reverse=True): {sorted(cars, reverse=True)}')
print(f' list after sorted(): {cars}')
sorted_cars_asc = sorted(cars)
sorted_cars_desc = sorted(cars, reverse=True)
print(f'sorted_cars_asc: {sorted_cars_asc}')
print(f'sorted_cars_desc: {sorted_cars_desc}')

print("## permanent sorting of list with sort() -----------")
# cars.sort()  # permanent sorting by default in ascending order.
# print(f'sorted cars list with sort(): {cars}')
cars.sort(reverse=True)  # permanent sorting in descending order.
print(f'sorted cars list with sort(reverse=True): {cars}')
cars.append('honda')
print(f'cars after append: {cars}')

# problem-solving question: you have huge list of integers,
# how you can find smallest and largest number
nums = [4, 23, 6, 0, -11, 4567, 1234]
# solution 1
nums.sort()
smallest_num = nums[0]
largest_num = nums[-1]
# solution 2
smallest_num2 = sorted(nums)[0]
largest_num2 = sorted(nums)[-1]

print("# reversing the list with reverse() ---------------------")
nums2 = [3, 5, 1, 0, -55, 100]
print(f'original list : {nums2}')
nums2.reverse()
print(f'reversed list : {nums2}')

# IndentationError, SyntaxError, TypeError, IndexError, NameError
# Avoiding Index Errors When Working with Lists
# IndexError: list index out of range
print(f'out of range index nums2[6]: {nums2[6]}')

