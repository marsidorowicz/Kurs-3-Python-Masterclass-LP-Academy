name = input("Podaj swoje imię ")
age = int(input("Podaj swój wiek "))

if name and age:
    if 18 <= age < 31:
        print("{} jesteś zaproszony na wakacje, masz {} lat".format(name, age))
    else:
        print("Niestety nie możesz z nami jechać")
else:
    print("Brak danych, kończę program")