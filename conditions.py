age = int(input("Ile masz lat? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Miłego dnia w pracy")
else:
    print("Miłego wolnego czasu :) ")

print("-" * 80)

if age < 16 or age > 65:
    print("Miłego wolnego czasu :) ")
else:
    print("Miłego dnia w pracy")