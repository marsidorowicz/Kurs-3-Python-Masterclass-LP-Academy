low = 1
high = 1000

print("Pomyśl liczbę między {} a {}".format(low, high))
input("Naciśnij ENTER aby zacząć")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    high_low = input("Zgaduję, że to {}. w więcej, "
    "m mniej, c zgadłem ? : ".format(guess)).casefold()

    if high_low == "w":
        low = guess + 1
    elif high_low == "m":
        high = guess - 1
    elif high_low == "c":
        print("Zgadłem po {} próbach".format(guesses))
        break
    else:
        print("Naciśnij w, m, lub c ")
        continue
    guesses += 1
else:
    print("Pomyślałeś o liczbie {}".format(low))
    print("Zgadłem po {} próbach".format(guesses))