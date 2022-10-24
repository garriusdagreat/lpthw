from sys import argv

script, filename = argv # get filename

txt = open(filename) # run 'python -m pydoc open' for more info

print(f"Here's your {filename}:")
print(txt.read()) # reads the content of the file in filename

print(f"Type the filename again:")
file_again = input("> ") # type in filename again

txt_again = open(file_again) # open the input() from variable file_again

print(txt_again.read()) # reads the contents of variable txt_again

### ERRORS ###
# Traceback (most recent call last):
#   File "C:\Users\garri.DESKTOP-CBUKV0L\lpthw\ex15.py", line 13, in <module>
#     txt_again = open(file_again) # open the input() from variable file_again
# FileNotFoundError: [Errno 2] No such file or directory: 'easd'
# PS C:\Users\garri.DESKTOP-CBUKV0L\lpthw> python ex15.py

# Error for line 11 if trying to input a filename which does not exist

# Traceback (most recent call last):
#   File "C:\Users\garri.DESKTOP-CBUKV0L\lpthw\ex15.py", line 3, in <module>
#     script, filename = argv # get filename
# ValueError: not enough values to unpack (expected 2, got 1)

# Error if argv function is called without enough values
