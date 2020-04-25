import shelve

# bit = ["bekon", "sos", "chleb"]
# beams_on_toast = ["fasola", "chleb"]
scrambled_eggs = ["jaja", "masło", "mleko"]

with shelve.open('przepisy', writeback=True) as przepisy:
    # przepisy["bit"] = bit
    # przepisy["beans_on_toast"] = beams_on_toast
    # przepisy["scrambled_eggs"] = scrambled_eggs
    # przepisy["scrambled_eggs"] = scrambled_eggs
    #
    # przepisy["bit"].append("masło")
    # temp_list = przepisy["bit"]
    # temp_list.append("masło")
    # przepisy["bit"] = temp_list
    #
    # przepisy["scrambled_eggs"].append("energy")
    przepisy["scrambled_eggs"] = scrambled_eggs
    przepisy.sync()
    scrambled_eggs.append("krem")

    for snack in przepisy:
        print(snack, przepisy[snack])