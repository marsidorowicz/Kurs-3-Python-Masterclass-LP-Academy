class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Ale zabawa!")
        elif self.ratio == 1:
            print("Ciężko ale latam")
        else:
            print("Chyba sobie pochodzę")


class Duck(object):

    def __init__(self):
        self._wing = Wing(1.8 )

    def walk(self):
        print("Klap, klap, klap")

    def swim(self):
        print("Chodź popływać")

    def quack(self):
        print("Kwa, kwa, kwa")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Klap, klap, klap, też człapię")

    def swim(self):
        print("Chodź, ale uważaj, woda tu jest dużo chłodniejsza")

    def quack(self):
        print("Jestem pingwin i nie kwaczę")

    def aviate(self):
        print("Wygrałem na loterii i mam szybowca")


class Mallard(Duck):
    pass

# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:  # to allow only Duck type, otherwise give none
        # if isinstance(duck, Duck):  #checkk if its Duck class type
        #     self.flock.append(duck)
        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError('Cannot add duck, are you sure it is not a ' + str(type(duck).__name__))

    def migrate(self):
        try:
            for duck in self.flock:
                duck.fly()
                raise AttributeError("Test działania wyjątków")  # TODO remove before releasing
        except AttributeError:
            print("This one cannot be migrated")


if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    # test_duck(donald)

    # szeregowy = Penguin()
    # test_duck(szeregowy)