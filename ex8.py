# formatter string takes in four arguments represented by the number of {}
formatter = "{} {} {} {}"
# call .format() function and insert four arguments (less than 4 causes error)
## separate each argument with , or else error
### arguments can be any value or string or even variable
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "A world of dew,",
    "And within every dewdrop",
    "A world of struggle.",
    "-Kobayashi Issa ('A World of Dew')"
))
