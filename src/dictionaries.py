# 4/22/2023  Dictionary - data structure, each element key (word, column, field) and value (definition, value in DB)
# each element is key-value pair, key is unique
# known with { }, key and value are separated by ':'
# Dictionaries in Java : HashMap, HashSet, HashTable

students_dictionary = {
    'student1': ['john', 23, 'tampa'],
    'student2': [['jane', 'doe'], 29, 'brooklyn'],
    'student3': ['david', 25, 'jersey city'],
    'student5': ['david', 25, 'jersey city']
}

student4 = {'name': 'raj', 'age': 27, 'location': 'dallas'}

# multidimensional list (list in a list), NESTED LIST
students_list = [
    ['john', 23, 'tampa'],
    [
        ['jane', 'doe'],
        29,
        'brooklyn'
    ],
    ['david', 25, 'jersey city'],
    ['david', 25, 'jersey city'],
    ['raj', 27, 'dallas'],
]

# newlist = students[1]    # ['jane', 29, 'brooklyn']
print('information of jane, name: ', students_list[1][0][0])
print('information of jane, lastname: ', students_list[1][0][1])

customers = [
    {'customerid': 'aaaa', 'companyname': 'level up'},
    {'customerid': 'aaab', 'companyname': 'level up'},
    {'customerid': 'aaac', 'companyname': 'level up'}
]


print("#################################################")

print("# CRUD with Dictionaries")

student7 = {}
student8 = dict()
student6 = {'name': 'raj', 'age': 27, 'location': 'dallas'}

print("# Read - how to access the elements, values of the dictionary _________")
print(student6)
print(f"name of the student6: {student6['name'].title()}")
print(f"age of the student6: {student6['age']}")
print(f"location of the student6: {student6['location'].upper()}")

print("Update - modifying the dictionaries -----------------------")
student6['age'] = 30
print(f"After updating the age of the student6: {student6}")
print("Update - adding new element to a dictionary")
student6['last_name'] = 'patel'
print(f"After adding new key-value pair to the student6: {student6}")
student6.setdefault('last_name2', 'doe')
print(f"After setdefault new key-value pair to the student6: {student6}")

print("Delete - removing the elements from the dictionary.")
del student6['last_name']
print(f"After deleting  key-value pair from student6: {student6}")

# H/W on Problem-solving:
# 1. given string input count how many vowels used in the string. (e, a, i, o, u)
    # hello -> 2 (count)
    # count = 0
# 2. given string input count how many times each letter is used. Ignore whitespace(spaces, tabs, enters)
    # helloe -> result={'h':1, 'e':1, 'l':2, 'o':1}
    # loop through input
    # result.setdefault('o', 1)
    # result['o'] = result['o'] + 1
for letter in 'hello':
    print(letter)

