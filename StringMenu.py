# Develop a basic Menu screen to display to patrons
# while utilizing builtin Python string operators
# such as title(), r/ljust(), center(), et. al.,

# Header for the Menu's title, formatted accordingly and menu list
# Utilizing tuples, no need for mutability for now
header = "  quality cookery menu  ".title().center(30, "=")
foods = ("Takoyaki 5pc", "Takoyaki 10pc", "Taiyaki Small",
        "Taiyaki Large", "Pizza (12 inch)", "Pizza (16 inch)")
prices = ("$5", "$8", "$5", "$8", "$10", "$15")

# Adding Menu items for display - utilizng print and justifications
# Using a loop that matches the two tuples prices to the foods
# Consider creating an object for this in the future OR key-value pairs
print("\n" + header)
for x in range(len(foods)):
    print(foods[x].ljust(28, ".") + prices[x].rjust(2))
print()
