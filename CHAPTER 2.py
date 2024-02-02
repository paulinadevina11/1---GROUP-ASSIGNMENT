#2.1 SIMPLE MESSAGE
msg = "I love learning to use Python."
print(msg)

#2.3 PERSONAL MESSAGE
name = "eric"
msg = f"Hello {name.title()}, would you like to learn some Python today?"
print(msg)

#2.4 NAME CASES
name = "eric"

print(name.lower())
print(name.upper())
print(name.title())

#2.5 FAMOUS QUOTE
print('Albert Einstein once said, "A person who never made a mistake')
print('never tried anything new."')

#2.7 STRIPPING NAMES
name = "\tEric Matthes\n"

print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())

#2.8 FILE EXTENSIONS
filename = 'python_notes.txt'
simple_filename = filename.removesuffix('.txt')

print(simple_filename)

#2.10 FAVORITE NUMBER
fav_num = 42
msg = f"My favorite number is {fav_num}."

print(msg)