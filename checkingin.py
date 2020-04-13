text = "Mariusz siedzi w domu"

litera = input("Podaj literkę: ")

if litera in text:
    print("{} jest w {}".format(litera, text))
else:
    print("Nie o tę literę chodziło :)")