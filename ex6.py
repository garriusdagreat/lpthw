# two variables: types_of_people, x
# variables can contain any value or string or boolean (words/strings)
types_of_people = 10
x = f"There are {types_of_people} types of people." # 1 string inside string (SIS)
# three variables: binary, do_not, y
binary = "binary"
do_not = "don't"
y = f"Those know {binary} and those who {do_not}." # 2 SIS
# print statement for above variables
print(x)
print(y)
# repeat above but with extra strings
print(f"I said: {x}") # 3 SIS
print(f"I also said: '{y}'") # 4 SIS
# two variables: hilarious, joke_evaluation
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
# print statement with fstring (.format(variable))
print(joke_evaluation.format(hilarious))
# two new variable containing strings: w, e
w = "This is the left side of..."
e = "a string with a right side."
# print statement for above two variables
print(w + e)
