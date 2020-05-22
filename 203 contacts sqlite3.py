import sqlite3

db = sqlite3.connect("contacts.sqlite")

# for row in db.execute("SELECT * FROM contacts"):
#     print(row)

new_email = "abc2@even.pl"
phone = input("Please enter your phone number: ")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"  # to avoid sql injection attacks
print(update_sql)
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()  # connection to commit instead of commit directly db.commit()
update_cursor.close()


for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name, phone, email)


db.close()