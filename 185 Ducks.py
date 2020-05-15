class Duck(object):

    def walk(self):
        print("Klap, klap, klap")

    def swim(self):
        print("Chodź popływać")

    def quack(self):
        print("Kwa, kwa, kwa")


class Penguin(object):

    def walk(self):
        print("Klap, klap, klap, też człapię")

    def swim(self):
        print("Chodź, ale uważaj, woda tu jest dużo chłodniejsza")

    def quack(self):
        print("Jestem pingwin i nie kwaczę")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == "__main__":
    donald = Duck()
    test_duck(donald)

    szeregowy = Penguin()
    test_duck(szeregowy)