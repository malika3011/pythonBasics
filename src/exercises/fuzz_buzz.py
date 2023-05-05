# H/W: FuzzBuzz ./fuzz_buzz.py
# create condition that prints 'Fuzz' if number is dividable by 3,
# returns 'Buzz' if number is dividable by 5, returns 'FuzzBuzz' if the number dividable by 15

# Sample inputs/outputs:
# num = 3  # output 'Fuzz' -> True/False -> Pass/Fail
# num = 27  # output 'Fuzz' -> Pass/Fail
# num = 10  # output 'Buzz' -> Pass/Fail
# num = 30  # output 'FuzzBuzz' -> Pass/Fail
# num = 45  # output 'FuzzBuzz' -> Pass/Fail
# num = 100  # output 'Buzz' -> Pass/Fail
# num = 0  # output 'Not Valid Entry', for any input less than 3 -> Pass/Fail
# num = 'a'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = ''  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail
# num = '\t'  # output 'Not Valid Entry', for any input other than integer -> Pass/Fail

# H/W
# for num in range(1, 21):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fuzz"  # string=Fuzz
#     if num % 5 == 0:
#         string = string + "Buzz"  # sting=FuzzBuzz
#     if num % 5 != 0 and num % 3 != 0:
#         string = string + str(num)  # string = '' + 1 = 1
#     print(string)
# print('-------------------------------')

def fizz_buzz(num):
    string = ""
    if num % 3 == 0:
        string = string + "Fuzz"  # string=Fuzz
    if num % 5 == 0:
        string = string + "Buzz"  # sting=FuzzBuzz
    if num % 5 != 0 and num % 3 != 0:
        string = string + str(num)  # string = '' + 1 = 1
    return string


print(fizz_buzz(15) == 'FuzzBuzz')  # comparison of function result and string 'FuzzBuzz'
print(fizz_buzz(3) == 'Fuzz')
print(fizz_buzz(45) == 'FuzzBuzz')
print(fizz_buzz(5) == 'Buzz')
# print(fizz_buzz('a') == 'Not Valid Entry') # special cases were not handled in the solution
# assert is builtin python statement that verifies the actual result with expected, if matches it goes next line
# if fails (expression returns false) code execution stops at that line, and you get AssertError
assert fizz_buzz(15) == 'FuzzBuzz', f'fizz_buzz(15) failed, please check this case.'

print('assert is executed')

print('***********************************')


def fuzz_buzz(num):
    result = ''
    # num.isalpha() # return True if num is alphabetic character, works for string only
    if num == 0 or not isinstance(num, int):  # true or false -> true
    # if num == 0 or not num.isnumeric():  # true or false -> true
        result = f'you entered "{num}", Not Valid Entry'
    elif num % 5 == 0 and num % 3 == 0:  # true and true -> true ; true and false -> false
        result = 'FuzzBuzz'
    elif num % 3 == 0:
        result = 'Fuzz'
    elif num % 5 == 0:
        result = 'Buzz'
    else:
        result = f'you entered "{num}".not dividable by 3 or 5'
    return result


print(fuzz_buzz('hjk'))
result_for_a = fuzz_buzz('a')
print('Not Valid Entry' in fuzz_buzz('a'))  # checking if 'Not Valid Entry' is part of the returned string
assert ('Not Valid Entry' in fuzz_buzz('a'))  # checking if 'Not Valid Entry' is part of the returned string

fuzz_buzz('')
fuzz_buzz('\t')
fuzz_buzz('0')
fuzz_buzz(45)

print(f'value of the variable: {result_for_a}')
print("############################################")


# values = input('enter value:')
def fuzz_buzz_2(values):
    if (values >= 'a' and values <= 'z') or (values >= 'A' and values <= 'Z') or values.strip() == '' or int(
            values) < 3:
        print('not valid entry')
    elif int(values) == 0:
        print('not valid entry')
    elif int(values) % 15 == 0:
        print('FuzzBuzz')
    elif int(values) % 3 == 0:
        print('Fuzz')
    elif int(values) % 5 == 0:
        print('Buzz')
    else:
        print(f'entered {values}')


fuzz_buzz_2('aa')  # since this is just printing you need validate visually from STDOUT (Run tab)
# print(fuzz_buzz_2('aa') == 'not valid entry')  # will work if you update function with return statement
