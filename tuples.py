# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

Mariusz = "Mariusz", "Lat 35", "1985"
Lidia = "Lidia", "Lat 30", "1990"

print(Mariusz)
print(Mariusz[1])

Mariusz = Mariusz[0], "Lat 35", Mariusz[2]
print(Mariusz)

imie, wiek, rok_ur = Mariusz
print(imie)
print(wiek)
print(rok_ur)
# tuples dont use append
Mariusz = "Mariusz", "Lat 35", "1985"
Lidia = "Lidia", "Lat 30", "1990", [(1, "Chora"), (2, "Zdrowa")]
imie, wiek, rok_ur, stan = Lidia
print(stan)
print(Lidia)
Lidia[3].append((3, "Nie wiadomo"))
print(Lidia)
print(stan)