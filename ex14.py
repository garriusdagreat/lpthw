from sys import argv
# script and user_name are defined at start of script
script, user_name = argv
# variable prompt displays '> '
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
# variable prompt can be called inside input() function
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.
""")
