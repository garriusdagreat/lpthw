# from the sys module, import argv function
# modules aka libraries contain many different functions used in different fields
from sys import argv
# argv is the argument variable which holds arguments to pass to Python
# when the script is run

# the variable below holds the arguments contained by argv
script, first, second, third, fourth = argv
# the variable above can be split into separate arguments
print("This script is called", script) # name of script
print("Your first variable is:", first) # first variable
print("Your second variable is:", second) # second variable
print("Your third variable is:", third) # third variable
print("Your fourth variable is:", fourth) # and so on...

# Traceback (most recent call last):
#   File "C:\Users\garri.DESKTOP-CBUKV0L\lpthw\ex13.py", line 2, in <module>
#     script, first, second, third = argv
# ValueError: not enough values to unpack (expected 4, got 3)

# ValueError occurs when not enough variables are defined (see above)
# or too many variables are defined (see below)

# Traceback (most recent call last):
#   File "C:\Users\garri.DESKTOP-CBUKV0L\lpthw\ex13.py", line 2, in <module>
#     script, first, second, third, fourth = argv
# ValueError: too many values to unpack (expected 5)
