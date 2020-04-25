import shelve

with shelve.open("bike") as bike:
    bike["Make"] = "Honda"
    bike["Model"] = "Cbr"

    print(bike["Model"])