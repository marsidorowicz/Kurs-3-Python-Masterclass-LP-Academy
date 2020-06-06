import sqlite3
import pytz
import datetime

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, time1 TIMESTAMP NOT NULL,"
           " account TEXT NOT NULL, amount"
           " INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT STRFTIME('%Y-%m-%d %H:%M:%f', "
           "history.time, 'localtime') AS localtime, "
           "history.time1, history.account, history.amount FROM history ORDER BY history.time")


class Account(object):

    @staticmethod
    def _current_time():
        return pytz.utc.localize(datetime.datetime.utcnow())
        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Record found for: {}".format(self.name), end="")
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}, ".format(self.name), end="")
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        deposit_time_local = deposit_time.astimezone()
        print(deposit_time)
        print(deposit_time_local)
        db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        db.execute("INSERT INTO history VALUES(?, ?, ?, ?)", (deposit_time, deposit_time_local, self.name, amount))
        db.commit()
        self._balance = new_balance

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # new_balance = self._balance - amount
            # withdraw_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES (?, ?, ?)", (withdraw_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("Amount must be greater than 0 and less than your account balance")
            return 0.0

    def show_balance(self):
        print(" Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == "__main__":
    mario = Account("Mario")
    mario.deposit(1010)
    mario.deposit(1000)
    mario.deposit(10)
    mario.deposit(10)
    mario.withdraw(40)
    mario.withdraw(0)
    mario.show_balance()

    jon = Account("Jon", 1000)
    barry = Account("Barty", 9000)
    eric = Account("Eric", 1000)
    jon.show_balance()
    barry.show_balance()
    eric.show_balance()

    db.close()