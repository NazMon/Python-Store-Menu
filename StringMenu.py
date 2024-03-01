# Develop a basic Menu screen to display to patrons
# while utilizing builtin Python string operators
# such as title(), r/ljust(), center(), et. al.,

# Header for the Menu's title, formatted accordingly and menu list
# Utilizing tuples, no need for mutability
header = "  quality cookery menu  ".title().center(30, "=")
food = ("Takoyaki 5pc", "Takoyaki 10pc", "Taiyaki Small",
        "Taiyaki Large", "PIzza (12 inch)", "Pizza (16 inch)")

# Adding Menu items for display - utilizng print
# and justifications for now
print("\n" + header)
print(food[0].ljust(28, ".") + "$5".rjust(2))
print(food[1].ljust(28, ".") + "$8".rjust(2))
print(food[2].ljust(28, ".") + "$5".rjust(2))
print(food[3].ljust(28, ".") + "$8".rjust(2))
print(food[4].ljust(28, ".") + "$10".rjust(2))
print(food[5].ljust(28, ".") + "$15".rjust(2))
print()
