meaning = 42
print("")

# Conditional if elif and else in Python
if meaning > 10:
    print("Meaning is bigger than 10")
elif meaning < 10:
    print("Meaning is lesser than 10")
else:
    print("Meaning is 10")

# Conditional ternary operator in Python
print("Meaning is bigger than 10") if meaning > 10 else print(
    "Meaning is lesser or equal to 10"
)
