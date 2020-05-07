class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 10.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("hamilton", 14.99)

print("Modele: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Modele {0.make} = {0.price}. {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)
kenwood.switch_on = False
print(kenwood.switch_on)


print("*" * 60)

kenwood.power = 1.5
print(kenwood.power)
#print(hamilton.power)

Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# change one

kenwood.power_source = "gas"
print(kenwood.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)