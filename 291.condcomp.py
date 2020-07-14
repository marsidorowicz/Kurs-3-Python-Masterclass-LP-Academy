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
 
for meal in menu:
    if "spam" not in meal:
        print(meal)

meals = [meal for meal in menu if "spam" not in meal]  #cannot add else, but can add if

print(meals)

fussy_meals = [meal for meal in menu if "spam" in meal or "eggs" in meal
               if not ("bacon" in meal and "sausage" in meal)]

print(fussy_meals)