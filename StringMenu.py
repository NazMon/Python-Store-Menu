# Develop a basic Menu screen to display to patrons
# while utilizing builtin Python string operators
# such as title(), r/ljust(), center(), et. al.,

# Header for the Menu's title, formatted accordingly
header = "  quality cookery menu  "
titled_header = header.title()
centered_header = titled_header.center(30, "=")

# Adding Menu items for display - utilizng print
# and justifications for now
print("\n" + centered_header)
print("Takoyaki 5pc".ljust(28, ".") + "$5".rjust(2))
print("Takoyaki 10pc".ljust(28, ".") + "$8".rjust(2))
print("Taiyaki Small".ljust(28, ".") + "$5".rjust(2))
print("Taiyaki Large".ljust(28, ".") + "$8".rjust(2))
print("Pizza (12 inch)".ljust(28, ".") + "$10".rjust(2))
print("Pizza (16 inch)".ljust(28, ".") + "$15".rjust(2))
print()
