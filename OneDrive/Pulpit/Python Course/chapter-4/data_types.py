import math

# String data type

# Literal assignemnt
first = "Emilia"
last = "Kożuch"

# print(type(first))
# print(type(first) == str)
# print(isinstance(last, str))

# constructor function
# pizza = str("Pepperoni")
# print(pizza)
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatination
fullname = first + " " + last
# print(fullname)
fullname += " <3"
# print(fullname)

# Casting a number to a string
decade = str(2020)
# print(decade)
# print(isinstance(decade, int))

statement = "I like metal music from the " + decade + "s."
# print(statement)

# Multiple lines
multiline = """
    Hey, how are you?

    I was just checking in.
                All good?

"""

# print(multiline)

# Escaping special characters
sentence = "I'm back at work! \tHey!\n\nWhere's this at\\located?"
# print(sentence)

# String Methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                                                 "
multiline = "                                                 " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".title()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Tea".ljust(15, ".") + "$0.5".rjust(5))
print("Muffin".ljust(16, ".") + "$3".rjust(4))
print("Matcha".ljust(15, ".") + "$2.5".rjust(5))

print("")
# String index values
print(first[0])
print(first[0:])

# Some methods return boolean data
print(first.startswith("E"))
print(first.endswith("a"))

# Boolean data typr
my_value = True
x = bool(False)
print(type(x))
print(isinstance(my_value, bool))

# Numeric data types

# Inteeger type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))

# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functons for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error if attempt to cast incorrect data
# zip_value = int("New York")
