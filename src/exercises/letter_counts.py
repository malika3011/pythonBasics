# H/W on Problem-solving:
# Problem 1. given string input count how many vowels used in the string. (e, a, i, o, u)
# hello -> 2 (count)
# count = 0

# HW2 1. given string input count how many vowels used in the string. (e, a, i, o, u)
input_text = input('enter any word: ').lower()
vowel_count = 0
for letter in input_text:
    # if letter == 'a' or letter == 'e' or letter == 'o' or letter == 'u' or letter == 'i':
    if letter in 'aeoui':
        vowel_count += 1
print(f'number of vowels are: {vowel_count}')


print("****** Approach 2 *********")
sentence = input('enter the sentence:')
string = sentence.lower()
print(string)
count = 0
vowels = ["a", "e", "i", "o", "u"]
for char in string:
    if char in vowels:
        count = count + 1  # or  count +=1
print("number vowels in given sentence is:", count)

# Problem 2. given string input count how many times each letter is used. Ignore whitespace(spaces, tabs, enters)
# helloe -> result={'h':1, 'e':1, 'l':2, 'o':1}
# loop through input
# result.setdefault('o', 1)
# result['o'] = result['o'] + 1
# for letter in 'hello':
#     print(letter)

# msg = ''
# while msg.lower() != 'exit' and msg.upper() != 'X' and msg.lower() != 'no':
#     msg = input('enter your name: ').strip()
#     if msg == '':
#         print('whitespace characters were entered ...')
#         # continue # go to next iteration, ignore next lines in this iteration
#         break  # stop the loop, ignore next lines in this iteration
#     print(f'Hi {msg.title()}, have a wonderful day!!')
