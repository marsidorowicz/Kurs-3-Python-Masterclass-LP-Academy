import shelve

# with shelve.open("ShelfTest") as fruit:
fruit = shelve.open("ShelfTest")
# fruit["pomarańcz"] = "fajny soczek"
# fruit["jabłko"] = "czyści zęby"
# fruit["cytryna"] = "cierpka"
# fruit["lemonka"] = "zielona"

    # print(fruit["jabłko"])
    #

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         decr = fruit.get(dict_key)
#         print(decr)
#     else:
#         print("we dont have : "+ dict_key)
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print((f + " " + fruit[f]))

for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)
print(fruit.items())

fruit.close()