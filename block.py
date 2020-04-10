name = input("Podaj swoje imię: ")
wiek = int(input("Ile masz lat, {0} ".format(name)))
print(wiek)

if wiek >= 18:
    print("Masz wystarczająco lat by się napić alkoholu")
else:
    print("""Niestety nie można Ci jeszcze pić alkoholu
          ale za {0} lat będziesz mógł :)""".format(18-wiek))