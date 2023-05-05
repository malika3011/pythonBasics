# Chapter 4 Looping: Iterative actions

magicians = ['alice', 'david', 'carolina']

# for each loop
for abc in magicians:  # new variable abc created, scope is for loop block
    print(f'magician: {abc}')
    print(abc, '--------------')
    print('helloo')
    # for a in x:
    #     print(a)

print(abc)  # out of scope, abc should be used only inside the loop not outside
print('byeeee')

# range(startingNumber, endingNumber, steps)
# NOTE: range does not return a list, you need to use list() functions
# to see the result in a list

# range(10, 20, 2) -> 10, 12, 14, 16, 18
# range(5) -> range(0, 5, 1) -> 0, 1, 2, 3, 4
# range(16, 21) -> range(16, 21, 1) -> 16, 17, 18, 19, 20

print("# Working with number with range() ------")
print(f'range(): {list(range(5))}')
print(f'# # using range in a loop -----------------------')
for num in range(16, 21):
    print(f'num : {num}')

print(f'********* completed **********')

# Exercise : create a list of squares of numbers from 101 to 110 (inclusive)
for num in range(101, 111):
    print(num * num)

squares = []
for num in range(101, 111):
    squares.append(num ** 2)
print(squares)

square_nums_list = []
for num in range(101, 110):
    square = num * num
    print(square)
    square_nums_list.append(square)

for num in range(101, 111):
    print(f'square of {num} is : {num * num}')

squares = []

for value in range(101, 111):
    square = value ** 2
    squares.append(square)
print(squares)

# list comprehension
squares = [value ** 2 for value in range(101, 111)]

# find the sum of numbers from 55 to 95 (inclusive)
# phsuedocode - steps in words not in syntax
total = 0
for num in range(55, 96):
    total = total + num   #  total += num
print(total)

# total = total + num  # total += num
# total -= num  # total = total - num
# total *= num  # total = total * num

print("# Slicing in the list: ---------------------------")
nums = [4, 23, 6, 0, -11, 4567, 1234]
print(nums[2:5])  # this includes indexes 2, 3, 4
print(nums[2:])  # this includes all indexes starting from index 2
print(nums[:5])  # this includes all indexes up to index 5 (not including 5)
print(nums[:])  # this includes all indexes up to index 5 (not including 5)
nums_2_5 = nums[2:5]
nums_2_end = nums[2:]
nums_start_5 = nums[:5]
nums_copy = nums[:]   # created new list (object) by copying the list
nums_copy2 = nums   # created additional reference to the same object
print(f"nums_copy: {nums_copy}")
print(f"nums_copy2: {nums_copy2}")
print(f"original nums: {nums}")
print("----------------------------------")
nums_copy.append(555)
nums.append(666)
nums_copy2.append(777)
print(f"nums_copy after change: {nums_copy}")
print(f"nums_copy2 after change: {nums_copy2}")
print(f"original nums after change: {nums}")

# H/W all exercises of chapter 4 (excluding Tuples section)
