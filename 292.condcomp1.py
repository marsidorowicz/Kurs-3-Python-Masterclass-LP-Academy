menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]
 
# for meal in menu:
#     if "spam" not in meal:
#

# meals = [meal for meal in menu if "spam" not in meal]  #cannot add else, but can add if
#
# print(meals)
#
# # meals = [meal for meal in menu if "spam" not in meal]
# meals = [meal if "spam" not in meal else "a meal skipped" for meal in menu]
# meals_reject = [meal for meal in menu if "spam" in meal]
# print(meals)
# print(meals_reject)
#
# x = 12
# expression = "Twelve" if x == 12 else "Unknown"
# print(expression)

for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal else "contains egg" if "egg" in meal else "contains bacon")

print()

items = set()   # list of objects that are different
for meal in menu:
    for item in meal:
        items.add(item)

print(items)
print()

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))

list_fizz = []
for x in range(1, 31):
    fizzbuzz = ["fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0
                else "buzz" if x % 5 == 0 else str(x)]
    list_fizz.append(fizzbuzz)
print(list_fizz)
