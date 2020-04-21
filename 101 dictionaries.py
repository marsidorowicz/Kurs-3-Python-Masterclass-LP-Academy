fruit = {"jabłko": "soczyste, najlepsze czerwone :)",
         "pomarańcz": "pyszny soczek"
         }

# print(fruit)
# print(fruit["jabłko"])
fruit["kiwi"] = "trochę cierpkie, ale jak " \
                 "dojrzeje jest super"
print(fruit)
# adding item to dict replace existing key
# del command to remove item, del fruit all
# del "item" remove one
# while True:
#     dict_key = input("Podaj nazwę owocu : ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         opis = fruit.get(dict_key)
#         print(opis)
#     else:
#         print("Takiego nie mamy w bazie")
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()

# ordered_keys = sorted(list(fruit.keys()))
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):
# for f in fruit:
#     print(f  + " - " + fruit[f])
# for val in fruit.values():
#     print(val)
#
# print('-' * 40)
#
# for key in fruit:
#     print(fruit[key])

print(fruit.items())

for snack in fruit.items():
    item, opis = snack
    print(item + " to " + opis)