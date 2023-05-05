# 4/23/2023 Chapter 7: While Loop
# while loop - looping with conditions
# Note: you need to increment/decrement or make sure there is ending condition for the while loop

total = 0  # total < boundary value in a while loop
while total <= 5:
    # here is the code to execute when expression returns True
    print(total)
    # total = total + 1
    total += 1

print("********* starting second loop ******")
total = 10  # while loop should have lower boundary
while total >= 5:
    # here is the code to execute when expression returns True
    print(total)
    total -= 1

# num = 0
# while num != -1:
#     num = int(input('enter the number: ').strip())
#     print(f'square of the number is: {num**2}')

msg = ''
while msg.lower() != 'exit' and msg.upper() != 'X' and msg.lower() != 'no':
    msg = input('enter your name: ').strip()
    if msg == '':
        print('whitespace characters were entered ...')
        # continue # go to next iteration, ignore next lines in this iteration
        break  # stop the loop, ignore next lines in this iteration
    print(f'Hi {msg.title()}, have a wonderful day!!')

# how to find a number from the list of numbers and exit the loop when you find.
print(' ********** conditions with empty list and dictionary ********')
names = [2]
friends = {'a': 1}

while friends and names:
    print('data structure is not empty')
    # if you put just data structure name as condition, it returns true if not empty, otherwise it returns False
    names = []
    friends = {}

if not 0:
    print('returned True')
else:
    print('zero returns false, so this line is being executed...')

print('**** completed *****')
# H/W 7-8, 7-9, 7-10
