import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Mariusz', 4613515, 'mar@kjfdg.pl')")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Lidia', 546315634, 'lid@pl.pl')")


cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
# print(cursor.fetchall())  # giving a list of tuples

print(cursor.fetchone())  # giving one row

for name, phone, email in cursor:
    print(name, phone, email, sep=" | ")
    print("-"*40)

cursor.close()
db.commit()  # you need to commit always to make changes to database permanent
db.close()