print("# Loop with Dictionaries")
student6 = {
    'name': 'raj',
    'age': 27,
    'location': 'dallas'
}
# for var in iterable:
#     code to execute in each loop
# in Dictionary default iteration returns only key, that is why variable you create is for key
for key in student6:
    print(f'element, by default key: {key}')
    print(f'value of the key: {student6[key]}')

print("Making the loop explicitly by keys with keys() function.")
for key in student6.keys():
    print(f'element, by default key: {key}')
    print(f'value of the key: {student6[key]}')

print("Looping through values only with values() function.")
for value in student6.values():
    print(f'value : {value}')

print("Looping through keys and values at the same time with items() function.")
for key, value in student6.items():
    print(f'key: {key}')
    print(f'value : {value}')

# H/W : 6-4, 6-5, 6-6
