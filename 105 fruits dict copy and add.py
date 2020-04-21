fruit = {"jabłko": "soczyste, najlepsze czerwone :)", "pomarańcz": "pyszny soczek", "kiwi": "trochę cierpkie, ale jak " \
                                                                                            "dojrzeje jest super"}
vege = {"kapusta": "nie każdy lubi",
        "sałata": "króliki lubią",
        "seler": "tylko w zupie"}
vege.update(fruit)

print(vege)
print(fruit)

nice_nasty = fruit.copy()
nice_nasty.update(vege)
print(nice_nasty)