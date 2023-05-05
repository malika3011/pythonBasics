print("======= Variables ==========")

# print is the function that returns you what you have passed to the function
# use singe or double quote to enter the text
print('asldjalsdj`f')
print("asldja'lsdj`f")
print('asldja"lsdj`f')
print(4567)
print(45 + 4588)
print(45 * 4588)
# this is the comment line( not executable line)
# IndentationError: unexpected indent , remove spaces in the beginning of the line

# values covered with quotes (' ', "") considered as String data type
# Variables: container to hold the value
age = 10  # declaring the variable 'a', defining variable (set a value 10)
# ...
print(age)

print(age)
age = 15  # resetting the value of the variable
print(age)
# NOTEs for using the variables:
# best practice: name your variable with meaningful name
# rule: you can not start variable name with number, name must start with letter
# rule: no space in variable name, instead you can '_' -> my_friend
# rule: start with lower case and use lowercase letters

# printing multiple values with print function
print(23, 242, 23, 'hello', True)

my_name = 'jameS broWn'  # string value, text data type
my_age = 20  # integer value, numbers
am_i_cool = True  # boolean data type, True/False
first_name = 'janE    '
last_name = '    dOE'
full_name = (first_name.strip() + ' ' + last_name.strip()).title()
print("-----------------------------")
print('Hello, my name is', my_name)
print('thank you, this was', my_name, 'speaking with you tonight.')
print('if you have a comments please address it to', my_name)
print('I am', my_age, 'years old')
print('I will be', my_age + 5, 'years old in 5 years.')

print('------- string variables: built-in functions  -----------')
print('upper()-convert to upper case, lower()-lower case, title()-title each word')
print('Hello, my name is', my_name.upper())
print('thank you, this was', my_name.title(), 'speaking with you tonight.')
print('if you have a comments please address it to', my_name.lower())
print('Full name (concatenate):', first_name.title() + ' ' + last_name.title())
print('Full name (concatenate):', (first_name + ' ' + last_name).title())
print('Full name (concatenate):', full_name)

print('------- Number variables: built-in operations  -----------')
print('my age is:', my_age)
print('division:', my_age / 5)
print('multiplication:', my_age * 5)
print('floor division:', my_age // 3)  # f: 20/3 = 3 * f + r =  3 * 6 + 2 => 6 (how many 3s in 20)
print('modulo: ', my_age % 3)  # r: 20/3 = 3 * 6 + 2 => 2 (remainder when you divide 20 to 3)

class1 = 56
# H/W: chapter 2: Exercises 2.8, 2.9
