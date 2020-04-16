options = ["wyjście", "drzwi", "parapety", "podłogi"
           , "sufity", "ramy", "gwoździe", "belki"
           , "młoty", "okna"]
sel = 1
while sel != 0:
    print("Wybierz odpowiednią opcję: ")
    for i in range(0, 10):
        print("{}. {}".format(i, options[i]))
    sel = int(input())
    if 0<sel<10:
        print("Wybrano opcję numer {} - {}".format(sel, options[i]))
    elif sel == 0:
        print("Miłego dnia :) ")
