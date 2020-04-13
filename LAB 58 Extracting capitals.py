quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""
val = ""
# Use a for loop and an if statement to print just the capitals in the quote above.
for char in quote:
    if char.isupper():
        val = val + char
print(val)