import sqlite3

db = sqlite3.connect("contacts.sqlite")

# for row in db.execute("SELECT * FROM contacts"):
#     print(row)

update_sql = "UPDATE contacts SET email = 'mar@pl.pl'"  # WHERE contacts.phone = 4613515"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()  # connection to commit instead of commit directly db.commit()
update_cursor.close()


for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name, phone, email)


db.close()