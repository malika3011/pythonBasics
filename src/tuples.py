# 4/20/2023
# The same nature as list, but with parenthesis (not square brackets)
# immutable: in Tuples elements can not be updated, elements can not be deleted
# lists are mutable data structure, tuples are immutable data structure.

coordinatesL = [456, 3455]
coordinatesT = (456, 6577)
coordinatesL.append(7895)
print(coordinatesL)
print('List : coordinatesL[0]: ', coordinatesL[0])
print('Tuple : coordinatesT[0]: ',coordinatesT[0])
coordinatesL[0] = 789
# coordinatesT[0] = 789 # TypeError: 'tuple' object does not support item assignment
print('After, List : coordinatesL[0]: ', coordinatesL[0])
print('After, Tuple : coordinatesT[0]: ',coordinatesT[0])
print('now we are resetting the whole value of the variable to a different tuple ...')
coordinatesT = (789, 6577)
print('After, Tuple : coordinatesT[0]: ',coordinatesT[0])
