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
        self._wing = Wing(1.8)

    def walk(self):
        print("Klap, klap, klap")

    def swim(self):
        print("Chodź popływać")

    def quack(self):
        print("Kwa, kwa, kwa")

    def fly(self):
        self._wing.fly()


class Penguin(object):

    def walk(self):
        print("Klap, klap, klap, też człapię")

    def swim(self):
        print("Chodź, ale uważaj, woda tu jest dużo chłodniejsza")

    def quack(self):
        print("Jestem pingwin i nie kwaczę")


# def test_duck(duck):
#     duck.walk()
#     duck.swim()
#     duck.quack()

if __name__ == "__main__":
    donald = Duck()
    donald.fly()
    # test_duck(donald)

    # szeregowy = Penguin()
    # test_duck(szeregowy)