text = "Mariusz siedzi w domu 5 dni"
litery = ""

for character in text:
    print(character + " ", end="")
print()
print("*"*80)
for char in text:
    if not char.isnumeric():
        litery = litery + char
print(litery)