import sqlite3

db = sqlite3.connect("contacts.sqlite")  # łączy z istniejącą bazą danych

# for row in db.execute("SELECT * FROM contacts"):
#     print(row)

name = input("Podaj swoje Imię: ")
# name = name.capitalize()

# data_for_name = db.execute("SELECT * FROM contacts WHERE name = '{}'".format(name))
# for name, phone, email in data_for_name:
#     print(name, phone, email)

# inne podejście z użyciem zapytania
# data_for_name = db.execute("SELECT * FROM contacts WHERE name = ?", (name,))
# for name, phone, email in data_for_name:
#     print(name, phone, email)

# inne podejście by nie używać capitalize
data_for_name = db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,))  # po name dajemy przecinek,
# by wysłać jako tuple
for name, phone, email in data_for_name:
    print(name, phone, email)

db.close()