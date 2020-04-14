available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("Podaj kierunek: ").lower()
    if chosen_exit == "quit":
        print("Koniec gry!")
        break
print("Czy nie dobrze wyjść? :) ")
