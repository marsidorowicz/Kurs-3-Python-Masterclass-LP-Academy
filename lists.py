list1 = ["Mariusz", "Lidia", "Janek"]

for state in list1:
    print("W tej liście jest " + state)

list1.append("Bronek")

print(list1)

list1.sort()
print(list1)

even = [2, 4, 6, 8]

another_even = even
another_even.sort(reverse=True)
print(even)

menu = []
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "sausage", "spam"])
menu.append(["egg", "bacon"])
menu.append(["egg", "egg", "spam"])
menu.append(["spam", "bacon", "spam"])
menu.append(["spam", "bacon", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "spam"])

print(menu)

for meal in menu:
    if not "spam" in meal:
        for item in meal:
            print(item)