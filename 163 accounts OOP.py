import datetime
import pytz


class Account:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list = []
        self._transaction_list.append((Account._current_time(), self.__balance))
        print("Konto stworzone dla: " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount))
        else:
            print("Kwota pobrania musi być większa od 0")

    def withdraw(self, amount):
        if self.__balance > amount > 0:
            self.__balance -= amount
            self._transaction_list.append((Account._current_time(), -amount))
        else:
            print("Kwota pobrania musi być większa od 0 i mniejsza od stanu konta")
        self.show_balance()

    def show_balance(self):
        print("Stan konta wynosi: {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                trans_type = "Złożone w depozyt"
            else:
                trans_type = "Pobrane"
                amount *= -1
            print("{:6} {} w czasie {} (czasu lokalnego {}".format(amount, trans_type, date, date.astimezone()))


if __name__ == "__main__":

    Mariusz = Account("Mariusz", 200)
    Mariusz.withdraw(100)
    Mariusz.deposit(500)
    Mariusz.deposit(0)
    Mariusz.show_transactions()
    Mariusz.withdraw(50)
    Mariusz.withdraw(50)
    Mariusz.withdraw(50)

    Mariusz.show_transactions()

    Stefan = Account("Stefan", 800)
    Stefan.deposit(100)
    Stefan.withdraw(200)
    Stefan.show_transactions()
    print(Stefan.__dict__)
    Stefan._Account__balance = 40
    Stefan.show_balance()