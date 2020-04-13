name = input("Podaj swoje imię: ")
wiek = int(input("Ile masz lat, {0} ".format(name)))
print(wiek)

if wiek < 18:
    print("""Niestety nie można Ci jeszcze pić alkoholu
          ale za {0} lat będziesz mógł :)""".format(18-wiek))

elif wiek == 900:
    print("Przepraszam Yoda, ale umrzesz w Starwars: Powrót Jedi")
else:
    print("Masz wystarczająco lat by się napić alkoholu")
