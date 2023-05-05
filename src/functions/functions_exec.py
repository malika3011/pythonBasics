# Function execution file
# module, package, import
# ./src/functions/functions.py-> greet_user_by_name()
# from src.functions.functions import greet_user_by_name, greet_user, thank_you_by_name

# import line reads and executes the file
from src.functions.functions import greet_user_by_name, greet_user, thank_you_by_name
# You can use alias name for the imported function
from src.functions.functions import greet_user as greet
from src.functions.functions_return import *
# import src.functions.functions_return as function1
# you can use alias for modules, but you need to mention moduleAlias.functionName(), when you using function

print("# EXECUTION: ********")
greet_user_by_name('john')
greet_user()
greet_user_by_name('jane')
greet_user()
greet_user_by_name('britney')
thank_you_by_name('john', 10)
thank_you_by_name('jane', 5)
thank_you_by_name('britney', 20)
thank_you_by_name('mark', 1)
print('#EXECUTION:')
